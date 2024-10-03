from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic import ListView, DeleteView, DetailView
from catalog.models import Product
import random


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['add_data'] = {
            "len_products": len(Product.objects.all()),
               }

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/good.html"


def contacts(request):
    if request.method == 'POST':
        return render(request, 'catalog/success.html')

    return render(request, 'catalog/contacts.html')
