import os

from fastapi import FastAPI
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from starlette.responses import RedirectResponse

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
def get_ticker_symbol_info(ticker_symbol: str):
    try:
        spreadsheetId = api_functionality.create_spreadsheet(creds, "GOOGLEFINANCE-StocksRealTime")

        api_functionality.update_from_csv(creds, spreadsheetId, ticker_symbol)

        sheet_data = api_functionality.get_values(creds, spreadsheetId, "A4:B22")

        return sheet_data

    except:
        pass

    finally:
        api_functionality.delete_spreadsheet(creds, spreadsheetId)