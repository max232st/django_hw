from django.contrib import admin
from .models import Order, Product, Client

# Дополнительные действия
# @admin.action(description="Сбросить в ноль")
# def reset_quantity(modeladmin, request, queryset):
#     queryset.update(quantity=0)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "date_registr"]
    ordering = ["name", "date_registr"]
    list_filter = ["date_registr"]
    search_fields = ["name", "phone"]
    search_help_text = "Поиск по полю имя клиента и номеру телефона"
    ##
    fields = ["name", "email", "phone", "address", "date_registr"]
    readonly_fields = ["date_registr"]
    # actions = [reset_quantity] - вызов дополнительного действия


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name_product", "description", "price", "count_product",
        "date_add_product"
    ]
    ordering = ["name_product", "-price"]
    list_filter = ["date_add_product"]
    search_fields = ["name_product"]
    search_help_text = "Поиск по полю имя продукта"
    ##
    fieldsets = [
        (
            'Наименование продукта и его описание',
            {
                'classes': ['wide'],
                'fields': ['name_product', 'description'],
            },
        ),
        (
            'Цена продукции за 1шт',
            {
                'description': 'Категория товара и его подробное описание',
                'fields': ['price'],
            },
        ),
        ('Дата поступления товара и в каком количестве', {
            'classes': ['collapse'],
            'description': 'Дата и количество',
            'fields': ['date_add_product', 'count_product'],
        }),
    ]
    readonly_fields = ["date_add_product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "summ_price_order", "date_order"]
    ordering = ["customer", "date_order"]
    list_filter = ["date_order"]
    search_fields = ["customer"]
    search_help_text = "Поиск по полю имя продукта по ID клиента"
    ##
    fields = ["customer", "summ_price_order", "date_order", "products"]
    readonly_fields = ["date_order"]


'''
можно производить регистрацию моделей для А.П.
через декоратор:
   @admin.register(Класс модели)
вместо вызова метода
   admin.site.register(Client, ClientAdmin)
   admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
'''