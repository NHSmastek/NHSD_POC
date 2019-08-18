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

function loadchart()
{
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawVisualization);

    function drawVisualization() {
      // Some raw data (not necessarily accurate)
      var data = google.visualization.arrayToDataTable([
        ['Events', 'RR8', 'RR1', 'RR2', 'RR3','Average'],
        ['E1',  5,      10,         5,           10,7.5],
        ['E2',  10,      20,        10,           20,15],
        ['E3',  15,      30,        15,           30,22.5],
        ['E4',  5,      10,         5,           10,7.5],
      ]);

      var options = {
        title : 'Trust RR8 vs Peers',
        vAxis: {title: 'Transition Time (in days)'},
        hAxis: {title: 'RR8 and Peers'},
        seriesType: 'bars',
        series: {4: {type: 'line'}}
      };

      var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
      chart.draw(data, options);
}
}
window.onload = function() {
    get_trust_list();
    loadchart()
}