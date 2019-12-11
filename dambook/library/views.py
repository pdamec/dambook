from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookshelf
# Create your views here.

def home(request):

    context = {
        'bookshelf': get_books()
    } 
    return render(request, 'library/bookshelf.html', context)


# Methods where to place?
def get_books(user_id=0):
    bookshelf = Bookshelf.objects.filter(bookworm=2).first()
    if bookshelf is None:
        return None
    return bookshelf.book.all()
