var graphData;
$.ajax({
    method: "GET",
    url: "/graphrestapi/1",
    success: drawLessonsGraph,
    error: function (error_data) {
        console.log("can't get data for lessons graph");
        console.log(error_data);
        drawGraph({});
    }
});

function drawLessonsGraph(data) {
    var ctx = document.getElementById("lessonsGraph");
    var graph = new Chart(ctx, {
        type: "bar",
        data: data,
        options: {
        scales: {
            xAxes: [{
                stacked: true
            }],
            yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
        }
    }
    });
    ctx = graph;
}
