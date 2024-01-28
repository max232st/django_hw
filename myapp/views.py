from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from myapp.models import Order, Client
from django.utils import timezone
from datetime import datetime, date, time, timedelta

logger = logging.getLogger(__name__)


def hello_world(requesr):
    logger.info("Visit page Hello world")
    return HttpResponse('Hello world')


def main(request):
    descryption_main = '''
<h2>Framework Django</h2>
    '''
    logger.info("Visit page main")
    return HttpResponse(descryption_main)


def about(request):
    about_descryption = '''
    <h2>Я студент GB!!!</h2>
    '''
    logger.info("Visit page about")
    return HttpResponse(about_descryption)


def all_orders(request):
    order = Order.objects.all()
    return HttpResponse(order)


## Home work 3

# - Доработаем задание про клиентов,
# товары и заказы.
# - Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# -Подготовьте необходимый маршрут и представление.


def index_extend_base(request):
    return render(request, 'myapp/index.html')


# вывод заказа по ID
def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_id = Order.objects.get(pk=order_id).pk
    order_date = Order.objects.get(pk=order_id).date_order
    client = Order.objects.get(pk=order_id).customer.name
    summ_price_order = Order.objects.get(pk=order_id).summ_price_order
    order_products = Order.objects.get(pk=order_id).products.all()

    return render(
        request, 'myapp/order.html', {
            'order': order,
            'order_id': order_id,
            'order_date': order_date,
            'order_products': order_products,
            'client': client,
            'summ_price_order': summ_price_order,
        })


# Вывод списка заказов по ID-client, с переходом на содержимое заказа
def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    return render(request, 'myapp/client_orders.html', {
        'client': client,
        'orders': orders
    })


# Вывод списка всех продуктов по ID-client
def client_all_products(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    all_orders = Order.objects.filter(customer=client)

    return render(request, 'myapp/client_all_products.html', {
        'client': client,
        'all_orders': all_orders,
    })


# сортировка заказов клиента за последние "count_day" дней
def orders_order_by(request, client_id, count_day):
    client = get_object_or_404(Client, pk=client_id)
    all_orders = Order.objects.filter(customer=client)
    date_now = timezone.now()
    # print(f'текущая дата - {date_now}')
    start_date = date_now - timedelta(days=count_day)
    # print(f'дата {count_day} назад - {start_date}')
    list_filter_orders = []
    for order in all_orders:
        if start_date <= order.date_order:
            list_filter_orders.append(order)
    return render(
        request, 'myapp/orders_order_by.html', {
            'count_day': count_day,
            'client': client,
            'list_filter_orders': list_filter_orders,
        })
