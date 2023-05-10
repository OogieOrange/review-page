from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Product)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
