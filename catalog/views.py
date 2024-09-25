from django.shortcuts import render
from catalog.models import Category, Product
import random


def index(request):
    categories = Category.objects.all()
    rand_products: list = list(Product.objects.all())
    random.shuffle(rand_products)

    if len(rand_products) > 3 and rand_products:
        rand_products = rand_products[0:3]
    else:
        rand_products = rand_products[:len(rand_products)]

    context = {
        "categories": categories,
        "len_categories": len(categories),
        "rand_products": rand_products,
        "len_rand_products": len(rand_products)
               }

    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    if request.method == 'POST':
        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')


def get_category_items(request, pk):
    categories = Category.objects.all()
    context = {"categories": categories,
               "goods": Product.objects.filter(category=pk)}
    return render(request, 'catalog/details.html', context=context)


def get_item(request, pk):
    context = {"product": Product.objects.get(id=pk)}
    return render(request, 'catalog/good.html', context=context)
