from django.urls import path
from . import views as riak_views

urlpatterns = [
    # CRUD for Trust
    path("search_trust/<str:trust_name>/", riak_views.search_trust, name="search_trust"),
    path("get_trust_list/", riak_views.get_trust_list, name="trust_list"),
]
