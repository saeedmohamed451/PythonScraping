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

# Services to work with documents.
import DocumentServices
import csv
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
    parser.add_argument('--output', metavar='DIRECTORY', type=str, nargs=1,
                        help='Path to output directory')
    parser.add_argument('googleSheetRowNumbers', metavar='ROW NUMBER', type=int, nargs='+',
                        help='Google Sheet row numbers to scrape.')
    
    # Parse the input arguments.
    args = parser.parse_args()

    return args.output[0], args.googleSheetRowNumbers

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
# Scrape the catatlog from the retailer's flyer and write results.
#
def scrapeAndWrite(outputDir, retailer, location, store, site, flyerUrl, grouping):

    # Get catalogs associated with website.
    print("-> Scrape Retailer: " + str(retailer) + "-" + str(location) + "-" + str(flyerUrl))
    catalogs = WebServices.scrapeToCatalogs(site,
                                            [{"store": store,
                                              "location": location,
                                              "url": flyerUrl}],
                                            grouping)

    # Write the results to disk.
    DocumentServices.writeCatalogs(grouping, retailer, catalogs, outputDir)


#
# Verify input arguments for output directory and Google Sheet row numbers
# Perform the scrape of the given retailers and then write results to
# the ouput directory.
#

def main():
    outputDir, googleSheetRowNumbers = verifyInputArgs()
    data = []
    with open(os.getcwd() + "/input.csv") as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')
        i = 0
        # reader = csv.DictReader(f)
        for row in reader:
            row_new = row[0].split(',')
            if row_new[0] != 'Retailer':
                if i == googleSheetRowNumbers[0]:
                    addr = row[0].split('"')[1]
                    print addr
                    retailer = row_new[0]
                    location = row_new[1]
                    url = row_new[6]
                    grouping = row_new[7]
                    suburb = row_new[8]
                    store_code = row_new[9]
                    row = [retailer, location, addr,
                    url, grouping, suburb, store_code]
                    data.append(row)
                i += 1
    # At this point we have the row numbers to process in Google Sheets.
    for row in data:

                # Dynamically determine the catalogs for a given retailer's store.
                # Rows are: Retailer, RetailerUrl, Suburb, Store Code.
        flyer_urls = WebServices.findRetailerUrl(row[0], row[3], row[5], row[6])

                # Scrape the catalogs for the given retailer's store.
        if len(flyer_urls) > 0:
                    # Consider each catalog as there can be multiple catalogs for a
                    # single retailer.
            for flyerIndex, flyerUrl in enumerate(flyer_urls):
                        # Rows are: Retailer, Location, Store Addr, Retailer Url, flyerUrl, grouping
                scrapeAndWrite(outputDir, row[0], row[1], row[2], row[3], flyerUrl, row[4])
        else:
            print "Error: No flyer URLs found for this retailer."

#
#
#
if __name__ == '__main__':
    main()
