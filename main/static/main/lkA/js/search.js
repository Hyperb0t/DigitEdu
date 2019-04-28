
var input = document.getElementById("searchBox");

input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.getElementById("searchButton").click();
  }
});

function getStudList() {
    $("#searchBox").tooltip('hide');
    surname = document.getElementById("searchBox").value;
    console.log(surname);
    if(surname != "") {
        $.ajax({
            method: "GET",
            url: "/graphrestapi/search/" + surname,
            success: fillOffers,
            error: (function () {
                console.log("can't get search stud list");
            })
        })
    }
}

function fillOffers(data) {
    console.log(data)
    toolt = ""
    for (let i = 0; i < data["students"].length; i++) {
        toolt += data["students"][i]["name"];
        toolt += " ";
        toolt += data["students"][i]["surname"];
        toolt += '\n';
    }
    document.getElementById("searchBox").removeAttribute("studId")
    document.getElementById("searchBox").setAttribute("data-original-title", toolt);
    if(data["students"].length == 1)
        document.getElementById("searchBox").setAttribute("studId", data["students"][0]["id"]);
    $("#searchBox").tooltip('show');
    return data;
}

function redirectToStudCabinet() {
    toolt = document.getElementById("searchBox").getAttribute("data-original-title");
    if(document.getElementById("searchBox").hasAttribute("studId"))
        document.location.href = '/cabinet/' + document.getElementById("searchBox").getAttribute("studId");
}