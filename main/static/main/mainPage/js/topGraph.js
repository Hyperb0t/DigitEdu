function drawCallTopGraph() {
    subjectR = document.getElementById("topGraph").getAttribute("subjectId")
    var graphData;
$.ajax({
    method: "GET",
    url: "/graphrestapi/top/" + subjectR,
    success: drawTopGraph,
    error: function (error_data) {
        console.log("can't get data for top graph");
        console.log(error_data);
        drawTopGraph({});
    }
});
}


function drawTopGraph(data) {
    var ctx = document.getElementById("topGraph");
    var graph = new Chart(ctx, {
        type: "horizontalBar",
        data: data,
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 100,
                        fontColor: '#FFFFFF',
                        fontSize: 16
                    }
                }],
                yAxes: [{ticks: { fontColor: '#FFFFFF', fontSize: 18 }}]
            },
            legend: {
                labels: {
                    fontColor: '#FFFFFF',
                    fontSize: 14
                }
            }
        }}
    ,{scaleFontColor: "#FFFFFF"});
    ctx = graph;
}
