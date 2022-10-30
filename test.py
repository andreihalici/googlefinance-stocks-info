import json
import os
import time
from pprint import pprint

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google_sheets import api_functionality

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]

''' Generate required credentials to interact with Google Sheets API
More information: https://cloud.google.com/docs/authentication/provide-credentials-adc
'''
TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists(TOKEN_FILE):
    creds = Credentials.from_authorized_user_file(TOKEN_FILE)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE)
            creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())


try:
    #spreadsheetId = api_functionality.create_spreadsheet(creds, "GOOGLEFINANCE-StocksRealTime")

    stock_symbol = "TSLA"

    spreadsheetId = '1PCu-eDlE9R0ghAXPvX_db-yb9BahMDUA3Q0Kj3cgBo0'

    #api_functionality.update_from_csv(creds, spreadsheetId, stock_symbol)

    time.sleep(3)

    sheet_data = api_functionality.get_values(creds, spreadsheetId, "A4:B22")
    print(sheet_data)

except:
    pass

finally:
    pass
    #spreadsheetId = '1Jw1w2gGvVM5ywBNl341ZPajqoxZGN4hQrSo6gwg6Aqg'
    #api_functionality.delete_spreadsheet(creds, spreadsheetId)