from django.shortcuts import render,redirect
from django.urls import reverse
# So we can count the students in a class
from django.db.models import Count
from models import mainCourse
from ..course_apps.models import Course
from ..login_reg_app.models import User
# Create your views here.

def index(request):
    users = mainCourse.objects.getUsers()
    courses = Course.objects.getAll()
    # course_users = mainCourse.objects.all().values('course').annotate(total=Count('user')).order_by('total')
    counter = Course.objects.values('name').annotate(students = Count('users')).order_by('students')

    context = {
        'users' : users,
        'courses' : courses,
        'counter': counter
    }
    return render(request, 'course_and_user_app/index.html', context)

def create(request):
    Course.objects.add_users_to_course(
            user_id=request.POST['user_id'],
            course_id=request.POST['course_id']
            )
    return redirect(reverse('courses_users:index'))
