#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Process the input arguments.
import argparse

import os

import json

import sys

import datetime

# Get the non-standard python packages from the virtual environment 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../venv/Lib/site-packages')))

# Get the source code for Catalytics.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../code')))

import tempfile
import shutil


## Services to scrape web sites.
import WebServices

# ERROR: When include DocumentServices cannot run in the Azure cloud.
# Services to work with documents.
#import DocumentServices

# Interact with web server.
import requests

# Set the enviornment so we can make https requests.
# Note: This is different to the ususal Linux location.
os.environ["REQUESTS_CA_BUNDLE"] = "/cacert/cacert.pem"

# Location of where to place the documents and images.
OUTPUT_DIR = tempfile.mkdtemp(prefix='/local/', suffix='/')

#
#
#
def verifyInputArgs():
    
    parser = argparse.ArgumentParser(description='Azure Catalyics Scraping.')
    parser.add_argument('retailer', metavar='retailer', type=str, nargs=1,
                        help='Name of retailer, example Walmart.')
    parser.add_argument('location', metavar='location', type=str, nargs=1,
                        help='Location of retailer, example NY.')
    parser.add_argument('store', metavar='store', type=str, nargs=1,
                        help='Store of retailer.')
    parser.add_argument('retailerUrl', metavar='site', type=str, nargs=1,
                        help='Retailer URL, example www.walmart.com')
    parser.add_argument('grouping', metavar='grouping', type=str, nargs=1,
                        help='Grouping of retailer, example Flipp.')
    parser.add_argument('suburb', metavar='grouping', type=str, nargs=1,
                        help='Suburb of retailer.')
    parser.add_argument('storeCode', metavar='grouping', type=str, nargs=1,
                        help='Store code of retailer.')

    # Parse the input arguments.
    args = parser.parse_args()

    return args.retailer[0], args.location[0], args.store[0], args.retailerUrl[0], args.grouping[0], args.suburb[0], args.storeCode[0]


##
## Scrape the catatlog from the retailer's flyer and write results.
##
#def scrapeAndWrite(retailer, location, store, site, flyerUrl, grouping):
#
#    # Get catalogs associated with website.
#    print("-> Scrape Retailer: " + str(retailer) + "-" + str(location) + "-" + str(flyerUrl))
#
#    print "Create a cookie session..."
#    # Maintain cookies for interactions with retailer's website(s).
#    cookieSession = requests.Session()
#
#    try:
#        print "About to head"
#        print str(site)
#        r = cookieSession.head(site)
#        print "Got a head"
#    except requests.exceptions.RequestException as e:
#        print "Got a know exception"
#        errMsg = "Error: unable to send request to url ("
#        errMsg += str(site) + ")"
#        print e
#        raise ValueError(errMsg)
#    except:
#        print "Got an unknown exception..."
#        type, value, traceback = sys.exc_info()
#        print "Unexpected error:"
#        print "type: ", type
#        print "value: ", value,
#        print "traceback: ", traceback

#    catalogs = WebServices.scrapeToCatalogs(site,
#                                            [{"store": store,
#                                              "location": location,
#                                              "url": flyerUrl}],
#                                            grouping)
#
#    print "Got to here..."
#    if len(catalogs) == 0:
#        # No point trying to generate a spreadsheet or PDF.
#        print("Error: no weekly advertisement data found from (" + \
#              str(retailer) + ")")
#        return
#        
#    print("  -> Write Catalogs to XLSX")
#    DocumentServices.writeCatalogsToSpreadsheet(grouping,
#                                                retailer,
#                                                catalogs,
#                                                OUTPUT_DIR)

#    print("  -> Write Catalogs to CSV")
#    DocumentServices.writeCatalogsToCsv(grouping,
#                                        retailer,
#                                        catalogs,
#                                        OUTPUT_DIR)

#    print("  -> Write Catalogs to PDF")
#    DocumentServices.writeCatalogsToPdf(grouping,
#                                        retailer,
#                                        catalogs,
#                                        OUTPUT_DIR)



#
# Scrape the catatlog from the retailer's flyer and write results.
#
def findRetailerUrl(retailer, site, postCode, storeCode):

    catalogUrls = []

    if(retailer.lower() == 'aldi'):
        catalogUrls = WebServices.getAldiCatalogUrls(storeCode)
    elif(retailer.lower() == 'dollargeneral'):
        catalogUrls = WebServices.getDollarGeneralCatalogUrls(storeCode)
    elif(retailer.lower() == 'familydollar'):
        catalogUrls = WebServices.getFamilyDollarCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'foodlion'):
        catalogUrls = WebServices.getFoodlionCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'giantfood'):
        catalogUrls = WebServices.getGiantfoodCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'kroger'):
        catalogUrls = WebServices.getKrogerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'meijer'):
        catalogUrls = WebServices.getMeijerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'stopandshop'):
        catalogUrls = WebServices.getStopAndShopCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'walgreens'):
        catalogUrls = WebServices.getWalgreensCatalogUrls(storeCode)
    elif(retailer.lower() == 'cvs'):
        catalogUrls = WebServices.getCvsCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'riteaid'):
        catalogUrls = WebServices.getRiteAidCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'walmart'):
        catalogUrls = WebServices.getWalmartCatalogUrls(storeCode)
    elif((retailer.lower() == 'acmemarkets') or
         (retailer.lower() == 'albertsons') or
         (retailer.lower() == 'safeway') or
         (retailer.lower() == 'shoprite')):
        catalogUrls = WebServices.getWebgrocerCatalogUrls(site, storeCode)
    else:
        print "ERROR: Unsupported retailer found (" + str(retailer) + ")"

        
    return catalogUrls


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

    # Debug: Lets have a quick look at the results.
    for currentCatalogName, currentCatalog in catalogs.iteritems():
        print currentCatalogName


    # TODO: Write the results to disk.
    #DocumentServices.writeCatalogs(grouping, retailer, catalogs, outputDir)

    # TODO: Write results directly to Azure bucket.


#
#
#
def main():

    # Get the input arguments.
    retailer, location, store, retailerUrl, grouping, suburb, storeCode = verifyInputArgs()

    # Dynamically determine the catalogs for a given retailer's store.
    # Rows are: Retailer, RetailerUrl, Suburb, Store Code.
    flyerUrls = findRetailerUrl(retailer, retailerUrl, suburb, storeCode)

    # Scrape the catalogs for the given retailer's store.
    if len(flyerUrls) > 0:
        for flyerIndex, flyerUrl in enumerate(flyerUrls):
            print str(flyerUrl)
            # Rows are: Retailer, Location, Store Addr, Retailer Url, flyerUrl, grouping
            # scrapeAndWrite(OUTPUT_DIR, retailer, location, store, retailerUrl, flyerUrl, grouping)
    else:
        print "Error: No flyer URLs found for this retailer."

    # Nuke the output dir.
    shutil.rmtree(OUTPUT_DIR)

#
#
#
if __name__ == '__main__':
    main()
