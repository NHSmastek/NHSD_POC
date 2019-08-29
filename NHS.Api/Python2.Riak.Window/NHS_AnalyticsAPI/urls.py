from django.conf.urls import url
from . import views as riak_views

urlpatterns = [
    url("^search_trust/(?P<trust_name>[a-zA-Z0-8]+)$", riak_views.search_trust, name="search_trust"),
    url("get_trust_list/", riak_views.get_trust_list, name="trust_list"),
]