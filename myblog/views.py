from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from .models import Publish, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy
# Create your views here.


class HomeView(ListView):
    model = Publish
    template_name = 'home.html'
    ordering = ['-id']


class ArticleView(DetailView):
    model = Publish
    template_name = 'article.html'


class AddPost(CreateView):
    model = Publish
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategory(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePost(UpdateView):
    model = Publish
    form_class = UpdateForm
    template_name = 'update_post.html'


class DeletePost(DeleteView):
    model = Publish
    form_class = UpdateForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
