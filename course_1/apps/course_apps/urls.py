from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.create),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
]
