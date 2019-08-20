function get_performance_data_for_map(trust_code) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Will arrange the data according to the map
            console.log( JSON.parse(this.responseText))            
        }
    };
    xhttp.open("GET", trust_code, true);
    xhttp.send();
}

var grapType =
    {
        TvP:"TvP",
        TvR:"TvR",
        Regions:"Regions",
    }

var ApiResponse = {
    "Region_Code": "R1",
    "Region_Data": [
        { "Region_code": "R1", "E1": 95, "E2": 86, "E3": 67, "E4": 50 },
        { "Region_code": "R2", "E1": 45, "E2": 90, "E3": 47, "E4": 80 },
        { "Region_code": "R3", "E1": 65, "E2": 36, "E3": 77, "E4": 70 },
        { "Region_code": "R4", "E1": 85, "E2": 66, "E3": 17, "E4": 10 }
    ],
    "Trust_Data": [
        { "Org_code": "RR1", "E1": 95, "E2": 96, "E3": 97, "E4": 50 },
        { "Org_code": "RR2", "E1": 95, "E2": 96, "E3": 97, "E4": 50 },
        { "Org_code": "RR3", "E1": 95, "E2": 96, "E3": 97, "E4": 50 },
        { "Org_code": "RR8", "E1": 95, "E2": 96, "E3": 97, "E4": 50 }
    ]
}

var headerRow= {
    header: ['Events'],
    rows: [['E1'], ['E2'], ['E3'], ['E4']]
};

var datacreated = {};
Object.keys(grapType).forEach(key => {    
    datacreated[key] = headerRow        
});

function get_performance_data_for_map(org_Code) {
    
    //TVP
    for( i=0;i<ApiResponse.Trust_Data.length;i++)
    {       
        datacreated.TvP.header[i+1]=ApiResponse.Trust_Data[i]["Org_code"];
        datacreated.TvP.rows[0][i+1]=ApiResponse.Trust_Data[i]["E1"];
        datacreated.TvP.rows[1][i+1]=ApiResponse.Trust_Data[i]["E2"];
        datacreated.TvP.rows[2][i+1]=ApiResponse.Trust_Data[i]["E3"];
        datacreated.TvP.rows[3][i+1]=ApiResponse.Trust_Data[i]["E4"];        
    } 

    //Regions
    for( i=0;i<ApiResponse.Region_Data.length;i++)
    {
        datacreated.Regions.header[i+1]=ApiResponse.Region_Data[i]["Region_code"];
        datacreated.Regions.rows[0][i+1]=ApiResponse.Region_Data[i]["E1"];
        datacreated.Regions.rows[1][i+1]=ApiResponse.Region_Data[i]["E2"];
        datacreated.Regions.rows[2][i+1]=ApiResponse.Region_Data[i]["E3"];
        datacreated.Regions.rows[3][i+1]=ApiResponse.Region_Data[i]["E4"];
    } 

    //TVR
    for( i=0;i<ApiResponse.Trust_Data.length;i++)
    {
        if(ApiResponse.Trust_Data[i]["Org_code"] == "RR8") //org_Code
        {            
            datacreated.TvR.header[1]=ApiResponse.Trust_Data[i]["Org_code"];
            datacreated.TvR.rows[0][1]=ApiResponse.Trust_Data[i]["E1"];
            datacreated.TvR.rows[1][1]=ApiResponse.Trust_Data[i]["E2"];
            datacreated.TvR.rows[2][1]=ApiResponse.Trust_Data[i]["E3"];
            datacreated.TvR.rows[3][1]=ApiResponse.Trust_Data[i]["E4"];
        }
    } 
    for( i=0;i<ApiResponse.Region_Data.length;i++)
    {
        if(ApiResponse.Region_Data[i]["Region_code"] == "R1") //ApiResponse.Region_Code.value
        {
            datacreated.TvR.header[2]=ApiResponse.Region_Data[i]["Region_code"];
            datacreated.TvR.rows[0][2]=ApiResponse.Region_Data[i]["E1"];
            datacreated.TvR.rows[1][2]=ApiResponse.Region_Data[i]["E2"];
            datacreated.TvR.rows[2][2]=ApiResponse.Region_Data[i]["E3"];
            datacreated.TvR.rows[3][2]=ApiResponse.Region_Data[i]["E4"];
        }
    }   
}

var dummychartdata = {
    TvP: {
        data: {
            header: datacreated.TvP.header,           
            rows: [datacreated.TvP.rows[0], datacreated.TvP.rows[1], datacreated.TvP.rows[2], datacreated.TvP.rows[3]],            
            grapType:grapType.Tvp
        },
        options: {
            title: 'Trust RR8 vs Peers',
            vAxis: { title: 'Transition Time (in days)' },
            hAxis: { title: 'RR8 and Peers' },
            seriesType: 'bars',
            series: { 4: { type: 'line' } }
        }
    },
    Regions: {
        data: {
            header: datacreated.Regions.header,
            rows: [datacreated.Regions.rows[0], datacreated.Regions.rows[1], datacreated.Regions.rows[2], datacreated.Regions.rows[3]],         
            grapType:grapType.Regions
        },
        options: {
            title: 'Region R1 vs others',
            vAxis: { title: 'Transition Time (in days)' },
            hAxis: { title: 'Region R1 and others' },
            seriesType: 'bars',
            series: {4: {type: 'line'}}
          }
    },
    TvR: {
        data: {
            header: datacreated.TvR.header,           
            rows: [datacreated.TvR.rows[0], datacreated.TvR.rows[1], datacreated.TvR.rows[2], datacreated.TvR.rows[3]],
            grapType:grapType.TvR
        },
        options: {
            title: 'Trust RR8 vs Region R1',
            vAxis: { title: 'Transition Time (in days)' },
            hAxis: { title: 'RR8 and Region R1' },
            seriesType: 'bars',
            series: {2: {type: 'line'}}
        }
    }
}

function get_trust_list() {
    // Will get the trust_dict through AJAX call
    var trust_list = [
        {id:"RR8", value:"RR8"},
        {id:"RR1", value:"RR1"},
        {id:"RR2", value:"RR2"},
        {id:"RR3", value:"RR3"},
    ]
    var select = document.getElementById("trust_list")
    trust_list.forEach(function(item) {
        var el = document.createElement("option");
        el.textContent = item.id;
        el.value = item.value;
        select.appendChild(el)
    });
}

function loadchart(type) {
    let obj=dummychartdata[type]
        document.getElementById("current_selected_graph").value = type;
        google.charts.load('current', { 'packages': ['corechart'] });
        google.charts.setOnLoadCallback(drawVisualization);

    function drawVisualization() {
        // Some raw data (not necessarily accurate)
        var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
        var data = [obj.data.header, obj.data.rows[0], obj.data.rows[1], obj.data.rows[2], obj.data.rows[3]]
        chart.draw(google.visualization.arrayToDataTable(data), obj.options);
    }
}
window.onload = function() {
    get_trust_list();
    loadchart(grapType.Regions)
}

get_performance_data_for_map()