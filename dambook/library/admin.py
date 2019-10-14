from django.contrib import admin
from .models import Bookshelf, Book, Author


# Register your models here.
admin.site.register(Bookshelf)
admin.site.register(Book)
admin.site.register(Author)
