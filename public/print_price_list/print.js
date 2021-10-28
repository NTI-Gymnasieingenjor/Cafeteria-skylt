
function GetData(dataColumns){
    $.ajax({
        type: 'GET',
        url: "https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Priser'!" + dataColumns + "?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1388205127",
        success: function (data) {
            filteredList = data.values.filter(function (item) { return item != ''; });
            
            var node = document.createElement("div");
            node.id = filteredList[0][0];
            document.getElementById("tables").appendChild(node);
            
            node = document.createElement("H2");
            var textnode = document.createTextNode(filteredList[0][0]);
            node.appendChild(textnode);
            document.getElementById(filteredList[0][0]).appendChild(node);
            

            if (filteredList.length % 2 != 0){
                for (let i = 1; i < (filteredList.length-1)/2+1; i++){
                    // Create a table row element
                    var node = document.createElement("TR");
                    
                    // Create a header on table row with product
                    var product = document.createElement("TH");
                    var textnode = document.createTextNode(filteredList[i][0]);
                    product.appendChild(textnode);
                    node.appendChild(product);
                    // Create a table data on table row with price
                    var price = document.createElement("TD");
                    var textnode = document.createTextNode(filteredList[i][1]);
                    price.appendChild(textnode);
                    node.appendChild(price);
                    // Create a header on table row with product
                    var product = document.createElement("TH");
                    var textnode = document.createTextNode(filteredList[i+(filteredList.length-1)/2][0]);
                    product.appendChild(textnode);
                    node.appendChild(product);
                    // Create a table data on table row with price
                    var price = document.createElement("TD");
                    var textnode = document.createTextNode(filteredList[i+(filteredList.length-1)/2][1]);
                    price.appendChild(textnode);
                    node.appendChild(price);
                    
                    
                    document.getElementById(filteredList[0][0]).appendChild(node);
                }
            }
            else if (filteredList.length % 2 == 0){
                for (let i = 1; i < (filteredList.length-1)/2+1; i++){
                    // Create a table row element
                    var node = document.createElement("TR");
                    
                    // Create a header on table row with product
                    var product = document.createElement("TH");
                    var textnode = document.createTextNode(filteredList[i][0]);
                    product.appendChild(textnode);
                    node.appendChild(product);
                    // Create a table data on table row with price
                    var price = document.createElement("TD");
                    var textnode = document.createTextNode(filteredList[i][1]);
                    price.appendChild(textnode);
                    node.appendChild(price);
                    console.log((filteredList.length)/2);
                    if (i == (filteredList.length)/2){
                        // Create a header on table row with product
                        var product = document.createElement("TH");
                        var textnode = document.createTextNode('');
                        product.appendChild(textnode);
                        node.appendChild(product);
                        // Create a table data on table row with price
                        var price = document.createElement("TD");
                        var textnode = document.createTextNode('');
                        price.appendChild(textnode);
                        node.appendChild(price);
                    }
                    else{
                        // Create a header on table row with product
                        var product = document.createElement("TH");
                        var textnode = document.createTextNode(filteredList[i+(filteredList.length)/2][0]);
                        product.appendChild(textnode);
                        node.appendChild(product);
                        // Create a table data on table row with price
                        var price = document.createElement("TD");
                        var textnode = document.createTextNode(filteredList[i+(filteredList.length)/2][1]);
                        price.appendChild(textnode);
                        node.appendChild(price);
                    }
                    
                    
                    document.getElementById(filteredList[0][0]).appendChild(node);
                }

            }
        }
    });

}

setTimeout(() => { GetData('A4:B55'); }, 1000);
setTimeout(() => { GetData('E4:F55'); }, 2000);
setTimeout(() => { GetData('I4:J55'); }, 3000);
setTimeout(() => { GetData('M4:N55'); }, 4000);
setTimeout(() => { GetData('Q4:R55'); }, 5000);