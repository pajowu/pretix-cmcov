from django.conf.urls import url

from .views import OrderList

urlpatterns = [
    url(
        r"^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/orders/cmcov/$",
        OrderList.as_view(),
        name="index",
    ),
]
