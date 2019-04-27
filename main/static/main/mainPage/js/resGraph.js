function drawCallResGraph() {
    var graphData;
$.ajax({
    method: "GET",
    url: "/graphrestapi/res",
    success: drawResGraph,
    error: function (error_data) {
        console.log("can't get data for lessons graph");
        console.log(error_data);
        drawResGraph({});
    }
});
}


function drawResGraph(data) {
    var ctx = document.getElementById("resGraph");
    var graph = new Chart(ctx, {
        type: "pie",
        data: data,
        options: {}
    });
    ctx = graph;
}
