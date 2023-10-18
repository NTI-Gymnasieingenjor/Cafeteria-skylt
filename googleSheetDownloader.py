import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Links for authorizing google sheets api (drive is required for sheets!)
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Credentials for authorizing google sheets api
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "serviceAccount.json", scope
)
# Authorize the client sheet and gets get the relevant spreadsheet by key
client = gspread.authorize(credentials)
sh = client.open_by_key("1wN90DoWtkIRofBl3Jm_UkQMeDUDMMIszM-5tlwlPICA")
# Gets all values from the spreadsheet
csvContent = sh.sheet1.get_all_values()

# Writes the values into a csv file with the correct encoding
with open("public/productList.csv", "w", encoding="utf8") as file:
    for row in csvContent:
        file.write(",".join(row) + "\n")
