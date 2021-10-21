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
        url: `https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/B4:E8?key=AIzaSyCRYt-JT-5xfjBF4XdUYRzUbmYH1OtlcPg#gid=1388205127`,
        success: function (data) {
            console.log(day)
            var element = document.getElementById("morningClosedHours");
            element.innerHTML = data.values[day - 1][0] + " - " + data.values[day - 1][1];
            element = document.getElementById("eveningClosedHours");
            element.innerHTML = data.values[day - 1][2] + " - " + data.values[day - 1][3];
            element = document.getElementById("morningOpenHours");
            element.innerHTML = data.values[day - 1][0] + " - " + data.values[day - 1][1];
            element = document.getElementById("eveningOpenHours");
            element.innerHTML = data.values[day - 1][2] + " - " + data.values[day - 1][3];
            
            if(time < parseInt(data.values[day-1][0].replace(":","")) || 
            (time >= parseInt(data.values[day-1][1].replace(":","")) && time < parseInt(data.values[day-1][2].replace(":",""))) ||
            time >= parseInt(data.values[day-1][3].replace(":",""))){
                document.getElementById("closed").classList.remove('hidden');
        
                document.getElementById("open").classList.add('hidden');
            }
            else{
                document.getElementById("closed").classList.add('hidden');
                
                document.getElementById("open").classList.remove('hidden');
            }
        }
    });
    setTimeout(GetOpenHours, 60000);
}

function ConvertTime(h, m){
    return parseInt(h.toString() + CheckTime(m.toString()))
}

/*function ClosedDisplay(){
    var d = new Date();
    var hour = d.getHours();
    var min = d.getMinutes();
    var time = ConvertTime(hour, min);
    
    
    
    // If time is during cafe closed hours, show closed sign and hide slide carousel
    
    if((hour <= 7) || (hour <= 8 && min < 30) || (hour == 11 && min >= 30) || (hour == 15 && min >= 45) || (hour >= 16)){ 
        document.getElementById("closed").classList.remove('hidden');
        
        document.getElementById("open").classList.add('hidden');
    }
    else{
        document.getElementById("closed").classList.add('hidden');
        
        document.getElementById("open").classList.remove('hidden');
    }

    var t = setTimeout(ClosedDisplay, 10000); // Calls closedDisplay() again after 10 seconds to update
}*/

StartTime();
//ClosedDisplay();
GetOpenHours();