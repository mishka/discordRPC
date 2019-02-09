function CalcTime(time)
{   
    var hrs = ~~(time / 3600);
    var mins = ~~((time % 3600) / 60);
    var secs = ~~time % 60;

    var ret = "";

    if (hrs > 0) {
        ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
    }

    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
}

function getTime() {
    var ytplayer = document.getElementById("movie_player");
    var duration = CalcTime(ytplayer.getDuration());
    var current = ytplayer.getCurrentTime() + '';
    var editTime = current.split('.')[0]
    if (editTime > 60) {
        console.log(CalcTime(current) + ' / ' + duration);
    } else {
        console.log(CalcTime(editTime) + ' / ' + duration)
    }
}

getTime();