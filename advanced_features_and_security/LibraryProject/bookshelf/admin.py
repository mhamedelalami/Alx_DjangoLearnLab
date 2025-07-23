from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

# Custom user admin
class CustomUserAdmin(UserAdmin):
    pass  # You can customize if needed

admin.site.register(CustomUser, CustomUserAdmin)
