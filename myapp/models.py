from django.db import models


# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    address = models.CharField(max_length=254)
    date_registr = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'client name - {self.name}'


class Product(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_product = models.IntegerField()
    date_add_product = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name product - {self.name_product}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    summ_price_order = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'customer - {self.customer},\nproducts - {self.products},\nsumma price order = {self.summ_price_order},\ndate order - {self.date_order}'


class ProductImg(models.Model):
    name_product = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count_product = models.IntegerField()
    date_add_product = models.DateTimeField(auto_now_add=True)
    product_img = models.ImageField(
        upload_to='imges_product/')  # , height_field=300, width_field=300)


class MetaProductImg(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img_prod/')
