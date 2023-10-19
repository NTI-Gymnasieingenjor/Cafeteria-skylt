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
// Adds a new slide to the carousel
function newMenuSlide(container) {
    // Creates a new div for the slide and adds classes and attributes
    const slide = document.createElement("div")
    slide.className = "carousel-item slide"
    slide.setAttribute("data-interval", "10000")
    slide.setAttribute("style", "background-color: #190f27;")
    // SlideCaption adds the div that the container is in
    const slideCaption = document.createElement("div")
    slideCaption.className = "carousel-caption d-none d-md-block priceList"
    slideCaption.setAttribute("style", "margin-top: 26vh;")
    slide.appendChild(slideCaption)
    slideCaption.appendChild(container)
    // Adds the slide to the carousel
    const carousel = document.getElementById("menu")
    carousel.appendChild(slide)
}


function resetContainer() {
    // Makes container epmty
    container = document.createElement("div");
    container.className = "container"
    return container
}

function getItemAndPrice(items, i, y) {
    // Creates a new p for the item and price 
    const itemP = document.createElement("p");
    // Takes the item and price of the current item
    const itemText = document.createTextNode(items[0 + i * 4][y]);
    itemP.appendChild(itemText);
    const priceP = document.createElement("p");
    const priceText = document.createTextNode(items[1 + i * 4][y]);
    priceP.appendChild(priceText);
    return [itemP, priceP]
}
// This makes a new category and puts it in the container
function makeNewCategory(category, itemDiv, priceDiv, items, i) {
    // Creates a new div for the items and prices
    category = document.createElement("div");
    category.className = "row mb-5 mt-5";
    // paddingDiv creates a div that is 2 columns wide
    let paddingDiv = document.createElement("div");
    paddingDiv.className = "col-2";
    let productDiv = document.createElement("div");
    productDiv.className = "col-7";
    // h2 is title for each category
    let header2 = document.createElement("h2");
    // Takes the category title of the current category
    let header2Text = document.createTextNode(items[0 + i * 4][0]);
    header2.appendChild(header2Text);
    // Creates a new div for the items and prices and add their classes
    itemDiv = document.createElement("div");
    priceDiv = document.createElement("div");
    priceDiv.className = "col-3 text-right aligner"
    category.appendChild(paddingDiv);
    productDiv.appendChild(header2);
    return [category, productDiv, itemDiv, priceDiv]
}
// This creates slides for the menu
function getMenuHelper(data) {
    // This splits data into lists
    const rows = data.split("\n");
    let rawMenuList = rows.map(row => row.split(','));
    // This removes empty items
    const menuList = rawMenuList.map(row => row.filter(value => value !== ""));
    let container = resetContainer();
    // This counts items on the slide to make sure it fits
    let counter = 0;
    // This loops through the categories 
    for (let foodCategory = 0; foodCategory < menuList.length / 4; foodCategory++) {
        // List of booleans for each category
        const booleanList = menuList[2 + foodCategory * 4];
        let headerHasBeenMade = false;
        let section, itemDiv, priceDiv;
        for (let itemIndex = 0; itemIndex < booleanList.length; itemIndex++) {
            if (booleanList[itemIndex] === "FALSE") {
                continue;
            } else if (booleanList[itemIndex] === "TRUE") {
                // This makes a new slide if the if() statement is true
                if (!headerHasBeenMade && counter >= 22) {
                    newMenuSlide(container);
                    counter = 0;
                    headerHasBeenMade = false;
                    container = resetContainer();
                }
                // This happens if no header has been made, it makes a new section
                if (!headerHasBeenMade) {
                    section = makeNewCategory(section, itemDiv, priceDiv, menuList, foodCategory)[0]
                    productDiv = makeNewCategory(section, itemDiv, priceDiv, menuList, foodCategory)[1]
                    itemDiv = makeNewCategory(section, itemDiv, priceDiv, menuList, foodCategory)[2]
                    priceDiv = makeNewCategory(section, itemDiv, priceDiv, menuList, foodCategory)[3]
                    productDiv.appendChild(itemDiv);
                    section.appendChild(productDiv);
                    section.appendChild(priceDiv);
                    headerHasBeenMade = true;
                    counter += 2;
                }
                // This gets the item and price and adds it to the item/price div
                itemDiv.appendChild(getItemAndPrice(menuList, foodCategory, itemIndex)[0]);
                priceDiv.appendChild(getItemAndPrice(menuList, foodCategory, itemIndex)[1]);
                counter += 1;
                // If counter is 24 or bigger it makes a new slide
                if (counter >= 24) {
                    container.appendChild(section);
                    newMenuSlide(container);
                    container = resetContainer();
                    counter = 0;
                    headerHasBeenMade = false;
                }
            }
        }
        // Adds category to the container
        if (headerHasBeenMade) {
            container.appendChild(section)
        }
    }
    // Create a new menuslide with the remaining items
    if (counter !== 0) {
        newMenuSlide(container)
    }
}
function getMenu() {
    $.ajax({
        type: 'GET',
        // The server address for Windows
        url: "http://localhost:8000/productList.csv",
        success: function (data) { getMenuHelper(data) }
    });
    $.ajax({
        type: 'GET',
        // The server address for Linux
        url: "http://0.0.0.0:8000/productList.csv",
        success: function (data) { getMenuHelper(data) }
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