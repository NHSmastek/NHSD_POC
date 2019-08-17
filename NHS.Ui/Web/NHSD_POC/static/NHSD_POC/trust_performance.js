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

window.onload = function() {
    get_trust_list()
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
