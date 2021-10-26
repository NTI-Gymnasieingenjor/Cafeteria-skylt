var d = new Date();
var day = d.getDay();

//Shows the clock on the website
function StartTime() {
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    m = CheckTime(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
    setTimeout(StartTime, 1000); //Updates the clock every second
}

function CheckTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}

//Shows the openhours on Monday-Friday and a close-text on weekends
function GetOpenHours(){ 
    $.ajax({
        type: 'GET',
        url: 'https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/B4:C8?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1388205127',
        success: function (data) {
            if(day <= 5 && day > 0){
                element = document.getElementById("openHours");
                element.innerHTML = data.values[day - 1][0] + " - " + data.values[day - 1][1];

                document.getElementById("weekend").classList.add('hidden');
                document.getElementById("open").classList.remove('hidden');
            }
            else{
                document.getElementById("weekend").classList.remove('hidden');
                document.getElementById("open").classList.add('hidden');
            }
        }
    });
    setTimeout(GetOpenHours, 60000); //Update the openhours-status every minute 
}

StartTime();
GetOpenHours();