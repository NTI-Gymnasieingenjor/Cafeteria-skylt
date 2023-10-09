var d = new Date();
var day = d.getDay();

//Shows the clock on the website
function startTime() {
    var d = new Date();
    var h = d.getHours();
    var m = d.getMinutes();

    m = checkTime(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
    setTimeout(startTime, 1000); //Updates the clock every second
}

function checkTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}

//Shows the openhours on Monday-Friday and a close-text on weekends
function getOpenHours(){ 
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
    setTimeout(getOpenHours, 60000); //Update the openhours-status every minute 
}

//Gets the products information and puts them in their div
function getData(){
    let apiList = ["A5:A55", "I5:I55", "E5:E55", "M5:M55"];
    let productsList = ["products1", "products2", "products3", "products4"];
    for(let i = 0; i < productsList.length; i ++){
        $.ajax({
            type: 'GET',
            url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/%27Datahantering%27!" + apiList[i] + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637",

            success: function (data) {
                let products = data.values;
                let productFull = products.filter(function (item){ return item != ''});
                for(let j = 0; j < productFull.length; j++){
                    document.getElementById(productsList[i]).children[j].innerHTML= productFull[j];
                }
            }
        });
    }
}

//Gets the prices information and puts them in their dev
function getPrices(){
    let apiList = ["B5:B55", "J5:J55","F5:F55", "N5:N55"];
    let pricesStatusList = ["price/status1", "price/status2", "price/status3", "price/status4"];
    for(let i = 0; i < pricesStatusList.length; i++){
        $.ajax({
            type: 'GET',
            url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/%27Datahantering%27!" + apiList[i] + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637",

            success: function (data) {
                let products = data.values;
                let productFull = products.filter(function (item){ return item != ''});
                for(let j = 0; j < productFull.length; j++){
                    document.getElementById(pricesStatusList[i]).children[j].innerHTML= productFull[j];
                }
            }
        });
    }
}


startTime();
getOpenHours();
getData();
getPrices();
