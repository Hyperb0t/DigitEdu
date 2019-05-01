function drawCallTopGraph() {
    subjectR = document.getElementsByClassName("cur_theme")[0].getAttribute("id");
    var graphData;
$.ajax({
    method: "GET",
    url: "/graphrestapi/top/" + subjectR,
    success: function (data) {
        drawTopGraph(data);
    },
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
    let label = (data["datasets"][0]["label"]).replace('Топ лучших студентов по предмету ', "").replace(" за последний семестр","");
    $(".cur_theme").html(label);
    // console.log(data["datasets"][0]["label"]);
    console.log(label);
}
