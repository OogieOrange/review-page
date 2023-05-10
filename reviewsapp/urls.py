from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductPosts.as_view(), name='index')
]
