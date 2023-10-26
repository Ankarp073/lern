from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog', BlogView.as_view(), name='blog'),
]