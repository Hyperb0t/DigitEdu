
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




















/*
    $(className).fadeOut(FADE_TIME, function() {
        // block.toggleClass("clicked");
        $(className + ".clicked").fadeIn(FADE_TIME);
    });*/

/*
    $(this).parent().bind( 'transitionend', function() {
        $(this).find(".content").css("display", "block");
        $(this).find(".content").css("transition", "5s");
    });*/

/*$(this).addEventListener("transitionend", function () {
    console.log("transitioned!");
    /!*if ($(this).hasClass("clicked")) {
        $(this).find(".content")
        $(this).find(".chart_block").css("display", "none");
    } else {
        $(this).find(".chart_block").css("display", "block");
    }*!/
});*/


/*let class_ = this.className;
let key = class_.split(" ")[0].replace("main__", "");
let pic = "";
if (class_.includes("clicked")) {
    pic = "bg_" + key + "_clicked" + ".png";
} else {
    pic = "bg_" + key + ".png";
}
let path = "../img/" + pic;

console.log(class_);
console.log(key);
console.log(pic);
console.log(path);
$(this).css("background", "url(\"" + path + "\") 0 no-repeat");*/

