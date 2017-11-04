#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# Interact with web server.
import requests
# Parse the web server response.
import json

# Services to scrape web sites.
import WebServices

# Services to work with documents.
import DocumentServices

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

# ID of the Google Spreadsheet.
SPREADSHEET_ID = '1b9jCm0qMOHaw819uYBhPExKcQryYNgHbL1OG1suNhcU'

# Location of where to place the spreadsheet and PDF.
OUTPUT_DIR = "./output/"

#
# From the user command line get the list of Google sheet
# row numbers that this script needs to scrape.
#
def verifyGoogleSheetRowNumbers():

    parser = argparse.ArgumentParser(description='Catalyics Scraping.')
    parser.add_argument('googleSheetRowNumbers', metavar='rowNumbers', type=int, nargs='+',
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
# Use the store code to compute the Aldi Catalogs URLs.
#
def getAldiCatalogUrls(storeCode):

    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    aldiStoreUrl = 'https://flipp.aldi.us/flyers/aldi?type=2&store_code=' + str(storeCode)

    try:
        rawSoup = WebServices.urlToSoup(cookieSession, aldiStoreUrl)
    except ValueError as err:
        print err
    else:

        for currentScripts in rawSoup.find_all('script'):
            for currentScript in currentScripts:
                if ("window" in currentScript) and ("flyerConfigs" in currentScript):
                    hostedStackStr = currentScript.split('window[\'hostedStack\'] = ', 1)[1]
                    hostedStackStr = hostedStackStr.split(';', 1)[0]
                    # Load the JSON into a dictionary
                    hostedStackJson = json.loads(hostedStackStr)

                    for currentFlyer in hostedStackJson:
                        
                        currentFlyerUrl = "https://flipp.aldi.us/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
# Use the store code for the Catalog URLs.
#
def getDollarGeneralCatalogUrls(storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    dollarGeneralStoreUrl = 'http://weeklyads.dollargeneral.com/flyer_selector/dollargeneral'
    dollarGeneralStoreUrl += '?action=show&locale=en-US'
    dollarGeneralStoreUrl += '&store_code=' + str(storeCode)
    dollarGeneralStoreUrl += '&type=2'

    try:
        rawSoup = WebServices.urlToSoup(cookieSession, dollarGeneralStoreUrl)
    except ValueError as err:
        print err
    else:

        for currentScripts in rawSoup.find_all('script'):
            for currentScript in currentScripts:
                if ("window" in currentScript) and ("flyerConfigs" in currentScript):
                    hostedStackStr = currentScript.split('window[\'hostedStack\'] = ', 1)[1]
                    hostedStackStr = hostedStackStr.split(';', 1)[0]
                    # Load the JSON into a dictionary
                    hostedStackJson = json.loads(hostedStackStr)

                    for currentFlyer in hostedStackJson:
                        
                        currentFlyerUrl = "http://weeklyads.dollargeneral.com/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        catalogUrls.append(currentFlyerUrl)

    return catalogUrls
    

#
#
#
def getFamilyDollarCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []


    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # TODO: Merchant ID is code in the URL.
    familyDollarStoreUrl = 'https://weeklyads.familydollar.com/shopping_lists/available_flyers?merchant_id=2150'
    familyDollarStoreUrl += '&postal_code=' + str(postCode)
    familyDollarStoreUrl += '&store_code=' + str(storeCode)

    try:
        rawJson = WebServices.urlToJson(cookieSession, familyDollarStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):
            currentFlyerId = flyerDetails['flyer_id']

            currentFlyerUrl = 'https://weeklyads.familydollar.com/flyer_data/' + str(currentFlyerId)
            currentFlyerUrl += '?locale=en-US'

            catalogUrls.append(currentFlyerUrl)

    return catalogUrls
    

#
#
#
def getFoodlionCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    familyDollarStoreUrl = 'https://ad.foodlion.com/flyers/foodlion?type=2&window.location.search.substr(1)'
    familyDollarStoreUrl += '&store_code=' + str(storeCode)

    try:
        rawSoup = WebServices.urlToSoup(cookieSession, familyDollarStoreUrl)
    except ValueError as err:
        print err
    else:
        for currentScripts in rawSoup.find_all('script'):
            for currentScript in currentScripts:
                if ("window" in currentScript) and ("flyerConfigs" in currentScript):
                    hostedStackStr = currentScript.split('window[\'hostedStack\'] = ', 1)[1]
                    hostedStackStr = hostedStackStr.split(';', 1)[0]
                    # Load the JSON into a dictionary
                    hostedStackJson = json.loads(hostedStackStr)

                    for currentFlyer in hostedStackJson:
                        
                        currentFlyerUrl = "https://ad.foodlion.com/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#
def getGiantfoodCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()
    # https://circular.giantfood.com/shopping_lists/available_flyers?merchant_id=2520&store_code=0304&postal_code=20603
    giantfoodStoreUrl = 'https://circular.giantfood.com/shopping_lists/available_flyers?merchant_id=2520'
    giantfoodStoreUrl += '&store_code=' + str(storeCode) 
    giantfoodStoreUrl += '&postal_code=' + str(postCode)

    try:
        rawJson = WebServices.urlToJson(cookieSession, giantfoodStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://circular.giantfood.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#
def getKrogerCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # 
    # Get the flyer ID from the JSON returned from this URL.
    krogerStoreUrl = 'https://wklyads-krogeratlanta.kroger.com/shopping_lists/available_flyers?merchant_id=2774'
    krogerStoreUrl += '&store_code=' + str(storeCode) 
    krogerStoreUrl += '&postal_code=' + str(postCode)

    try:
        rawJson = WebServices.urlToJson(cookieSession, krogerStoreUrl)
    except ValueError as err:
        print err
    else:
        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://wklyads-krogeratlanta.kroger.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#
def getMeijerCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    meijerStoreUrl = 'https://api.circularhub.com/content_showcase/v2/items?access_token=27fecb7dc705ffede8283cba8d989431'
    meijerStoreUrl += '&store_code=' + str(storeCode) 
    meijerStoreUrl += '&item_limit=0'

    try:
        rawJson = WebServices.urlToJson(cookieSession, meijerStoreUrl)
    except ValueError as err:
        print err
    else:
        print rawJson
        #https://weeklyad.meijer.com/flyer_data/1326357?locale=en-US            

    return catalogUrls


def getStopAndShopCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    #https://circular.stopandshop.com/shopping_lists/available_flyers?merchant_id=2393&store_code=0822&postal_code=07103
    StopAndShopStoreUrl = 'https://circular.stopandshop.com/shopping_lists/available_flyers?merchant_id=2393'
    StopAndShopStoreUrl += '&store_code=' + str(storeCode) 
    StopAndShopStoreUrl += '&postal_code=' + str(postCode)

    try:
        rawJson = WebServices.urlToJson(cookieSession, StopAndShopStoreUrl)
    except ValueError as err:
        print err
    else:
        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://circular.stopandshop.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            catalogUrls.append(currentFlyerUrl)


    return catalogUrls
    

#
# Use the store code for the Catalog URLs.
#
def getWalgreensCatalogUrls(storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    walgreensStoreUrl = 'https://flyer.walgreens.com/flyers/ffwalgreens-flyer?type=2&show_shopping_list_integration=1'
    walgreensStoreUrl += '&store_code=' + str(storeCode)

    try:
        rawSoup = WebServices.urlToSoup(cookieSession, walgreensStoreUrl)
    except ValueError as err:
        print err
    else:
        for currentScripts in rawSoup.find_all('script'):
            for currentScript in currentScripts:
                if ("window" in currentScript) and ("flyerConfigs" in currentScript):
                    hostedStackStr = currentScript.split('window[\'hostedStack\'] = ', 1)[1]
                    hostedStackStr = hostedStackStr.split(';', 1)[0]
                    # Load the JSON into a dictionary
                    hostedStackJson = json.loads(hostedStackStr)

                    for currentFlyer in hostedStackJson:
                        
                        # https://flyer.walgreens.com/flyer_data/1297564?locale=en-US
                        currentFlyerUrl = "https://flyer.walgreens.com/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        catalogUrls.append(currentFlyerUrl)


    return catalogUrls

#
# Use the store code for the Catalog URLs.
#
def getWalmartCatalogUrls(storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    walmartStoreUrl = 'https://weeklyads.walmart.com/hosted/walmart?locale=en&'
    walmartStoreUrl += 'store_code=' + str(storeCode)
    walmartStoreUrl += '&hide='

    try:
        rawJson = WebServices.urlToJson(cookieSession, walmartStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):
            currentFlyerId = flyerDetails['id']

            currentFlyerUrl = 'https://weeklyads.walmart.com/hosted/walmart/flyers/' + str(currentFlyerId)
            currentFlyerUrl += '?locale=en'
            currentFlyerUrl += '&store_code=' + str(storeCode)
            
            catalogUrls.append(currentFlyerUrl)

    return catalogUrls
    

#
# Scrape the catatlog from the retailer's flyer and write results.
#
def findRetailerUrl(retailer, postCode, storeCode):

    catalogUrls = []

    if(retailer.lower() == 'aldi'):
        catalogUrls = getAldiCatalogUrls(storeCode)
    elif(retailer.lower() == 'dollargeneral'):
        catalogUrls = getDollarGeneralCatalogUrls(storeCode)
    elif(retailer.lower() == 'familydollar'):
        catalogUrls = getFamilyDollarCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'foodlion'):
        catalogUrls = getFoodlionCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'giantfood'):
        catalogUrls = getGiantfoodCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'kroger'):
        catalogUrls = getKrogerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'meijer'):
        catalogUrls = getMeijerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'stopandshop'):
        catalogUrls = getStopAndShopCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'walgreens'):
        catalogUrls = getWalgreensCatalogUrls(storeCode)
    elif(retailer.lower() == 'walmart'):
        catalogUrls = getWalmartCatalogUrls(storeCode)
    else:
        print "ERROR: Unsupported retailer found (" + str(retailer) + ")"

        
    return catalogUrls
    

#
#
#
def main():

    # At this point we have the row numbers to process in Google sheets.
    googleSheetRowNumbers = verifyGoogleSheetRowNumbers()

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)


    # Report the Google Sheet row numbers.
    for currentRow in googleSheetRowNumbers:
        print "Catalytics Scrape for Google Sheet row: " + str(currentRow)

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
                # Load the values from the spreadsheet.
                retailerUrls = findRetailerUrl(row[0], row[8], row[9])
                print retailerUrls
                

#
#
#
if __name__ == '__main__':
    main()
