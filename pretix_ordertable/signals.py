from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import ugettext_lazy as _
from pretix.control.signals import nav_event


@receiver(nav_event, dispatch_uid="ordertable_tableview")
def ordertable_tableview(sender, request, **kwargs):
    url = resolve(request.path_info)
    return [
        {
            "label": _("CMCOV"),
            "url": reverse(
                "plugins:pretix_ordertable:index",
                kwargs={
                    "event": request.event.slug,
                    "organizer": request.event.organizer.slug,
                },
            ),
            "active": url.namespace == "plugins:pretix_ordertable",
            "icon": "table",
            "parent": reverse(
                "control:event.orders",
                kwargs={
                    "event": request.event.slug,
                    "organizer": request.event.organizer.slug,
                },
            ),
        }
    ]
