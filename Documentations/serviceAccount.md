
# Google service account setup

1. Go to [Google Cloud IAM](https://console.cloud.google.com/iam-admin) and create a project. 

2. Go to the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) tab in your project and create a Google service account with the appropriate permissions. This project requires the service account to be an editor.

3. Go to the API Marketplace to download the [Google Sheets API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com) and the [Google Drive API](https://console.cloud.google.com/marketplace/product/google/drive.googleapis.com).

4. Edit the service account you created and under the keys tab click create a new key. Choose the key type json and a json file will be downloaded to the computer. This json file contains the service account credentials and is required on the raspberry pi for the website to get data from the spreadsheet.

5. Rename the downloaded json file `serviceAccount.json`.

6. Move the json file to the Cafeteria-display directory. If the json file already exists, replace it.

7. Go to the Google Sheets sheet you want to use and share the sheet with the service account email which you can find either on the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) tab in your project or in the json file.

8. Copy the ID in the url from the Google Sheets sheet you want to upload data to. The ID is the part of the url after the `/spreadsheets/d/`. In this example: `docs.google.com/spreadsheets/d/123456789/edit#gid=0`, the ID is `123456789`. The Google Sheets sheet url ID is used in `googleSheetDownloader.py` to specify which sheet you want to upload data to.

9. After this `googleSheetDownloader.py` should run correctly. You may have to install the packages `gspread` and `oauth2client` with pip for the file to run correctly.
