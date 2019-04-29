/*** USER SETTINGS ***/
// transition
let FADE_TIME = 700;
let CLICKED_TIME = 1500;

/********************************** slider ********************************/
$('.previous').click(function () {
    slick(-1);
    event.stopPropagation();
    drawCallTopGraph();
});

$('.next').click(function () {
    slick(1);
    event.stopPropagation();
    drawCallTopGraph();
});

function slick(delta) {
    let cur_theme = $(".cur_theme");

    let UPPER_BOUND = 7;//parseInt($(".theme_slider").attr('id'));
    let LOWER_BOUND = 1;

    let current = parseInt(cur_theme.attr("id"));

    if (current === UPPER_BOUND && delta > 0) {
        current = LOWER_BOUND;
    } else if (current === LOWER_BOUND && delta < 0 ) {
        current = UPPER_BOUND;
    } else {
        current = current + delta;
    }

    cur_theme.attr("id", current);

    $(".cur_theme, .chart").fadeOut(FADE_TIME, function () {
        // cur_theme.html("[" + current + "]");;

    //     $.ajax({
    // method: "GET",
    // url: "/graphrestapi/subjname/" + document.getElementsByClassName("cur_theme")[0].getAttribute("id"),
    //         success: function (data) {
    //         $(".cur_theme").html(data["subject"]);
    //         console.log(data["subject"]);
    //     },
    //         error: function (data) {
    //         $(".cur_theme").html(data["subject"]);
    //         }
    //     });

        $(".cur_theme, .chart").fadeIn(FADE_TIME);
        // cur_theme.html(label)
    });

    console.log(current)
}
/********************************** fading-expanding ********************************/
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

