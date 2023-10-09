
function getData(dataColumns){
    $.ajax({
        type: 'GET',
        url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Priser'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1388205127",
        success: function (data) {
            // Filter out all empty items in list
            filteredList = data.values.filter(function (item) { return item != ''; });
            
            // Create a div with the id of the category header, (item[0] in list of products)
            var node = document.createElement("div");
            node.id = filteredList[0][0];
            document.getElementById("tables").appendChild(node);
            
            // Append a h2 to the div as a header for the category
            node = document.createElement("H2");
            var textNode = document.createTextNode(filteredList[0][0]);
            node.appendChild(textNode);
            document.getElementById(filteredList[0][0]).appendChild(node);
            
            // Check if the list(+header) is odd, meaning the content is even
            if (filteredList.length % 2 != 0){
                for (let i = 1; i < (filteredList.length-1)/2+1; i++){
                    // Create a table row element
                    var node = document.createElement("TR");
                    
                    // Create a header(product) on table row(node) with product
                    var product = document.createElement("TH");
                    var textNode = document.createTextNode(filteredList[i][0]);
                    product.appendChild(textNode);
                    node.appendChild(product);
                    // Create a table data(price) on table row(node) with price
                    var price = document.createElement("TD");
                    var textNode = document.createTextNode(filteredList[i][1]);
                    price.appendChild(textNode);
                    node.appendChild(price);
                    // Create a header on table row with product for the right column
                    var product = document.createElement("TH");
                    var textNode = document.createTextNode(filteredList[i+(filteredList.length-1)/2][0]);
                    product.appendChild(textNode);
                    node.appendChild(product);
                    // Create a table data on table row with price for the right column
                    var price = document.createElement("TD");
                    var textNode = document.createTextNode(filteredList[i+(filteredList.length-1)/2][1]);
                    price.appendChild(textNode);
                    node.appendChild(price);
                    
                    // Lastly append the table row(node) to the div with the header as id
                    document.getElementById(filteredList[0][0]).appendChild(node);
                }
            }
            // If list is even with header, odd without
            else if (filteredList.length % 2 == 0){
                for (let i = 1; i < (filteredList.length-1)/2+1; i++){
                    // Create a table row element
                    var node = document.createElement("TR");
                    
                    // Create a table data(price) on table row(node) with price
                    var product = document.createElement("TH");
                    var textNode = document.createTextNode(filteredList[i][0]);
                    product.appendChild(textNode);
                    node.appendChild(product);
                    // Create a table data(price) on table row(node) with price
                    var price = document.createElement("TD");
                    var textNode = document.createTextNode(filteredList[i][1]);
                    price.appendChild(textNode);
                    node.appendChild(price);
                    // On the last item add an empty th and td to fill the blank spot in the right column
                    if (i == (filteredList.length)/2){
                        // Create a header on table row with empty string
                        var product = document.createElement("TH");
                        var textNode = document.createTextNode('');
                        product.appendChild(textNode);
                        node.appendChild(product);
                        // Create a table data on table row with empty string
                        var price = document.createElement("TD");
                        var textNode = document.createTextNode('');
                        price.appendChild(textNode);
                        node.appendChild(price);
                    }
                    // When not on the last item, add the correct item in the right column
                    else{
                        // Create a header on table row with product
                        var product = document.createElement("TH");
                        var textNode = document.createTextNode(filteredList[i+(filteredList.length)/2][0]);
                        product.appendChild(textNode);
                        node.appendChild(product);
                        // Create a table data on table row with price
                        var price = document.createElement("TD");
                        var textNode = document.createTextNode(filteredList[i+(filteredList.length)/2][1]);
                        price.appendChild(textNode);
                        node.appendChild(price);
                    }
                    
                    // Lastly append the table row(node) to the div with the header as id
                    document.getElementById(filteredList[0][0]).appendChild(node);
                }

            }
        }
    });

}

// Get data for different categories of products, delay to make sure the elements load in the correct order
setTimeout(() => { getData('A4:B55'); }, 1000);
setTimeout(() => { getData('E4:F55'); }, 2000);
setTimeout(() => { getData('I4:J55'); }, 3000);
setTimeout(() => { getData('M4:N55'); }, 4000);
setTimeout(() => { getData('Q4:R55'); }, 5000);