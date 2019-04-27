var graphData;
$.ajax({
    method: "GET",
    url: "/graphrestapi/a_a",
    success: drawDynGraph,
    error: function (error_data) {
        console.log("can't get data for dynamics graph");
        console.log(error_data);
        drawGraph({});
    }
});

function drawDynGraph(data) {
    var ctx = document.getElementById("dynamicsGraph");
    var graph = new Chart(ctx, {
        type: "line",
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    })
    ctx = graph;
}
