from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import BlogModel


class BlogListView(ListView):
    model = BlogModel
    template_name = "blog/index.html"
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)




class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = BlogModel
    template_name = "blog/new_blog.html"
    fields = ['title', 'inner', 'preview', 'is_active']
    success_url = reverse_lazy("blog:home")


class BlogUpdateView(UpdateView):
    model = BlogModel
    template_name = "blog/new_blog.html"
    fields = ['title', 'inner', 'preview', 'is_active']

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = BlogModel
    context_object_name = 'blog'
    template_name = "blog/blog_detail.html"
    success_url = reverse_lazy('blog:home')


class TestView(TemplateView):
    template_name = 'blog/index.html'
