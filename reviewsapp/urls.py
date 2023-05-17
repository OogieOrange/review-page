from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductPosts.as_view(), name='index'),
    path('<slug:slug>/', views.ProductDetails.as_view(), name='product_detail'),
    path('edit/<comment_id>', views.edit_comment, name='edit'),
    path('delete/<comment_id>', views.delete_comment, name='delete'),
]
