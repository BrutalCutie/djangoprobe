from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from catalog.models import Product, Category
from .forms import ProductForm, CategoryForm


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(checkbox=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['add_data'] = {
            "len_products": len(Product.objects.all()),
               }

        return context


class ProductsAllListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['add_data'] = {
            "len_products": len(Product.objects.all()),
               }

        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/good.html"


class ProductPublicateSwitch(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "catalog/product_switch_confirm.html"
    fields = []

    def post(self, request, *args, **kwargs):

        product = get_object_or_404(Product, pk=kwargs.get('pk'))

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У Вас нет прав для изменения')

        checkbox = product.checkbox
        if checkbox:
            product.checkbox = False
        else:
            product.checkbox = True

        product.save()

        return redirect("catalog:good", pk=product.pk)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_new.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_new.html'

    def get_success_url(self):
        return reverse("catalog:good", kwargs={'pk': self.object.pk})

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        user = request.user

        # Контрольный список на группу модератора или владельца карточки
        perms_control = [
            user.has_perm('catalog.can_unpublish_product'),
            user.pk == product.owner.pk,
        ]

        # Если есть хотябы что-то одно(права или владелец карточки) - позволить удалить
        if not any(perms_control):
            return HttpResponseForbidden(f'У Вас нет прав для изменения')

        return super().get(self, request, *args, **kwargs)






class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete_confirm.html'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        user = request.user

        # Контрольный список на группу модератора или владельца карточки
        perms_control = [
            user.has_perm('catalog.can_unpublish_product'),
            user.pk == product.owner.pk,
        ]

        # Если есть хотябы что-то одно(права или владелец карточки) - позволить удалить
        if not any(perms_control):
            return HttpResponseForbidden(f'У Вас нет прав для удаления')

        product.delete()

        return redirect('catalog:home')


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
