# Google Apps Script
The projects Google Sheet uses an Apps Script. The script automatically add checkboxes and formats price in the Google Sheet. If you're working with a new Google Sheet, a new Apps Script should be added. 

## How to add an Apps Script
* In the Google Sheet, click on "Add-ons" in the top toolbar and choose "Apps Script".

* Replace all code in the new file with the following:

  ``` JavaScript
  function updateCheckboxAndFormat(nameCell, priceCell, visibilityCell) {
    const hasVisibilityCheckbox = visibilityCell.getValue() === true || visibilityCell.getValue() === false;
    // Sets the cells format to Swedish krona, example: 12 => 12 kr
    priceCell.setNumberFormat("#0 kr;(#0) kr")

    if (nameCell.getValue() && !hasVisibilityCheckbox) {
      visibilityCell.insertCheckboxes();
      visibilityCell.check();
    } 
    
    if(!nameCell.getValue() && !priceCell.getValue() && hasVisibilityCheckbox){
      visibilityCell.removeCheckboxes();
    }
  }

  function onEdit(e) {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Produkter')

    const row = e.range.getRow()
    const col = e.range.getColumn()

    const isCategoryColumn = (col === 1)

    if (isCategoryColumn) {
      return
    }

    const rowsPerCategory = 4
    const categoryIndex = Math.floor((row-1) / rowsPerCategory)

    const nameCell = sheet.getRange(categoryIndex * rowsPerCategory + 1, col)
    const priceCell = sheet.getRange(categoryIndex * rowsPerCategory + 2, col)
    const visibilityCell = sheet.getRange(categoryIndex * rowsPerCategory + 3, col)

    updateCheckboxAndFormat(nameCell, priceCell, visibilityCell)
  }
  ```