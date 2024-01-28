from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'Выбрать заказ для удаления заказа, указав ID заказа передав один аргумент'

    def add_arguments(self, parser):
        parser.add_argument('id_order', type=int)

    def handle(self, *args, **kwargs):
        id_order = kwargs['id_order']
        Order.objects.filter(pk=id_order).delete()
        print('Заказ удалён')
