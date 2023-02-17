from rest_framework import viewsets

from data.models import Transaction
from data.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
