from .forms import ArticleForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *


class HomeView(TemplateView):
    template_name = 'class_app2/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп. информация'
        return context

class ArticleListView(ListView):
    model = Article
    # template_name = 'articles.html'
    # context_object_name = 'articles'
    # template_name = 'class_app2/blog.html'

class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = Book.objects.filter(article=self.object)
        return context





class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

