function startTime() {
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    m = checkTime(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}
startTime();