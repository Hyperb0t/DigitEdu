$(".block").click(function() {
    $(this).toggleClass("clicked");
    if (this.className.includes("clicked")) {
        $(this).find(".chart").css("display", "block");
    } else {
        $(this).find(".chart").css("display", "none");
    }
});
