from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import ArticleForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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


# class BookListView(ListView):
#     model = Book
#
#
# class BookDetailView(DetailView):
#     model = Book
#
#
# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookForm
#     success_url = '/books/'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'class_app2/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name = form.cleaned_data['full_name']
        user.birth_date = form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class ProfileView(TemplateView):
    template_name = 'class_app2/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

