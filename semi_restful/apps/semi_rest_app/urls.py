from django.conf.urls import url
from views import products, products_with_id, new, edit, destroy

urlpatterns = [
    # This route deals with GET or POST to users (either index or create)
    url(r'^$', products),
    url(r'^new$', new),
    # This route deals with GET or POST to /products/<id> (either update or show)
    url(r'^(?P<id>\d+)/$', products_with_id),
    # This route deals w/ Editing or Deleting a product
    url(r'^(?P<id>\d+)/edit/$', edit),
    url(r'^(?P<id>\d+)/destroy/$', destroy)
]
