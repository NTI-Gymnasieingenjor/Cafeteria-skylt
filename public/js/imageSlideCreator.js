function helperGetImageSlide(data) {
    // Hinders the creation of image slides if closed
    if (isClosed) {
        return;
    }

    const imageList = parseCsvString(data);
    const slideCreator = new ImageSlideCreator()

    // This loops through the slides 
    for (let currentSlide = 1; currentSlide < imageList[4].length; currentSlide++) {
        // Checks if slide should be shown or not 
        if (imageList[4][currentSlide] === "TRUE") {
            // Genererates HTML code for slides
            slideCreator.addSlide();
            slideCreator.addBackground();
            slideCreator.addProductImage(`images/products/${imageList[2][currentSlide]}`);
            slideCreator.addProductInfo(imageList[0][currentSlide], imageList[3][currentSlide]);
        }
    }
};

class ImageSlideCreator {
    constructor() {
        this.carousel = document.getElementById("menu");
    }

    addSlide() {
        this.imageSlide = document.createElement("div");
        this.imageSlide.className = "carousel-item slide";
        this.imageSlide.setAttribute("data-interval", "5000");
        this.imageSlide.setAttribute("style", "background-color: rgb(0,35,96);");
        this.carousel.append(this.imageSlide);
    }

    addBackground() {
        const backgroundElement = document.createElement("img");
        backgroundElement.className = "productSlide dot";
        this.imageSlide.append(backgroundElement);
    }

    addProductImage(path) {
        const productImage = document.createElement("img");
        productImage.className = "productSlide productImage";
        productImage.setAttribute("src", path);
        productImage.setAttribute("height", "700");
        this.imageSlide.append(productImage)
    }

    addProductInfo(name, price) {
        const infoBackground = document.createElement("img")
        infoBackground.className = "productSlide productInfoBackground";
        infoBackground.setAttribute("src", "images/vibrant_dot.png")

        const infoContainer = document.createElement("div");
        infoContainer.className = "carousel-caption d-none d-md-block productPrice";

        const productElement = document.createElement("p");
        productElement.className = "itemText";
        productElement.innerText = name;

        const priceElement = document.createElement("p");
        priceElement.className = "price";
        priceElement.innerText = price;

        infoContainer.append(productElement);
        infoContainer.append(priceElement);
        this.imageSlide.append(infoBackground)
        this.imageSlide.append(infoContainer)
    }
}
