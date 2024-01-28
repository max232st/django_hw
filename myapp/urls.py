from django.urls import path
from myapp import views

urlpatterns = [
    path("main/", views.main, name='main'),
    path("about/", views.about, name='about'),
    path("all_orders/", views.all_orders, name='all_orders'),
    path("index_extend_base/",
         views.index_extend_base,
         name='index_extend_base'),
    path("client_orders/<int:client_id>",
         views.client_orders,
         name='client_orders'),
    path("order/<int:order_id>", views.order, name='order'),
    path("client_all_products/<int:client_id>", views.client_all_products, name='client_all_products'),
    path("orders_order_by/<int:client_id>/<int:count_day>", views.orders_order_by, name='orders_order_bys'),
    path("editor_product/<int:product_id>",
         views.editor_product,
         name='editor_product'),
    path("add_product/", views.add_product, name='add_product'),
    path("del_product/", views.del_product, name='del_product'),
    path("product_with_img/", views.product_with_img, name='product_with_img'),
    path("print_all_product_img/",
         views.print_all_product_img,
         name='print_all_product_img'),

    path('add_meta_product_img',
         views.AddMetaProductImg.as_view(),
         name='AddMetaProductImg'),

    path('print_meta_product_img',
         views.ReadMetaProductImg.as_view(),
         name='ReadMetaProductImg'),
]
