#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# Services to scrape web sites.
import WebServices

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

# ID of the Google Spreadsheet.
SPREADSHEET_ID = '1b9jCm0qMOHaw819uYBhPExKcQryYNgHbL1OG1suNhcU'

#
# Verify the required input arguments from the user command line
# to get the output directory and the list of Google Sheet's
# row numbers that this script needs to scrape.
#
def verifyInputArgs():

    parser = argparse.ArgumentParser(description='Catalyics Scraping.')
    parser.add_argument('googleSheetRowNumbers', metavar='ROW NUMBER', type=int, nargs='+',
                        help='Google Sheet row numbers to scrape.')
    
    # Parse the input arguments.
    args = parser.parse_args()

    return args.googleSheetRowNumbers

#
# Gets valid user credentials from storage.
#
def get_credentials():

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')

    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME

        credentials = tools.run(flow, store)

    return credentials

#
# Verify input arguments for output directory and Google Sheet row numbers
# Perform the scrape of the given retailers and then write results to
# the ouput directory.
#
def main():

    # At this point we have the row numbers to process in Google Sheets.
    googleSheetRowNumbers = verifyInputArgs()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)


    # Report the Google Sheet row numbers.
    for currentRow in googleSheetRowNumbers:
        print "-----"
        print "-> Catalytics Scrape for Google Sheet row: " + str(currentRow)

        # Only interested in these retailers.
        rangeName = 'CatalyticsConfiguration!A' + str(currentRow)
        rangeName += ':AI' + str(currentRow)
    
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID, range=rangeName).execute()

        values = result.get('values', [])

        # Lets parse the Google Sheet to kick-off the
        # scrape of the web sites.
        if not values:
            print('Error: No data found.')
        else:
            # Assume first row has data and we have skipped the table header.
            for row in values:
                
                # Dynamically determine the catalogs for a given retailer's store.
                # Rows are: Retailer, RetailerUrl, Suburb, Store Code.
                flyerUrls = WebServices.findRetailerUrl(row[0], row[3], row[5], row[6])
                print row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                if len(flyerUrls) > 0:
                    print "Found:"
                    for currentFlyer in flyerUrls:
                        print currentFlyer
                else:
                    print "No flyers found for retailer"



#
#
#
if __name__ == '__main__':
    main()

