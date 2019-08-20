from django.conf.urls import url
from . import views as riak_views

urlpatterns = [
    # CRUD for Trust
    url("^search_trust/(?P<trust_name>[a-zA-Z0-8]+)$", riak_views.search_trust, name="search_trust"),
    # url("^write_trust", riak_views.write_trust, name="write_trust"),
    # url("^update_trust", riak_views.update_trust, name="update_trust"),
    # url("^delete_trust", riak_views.delete_trust, name="delete_trust"),

    # CRUD for Region
    # url("^write_region", riak_views.write_region, name="write_region"),
    # url("^update_region", riak_views.update_region, name="update_region"),
    # url("^delete_region", riak_views.delete_region, name="delete_region"),
]