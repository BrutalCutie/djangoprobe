from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='home'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('good/<int:pk>/', views.ProductDetailView.as_view(), name='good'),
    path('thankYou/', views.SuccessTemplateView.as_view(), name='success'),

    path('product_new/', views.ProductCreateView.as_view(), name='product_new'),
    path('product_update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('category_new/', views.ProductDeleteView.as_view(), name='category_new'),
    path('category_update/<int:pk>/', views.ProductDeleteView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', views.ProductDeleteView.as_view(), name='category_delete'),
    path('category_detail/<int:pk>/', views.ProductDeleteView.as_view(), name='category_detail'),
    path('category_list/', views.ProductDeleteView.as_view(), name='category_list'),

]

