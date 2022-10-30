#!/usr/bin/env python3
from __future__ import print_function

from pprint import pprint
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CSV_FILE = os.getcwd() + str("/artifacts/GOOGLEFINANCE-StocksRealTime-TEMPLATE.csv")

def create_spreadsheet(creds, title):
    """
    Creates the Sheet the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # pylint: disable=maybe-no-member
    try:
        service = build('sheets', 'v4', credentials=creds)
        spreadsheet = {
            'properties': {
                'title': title
            }
        }

        spreadsheet = service.spreadsheets().create(body=spreadsheet,
                                                                fields='spreadsheetId') \
            .execute()

        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return spreadsheet.get('spreadsheetId')

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def delete_spreadsheet(creds, spreadsheetId):
    """
    Creates the Sheet the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    # pylint: disable=maybe-no-member
    try:
        service = build('drive', 'v3', credentials=creds)

        service.files().delete(fileId=spreadsheetId).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

def update_from_csv(creds, spreadsheet_id, stock_symbol: str):
    try:
        service = build('sheets', 'v4', credentials=creds)

        with open(CSV_FILE) as f:
            csvContents = f.read().replace("STOCK_SYMBOL_REPLACE_ME", stock_symbol)

        batch_update_spreadsheet_request_body = {
            # A list of updates to apply to the spreadsheet.
            # Requests will be applied in the order they are specified.
            # If any request is not valid, no requests will be applied.
            'requests': [{
                'pasteData': {
                    "coordinate": {
                        "sheetId": "0",
                        "rowIndex": "0",  # adapt this if you need different positioning
                        "columnIndex": "0",  # adapt this if you need different positioning
                    },
                    "data": csvContents,
                    "type": 'PASTE_NORMAL',
                    "delimiter": ',',
                }
            }],
        }

        request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id,
                                                     body=batch_update_spreadsheet_request_body)
        response = request.execute()

        # TODO: Change code below to process the `response` dict:
        pprint(response)

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


