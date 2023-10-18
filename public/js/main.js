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

function getItemAndPrice(cleanItems, i, y){
    const itemP = document.createElement("p");
    const itemText = document.createTextNode(cleanItems[0 + i * 4][y]);
    itemP.appendChild(itemText);
    const priceP = document.createElement("p");
    const priceText = document.createTextNode(cleanItems[1 + i * 4][y]);
    priceP.appendChild(priceText);
    return [itemP, priceP]
}

function makeNewSection(section, itemDiv, priceDiv, cleanItems, i){
    section = document.createElement("div");
    section.className = "row mb-5 mt-5";
    let div1 = document.createElement("div");
    div1.className = "col-2";
    let div2 = document.createElement("div");
    div2.className = "col-7";
    let header2 = document.createElement("h2");
    let header2Text = document.createTextNode(cleanItems[0 + i * 4][0]);
    header2.appendChild(header2Text);
    itemDiv = document.createElement("div"); // Initialize 'itemDiv'
    priceDiv = document.createElement("div"); // Initialize 'priceDiv'
    priceDiv.className = "col-3 text-right aligner"
    section.appendChild(div1);
    div2.appendChild(header2);
    return [section, div2, itemDiv, priceDiv]
}
//Gets the products information and puts them in their div
function getMenu() {
    $.ajax({
        type: 'GET',
        url: "http://localhost:8000/productList.csv",
        success: function (data) {
            const rows = data.split("\n");
            let items = rows.map(row => row.split(','));
            const cleanItems = items.map(row => row.filter(value => value !== ""));
            let container = resetContainer();
            let counter = 0;
            for (let i = 0; i < 6; i++) {
                const showList = cleanItems[2 + i * 4];
                let headerHasBeenMade = false;
                let section, itemDiv, priceDiv;
                for (let y = 0; y < showList.length; y++) {
                    if (showList[y] === "FALSE") {
                        continue;
                    } else if (showList[y] === "TRUE") {
                        if (!headerHasBeenMade && counter >= 22) {
                            newMenuSlide(container);
                            counter = 0;
                            headerHasBeenMade = false;
                            container = resetContainer();
                        }
                        if (!headerHasBeenMade) {
                            section = makeNewSection(section, itemDiv, priceDiv,cleanItems, i)[0]
                            div2 = makeNewSection(section, itemDiv, priceDiv,cleanItems, i)[1]
                            itemDiv = makeNewSection(section, itemDiv, priceDiv,cleanItems, i)[2]
                            priceDiv = makeNewSection(section, itemDiv, priceDiv,cleanItems, i)[3]
                            div2.appendChild(itemDiv);
                            section.appendChild(div2);
                            section.appendChild(priceDiv);
                            headerHasBeenMade = true;
                            counter += 2;
                        }
                        itemDiv.appendChild(getItemAndPrice(cleanItems, i, y)[0]);
                        priceDiv.appendChild(getItemAndPrice(cleanItems, i, y)[1]);
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