from django.urls import path
from myapp import views

urlpatterns = [
    path("main/", views.main, name='main'),
    path("about/", views.about, name='about')
]
