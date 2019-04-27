function displayStudentSecondGraph(student) {
    var graphData;
    $.ajax({
        method: "GET",
        url: "/graphrestapi/last/" + student,
        success: drawSecondGraph,
        error: function (error_data) {
            console.log("can't get data for second graph");
            console.log(error_data);
            drawSecondGraph({});
        }
    });
}

function drawSecondGraph(data) {
    var ctx = document.getElementById("secondGraph");
    var graph = new Chart(ctx, {
        type: "bar",
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 100
                    }
                }]
            }
        }
    })
    ctx = graph;
}
