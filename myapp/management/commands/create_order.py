from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Создать заказ, указав аргкменты через пробел где первое значение ID клиента, остальные это ID товара'

    def add_arguments(self, parser):
        parser.add_argument('user', type=int)
        parser.add_argument('prod', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        user = kwargs['user']
        prod = kwargs['prod']
        sum = 0
        cli = Client.objects.get(pk=user)
        order = Order.objects.create(customer=cli, summ_price_order=sum)
        for i in prod:
            order.products.add(Product.objects.get(pk=i))
            sum += Product.objects.get(pk=i).price
            order.save()
        order.summ_price_order = sum
        order.save()
