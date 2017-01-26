from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.

class UserManager(models.Manager):#here we are inheriting the Manager class
    def reg_input_validation(self, data):
        errors =[]
        if not data['first_name'] or not data['alias'] or not data['email'] or not data['password'] or not data['cw_password']:
            errors.append('Fields are required!')
        if len(data['first_name'])  <= 2 or len(data['alias']) <= 2:
            errors.append("Please include a first and/or last name longer than two characters.")
        if bool(re.search(r'\d', data['first_name'])):
            errors.append("First name must contain only letters!")
        if not re.match(EMAIL_REGEX,data['email']):
            errors.append('Email not valid!')
        if len(data['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        if data['password'] != data['cw_password']:
            errors.append('Passwords must match!')
        return errors

    def log_input_validation(self, data):
        errors =[]
        if not data['email'] or not data['password']:
            errors.append('Fields are required!')
        elif not re.match(EMAIL_REGEX,data['email']):
            errors.append('Email not valid!')
        return errors

    def register_validation(self, data):#any no. of arguments
        errors = self.reg_input_validation(data)
        if len(errors)>0:
            return (False, errors)
        else:
            password = data['password'].encode()
            pw_hashed = bcrypt.hashpw(password,bcrypt.gensalt())
            user = User.objects.create(
                    first_name = data['first_name'],
                    alias = data['alias'],
                    email = data['email'],
                    password = pw_hashed
            )
            return (True,user)

    def login_validation(self, data):
        errors = self.log_input_validation(data)
        # # if there are errors than stop don't let login
        if len(errors)>0:
            return(False, errors)
        else:
            try:
                user = User.objects.get(email=data['email'])
                # The email matched a record in the database, now test passwords
                raw = data['password'].encode()
                hashed = user.password.encode()
                if bcrypt.hashpw(raw, hashed) == hashed:
                    #indeed there is a user
                    return (True, user)
            except:
                print 'Error ocured while quering the db!'
        errors.append("Email/password don't match.")
        return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length = 200)
    alias = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # repace with UserManager, since we are inheriting from models.Manager we don't lose
    # the ability to query the db that was implemented there.
    objects = UserManager()
