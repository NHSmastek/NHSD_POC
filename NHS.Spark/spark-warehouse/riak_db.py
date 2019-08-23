# import riak_machine
import riak

TrustRegionMapData= {
        'R1': [{'Region_Code':'R1'},'REM', 'RCF', 'RBS', 'RFF', 'RXL', 'RMC', 'RAE', 'RWY', 'RLN', 'RJR', 'RXP', 'RP5', 'RJN', 'RXR', 'RR7', 'RCD', 'RWA', 'RXN', 'RR8', 'RBQ', 'R0A', 'REP', 'RBT', 'RXF', 'RNL', 'RVW', 'RJL', 'RTF', 'RW6', 'RQ6', 'RM3', 'RCU', 'RHQ', 'RTR', 'RE9', 'RVY', 'RBN', 'RWJ', 'RMP', 'RBV', 'REN', 'RTD', 'RFR', 'RET', 'RTX', 'RWW', 'RBL', 'RRF', 'RCB'],
        'R2': [{'Region_Code':'R2'},'RDD', 'RC1', 'RQ3', 'RJF', 'RGT', 'RFS', 'RDE', 'RTG', 'RWH', 'R1L', 'RLT', 'RR1', 'RGQ', 'RGP', 'RNQ', 'RC9', 'RQ8', 'RD8', 'RM1', 'RGN', 'RNS', 'RX1', 'RGM', 'RXK', 'RK5', 'RXW', 'RJC', 'RAJ', 'RNA', 'RQW', 'RCX', 'RL1', 'RRJ', 'RL4', 'RWD', 'RRK', 'RKB', 'RWE', 'RJE', 'RBK', 'RWG', 'RGR', 'RWP', 'RLQ'],
        'R3': [{'Region_Code':'R3'},'RF4', 'R1H', 'RQM', 'RJ6', 'RVR', 'RP4', 'RJ1', 'RQX', 'RYJ', 'RJZ', 'RAX', 'RJ2', 'RAP', 'RT3', 'RAL', 'RAN', 'RJ7', 'RAS', 'RPY', 'RKE', 'RRV'],
        'R4': [{'Region_Code':'R4'},'RTK', 'RXH', 'RXQ', 'RN7', 'RBD', 'RVV', 'RXC', 'RDU', 'RTE', 'RN3', 'RN5', 'R1F', 'RWF', 'RPA', 'RVJ', 'RBZ', 'RTH', 'RK9', 'RD3', 'RHU', 'RPC', 'RHW', 'REF', 'RH8', 'RA2', 'RD1', 'RNZ', 'RTP', 'RBA', 'RDZ', 'RA9', 'RHM', 'RA7', 'RYR', 'RA3', 'RA4']
    }

# jsson ="{'TrustRegionMapData': {'R1': [{'Region_Code':'R1'},'REM', 'RCF', 'RBS', 'RFF', 'RXL', 'RMC', 'RAE', 'RWY', 'RLN', 'RJR', 'RXP', 'RP5', 'RJN', 'RXR', 'RR7', 'RCD', 'RWA', 'RXN', 'RR8', 'RBQ', 'R0A', 'REP', 'RBT', 'RXF', 'RNL', 'RVW', 'RJL', 'RTF', 'RW6', 'RQ6', 'RM3', 'RCU', 'RHQ', 'RTR', 'RE9', 'RVY', 'RBN', 'RWJ', 'RMP', 'RBV', 'REN', 'RTD', 'RFR', 'RET', 'RTX', 'RWW', 'RBL', 'RRF', 'RCB'],'R2': [{'Region_Code':'R2'},'RDD', 'RC1', 'RQ3', 'RJF', 'RGT', 'RFS', 'RDE', 'RTG', 'RWH', 'R1L', 'RLT', 'RR1', 'RGQ', 'RGP', 'RNQ', 'RC9', 'RQ8', 'RD8', 'RM1', 'RGN', 'RNS', 'RX1', 'RGM', 'RXK', 'RK5', 'RXW', 'RJC', 'RAJ', 'RNA', 'RQW', 'RCX', 'RL1', 'RRJ', 'RL4', 'RWD', 'RRK', 'RKB', 'RWE', 'RJE', 'RBK', 'RWG', 'RGR', 'RWP', 'RLQ'],'R3': [{'Region_Code':'R3'},'RF4', 'R1H', 'RQM', 'RJ6', 'RVR', 'RP4', 'RJ1', 'RQX', 'RYJ', 'RJZ', 'RAX', 'RJ2', 'RAP', 'RT3', 'RAL', 'RAN', 'RJ7', 'RAS', 'RPY', 'RKE', 'RRV'],'R4': [{'Region_Code':'R4'},'RTK', 'RXH', 'RXQ', 'RN7', 'RBD', 'RVV', 'RXC', 'RDU', 'RTE', 'RN3', 'RN5', 'R1F', 'RWF', 'RPA', 'RVJ', 'RBZ', 'RTH', 'RK9', 'RD3', 'RHU', 'RPC', 'RHW', 'REF', 'RH8', 'RA2', 'RD1', 'RNZ', 'RTP', 'RBA', 'RDZ', 'RA9', 'RHM', 'RA7', 'RYR', 'RA3', 'RA4']}}"
# jssss=TrustRegionMapData.toJSON()
# riak=riak_machine.riak_machine()
# trust_data="TrustData:{RR1:{E1:95,E2:96,E3:97,E4:50}, RR2:{E1:95,E2:96,E3:97,E4:50}, RR3:{E1:95,E2:96,E3:97,E4:50},RR4:{E1:95,E2:96,E3:97,E4:50}}"
# region_data="RegionData:{R1:{E1:95,E2:96,E3:97,E4:50},R2:{E1:95,E2:96,E3:97,E4:50},R3:{E1:95,E2:96,E3:97,E4:50},R8:{E1:95,E2:96,E3:97,E4:50} }"

# for item in TrustRegionMapData:
#     print(item)
#     print(TrustRegionMapData[item])
#     riak.write_to_riak("TrustRegionMap",item,TrustRegionMapData[item])


# def get_data_from_inner():
def get_data_from_inner(bucket_name, search_key,mapping_key_name):
    trust_dict = {}
    client = riak.RiakClient(host="35.176.37.177", http_port=8087)
    query = client.add(bucket_name)
    query_str = "function(v) {\
        var val = JSON.parse(v.values[0].data);\
            return [val[0]];\
        # for (var key in val) {\
        #     if (val[key]['"+ mapping_key_name+"']=='" + search_key+ "'){\
        #         return [val[key]];\
        #     }\
        # }\
    }"
    # query.map(query_str)
    for trust_data in query.run():
            trust_dict[search_key] = trust_data

    # try:
    #     for trust_data in query.run():
    #         trust_dict[search_key] = trust_data
    # except riak.RiakError:
    #     return trust_dict
    # TODO :- Get Trust Peers
    print(trust_dict)

get_data_from_inner("TrustPerformance","RR8","Org_Code")
# riak.write_to_riak("TrustRegionMap","TrustRegionMapData",TrustRegionMapData)