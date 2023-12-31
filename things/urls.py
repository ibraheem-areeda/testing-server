from django.urls import path
from .views import ThingList, ThingDetail,charge_webhook,merchant_status_webhook_test

urlpatterns = [
    path("", ThingList.as_view(), name="thing_list"),
    path("<int:pk>/", ThingDetail.as_view(), name="thing_detail"),
    path("charge-webhook/", charge_webhook, name="thing_detail"),
    path("merchant_status/", merchant_status_webhook_test, name="thing_detail"),
]
