config={
    'Helper':{'TrustRegionMapData':
    {
        'R1': [{'Region_Code':'R1'},'REM', 'RCF', 'RBS', 'RFF', 'RXL', 'RMC', 'RAE', 'RWY', 'RLN', 'RJR', 'RXP', 'RP5', 'RJN', 'RXR', 'RR7', 'RCD', 'RWA', 'RXN', 'RR8', 'RBQ', 'R0A', 'REP', 'RBT', 'RXF', 'RNL', 'RVW', 'RJL', 'RTF', 'RW6', 'RQ6', 'RM3', 'RCU', 'RHQ', 'RTR', 'RE9', 'RVY', 'RBN', 'RWJ', 'RMP', 'RBV', 'REN', 'RTD', 'RFR', 'RET', 'RTX', 'RWW', 'RBL', 'RRF', 'RCB'],
        'R2': [{'Region_Code':'R2'},'RDD', 'RC1', 'RQ3', 'RJF', 'RGT', 'RFS', 'RDE', 'RTG', 'RWH', 'R1L', 'RLT', 'RR1', 'RGQ', 'RGP', 'RNQ', 'RC9', 'RQ8', 'RD8', 'RM1', 'RGN', 'RNS', 'RX1', 'RGM', 'RXK', 'RK5', 'RXW', 'RJC', 'RAJ', 'RNA', 'RQW', 'RCX', 'RL1', 'RRJ', 'RL4', 'RWD', 'RRK', 'RKB', 'RWE', 'RJE', 'RBK', 'RWG', 'RGR', 'RWP', 'RLQ'],
        'R3': [{'Region_Code':'R3'},'RF4', 'R1H', 'RQM', 'RJ6', 'RVR', 'RP4', 'RJ1', 'RQX', 'RYJ', 'RJZ', 'RAX', 'RJ2', 'RAP', 'RT3', 'RAL', 'RAN', 'RJ7', 'RAS', 'RPY', 'RKE', 'RRV'],
        'R4': [{'Region_Code':'R4'},'RTK', 'RXH', 'RXQ', 'RN7', 'RBD', 'RVV', 'RXC', 'RDU', 'RTE', 'RN3', 'RN5', 'R1F', 'RWF', 'RPA', 'RVJ', 'RBZ', 'RTH', 'RK9', 'RD3', 'RHU', 'RPC', 'RHW', 'REF', 'RH8', 'RA2', 'RD1', 'RNZ', 'RTP', 'RBA', 'RDZ', 'RA9', 'RHM', 'RA7', 'RYR', 'RA3', 'RA4']
        }},
        'Riak':{
            'Ip':"18.220.160.111",'Port':8087,
            'Buckets':{"Trust":"TrustPerformance","Region":"RegionPerformance","TRUST_REGION_MAP":"TrustRegionMap"},
            'BucketsKey':{"Trust":"TrustData","Region":"RegionData","TRUST_REGION_MAP":"TrustRegionMapData"}
        }
}        