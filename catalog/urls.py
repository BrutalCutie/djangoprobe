from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('details/<int:pk>/', views.get_category_items, name='categories'),
    path('good/<int:pk>/', views.get_item, name='good'),
]
