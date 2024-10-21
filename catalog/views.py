from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Category
from .forms import ProductForm, CategoryForm


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(checkbox=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['add_data'] = {
            "len_products": len(Product.objects.all()),
               }

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/good.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_new.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_new.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete_confirm.html'
    success_url = reverse_lazy('catalog:home')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class SuccessTemplateView(TemplateView):
    template_name = 'catalog/success.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
    context_object_name = 'category'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_new.html'
    success_url = reverse_lazy('catalog:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_new.html'
    success_url = reverse_lazy('catalog:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/category_delete_confirm.html'
    success_url = reverse_lazy('catalog:category_list')
