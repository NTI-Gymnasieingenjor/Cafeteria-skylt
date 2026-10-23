const queryString = window.location.search;

const urlParams = new URLSearchParams(queryString);

const openHoursListPathDefault = "openHoursList.csv";
const imageListPathDefault = "imageList.csv";
const productListPathDefault = "productList.csv";

let openHoursListPath = urlParams.has('openHours') ? urlParams.get('openHours') : openHoursListPathDefault;
let imageListPath = urlParams.has('images') ? urlParams.get('images') : imageListPathDefault;
let productListPath = urlParams.has('products') ? urlParams.get('products') : productListPathDefault;

// Runs getOpeningHours() with data from openHoursList.csv
function getOpeningHours() {
    $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/csv/" + openHoursListPath,
        success: function (data) { 
            getOpeningHoursHelper(data);
            getImageSlide();
        }
    });
}

// Runs getImageSlide() with data from imageList.csv
function getImageSlide(){
    $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/csv/" + imageListPath,
        success: function (data) {
            helperGetImageSlide(data);
            getMenu();
        }
    });
}

// Runs get menu with data from productList.csv
function getMenu() {
    $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:8000/csv/" + productListPath,
        success: function (data) { createMenuSlides(data) }
    });
}

getOpeningHours();

let willRefresh = false

window.setInterval(function () {
    if (isClosed) {
        location.reload();
    }
    willRefresh = true
}, 1000 * 60 * 10)

// if 10 minutes has passed, then refresh site on opening hours slide to get updates
$('#carousel').on('slide.bs.carousel', function (event) {
    if (willRefresh) {
        // It checks if the slide has the class 'refreshSlide' and if it does then it reloads the current page
        if ($(event.relatedTarget).hasClass('refreshSlide')) {
            location.reload();
        }
    }
})
