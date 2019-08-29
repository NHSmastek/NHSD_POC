config = {
    'App_Path': 'local',
    'App_Name': 'Simple App',
    'IsLocal': True,
    'Start_Delay':100,
    'Interval':100,
    'Files': {
        'TrustDataFile': 'NhsdSampleData_1Lac.csv',
        'TrustRegionMappingFile': 'NhsdROMapping.csv',
    },
    'Riak': {
        'Ip': "35.176.37.177", 'Port': 8087,
        'Buckets': {
            "Trust": "TrustPerformance",
            "Region": "RegionPerformance",
            "TRUST_REGION_MAP": "TrustRegionMap",
            "Trusts_Region_Map": "test"
        },
        'BucketsKey': {
            "Trust": "TrustData",
            "Region": "RegionData",
            "TRUST_REGION_MAP": "TrustRegionMapData"
        }
    }
}

sparkReadFormat = {
    'options': {
        'header': str('true'),
        'treatEmptyValuesAsNulls': str('true'),
        'inferSchema': str('true'),
        'mode': str('DROPMALFORMED'),
        'timestampFormat': str('MM-dd-yyyy hh mm ss')
    }
}
