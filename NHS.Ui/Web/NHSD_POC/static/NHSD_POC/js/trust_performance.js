
var ApiResponse = {}
function get_performance_data_for_map(trust_code) {
    show_Hide_panel()
    $.ajax({
        //TODO : replace static url with correct url
        // url: "http://172.16.243.211:8009/getDummy"
        url: ajax_url+"search_trust/" + trust_code

    }).then(function (data) {
        //Use response here        
        ApiResponse = {};
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
    var org_Code_value = document.getElementById("trust_input").value
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

    var region_code = ApiResponse.Region_Code;
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
                title: 'Trust ' + org_Code + ' vs Peers',
                vAxis: { title: 'Transition Time (in days)' },
                hAxis: { title: org_Code + ' and Peers' },
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
                title: 'Region ' + region_code + ' vs others',
                vAxis: { title: 'Transition Time (in days)' },
                hAxis: { title: 'Region ' + region_code + ' and others' },
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
                title: 'Trust ' + org_Code + ' vs Region ' + region_code,
                vAxis: { title: 'Transition Time (in days)' },
                hAxis: { title: org_Code + ' and Region ' + region_code },
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
window.onload = function () {
    show_Hide_panel()
}

var search = document.querySelector('#trust_input');
var results = document.querySelector('#trustresults');
var templateContent = document.querySelector('#trustResultsTemplate').content;
search.addEventListener('keyup', function handler(event) {
    while (results.children.length) results.removeChild(results.firstChild);
    var inputVal = new RegExp(search.value.trim(), 'i');
    var clonedOptions = templateContent.cloneNode(true);
    var set = Array.prototype.reduce.call(clonedOptions.children, function searchFilter(frag, el) {
        if (inputVal.test(el.textContent) && frag.children.length < 10) frag.appendChild(el);
        return frag;
    }, document.createDocumentFragment());
    results.appendChild(set);
});
