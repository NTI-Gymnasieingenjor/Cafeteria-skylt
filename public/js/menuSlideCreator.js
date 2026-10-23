// Base value of the height of an item counted in lines
const itemHeightInLines = 1;
// A value that should roughly reflect how many times greater the height of a header is compared to an item's height
const headerHeightInLines = 2 * itemHeightInLines;
// The number of rows per category in the product list csv file
const linesPerCategory = 4;
// Used to index different rows within each category
const nameRowIndex = 0;
const priceRowIndex = 1;
const visibilityRowIndex = 2;

const maxLinesAllowedForNewItem = 23 * itemHeightInLines;
const maxLinesAllowedForNewHeader = maxLinesAllowedForNewItem - headerHeightInLines;

// Adds a new slide to the carousel
function newMenuSlide(slideContent) {
    const slide = document.createElement("div");
    slide.className = "carousel-item slide text-light priceList";
    slide.setAttribute("data-interval", "10000"); // Sets the duration of the slide to 10 seconds
    slide.append(slideContent);

    // Adds the slide to the carousel
    const carousel = document.getElementById("menu");
    carousel.appendChild(slide);
}

class Category {
    // Creates an empty category
    constructor(categoryName) {
        let sectionHeading = this.#createHeading(categoryName);
        let nameDiv = document.createElement("div");
        let productDiv = this.#createProductDiv(sectionHeading, nameDiv);
        let paddingDiv = this.#createPaddingDiv();
        let priceDiv = this.#createPriceDiv();

        let section = this.#createSection(paddingDiv, productDiv, priceDiv);

        this.section = section;
        this.nameDiv = nameDiv;
        this.priceDiv = priceDiv;
    }

    addProduct(name, price) {
        const itemNameElement = document.createElement("p");
        const itemPriceElement = document.createElement("p");

        itemNameElement.innerText = name;
        itemPriceElement.innerText = price;

        this.nameDiv.appendChild(itemNameElement);
        this.priceDiv.appendChild(itemPriceElement);
    }

    #createPaddingDiv() {
        // PaddingDiv creates a div that is 2 columns wide
        let paddingDiv = document.createElement("div");
        paddingDiv.className = "col-2";

        return paddingDiv;
    }

    #createHeading(sectionTitle) {
        // h2 is title for the category
        let sectionHeading = document.createElement("h2");
        sectionHeading.innerText = sectionTitle

        return sectionHeading;
    }

    #createPriceDiv() {
        let priceDiv = document.createElement("div");
        priceDiv.className = "col-3 text-right aligner";

        return priceDiv;
    }

    #createProductDiv(sectionHeading, nameDiv) {
        let productDiv = document.createElement("div");
        productDiv.className = "col-7";
        productDiv.appendChild(sectionHeading);
        productDiv.appendChild(nameDiv);

        return productDiv;
    }

    #createSection(paddingDiv, productDiv, priceDiv) {
        // Creates a new div for the items and prices
        let section = document.createElement("div");
        section.className = "row my-5";

        section.appendChild(paddingDiv);
        section.appendChild(productDiv);
        section.appendChild(priceDiv);

        return section;
    }
}

class MenuSlidesCreator {
    constructor() {
        this.addSlide();
    }

    addSlide() {
        this.slideContent = document.createElement("div");
        this.slideContent.className = "container";
        newMenuSlide(this.slideContent);
        this.currentLineCounter = 0;
    }

    addCategory(categoryName) {
        this.category = new Category(categoryName);
        this.slideContent.appendChild(this.category.section);
        this.currentLineCounter += headerHeightInLines;
    }

    addProduct(productName, productPrice) {
        this.category.addProduct(productName, productPrice);
        this.currentLineCounter += itemHeightInLines;
    }

    enoughSpaceToAddCategory() {
        return this.currentLineCounter <= maxLinesAllowedForNewHeader;
    }

    enoughSpaceToAddProduct() {
        return this.currentLineCounter <= maxLinesAllowedForNewItem;
    }
}

// This creates slides for the menu
function createMenuSlides(data) {
    // Hinders the creation of menu slides if closed
    if (isClosed) {
        return;
    }

    const menuList = parseCsvString(data);
    let categoryCount = menuList.length / linesPerCategory;
    let slideCreator = new MenuSlidesCreator();

    for (let categoryIndex = 0; categoryIndex < categoryCount; categoryIndex++) {
        const categoryStartRow = categoryIndex * linesPerCategory;
        const productVisibilityList = menuList[visibilityRowIndex + categoryStartRow];
        // Indexed by zero since the first value of a name row in the csv is the category name
        const categoryName = menuList[nameRowIndex + categoryStartRow][0];

        // Subtracted by one since the values in the first column don't include products
        const productCount = productVisibilityList.length - 1;
        if (productCount <= 0) {
            // Skips the category if there are no products
            continue;
        }

        if (!slideCreator.enoughSpaceToAddCategory()) {
            slideCreator.addSlide();
        }
        slideCreator.addCategory(categoryName);

        for (let itemIndex = 0; itemIndex < productVisibilityList.length; itemIndex++) {
            const productName = menuList[nameRowIndex + categoryStartRow][itemIndex];
            const productPrice = menuList[priceRowIndex + categoryStartRow][itemIndex];
            const showProduct = productVisibilityList[itemIndex] === "TRUE";

            if (!showProduct) {
                continue;
            }

            if (!slideCreator.enoughSpaceToAddProduct()) {
                slideCreator.addSlide();
                slideCreator.addCategory(categoryName);
            }
            slideCreator.addProduct(productName, productPrice);
        }
    }
}
