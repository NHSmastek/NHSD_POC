DJANGO REST FRAMEWORK - RIAK INTEGRATION

INTRODUCTION :-
This application exposes django rest api for interaction with RIAK

INSTALLATION :-
Run requirement27.txt file.

API's :-
LIST OF TRUSTS
Get : "http://<Domain Name>:<port_number>/get_trust_list"

Trust CRUD :-
Search : "http://<Domain Name>:<port_number>/search_trust/<trust_key_name>"
# Write : "http://<Domain Name>:<port_number>/write_trust"
# Delete : "http://<Domain Name>:<port_number>/delete_trust"
# Update : "http://<Domain Name>:<port_number>/update_trust"

Region CRUD :-
# Write : "http://<Domain Name>:<port_number>/write_region"
# Delete : "http://<Domain Name>:<port_number>/delete_region"
# Update : "http://<Domain Name>:<port_number>/update_region"

**Note :- Update API is not functional till now. Key_name(Name of Trust / Name of Region).

Mock Data :
The schema of Mock data is temporary and can be changed. For time being I have hard coded the data to be written in RIAK.

TrustData = [
    {"OrgCode": "RR8", "E1": 21, "E2": 23, "E3": 24, "E4": 25},
    {"OrgCode": "RR1", "E1": 21, "E2": 23, "E3": 24, "E4": 25},
    {"OrgCode": "RR2", "E1": 21, "E2": 23, "E3": 24, "E4": 25},
    {"OrgCode": "RR3", "E1": 21, "E2": 23, "E3": 24, "E4": 25},
    {"OrgCode": "RR4", "E1": 21, "E2": 23, "E3": 24, "E4": 25},
]

RegionData = [
    {"RegionCode": "R1", "E1": 11, "E2": 12, "E3": 13, "E4": 14},
    {"RegionCode": "R2", "E1": 11, "E2": 12, "E3": 13, "E4": 14},
    {"RegionCode": "R3", "E1": 11, "E2": 12, "E3": 13, "E4": 14},
    {"RegionCode": "R4", "E1": 11, "E2": 12, "E3": 13, "E4": 14},
]


RIAK SERVER CONFIG :-
Riak server config is present inside the riak_crud application. For time being the host is present at "35.176.37.177"
and port number "8087"
Validate the above host is up and running before running the application. Try to ping the host server.