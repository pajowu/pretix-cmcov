from django.db.models import (
    Count,
    IntegerField,
    OuterRef,
    Prefetch,
    ProtectedError,
    Q,
    Subquery,
    Sum,
)
from django.utils.functional import cached_property
from django.views.generic import ListView
from pretix.base.models import (
    CachedCombinedTicket,
    CachedFile,
    CachedTicket,
    Invoice,
    InvoiceAddress,
    Item,
    ItemVariation,
    LogEntry,
    Order,
    QuestionAnswer,
    Quota,
    generate_position_secret,
    generate_secret,
)
from pretix.base.models.orders import OrderPosition
from pretix.control.forms.filter import (
    EventOrderFilterForm,
    OverviewFilterForm,
    RefundFilterForm,
)
from pretix.control.permissions import EventPermissionRequiredMixin
from pretix.control.views import PaginationMixin

from .forms import QuestionForm


class OrderList(EventPermissionRequiredMixin, PaginationMixin, ListView):
    model = Order
    context_object_name = "orders"
    template_name = "pretix_ordertable/orderview.html"
    permission = "can_view_orders"

    def get_queryset(self):
        qs = Order.objects.filter(event=self.request.event)

        if self.filter_form.is_valid():
            qs = self.filter_form.filter_qs(qs)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filter_form"] = self.filter_form

        # Only compute this annotations for this page (query optimization)
        s = (
            OrderPosition.objects.filter(order=OuterRef("pk"))
            .order_by()
            .values("order")
            .annotate(k=Count("id"))
            .values("k")
        )

        if ctx["page_obj"].paginator.count < 1000:
            # Performance safeguard: Only count positions if the data set is small
            ctx["sums"] = (
                self.get_queryset()
                .annotate(pcnt=Subquery(s, output_field=IntegerField()))
                .aggregate(s=Sum("total"), pc=Sum("pcnt"), c=Count("id"))
            )
        else:
            ctx["sums"] = self.get_queryset().aggregate(s=Sum("total"), c=Count("id"))
        return ctx

    @cached_property
    def filter_form(self):
        return QuestionForm(data=self.request.GET, event=self.request.event)
