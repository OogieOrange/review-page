from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product
from .forms import CommentForm


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
        comments = post.comments.order_by("created_on")

        return render(
            request,
            "review-details.html",
            {
                "product": post,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
