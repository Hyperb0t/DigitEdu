function drawStudentLessonsGraph(student) {
    var graphData;
    $.ajax({
        method: "GET",
        url: "/graphrestapi/" + student,
        success: drawLessonsGraph,
        error: function (error_data) {
            console.log("can't get data for lessons graph");
            console.log(error_data);
            drawLessonsGraph({});
        }
    });
}


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
