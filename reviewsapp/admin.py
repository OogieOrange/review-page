from django.contrib import admin
from .models import Product, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'title')
    list_display = ('title', 'slug', 'created_on', 'status')
    search_fields = ['title', 'description']
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('name', 'created_on')
    list_display = ('name', 'post', 'created_on')
    search_fields = ['name', 'created_on', 'body']
