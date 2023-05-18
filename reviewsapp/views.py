from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Product, Comment, BugReport
from .forms import CommentForm, ReportForm


class ProductPosts(generic.ListView):
    model = Product
    queryset = Product.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'product_posts'
    paginate_by = 12

# ProductDetails taken from "I think therefore I blog" and modified


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
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Product.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review-details.html",
            {
                "product": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
        return render(request, 'comment-edited.html')

    comment_form = CommentForm(instance=comment)
    context = {
        'comment_form': comment_form
    }

    return render(request, 'edit-comment.html', context)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return render(request, 'comment-deleted.html')


def bug_reports(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report_form.instance.name = request.user.username
            report_form.save()
        return render(request, 'report-sent.html')
    report_form = ReportForm()
    context = {
        'report_form': report_form
    }

    return render(request, 'report-page.html', context)
