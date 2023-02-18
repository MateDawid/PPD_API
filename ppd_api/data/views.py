from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from data.models import Transaction
from data.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    model = serializer_class.Meta.model
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'transaction_id': ['exact'],
        'price': ['exact', 'gte', 'lte'],
        'transaction_date': ['exact', 'gte', 'lte'],
        'postcode': ['exact'],
        'new_building': ['exact'],
        'duration': ['exact'],
        'city': ['exact'],
        'street': ['exact'],
        'paon': ['exact'],
        'saon': ['exact'],
        'category_type': ['exact'],
        'record_status': ['exact'],
    }
