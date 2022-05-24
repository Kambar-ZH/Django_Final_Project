from django.contrib import admin
from book.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'num_pages', 'genre',)


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'publisher', 'type',)
