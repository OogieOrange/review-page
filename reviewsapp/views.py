from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product


class ProductPosts(generic.ListView):
    model = Product
    queryset = Product.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'product_posts'
    paginate_by = 12


class ProductDetails(generic.ListView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Product.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "review_details.html",
            {
                "product": post,
            },
        )
