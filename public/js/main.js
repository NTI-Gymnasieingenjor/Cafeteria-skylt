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

//Gets the products information and puts them in their div
function getData() {
    $.ajax({
        type: 'GET',
        url: "http://localhost:8000/productList.csv",
        success: function (data) {
            const rows = data.split("\n");
            let items = rows.map(row => row.split(','));
            const cleanItems = items.map(row => row.filter(value => value !== ""));
            const container = document.createElement("div");
            container.className = "container"
            let counter = 0;

            for (let i = 0; i < 6; i++) {
                const showList = cleanItems[2 + i * 4];
                let divHasBeenMade = false;
                let section;
                let itemDiv;
                let priceDiv;

                for (let y = 0; y < showList.length; y++) {
                    if (showList[y] === "FALSE") {
                        continue;
                    } else if (showList[y] === "TRUE") {
                        if (!divHasBeenMade) {
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
                            section.appendChild(div2);
                            div2.appendChild(header2);
                            div2.appendChild(itemDiv);
                            section.appendChild(priceDiv);
                            divHasBeenMade = true;
                        }
                        const itemPara = document.createElement("p");
                        const itemNode = document.createTextNode(cleanItems[0 + i * 4][y]);
                        itemPara.appendChild(itemNode);
                        const pricePara = document.createElement("p");
                        const priceNode = document.createTextNode(cleanItems[1 + i * 4][y]);
                        pricePara.appendChild(priceNode);
                        itemDiv.appendChild(itemPara);
                        priceDiv.appendChild(pricePara);
                        counter += 1;
                        console.log(counter)

                    }
                }

                if (divHasBeenMade) {
                    container.appendChild(section)
                }
            }
            if (counter !== 0) {
                newMenuSlide(container)
            }
        }
    });
}


//Gets the prices information and puts them in their div
// function getPrices() {
//     let apiList = ["B5:B55", "J5:J55", "F5:F55", "N5:N55"];
//     let pricesStatusList = ["price/status1", "price/status2", "price/status3", "price/status4"];
//     for (let i = 0; i < pricesStatusList.length; i++) {
//         $.ajax({
//             type: 'GET',
//             url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/%27Datahantering%27!" + apiList[i] + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1816022637",

//             success: function (data) {
//                 let products = data.values;
//                 let productFull = products.filter(function (item) { return item != '' });
//                 for (let j = 0; j < productFull.length; j++) {
//                     document.getElementById(pricesStatusList[i]).children[j].innerHTML = productFull[j];
//                 }
//             }
//         });
//     }
// }
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

getData();
// getPrices();
