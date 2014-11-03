from django.contrib import admin
from books.models import Publisher, Author, Book
from userregister.models import User

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    """docstring for BookAdmin"""
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    ordering = ('-publication_date',)
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
        


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User)

