from django.urls import path
from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name


urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('new/', views.BlogCreateView.as_view(), name='new_blog'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>', views.BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='blog_delete'),
]
