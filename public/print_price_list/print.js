
function GetData(link){
    $.ajax({
        type: 'GET',
        url: link,
        success: function (data) {
            filteredList = data.values.filter(function (item) { return item != ''; });
            console.log(filteredList);
            
            var node = document.createElement("H2");
            var textnode = document.createTextNode(filteredList[0][0]);
            node.appendChild(textnode);
            document.getElementById("tables").appendChild(node);
            
            document.createElement("table");
            node.id = filteredList[0][0];

            for (let i = 1; i < filteredList.length; i++){
                var node = document.createElement("TR");
                var textnode = document.createTextNode(filteredList[i][0]);
                node.appendChild(textnode);
                document.getElementById(filteredList[0][0]).appendChild(node);
                var textnode = document.createTextNode(filteredList[i][1]);
                node.appendChild(textnode);
                document.getElementById(filteredList[0][0]).appendChild(node);
            }
        }
    });

}
GetData("https://sheets.googleapis.com/v4/spreadsheets/1x-orVp4FAC1rCucW2jtH5WTWgBSbgAaDLp23wa-V2fQ/values/'Datahantering'!A4:B55?key=AIzaSyBPtjjvvCJ5Jy88dPjtlPXlsYCxGO8Kw7Q#gid=1388205127")

