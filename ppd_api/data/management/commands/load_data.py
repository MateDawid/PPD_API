import csv
from codecs import iterdecode
from contextlib import closing
from datetime import datetime
from itertools import islice

from django.core.management import BaseCommand
import requests

from data.models import Transaction

CSV_HEADERS = (
    'transaction_id', 'price', 'transaction_date', 'postcode', 'property_type', 'new_building', 'duration',
    'paon', 'saon', 'street', 'locality', 'city', 'district', 'county', 'category_type', 'record_status'
)

NEW_BUILDING_MAPPING = {
    'Y': True,
    'N': False
}


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)
        parser.add_argument('--rows', type=int)

    @staticmethod
    def format_row(row):
        formatted_row = {}
        for key in row:
            if key == 'transaction_id':
                formatted_row[key] = row[key].replace('{', '').replace('}', '')
            elif key == 'transaction_date':
                formatted_row[key] = datetime.strptime(row[key], "%Y-%m-%d %H:%M").date()
            elif key == 'price':
                formatted_row[key] = int(row[key])
            elif key == 'new_building':
                formatted_row[key] = NEW_BUILDING_MAPPING.get(row[key])
            else:
                formatted_row[key] = row[key]
        return formatted_row

    def handle(self, *args, **kwargs):
        url = kwargs.get('url')
        if url is None:
            raise Exception('Argument --url not provided')
        rows_count = kwargs.get('rows')
        if rows_count is None:
            rows_count = 100
        transaction_fields = [field.attname for field in Transaction._meta.fields if field.attname != 'id']
        with closing(requests.get(url, stream=True)) as r:
            lines_decoded = iterdecode(r.iter_lines(), 'utf-8')
            reader = csv.DictReader(lines_decoded, fieldnames=CSV_HEADERS)
            for idx, row in enumerate(islice(reader, rows_count), start=1):
                formatted_row = self.format_row(row)
                transaction_id = formatted_row['transaction_id']
                try:
                    Transaction.objects.get(transaction_id=transaction_id)
                except Transaction.DoesNotExist:
                    kwargs = {attr: formatted_row[attr] for attr in transaction_fields}
                    print(f'CREATE: Transaction {transaction_id}')
                    Transaction.objects.create(**kwargs)
