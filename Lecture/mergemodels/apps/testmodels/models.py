from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 45)
    blog = models.TextField(max_length=1000)
    blog_creator = models.ForeignKey(User)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now= True)
