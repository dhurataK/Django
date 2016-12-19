from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.

class UserManager(models.Manager):#here we are inheriting the Manager class
    def register(self, data):#any no. of arguments
        errors = []
        #Validations for first_name
        if not data['first_name']:
            errors.append('First name is required')
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
            password = data['password']
            pw_hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
            user = User.objects.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'],password = pw_hashed)
            return (True,user)

    def login(self, data):
        email = data['email']
        try:
            user = User.objects.get(email=email)
            # The email matched a record in the database, now test passwords
            password = data['password'].encode()
            if bcrypt.hashpw(password, user.password.encode()):
                return (True, user)
        except:
            pass

        return (False, ["Email/password don't match."])
        
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
