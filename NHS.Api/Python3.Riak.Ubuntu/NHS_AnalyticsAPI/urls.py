from django.urls import path
from . import views as riak_views

urlpatterns = [
    # CRUD for Trust
    path("search_trust/<str:trust_name>/", riak_views.search_trust, name="search_trust"),
    path("get_trust_list/", riak_views.get_trust_list, name="trust_list"),
    # url("^write_trust", riak_views.write_trust, name="write_trust"),
    # url("^update_trust", riak_views.update_trust, name="update_trust"),
    # url("^delete_trust", riak_views.delete_trust, name="delete_trust"),

    # CRUD for Region
    # url("^write_region", riak_views.write_region, name="write_region"),
    # url("^update_region", riak_views.update_region, name="update_region"),
    # url("^delete_region", riak_views.delete_region, name="delete_region"),
]