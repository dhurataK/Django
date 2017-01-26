from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from ..login_reg_app.models import User
from .models import Review, Book
# Create your views here.
def index(request):
    reviews = Review.objects.all().order_by('-id')[:3]
    books = Book.objects.all()
    context = {
        'reviews': reviews,
        'books':books
    }
    return render(request, 'books_app/index.html', context)

def new(request):
    return render(request, 'books_app/new.html')

def add_book_review(request):
    if request.method == 'POST':
        result = Review.objects.add_book_review(request.POST, request.session['user'])
        if not result[0]:
            for error in result[1]:
                messages.error(request, error)
            return redirect(reverse('books:new'))
        else:
            review = result[1]
            # print "Review form result: ",review
            book_id = review.book.id
            # print "Book id ", book_id
            return redirect(reverse('books:show', kwargs ={'id':book_id}))

def show(request, id):
    book = Book.objects.get(id = id)
    # print "Book inside the show method: ",book
    result = Review.objects.filter(book= book)
    # print "Review inside show ",result[0].book.title
    context = {
        'reviews':result
    }
    return render(request, 'books_app/show.html', context)

def add_review(request):
    book_id = request.POST['book_id']
    result = Review.objects.add_review(request.POST, request.session['user'])
    if not result[0]:
        for error in result[1]:
            messages.error(request, error)
    return redirect(reverse('books:show', kwargs ={'id':book_id}))

def users(request,id):
    user = User.objects.get(id=id)
    reviews = Review.objects.filter(user = user)
    count_reviews = Review.objects.filter(user = user).count()
    context = {
        'user':user,
        'reviews':reviews,
        'count_reviews':count_reviews
    }
    return render(request, 'books_app/show_user.html', context)

def delete(request, id):
    book_id = request.POST['book_id']
    Review.objects.filter(id=id).delete()
    return redirect(reverse('books:show', kwargs ={'id':book_id}))
