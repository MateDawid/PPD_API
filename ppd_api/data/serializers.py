from rest_framework import serializers

from data.models import Transaction


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
