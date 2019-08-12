from django.conf.urls import url
from . import views as riak_views

urlpatterns = [
    url("^search/(?P<key>[a-zA-Z0-8]+)$", riak_views.search, name="search"),
    url("^write/(?P<key>[a-zA-Z0-8]+)$", riak_views.write, name="write"),
    url("^update/(?P<key>[a-zA-Z0-8]+)$", riak_views.update, name="update"),
    url("^delete/(?P<key>[a-zA-Z0-8]+)$", riak_views.delete, name="delete"),
]