from django import forms
from .models import Product, MetaProductImg


class EditorProduct(forms.Form):
    name_product = forms.CharField(max_length=100)
    description = forms.CharField(
        widget=forms.Textarea())  # wiget - дополнительные валидирующие условия
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count_product = forms.IntegerField()


# в случаи если модель не отличается от формы,
# наследование от класаа (forms.ModelForm)
class AddProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_product', 'description', 'price', 'count_product']


class DelProduct(forms.Form):
    product_id = forms.IntegerField()


class ProductWithImgForm(forms.Form):
    name_product = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    count_product = forms.IntegerField()
    product_img = forms.ImageField()


class FormMetaProductImg(forms.ModelForm):
    class Meta:
        model = MetaProductImg
        fields = '__all__'
