
var ApiResponse = {}
var region_code, org_Code;
function IsValidTrust(trust_code){
    var IsValid;
    $("#trustresults > option").each(function(i){
          trust_cd = $(this).text().trim();
          if(trust_cd == trust_code.toUpperCase()){
            IsValid = true;
          }
    });
    return IsValid;
}
function get_performance_data_for_map(trust_code) {
    if(trust_code == '' || IsValidTrust(trust_code) != true)
    {
        document.getElementById("dv_chart_no_selection_panel").style.display = "block";
        document.getElementById("default-img").style.display = "block";
        document.getElementById("loader").style.display = "none";
        document.getElementById("dv_chart_row_panel").style.display = "none";
        return false;
    }    
    showHideLoaderContent(true);
    showHideLoaderChart(true);

    show_Hide_panel()

    $.ajax({
        url: ajax_url + "search_trust/" + trust_code
    }).then(function (data) {
        //Use response here        
        ApiResponse = {};        
        ApiResponse = JSON.parse(data);       
        region_code = ApiResponse.Region_Code;
        org_Code = trust_code;
        createChartsData()
        loadchart(grapType.TvR)
    });
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


//Loader on very first time on content
function showHideLoaderContent(loaderStatus) {
    if (loaderStatus) {
        document.getElementById("default-img").style.display = "none";
        document.getElementById("loaderbg").style.display = "block";
        document.getElementById("loader").style.display = "block";
    }
    else {
        document.getElementById("loaderbg").style.display = "none";
        document.getElementById("loader").style.display = "none";
        document.getElementById("default-img").style.display = "block";
    }
}

// Loader for only chart div
function showHideLoaderChart(loaderStatus) {
    if (loaderStatus) {
        document.getElementById("loaderbg").style.display = "block";
    }
    else {
        document.getElementById("loaderbg").style.display = "none";
    }
}
window.onload = function () {
    show_Hide_panel()
}
function showchart(chartType)
{
    document.getElementById("current_selected_graph").value = chartType;
    
    loadchart(chartType)
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
