function parseCsvString(dataString) {
    // This splits data into an array of lines
    const rows = dataString.split("\n");
    let rawDataList = rows.map(row => row.split(','));

    // This removes whitespace characters like "\r"
    let dataList = rawDataList.map(row => row.map(value => value.trim()));
    // This removes empty items
    dataList = dataList.map(row => row.filter(value => value !== ""));

    return dataList;
}