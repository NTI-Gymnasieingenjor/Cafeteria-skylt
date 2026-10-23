const daysOfWeek = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]
let isClosed = false;

//Shows the clock on the website
function getTime(date) {
    let h = date.getHours();
    let m = date.getMinutes();

    h = addZeroUpTo10(h);
    m = addZeroUpTo10(m);

    document.getElementById("clock").innerHTML = h + ":" + m;
}

function addZeroUpTo10(i) {
    if (i < 10) { i = "0" + i }; //Adds a zero infront of numbers < 10
    return i;
}

// Shows todays weekday and date on the website
function getDate(date) {
    const day = date.getDay();
    const weekdayName = daysOfWeek[day];
    // Changes date to Swedish format
    date = date.toLocaleDateString("sv-SE");
    document.getElementById("day").innerHTML = weekdayName;
    document.getElementById("date").innerHTML = date;
}

// Runs getTime() every 5 seconds
window.setInterval(function () {
    getTime(new Date());
}, 1000 * 5)
getTime(new Date());

// Runs getDate() every hour
window.setInterval(function () {
    getDate(new Date());
}, 1000 * 60 * 60)
getDate(new Date());