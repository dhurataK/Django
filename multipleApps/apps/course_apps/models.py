from __future__ import unicode_literals

from django.db import models
from ..login_reg_app.models import User

class CourseManager(models.Manager):
	def createCourse(self, **kwargs):
		results = Course.objects.create(name=kwargs['name'], description=kwargs['description'])
		return (True, results.name)

	def getAll(self, *args):
		all_courses = Course.objects.all()
		return all_courses

	def getOne(self, args):
		result = Course.objects.get(id=args)
		return result

	def deleteOne(self, args):
		Course.objects.filter(id=args).delete()

	def add_users_to_course(self, **kwargs):
		print kwargs
		course = self.get(id=kwargs['course_id'])
		print "Course: ", course
		user = User.objects.get(id=kwargs['user_id'])
		print "User: ", user
		course.users.add(user)
		course.save()

class Course(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = CourseManager()
	# here we are creating a many to many relation to User in login_reg_app
	users = models.ManyToManyField('login_reg_app.User', related_name='courses')
