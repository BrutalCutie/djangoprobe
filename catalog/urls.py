from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('good/<int:pk>/', views.ProductDetailView.as_view(), name='good'),
]
