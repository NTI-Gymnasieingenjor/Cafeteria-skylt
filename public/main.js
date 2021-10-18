function startTime() {
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    m = checkTime(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
    var t = setTimeout(startTime, 1000);
}
function checkTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}
function closedDisplay(){
    var d = new Date();
    var hour = d.getHours();
    var min = d.getMinutes();

    hour = 8;
    min = 35;

    // If time is during cafe closed hours, show closed sign and hide slide carousel
    if((hour <= 7) || (hour <= 8 && min < 30) || (hour == 11 && min >= 30) || (hour == 15 && min >= 45) || (hour >= 16)){ 
        document.getElementById("closed").classList.remove('hidden');
        
        document.getElementById("open").classList.add('hidden');
        console.log("cafe closed");
    }
    else{
        document.getElementById("closed").classList.add('hidden');
        
        document.getElementById("open").classList.remove('hidden');
        console.log("cafe open");
    }

    var t = setTimeout(closedDisplay, 10000); // Calls closedDisplay() again after 10 seconds to update
}
startTime();
closedDisplay();