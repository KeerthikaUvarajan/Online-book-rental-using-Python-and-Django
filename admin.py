from django.contrib import admin
from .models import BookLeaseUser, Book, BorrowedBook, Reviews

# Register your models here.

admin.site.register(BookLeaseUser)
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Reviews)
