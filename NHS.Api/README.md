DJANGO REST FRAMEWORK - RIAK INTEGRATION

INTRODUCTION :-
This application exposes django rest api for interaction with RIAK

INSTALLATION :-
Run requirement27.txt file.

API's :-
Search : "http://<Domain Name>:<port_number>/<bucket_name>/search/<key_name>/"
Write : "http://<Domain Name>:<port_number>/<bucket_name>/write/<key_name>/"
Delete : "http://<Domain Name>:<port_number>/<bucket_name>/delete/<key_name>/"
Update : "http://<Domain Name>:<port_number>/<bucket_name>/update/<key_name>/"

**Note :- Update API is not functional till now. bucket_name(Table name) and key_name(Name of Trust).

Mock Data :
The schema of Mock data is temporary and can be changed. For time being I have hard coded the data to be written in RIAK.

"RR8" : {
    "E1": {
        "avg_gap": 10,
        "patient_count": 100,
    },
    "E2": {
        "avg_gap": 5,
        "patient_count": 100,
    },
    "E3": {
        "avg_gap": 8,
        "patient_count": 100,
    },
    "E4": {
        "avg_gap": 8,
        "patient_count": 100,
    },
    "E5": {
        "avg_gap": 6,
        "patient_count": 100,
    }
}

RIAK SERVER CONFIG :-
Riak server config is present inside the riak_crud application. For time being the host is present at "18.217.190.19"
Validate the above host is up and running before running the application. Try to ping the host server. If ping failed 
contact Akshay or Prabhat for starting the host server.