function tempClose(reason) {
    // This removes the opening hours and adds a message that the cafeteria is closed
    const openingHoursSlide = document.getElementById("cafeteria");
    let header = document.getElementById("openHoursHead");
    const openingHours = document.getElementById("openHours");
    openingHours.remove();
    header.style.fontSize = 90 + "px";
    header.innerText = "Cafeterian har tillfälligt stängt";
    // This adds a message with the reason for the closing 
    const reasoning = document.createElement("p");
    reasoning.className = "openHours";
    let reasoningText = document.createTextNode("");
    // If there are a reason write it out
    if (reason) {
        reasoningText = document.createTextNode('På grund av ' + reason);
    };
    reasoning.appendChild(reasoningText);
    openingHoursSlide.appendChild(reasoning);
    isClosed = true;
}

function getOpeningHoursHelper(data) {
    const openingHoursList = parseCsvString(data);
    // Checks if the cafeteria is temporarily closed
    const isTempClose = openingHoursList[2][1];
    // Adds the opening hours to the website
    const morningHours = document.getElementById("morningHours");
    const afternoonHours = document.getElementById("afternoonHours");
    morningHours.innerHTML = openingHoursList[0][1];
    afternoonHours.innerHTML = openingHoursList[1][1];
    // If closed, run tempClose()
    if (isTempClose === "TRUE") {
        tempClose(openingHoursList[3][1]);
    };
}
