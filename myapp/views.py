from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from django.utils import timezone
from datetime import timedelta
from myapp.models import Order, Client, Product, ProductImg
from .forms import EditorProduct, AddProduct, DelProduct, ProductWithImgForm
from django.core.files.storage import FileSystemStorage

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


# Home work 4

#  Измените модель продукта, добавьте поле для хранения фотографии продукта.
#  Создайте форму, которая позволит сохранять фото.


# добавить новый продукт
def add_product(request):
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            # name_product = form.cleaned_data['name_product']
            # description = form.cleaned_data['description']
            # price = form.cleaned_data['price']
            # count_product = form.cleaned_data['count_product']
            # product = Product(name_product=name_product,
            #                   description=description,
            #                   price=price,
            #                   count_product=count_product)
            # product.save()
            form.save()
            # в случаи с 'Class Meta'!
    else:
        form = EditorProduct()

    return render(request, 'myapp/editor_product.html', {'form': form})


# Редактировать продукт указав его id
def editor_product(request, product_id):
    if request.method == 'POST':
        form = EditorProduct(request.POST)
        if form.is_valid():
            product = Product.objects.get(pk=product_id)
            product.name_product = form.cleaned_data['name_product']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            product.count_product = form.cleaned_data['count_product']
            product.save()
    else:
        form = EditorProduct()
    return render(request, 'myapp/editor_product.html', {'form': form})


# Удалить продукт по id
def del_product(request):
    if request.method == 'POST':
        form = DelProduct(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            Product.objects.filter(pk=product_id).delete()
    form = DelProduct()
    return render(request, 'myapp/del_product.html', {'form': form})


# сохранение в БД продукта с картинкой
def product_with_img(request):
    if request.method == 'POST':
        form = ProductWithImgForm(request.POST, request.FILES)
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count_product = form.cleaned_data['count_product']
            product_img = form.cleaned_data['product_img']
            fs = FileSystemStorage()
            filename = fs.save(product_img.name, product_img)
            # file_url = fs.url(filename)  путь к файлу
            product = ProductImg(name_product=name_product,
                                 description=description,
                                 price=price,
                                 count_product=count_product,
                                 product_img=filename)
            product.save()
    else:
        form = ProductWithImgForm()
    return render(request, 'myapp/product_with_img.html', {'form': form})


# выгрузка в шаблоны БД с media картинкамии
def print_all_product_img(request):
    all_product = ProductImg.objects.all()
    return render(request, 'myapp/print_all_product_img.html',
                  {'all_product': all_product})


# загрузка и выгрузка через класс "CreateView"
from django.views.generic import CreateView
from .models import MetaProductImg
from .forms import FormMetaProductImg


# загузка
class AddMetaProductImg(CreateView):
    model = MetaProductImg
    form_class = FormMetaProductImg
    template_name = 'myapp/add_meta_product_img.html'
    success_url = 'add_meta_product_img'


# выгрузка
class ReadMetaProductImg(CreateView):
    model = MetaProductImg
    form_class = FormMetaProductImg
    extra_context = {'imgs': MetaProductImg.objects.all()}
    template_name = 'myapp/print_meta_product_img.html'
