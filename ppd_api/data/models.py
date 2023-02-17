from django.db import models


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=40)
    price = models.IntegerField()
    transaction_date = models.DateField()
    postcode = models.CharField(max_length=10)
    property_type = models.CharField(max_length=1)
    new_building = models.BooleanField()
    duration = models.CharField(max_length=1)
    paon = models.CharField(max_length=256)
    saon = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    locality = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    county = models.CharField(max_length=256)
    category_type = models.CharField(max_length=128)
    record_status = models.CharField(max_length=128)

    def __str__(self):
        return self.transaction_id
