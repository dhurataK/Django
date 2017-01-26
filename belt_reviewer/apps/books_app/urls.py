from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^new/$', views.new, name ='new'),
    url(r'^show/(?P<id>\d+)$', views.show, name = 'show'),
    url(r'^users/(?P<id>\d+)$', views.users, name ='users'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^add_book_review$', views.add_book_review, name='add_book_review'),
    url(r'^add_review$', views.add_review, name ='add_review')
]
