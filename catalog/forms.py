from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "descr", "img", "price", 'checkbox']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name in self.fields.keys():
            if field_name == 'checkbox':
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-check-input'
                })
            else:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ["name", "descr"]

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields["descr"].widget.attrs.update({
            'class': 'form-control'
        })
