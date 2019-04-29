function displayStudentDynGraph(student, subject) {
    var graphData;
    $.ajax({
        method: "GET",
        url: "/graphrestapi/" + student +"_" + subject,
        success: drawDynGraph,
        error: function (error_data) {
            console.log("can't get data for dynamics graph");
            console.log(error_data);
            drawDynGraph({});
        }
    });
}

function drawDynGraph(data) {
    var ctx = document.getElementById("dynamicsGraph");
    var graph = new Chart(ctx, {
        type: "line",
        data: data,
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 100,
                        fontColor: '#FFFFFF'
                    }
                }],
                xAxes: [{ticks: {fontColor: '#FFFFFF'}}]
            }
        }
    })
    ctx = graph;
}
