from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'удаление всех заказов'

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        print('Все заказы удалены')
