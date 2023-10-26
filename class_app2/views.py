from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class HomeView(TemplateView):
    template_name = 'class_app2/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Доп. информация'
        return context

class BlogView(ListView):
    model = Article
    # template_name = 'class_app2/blog.html'
