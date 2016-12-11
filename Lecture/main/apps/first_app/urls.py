  # # Now from within your newly created apps/first_app/urls.py file...
  # print "I will be your future routes; HTTP requests will be captured by me."
from django.conf.urls import url
from . import views # This gives us access to everything in a views.py
# from 'everywhere we are' go get that 'views.py' and access to everything that's there
urlpatterns = [
    url(r'^$', views.index) # And now we use include to pull in our first_app.urls...
]
