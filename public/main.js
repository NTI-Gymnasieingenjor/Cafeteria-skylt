var d = new Date();
var day = d.getDay();

function StartTime() {
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    m = CheckTime(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
    var t = setTimeout(StartTime, 1000);
}

function CheckTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}

function GetOpenHours(){
    var d = new Date();
    var hour = d.getHours();
    var min = d.getMinutes();
    var time = ConvertTime(hour, min);
    
    $.ajax({
        type: 'GET',
        url: 'https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/B4:E8?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1388205127',
        success: function (data) {
            if(day <= 5 && day > 0){
                element = document.getElementById("morningOpenHours");
                element.innerHTML = data.values[day - 1][0] + " - " + data.values[day - 1][1];
                element = document.getElementById("eveningOpenHours");
                element.innerHTML = data.values[day - 1][2] + " - " + data.values[day - 1][3];

                document.getElementById("weekend").classList.add('hidden');
                document.getElementById("open").classList.remove('hidden');
            }
            else{
                document.getElementById("weekend").classList.remove('hidden');
                document.getElementById("open").classList.add('hidden');
            }
        }
    });
    setTimeout(GetOpenHours, 60000);
}

function ConvertTime(h, m){
    return parseInt(h.toString() + CheckTime(m.toString()))
}

StartTime();
GetOpenHours();