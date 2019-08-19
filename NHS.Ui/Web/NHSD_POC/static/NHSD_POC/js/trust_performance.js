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
Tvp:"TvP",
TvR:"TvR",
Regions:"Regions",
}
var ApiResponse = {
    "Region_Code": "R1",
    "Region_Data": [
        { "Region_code": "R1", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Region_code": "R1", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Region_code": "R1", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Region_code": "R1", "E1": "95", "E2": "96", "E3": "97", "E4": "50" }
    ],
    "Trust_Data": [
        { "Org_code": "RR1", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Org_code": "RR2", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Org_code": "RR3", "E1": "95", "E2": "96", "E3": "97", "E4": "50" },
        { "Org_code": "RR8", "E1": "95", "E2": "96", "E3": "97", "E4": "50" }
    ]
}
function get_performance_data_for_map(org_Code) {
    alert(org_Code)
    for( i=0;i<ApiResponse.Trust_Data.length;i++)
    {
        header[i+1]=ApiResponse.Trust_Data[i];
        rows[0][i+1]=ApiResponse.Trust_Data["E1"];
        rows[1][i+1]=ApiResponse.Trust_Data["E2"];
        rows[0][i+1]=ApiResponse.Trust_Data["E3"];
        rows[0][i+1]=ApiResponse.Trust_Data["E4"];
    } 
    datacreated.TvP.header
}
var datacreated = {
    TvP: {
        header: ['Events'],
        rows: [
            ['E1'],
            ['E2'],
            ['E3'],
            ['E4']
        ]
    }
};

var dummychartdata = {
    TvP: {
        data: {
            header: ['Events', 'RR8', 'RR1', 'RR2', 'RR3', 'Average'],
            rows: [
                ['E1', 5, 10, 5, 10, 7.5],
                ['E2', 10, 20, 10, 20, 15],
                ['E3', 15, 30, 15, 30, 22.5],
                ['E4', 5, 10, 5, 10, 7.5]
            ],
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
            header: ['Events', 'R1', 'R2', 'R3', 'R4', 'Average'],
            rows: [
                ['E1', 5, 10, 5, 10, 7.5],
                ['E2', 10, 20, 10, 20, 15],
                ['E3', 15, 30, 15, 30, 22.5],
                ['E4', 5, 10, 5, 10, 7.5]
            ],
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
            header: ['Events', 'RR8', 'RR1', 'Average'],
            rows: [
                ['E1', 5, 10, 7.5],
                ['E2', 10, 20, 15],
                ['E3', 15, 30, 22.5],
                ['E4', 5, 10, 7.5]
            ],
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
        data = [obj.data.header, obj.data.rows[0], obj.data.rows[1], obj.data.rows[2], obj.data.rows[3]]
        chart.draw(google.visualization.arrayToDataTable(data), obj.options);
    }
}
window.onload = function() {
    get_trust_list();
    loadchart(grapType.TvR)
}