from __future__ import unicode_literals

from django.db import models


class Friendships(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, related_name="usersfriend")
    friend = models.ForeignKey('Users', models.DO_NOTHING, related_name ="friendsfriend")
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendships'


class Users(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
