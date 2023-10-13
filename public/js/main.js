const daysOfWeek = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]

//Shows the clock on the website
function startTime(date) {
    let h = date.getHours();
    let m = date.getMinutes();

    m = checkTime(m);
    h = checkTime(h);

    document.getElementById("clock").innerHTML = h + ":" + m;
}

function checkTime(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}

// Shows todays date and year on the website
function todaysDate(date) {
    const day = date.getDay()
    const weekdayName = daysOfWeek[day];
    // Changes date to swedish format
    date = date.toLocaleDateString("sv-SE")
    document.getElementById("day").innerHTML = weekdayName;
    document.getElementById("date").innerHTML = date;
}

//Shows the openhours on Monday-Friday and a close-text on weekends
function getOpenHours(date) {
    const day = date.getDay();
    if (day <= 5 && day > 0) {
        document.getElementById("weekend").classList.add('hidden');
        document.getElementById("open").classList.remove('hidden');
    }
    else {
        document.getElementById("weekend").classList.remove('hidden');
        document.getElementById("open").classList.add('hidden');
    }
}

//Gets the products information and puts them in their div
function getData() {
    let apiList = ["A5:A55", "I5:I55", "E5:E55", "M5:M55"];
    let productsList = ["products1", "products2", "products3", "products4"];
    for (let i = 0; i < productsList.length; i++) {
        $.ajax({
            type: 'GET',
            url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/%27Datahantering%27!" + apiList[i] + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637",

            success: function (data) {
                let products = data.values;
                let productFull = products.filter(function (item) { return item != '' });
                for (let j = 0; j < productFull.length; j++) {
                    document.getElementById(productsList[i]).children[j].innerHTML = productFull[j];
                }
            }
        });
    }
}

//Gets the prices information and puts them in their div
function getPrices() {
    let apiList = ["B5:B55", "J5:J55", "F5:F55", "N5:N55"];
    let pricesStatusList = ["price/status1", "price/status2", "price/status3", "price/status4"];
    for (let i = 0; i < pricesStatusList.length; i++) {
        $.ajax({
            type: 'GET',
            url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/%27Datahantering%27!" + apiList[i] + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637",

            success: function (data) {
                let products = data.values;
                let productFull = products.filter(function (item) { return item != '' });
                for (let j = 0; j < productFull.length; j++) {
                    document.getElementById(pricesStatusList[i]).children[j].innerHTML = productFull[j];
                }
            }
        });
    }
}
// Runs the function every 5 seconds
var intervalDate = window.setInterval(function () {
    startTime(new Date());
}, 1000 * 5)
startTime(new Date());
// Runs the function every hour
var intervalDate = window.setInterval(function () {
    todaysDate(new Date());
}, 1000 * 60 * 60)
todaysDate(new Date());
// Runs the function every minute
var intervalDate = window.setInterval(function () {
    getOpenHours(new Date());
}, 1000 * 60)
getOpenHours(new Date());

getData();
getPrices();
