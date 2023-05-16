from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    upvotes = models.ManyToManyField(
        User, related_name='reviewsapp_upvotes', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='reviewsapp_downvotes', blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()

    def number_of_downvotes(self):
        return self.downvotes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=800)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} created by {self.name}"
