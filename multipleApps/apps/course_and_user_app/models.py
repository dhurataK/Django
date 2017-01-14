from __future__ import unicode_literals

from django.db import models
from ..course_apps.models import Course
from ..login_reg_app.models import User
# Create your models here.

class CourseManager(models.Manager):
    #Getting users that are created in login_reg_app
    def getUsers(self):
        users = User.objects.all().values('first_name', 'id')
        return users

    #Getting courses from course_apps
    def getCourses(self):
        courses = Course.objects.all()
        return courses

class mainCourse(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    created_at = models.DateField(auto_now_add =True)
    updated_at = models.DateField(auto_now = True)
    objects = CourseManager()
