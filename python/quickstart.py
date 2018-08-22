from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import json
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1bPueolFmgpbzbJzob4s9m0NSiywLodHud1mRQ9rx3Fg'
SAMPLE_RANGE_NAME = 'Form Responses 1!A:AA'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1bPueolFmgpbzbJzob4s9m0NSiywLodHud1mRQ9rx3Fg'
    RANGE_NAME = 'Form Responses 1!A:AA'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])

    # Set up dataframe
    d = pd.DataFrame(values)
    for row in d[1:].iterrows():
        generatePage(row)

    if not values:
        print('No data found.')
    else:
        print ('Got data from sheet:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            # print(row)
            continue

def exportToFile(data):
    with open((data[0] + '.txt'), 'a') as the_file:
        the_file.write(str(data))

def generatePage(page):
  business_name = str(page[1][1])
  contact_phone = str(page[1][2])
  contact_email = str(page[1][3])
  business_address = str(page[1][4])
  tagline = str(page[1][5])
  output = [business_name, contact_phone, contact_email, business_address, tagline]
  # Assemble components on page and arrange them in markdown format
  # Exports MD file with items populated from input form
  exportToFile(output)



if __name__ == '__main__':
    main()
