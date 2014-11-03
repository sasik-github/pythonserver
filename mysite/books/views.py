from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains = q)
            b = Book(title = '<script>alert(\'hello\')</script>')
            print b
            books = list(books)
            books.append(b)
            return render(request, 'search_result.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})
    