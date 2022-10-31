import json
import os
from pprint import pprint

import coloredlogs, logging

from fastapi import FastAPI
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from starlette.responses import RedirectResponse
from google_sheets import api_functionality

# Use colorlogs
coloredlogs.install()

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


app = FastAPI(
    title="googlefinance-stocks-info",
    description="Simple API which allows to pull realtime and historical data from Google Finance ",
    version="0.1",
    terms_of_service="https://www.gnu.org/licenses/gpl-3.0.en.html",
    contact={
        "name": "Andrei Halici",
        "url": "https://bindingpixels.com",
        "email": "andrei.halici@bindingpixels.com",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC LICENSE Version 3",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
)

@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')

@app.get("/stocks/realtime/{ticker_symbol}")
def get_ticker_symbol_realtime_info(ticker_symbol: str):
    CSV_TEMPLATE_FILE = os.getcwd() + str("/artifacts/GOOGLEFINANCE-StocksRealTime-TEMPLATE.csv")

    try:
        spreadsheetId = api_functionality.create_spreadsheet(creds, "GOOGLEFINANCE-StocksRealTime")
        logging.info("The generated spreadsheetId is: %s", spreadsheetId)

        api_functionality.update_from_csv(creds, spreadsheetId, ticker_symbol, CSV_TEMPLATE_FILE)

        sheet_data = api_functionality.get_values(creds, spreadsheetId, "A4:B22")

        json_object = json.dumps(dict(sheet_data['values']), indent=4)
        return json_object

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

    finally:
        api_functionality.delete_spreadsheet(creds, spreadsheetId)

@app.get("/stocks/historical/{ticker_symbol}")
def get_ticker_symbol_historical_info(ticker_symbol: str):
    CSV_TEMPLATE_FILE = os.getcwd() + str("/artifacts/GOOGLEFINANCE-HistoricalMarketData-TEMPLATE.csv")

    try:
        spreadsheetId = api_functionality.create_spreadsheet(creds, "GOOGLEFINANCE-StocksRealTime")
        logging.info("The generated spreadsheetId is: %s", spreadsheetId)

        api_functionality.update_from_csv(creds, spreadsheetId, ticker_symbol, CSV_TEMPLATE_FILE)

        sheet_data = api_functionality.get_values(creds, spreadsheetId, "Sheet1")

        # Cleanup some unused keys
        keys_to_remove = ['range', 'majorDimension']

        for key in keys_to_remove:
            if key in sheet_data:
                del sheet_data[key]

        json_object = json.dumps(sheet_data, indent=4)
        return json_object

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)

    finally:
        api_functionality.delete_spreadsheet(creds, spreadsheetId)