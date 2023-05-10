from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductPosts(generic.ListView):
    model = Product
    queryset = Product.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12
