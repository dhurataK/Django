from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.

class UserManager(models.Manager):#here we are inheriting the Manager class
    def register_validations(self, data):#any no. of arguments
        errors = []
        #Validations for first_name
        if not data['first_name']:
            errors.append('First name is required!')
        elif len(data['first_name']) <= 2:
            errors.append('First name must be longer than 2 characters')
        elif bool(re.search(r'\d', data['first_name'])):
            errors.append('First name must contain only letters!')
        # Validations for last_name
        if not data['last_name']:
            errors.append('Last name is required')
        elif len(data['last_name']) <= 2:
            errors.append('Last name must be longer than 2 characters')
        elif bool(re.search(r'\d', data['last_name'])):
            errors.append('Last name must contain only letters!')
        #Validations for email
        if not data['email']:
            errors.append('Email is required')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Invalid email!')
        #Validations for password
        if not data['password']:
            errors.append('Password is required')
        elif len(data['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        elif data['password'] != data['cw_password']:
            errors.append('Passwords must match!')
        if errors:
            return(False, errors)
        else:
            password = data['password'].encode()
            pw_hashed = bcrypt.hashpw(password,bcrypt.gensalt())
            user = User.objects.create(
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    email = data['email'],
                    password = pw_hashed
            )
            return (True,user)

    def login_validations(self, data):
        errors = []
        #Validations for email
        if data['email']:
            if not re.match(EMAIL_REGEX,data['email']):
                errors.append('Email not valid!')
        else:
            errors.append('Email is empty!')
        #Validations for password
        if not data['password']:
            errors.append('Password is empty!')
        # if there are errors than stop don't let login
        if errors:
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
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # repace with UserManager, since we are inheriting from models.Manager we don't lose
    # the ability to query the db that was implemented there.
    objects = UserManager()
