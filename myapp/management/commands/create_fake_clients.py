from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Создание фейковых клиентов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name_client{i}',
                            email=f'mail{i}@mail.ru',
                            phone=f'{555000 + i}',
                            address=f'address_{i}')
            client.save()
