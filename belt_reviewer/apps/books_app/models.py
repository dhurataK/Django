from __future__ import unicode_literals
from ..login_reg_app.models import User
from django.db import models

# Create your models here.
class ReviewManager(models.Manager):
    #This method is used for checking if empty data are sent
    def add_book_review_validations(self, form_data):
        errors = []
        if not form_data['book_title'] or not form_data['review']:
            errors.append('Field must be filled!')
        if form_data['author_id'] == 'None' and not form_data['new_author']:
            errors.append('You must either select an author form list or add new one!')
        if form_data['rating'] == 'None':
            errors.append('You must select a rate number!')
        return errors

    def add_book_review(self, form_data, session_user):
        errors = self.add_book_review_validations(form_data)
        if len(errors)>0:
            # for error in errors:
            #     print error
            return (False, errors)
        else:
            book_title = form_data['book_title']
            review_input = form_data['review']
            rating = form_data['rating']
            this_user_id = session_user['id']

            if form_data['author_id'] != 'None':
                author_input = form_data['author_id']
                # print "Author from selection ", author_input
            else:
                author_input = form_data['new_author']
                # print "Author from input ", author_input

            author = self.create_author(author_input)
            # print "Author: ",author
            book = Book.objects.create(title = book_title, author = author)
            # print "Book :", book
            user = User.objects.get(id = this_user_id)
            # print "This user: ",user
            review = Review.objects.create(review= review_input, rating= rating, book = book, user = user)
            # print "Review: ",review
            return (True, review)

    def create_author(self, data):
        # print "Inside create_author: ",data
        author = Author.objects.create(name=data)
        return author

    def add_review_validations(self, form_data):
        errors = []
        if not form_data['review']:
            errors.append('Field must be filled!')
        elif form_data['rating'] == 'None':
            errors.append('You must select a rate number!')
        return errors

    def add_review(self, data, session_user):
        errors = self.add_review_validations(data)
        if len(errors)>0:
            for error in errors:
                print error
            return (False, errors)
        else:
            book = Book.objects.get(id = data['book_id'])
            this_user_id = session_user['id']
            user = User.objects.get(id = this_user_id)
            in_review = data['review']
            rating = data['rating']
            review = Review.objects.create(review = in_review, rating = rating, book = book, user = user)
            return(True, review)

class Author(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book)
    user = models.ForeignKey('login_reg_app.User')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = ReviewManager()
