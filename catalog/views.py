from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    categories = Category.objects.all()
    context = {"categories": categories}
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

