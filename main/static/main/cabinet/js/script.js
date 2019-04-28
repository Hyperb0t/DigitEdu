/*
$(".block").click(function() {
    $(this).toggleClass("clicked");
    if (this.className.includes("clicked")) {
        $(this).find(".chart").css("display", "block");
    } else {
        $(this).find(".chart").css("display", "none");
    }
});
*/


$(".block").click(function(){
    // console.log("active!!!");
    // $(className).css("background-image", 'url("img/bg_rating_clicked.png")');

    // transition
    let FADE_TIME = 700;
    let CLICKED_TIME = 1500;

    let fullClassName = this.className;
    let className = "." + fullClassName.split(" ")[0];

    $(className).find(".content").fadeOut(FADE_TIME, function () {
        className = touch(fullClassName); // invert className
        setTimeout(function () {
            if ($(className).hasClass("clicked")) {
                $(className).find(".content, .chart_block").fadeIn(FADE_TIME);
            } else {
                $(className).find(".chart_block").css("display", "none");
                $(className).find(".content").fadeIn(FADE_TIME);
            }

        }, CLICKED_TIME);
    });
});

function touch(fullClassName) {
    let className = "." + fullClassName.split(" ")[0];
    console.log(className);
    $(className).toggleClass("clicked");

    if (fullClassName.includes("clicked")) {
        return className;
    } else {
        return className + ".clicked";
    }

}