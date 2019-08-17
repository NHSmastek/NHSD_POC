DJANGO REST FRAMEWORK - RIAK INTEGRATION

INTRODUCTION :-
This application exposes django rest api for interaction with RIAK

INSTALLATION :-
Run requirement27.txt file.

API's :-
Trust CRUD :-
Search : "http://<Domain Name>:<port_number>/search_trust/<trust_key_name>/"
# Write : "http://<Domain Name>:<port_number>/write_trust/<trust_key_name>/"
# Delete : "http://<Domain Name>:<port_number>/delete_trust/<trust_key_name>/"
# Update : "http://<Domain Name>:<port_number>/update_trust/<trust_key_name>/"

Region CRUD :-
# Write : "http://<Domain Name>:<port_number>/write_region/<region_key_name>/"
# Delete : "http://<Domain Name>:<port_number>/delete_region/<region_key_name>/"
# Update : "http://<Domain Name>:<port_number>/update_region/<region_key_name>/"

**Note :- Update API is not functional till now. Key_name(Name of Trust / Name of Region).

Mock Data :
The schema of Mock data is temporary and can be changed. For time being I have hard coded the data to be written in RIAK.

TrustData = {
    "E1": 20,
    "E2": 100,
    "E3": 25,
    "E4": 32,
}

RegionData = {
    "E1": 20,
    "E2": 30,
    "E3": 40,
    "E4": 50,
}


RIAK SERVER CONFIG :-
Riak server config is present inside the riak_crud application. For time being the host is present at "35.176.37.177"
and port number "8087"
Validate the above host is up and running before running the application. Try to ping the host server.