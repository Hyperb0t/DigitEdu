$.getScript('/static/main/mainPage/js/timer/digital-countdown.js', function () {
    $(function () {
        $("#this_clock").countdownDigital({
            dateTo: '2019-05-20T17:00'
        });
    });
});