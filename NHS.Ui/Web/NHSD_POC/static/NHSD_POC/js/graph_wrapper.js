var grapType =
{
    TvP: "TvP",
    TvR: "TvR",
    Regions: "Regions",
}

var graphOption =
{
    headerRow: {
        header: ['Events'],
        rows: [['E1'], ['E2'], ['E3'], ['E4']]
    }
};

var dummychartdata = {};
var headerRow = graphOption.headerRow

function createChartsData() {
    show_Hide_panel();
    var datacreated = {}
    Object.keys(grapType).forEach(key => {
        datacreated[key] = JSON.parse(JSON.stringify(headerRow));
    });

    var i = 0;
    //TVP
    Object.keys(ApiResponse.Trust_Data).forEach(trust => {
        datacreated.TvP.header[i + 1] = trust;
        datacreated.TvP.rows[0][i + 1] = ApiResponse.Trust_Data[trust]["E1"];
        datacreated.TvP.rows[1][i + 1] = ApiResponse.Trust_Data[trust]["E2"];
        datacreated.TvP.rows[2][i + 1] = ApiResponse.Trust_Data[trust]["E3"];
        datacreated.TvP.rows[3][i + 1] = ApiResponse.Trust_Data[trust]["E4"];
        i++;
    });

    //Region
    i = 0;
    Object.keys(ApiResponse.Region_Data).forEach(region => {
        datacreated.Regions.header[i + 1] = region;
        datacreated.Regions.rows[0][i + 1] = ApiResponse.Region_Data[region]["E1"];
        datacreated.Regions.rows[1][i + 1] = ApiResponse.Region_Data[region]["E2"];
        datacreated.Regions.rows[2][i + 1] = ApiResponse.Region_Data[region]["E3"];
        datacreated.Regions.rows[3][i + 1] = ApiResponse.Region_Data[region]["E4"];
        i++;
    });

    //TVR    
    Object.keys(ApiResponse.Trust_Data).forEach(trust => {
        if (trust == org_Code) {
            datacreated.TvR.header[1] = trust;
            datacreated.TvR.rows[0][1] = ApiResponse.Trust_Data[trust]["E1"];
            datacreated.TvR.rows[1][1] = ApiResponse.Trust_Data[trust]["E2"];
            datacreated.TvR.rows[2][1] = ApiResponse.Trust_Data[trust]["E3"];
            datacreated.TvR.rows[3][1] = ApiResponse.Trust_Data[trust]["E4"];
        }
    });
    Object.keys(ApiResponse.Region_Data).forEach(region => {
        if (region == region_code) {
            datacreated.TvR.header[2] = region;
            datacreated.TvR.rows[0][2] = ApiResponse.Region_Data[region]["E1"];
            datacreated.TvR.rows[1][2] = ApiResponse.Region_Data[region]["E2"];
            datacreated.TvR.rows[2][2] = ApiResponse.Region_Data[region]["E3"];
            datacreated.TvR.rows[3][2] = ApiResponse.Region_Data[region]["E4"];
        }
    });

    //Average calculation 
    Object.keys(datacreated).forEach(function (key) {
        var type = datacreated[key];
        var j = Object.keys(datacreated[key].header).length;
        datacreated[key].header[j] = "Average";

        Object.keys(datacreated[key].rows).forEach(function (r) {
            var k = Object.keys(datacreated[key].rows[r]).length;
            var sum = 0;
            for (var i = 1; i < k; i++) {
                sum += datacreated[key].rows[r][i];
            }
            var avg = sum / (k - 1);
            datacreated[key].rows[r][k] = parseInt(avg);
        });
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
                vAxis: { title: 'Transition Time (in days)' },                
                seriesType: 'bars',
                series: { 4: { type: 'line' } },
                colors: ['#3366cc', '#dc3912', '#ff9900', '#109618', '#990099']
            }
        },
        Regions: {
            data: {
                header: datacreated.Regions.header,
                rows: [datacreated.Regions.rows[0], datacreated.Regions.rows[1], datacreated.Regions.rows[2], datacreated.Regions.rows[3]],
                grapType: grapType.Regions
            },
            options: {                
                vAxis: { title: 'Transition Time (in days)' },                
                seriesType: 'bars',
                series: { 4: { type: 'line' } },
                colors: ['#dc3912', '#3366cc', '#ff9900', '#109618', '#990099']
            }
        },
        TvR: {
            data: {
                header: datacreated.TvR.header,
                rows: [datacreated.TvR.rows[0], datacreated.TvR.rows[1], datacreated.TvR.rows[2], datacreated.TvR.rows[3]],
                grapType: grapType.TvR
            },
            options: {                
                vAxis: { title: 'Transition Time (in days)' },                
                seriesType: 'bars',
                series: { 2: { type: 'line' } },
                colors: ['#3366cc', '#dc3912', '#990099']
            }
        }
    }
    loadchart(grapType.TvR)
}

function loadchart(type) {
    showHideLoaderChart(true);
    var gt=document.getElementById("current_selected_graph").value
    if(gt != undefined && gt != null && gt != '')
    {
        type=gt
    }
    let obj = dummychartdata[type]
    getTopHeaderTitle(type);
    $("#dvSidePanel"+type).addClass("box-shadow");
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawVisualization);

    function drawVisualization() {
        var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
        var data = [obj.data.header, obj.data.rows[0], obj.data.rows[1], obj.data.rows[2], obj.data.rows[3]]

        //chart.draw(google.visualization.arrayToDataTable(data), obj.options);
        //set column order
        var count = obj.data.header.length;
        var viewHeaders = JSON.parse(JSON.stringify(obj.data.header));
        var matchCode = (type == "TvR") || (type == "TvP") ? org_Code : region_code;
        for (var i = 0; i < count; i++) {
            if (obj.data.header[i] == matchCode) {
                var text = viewHeaders[1];
                viewHeaders[1] = obj.data.header[i];
                viewHeaders[i] = text;
            }
        }

        // build data view
        var preData = google.visualization.arrayToDataTable(data);
        var view = new google.visualization.DataView(preData);
        view.setColumns(viewHeaders);
        chart.draw(view, obj.options);

        showHideLoaderChart(false);
    }
}
function getTopHeaderTitle(type){
    var topText="",PeersTrust="",Trustresult=[],isTrustExist;
    if(type == "TvP"){
        Trustresult = ApiResponse.Trust_Data;
        isTrustExist = org_Code;  
    }else if(type == "Regions"){
        Trustresult = ApiResponse.Region_Data;
        isTrustExist = region_code;
    }else{}
    Object.keys(Trustresult).forEach(trust => {
         if(trust != isTrustExist){
            PeersTrust += trust+','
         }
    });
    if(type == "TvR"){
        topText = 'Derived waiting time of trust '+org_Code+' with its underlying region '+region_code+'';
    }else if(type == "TvP"){
        topText = 'Derived waiting time of trust '+org_Code+' with peers ('+PeersTrust.slice(0, -1)+'), underlying the same region '+region_code+'';
    }else if(type == "Regions"){
        topText = 'Derived waiting time of underlying region '+region_code+' with other regions '+PeersTrust.slice(0, -1)+'';
    }else{}
    $('#region_nd_other').show();
    $('#region_display').html(topText);
}