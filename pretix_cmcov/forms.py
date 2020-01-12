from django import forms
from django.utils.translation import ugettext_lazy as _
from pretix.base.models.items import Question
from pretix.control.forms.filter import OrderFilterForm


class QuestionForm(OrderFilterForm):
    def __init__(self, *args, event, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["questions"] = forms.ModelMultipleChoiceField(
            label=_("Questions"),
            required=False,
            queryset=Question.objects.filter(event=event),
            widget=forms.CheckboxSelectMultiple(
                attrs={"class": "scrolling-multiple-choice"}
            ),
        )
        self.fields["hide_user"] = forms.BooleanField(required=False)
        self.fields["show_all_orders"] = forms.BooleanField(
            required=False, label=_("Show all orders")
        )

    def filter_qs(self, qs):
        fdata = self.cleaned_data
        qs = super().filter_qs(qs)
        if not fdata["show_all_orders"]:
            qs = qs.filter(
                all_positions__answers__question__in=fdata["questions"]
            ).distinct()
        return qs
