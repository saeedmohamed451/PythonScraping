#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# Services to scrape web sites.
import WebServices

# Services to work with documents.
import DocumentServices


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

# Location of where to place the spreadsheet and PDF.
OUTPUT_DIR = "./quickstartoutput/"


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
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
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    # ID of the Google Spreadsheet.
    spreadsheetId = '1b9jCm0qMOHaw819uYBhPExKcQryYNgHbL1OG1suNhcU'
    # Interested in ALL Data from A2. (skip the table header)
    # rangeName = 'CatalyticsConfiguration!A2:AI500'

    # Only interested in running the Walmart retailer.
    # rangeName = 'CatalyticsConfiguration!A26:AI26'

    # Only interested in the Flipp for VPN.
    # rangeName = 'CatalyticsConfiguration!A26:AI27'
    
    # Only interested in these retailers.
    rangeName = 'CatalyticsConfiguration!A28:AI28'
    
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()

    values = result.get('values', [])

    # Lets parse the Google Sheet to kick-off the
    # scrape of the web sites.

    if not values:
        print('Error: No data found.')
    else:
        # Assume first row has data and we have skipped the table header.
        for row in values:

            # Load the values in the spreadsheet into memory.
            retailer = row[0]
            location = row[1]
            store = row[4]
            site = row[5]
            flyerUrl = row[6]
            grouping = row[7]

            # Get catalogs associated with website.
            print("-> Scrape Retailer: " + str(retailer) + "-" + str(location) + "-" + str(flyerUrl))
            catalogs = WebServices.scrapeToCatalogs(site,
                                                    [{"store": store,
                                                      "location": location,
                                                      "url": flyerUrl}],
                                                    grouping)
            

            if len(catalogs) == 0:
                # No point trying to generate a spreadsheet or PDF.
                print("Error: no weekly advertisement data found from (" + \
                    str(retailer) + ")")
                continue

            print("  -> Write Catalogs to XLSX")
            DocumentServices.writeCatalogsToSpreadsheet(grouping,
                                                        retailer,
                                                        catalogs,
                                                        OUTPUT_DIR)

            # TODO: Add logic here to populate the CSV, PDF and IMAGES.
            # Write the catalogs to a CSV.
            print("  -> Write Catalogs to CSV")
            DocumentServices.writeCatalogsToCsv(grouping,
                                                retailer,
                                                catalogs,
                                                OUTPUT_DIR)


            # Write the catalogs to a PDF.
            print("  -> Write Catalogs to PDF")
            DocumentServices.writeCatalogsToPdf(grouping,
                                                retailer,
                                                catalogs,
                                                OUTPUT_DIR)





if __name__ == '__main__':
    main()
