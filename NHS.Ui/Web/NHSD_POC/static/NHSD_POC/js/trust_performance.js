
var ApiResponse = {}
function get_performance_data_for_map(trust_code) {
    $.ajax({
        //TODO : replace static url with correct url
        url: "http://172.16.243.211:8009/getDummy"
    }).then(function (data) {
        //Use response here
        ApiResponse = {};
        ApiResponse = data;
        ApiResponse = JSON.parse(JSON.stringify(data));
        createChartsData(trust_code)
    });

}

var grapType =
{
    TvP: "TvP",
    TvR: "TvR",
    Regions: "Regions",
}

function show_Hide_panel() {
    var org_Code_value = document.getElementById("trust_list").value
    if (org_Code_value == '') {
        document.getElementById("dv_chart_row_panel").style.display = "none";
        document.getElementById("dv_chart_no_selection_panel").style.display = "block";
        return;
    } else {
        document.getElementById("dv_chart_row_panel").style.display = 'block';
        document.getElementById("dv_chart_no_selection_panel").style.display = "none";
    }
}

var dummychartdata = {};
var headerRow = {
    header: ['Events'],
    rows: [['E1'], ['E2'], ['E3'], ['E4']]
};


function createChartsData(org_Code) {

    show_Hide_panel();

    var datacreated = {}
    Object.keys(grapType).forEach(key => {    
        datacreated[key] = JSON.parse(JSON.stringify(headerRow));        
    });


    var i=0;
   //TVP
    Object.keys(ApiResponse.Trust_Data).forEach(trust => {    
        datacreated.TvP.header[i+1]=trust;
        datacreated.TvP.rows[0][i+1]=ApiResponse.Trust_Data[trust]["E1"];
        datacreated.TvP.rows[1][i+1]=ApiResponse.Trust_Data[trust]["E2"];
        datacreated.TvP.rows[2][i+1]=ApiResponse.Trust_Data[trust]["E3"];
        datacreated.TvP.rows[3][i+1]=ApiResponse.Trust_Data[trust]["E4"];      
        i++;
    });

   //Region
    i=0;
    Object.keys(ApiResponse.Region_Data).forEach(region => {    
        datacreated.Regions.header[i+1]=region;
        datacreated.Regions.rows[0][i+1]=ApiResponse.Region_Data[region]["E1"];
        datacreated.Regions.rows[1][i+1]=ApiResponse.Region_Data[region]["E2"];
        datacreated.Regions.rows[2][i+1]=ApiResponse.Region_Data[region]["E3"];
        datacreated.Regions.rows[3][i+1]=ApiResponse.Region_Data[region]["E4"];      
        i++;
    });
 
    //TVR    
    Object.keys(ApiResponse.Trust_Data).forEach(trust => {    
        if(trust==org_Code){
            datacreated.TvR.header[1]=trust;
            datacreated.TvR.rows[0][1]=ApiResponse.Trust_Data[trust]["E1"];
            datacreated.TvR.rows[1][1]=ApiResponse.Trust_Data[trust]["E2"];
            datacreated.TvR.rows[2][1]=ApiResponse.Trust_Data[trust]["E3"];
            datacreated.TvR.rows[3][1]=ApiResponse.Trust_Data[trust]["E4"];            
        }
    });    
    Object.keys(ApiResponse.Region_Data).forEach(region => {    
        if(region==ApiResponse.Region_Code){
        datacreated.TvR.header[2]=region;
        datacreated.TvR.rows[0][2]=ApiResponse.Region_Data[region]["E1"];
        datacreated.TvR.rows[1][2]=ApiResponse.Region_Data[region]["E2"];
        datacreated.TvR.rows[2][2]=ApiResponse.Region_Data[region]["E3"];
        datacreated.TvR.rows[3][2]=ApiResponse.Region_Data[region]["E4"];              
        }
    });


    dummychartdata = {};
    dummychartdata = {
        TvP: {
            data: {
                header: datacreated.TvP.header,
                rows: [datacreated.TvP.rows[0], datacreated.TvP.rows[1], datacreated.TvP.rows[2], datacreated.TvP.rows[3]],
                grapType: grapType.Tvp
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
                grapType: grapType.Regions
            },
            options: {
                title: 'Region R1 vs others',
                vAxis: { title: 'Transition Time (in days)' },
                hAxis: { title: 'Region R1 and others' },
                seriesType: 'bars',
                series: { 4: { type: 'line' } }
            }
        },
        TvR: {
            data: {
                header: datacreated.TvR.header,
                rows: [datacreated.TvR.rows[0], datacreated.TvR.rows[1], datacreated.TvR.rows[2], datacreated.TvR.rows[3]],
                grapType: grapType.TvR
            },
            options: {
                title: 'Trust RR8 vs Region R1',
                vAxis: { title: 'Transition Time (in days)' },
                hAxis: { title: 'RR8 and Region R1' },
                seriesType: 'bars',
                series: { 2: { type: 'line' } }
            }
        }
    }
    loadchart(grapType.TvR)
}

function loadchart(type) {
    let obj = dummychartdata[type]
    document.getElementById("current_selected_graph").value = type;
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawVisualization);

    function drawVisualization() {
        var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
        var data = [obj.data.header, obj.data.rows[0], obj.data.rows[1], obj.data.rows[2], obj.data.rows[3]]
        chart.draw(google.visualization.arrayToDataTable(data), obj.options);
    }
}
window.onload = function() {
    show_Hide_panel()
}
