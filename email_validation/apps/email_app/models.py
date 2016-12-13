from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, email_data):
        # Checks if field is left blank!
        if len(email_data) < 1:
            return(False, 'Field cannot be left blank!')
        # If the given email is a valid email ?
        elif not EMAIL_REGEX.match(email_data):
            return(False, 'Not a valid email address!')
        else:
            return(True, 'Success! The email address you enterd "{}" is a VALID email address!Thank you!'.format(email_data))

class Email(models.Model):
    email = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)

    objects = models.Manager()
    emailManager = EmailManager()
