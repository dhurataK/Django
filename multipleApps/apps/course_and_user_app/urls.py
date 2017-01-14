from django.conf.urls import url
from views import index, create

urlpatterns = [
    url(r'^$', index, name ='index'),
    url(r'^add_users_to_course$', create, name='users_to_course')
]
