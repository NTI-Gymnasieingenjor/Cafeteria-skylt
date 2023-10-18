const daysOfWeek = ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag"]

//Shows the clock on the website
function getTime(date) {
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
function getDate(date) {
    const day = date.getDay()
    const weekdayName = daysOfWeek[day];
    // Changes date to swedish format
    date = date.toLocaleDateString("sv-SE")
    document.getElementById("day").innerHTML = weekdayName;
    document.getElementById("date").innerHTML = date;
}

function newMenuSlide(container) {
    const slide = document.createElement("div")
    slide.className = "carousel-item slide"
    slide.setAttribute("data-interval","10000")
    slide.setAttribute("style","background-color: #190f27;")
    const slideCap = document.createElement("div")
    slideCap.className = "carousel-caption d-none d-md-block priceList"
    slideCap.setAttribute("style","margin-top: 26vh;")
    slide.appendChild(slideCap)
    slideCap.appendChild(container)
    const carousel = document.getElementById("menu")
    carousel.appendChild(slide)
}


function resetContainer(){
    container = document.createElement("div");
    container.className = "container"
    return container
}

function getItemAndPrice(items, i, y){
    const itemP = document.createElement("p");
    const itemText = document.createTextNode(items[0 + i * 4][y]);
    itemP.appendChild(itemText);
    const priceP = document.createElement("p");
    const priceText = document.createTextNode(items[1 + i * 4][y]);
    priceP.appendChild(priceText);
    return [itemP, priceP]
}

function makeNewSection(section, itemDiv, priceDiv, items, i){
    section = document.createElement("div");
    section.className = "row mb-5 mt-5";
    let paddingDiv = document.createElement("div");
    paddingDiv.className = "col-2";
    let productDiv = document.createElement("div");
    productDiv.className = "col-7";
    let header2 = document.createElement("h2");
    let header2Text = document.createTextNode(items[0 + i * 4][0]);
    header2.appendChild(header2Text);
    itemDiv = document.createElement("div");
    priceDiv = document.createElement("div");
    priceDiv.className = "col-3 text-right aligner"
    section.appendChild(paddingDiv);
    productDiv.appendChild(header2);
    return [section, productDiv, itemDiv, priceDiv]
}
function getMenuHelper(data) {
    const rows = data.split("\n");
    let rawItems = rows.map(row => row.split(','));
    const items = rawItems.map(row => row.filter(value => value !== ""));
    let container = resetContainer();
    let counter = 0;
    for (let foodCategory = 0; foodCategory < items.length/4; foodCategory++) {
        const booleanList = items[2 + foodCategory * 4];
        let headerHasBeenMade = false;
        let section, itemDiv, priceDiv;
        for (let itemIndex = 0; itemIndex < booleanList.length; itemIndex++) {
            if (booleanList[itemIndex] === "FALSE") {
                continue;
            } else if (booleanList[itemIndex] === "TRUE") {
                if (!headerHasBeenMade && counter >= 22) {
                    newMenuSlide(container);
                    counter = 0;
                    headerHasBeenMade = false;
                    container = resetContainer();
                }
                if (!headerHasBeenMade) {
                    section = makeNewSection(section, itemDiv, priceDiv, items, foodCategory)[0]
                    productDiv = makeNewSection(section, itemDiv, priceDiv, items, foodCategory)[1]
                    itemDiv = makeNewSection(section, itemDiv, priceDiv, items, foodCategory)[2]
                    priceDiv = makeNewSection(section, itemDiv, priceDiv, items, foodCategory)[3]
                    productDiv.appendChild(itemDiv);
                    section.appendChild(productDiv);
                    section.appendChild(priceDiv);
                    headerHasBeenMade = true;
                    counter += 2;
                }
                itemDiv.appendChild(getItemAndPrice(items, foodCategory, itemIndex)[0]);
                priceDiv.appendChild(getItemAndPrice(items, foodCategory, itemIndex)[1]);
                counter += 1;
                if (counter >= 24)  {
                    container.appendChild(section);
                    newMenuSlide(container);
                    container = resetContainer();
                    counter = 0;
                    headerHasBeenMade = false;
                }
            }
        }
        if (headerHasBeenMade) {
            container.appendChild(section)
        }
    }
    if (counter !== 0) {
        newMenuSlide(container)
    }
}
function getMenu() {
    $.ajax({
        type: 'GET',
        url: "http://localhost:8000/productList.csv",
        success: function (data) {getMenuHelper(data)}
    });
    $.ajax({
        type: 'GET',
        url: "http://0.0.0.0:8000/productList.csv",
        success: function (data) {getMenuHelper(data)}
    });
}

// Runs getTime() every 5 seconds
var intervalDate = window.setInterval(function () {
    getTime(new Date());
}, 1000 * 5)
getTime(new Date());

// Runs getDate() every hour
var intervalDate = window.setInterval(function () {
    getDate(new Date());
}, 1000 * 60 * 60)
getDate(new Date());

getMenu();