from django.contrib import admin
from books.models import Book

# Register your models here.

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

# class BookAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Book, BookAdmin)
