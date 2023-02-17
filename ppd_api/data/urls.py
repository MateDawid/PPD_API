from django.urls import path, include
from rest_framework import routers

from data.views import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
