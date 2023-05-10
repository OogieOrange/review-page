from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'title')
    list_display = ('title', 'slug', 'created_on', 'status')
    search_fields = ['title', 'description']
    summernote_fields = ('description')


