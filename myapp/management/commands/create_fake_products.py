from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Создание фейковых прродуктов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        num = 0.25
        for i in range(1, count + 1):
            product = Product(name_product=f'product_{i}',
                              description=f'text text {i}',
                              price=f'{i + num}',
                              count_product=f'{10 + i}')
            num += 0.25
            product.save()
