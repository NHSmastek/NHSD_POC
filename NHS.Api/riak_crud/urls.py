from django.conf.urls import url
from . import views as riak_views

urlpatterns = [
    url("^(?P<bucket>[a-zA-Z]+)/search/(?P<key>[a-zA-Z0-8]+)$", riak_views.search, name="search"),
    url("^(?P<bucket>[a-zA-Z]+)/write/(?P<key>[a-zA-Z0-8]+)$", riak_views.write, name="write"),
    url("^(?P<bucket>[a-zA-Z]+)/update/(?P<key>[a-zA-Z0-8]+)$", riak_views.update, name="update"),
    url("^(?P<bucket>[a-zA-Z]+)/delete/(?P<key>[a-zA-Z0-8]+)$", riak_views.delete, name="delete"),
]