from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Category


class ProductForm(forms.ModelForm):

    BAD_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар"
    ]

    BAD_WORDS_STR = ", ".join(BAD_WORDS)


    class Meta:
        model = Product
        fields = ["category", "name", "descr", "img", "price", 'checkbox']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name in self.fields.keys():
            if field_name == 'checkbox':
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-check-input',
                    'id': 'is_active'
                })

            elif field_name == 'descr':
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control',
                    'rows': 3
                })

            else:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError("Цена должна быть положительной!")

        return price

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name")
        descr = cleaned_data.get("descr")

        contains_badword = False
        for word in self.BAD_WORDS:
            if word in name.lower():
                contains_badword = True
                self.add_error('name', f'содержит запрещенное слово "{word}"')
            if word in descr.lower():
                contains_badword = True
                self.add_error('descr', f'содержит запрещенное слово "{word}"')

            if contains_badword:
                break






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
