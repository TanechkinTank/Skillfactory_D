from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    ordering = 'dateCreation'
    template_name = 'flatpages/news_list.html'
    context_object_name = 'news'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    pk_url_kwarg = 'id'


class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/create.html'


class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/edit.html'


class PostDelete(DeleteView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/delete.html'


