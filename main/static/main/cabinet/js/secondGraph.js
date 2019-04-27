function displayStudentSecondGraph(student) {
    var graphData;
    $.ajax({
        method: "GET",
        url: "/graphrestapi/" + student + "_1",
        success: drawSecondGraph,
        error: function (error_data) {
            console.log("can't get data for second graph");
            console.log(error_data);
            drawGraph({});
        }
    });
}

function drawSecondGraph(data) {
    var ctx = document.getElementById("secondGraph");
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
