#!/usr/bin/python
# -*- coding: utf-8 -*-

# Beautiful Soup for processing.
from bs4 import BeautifulSoup

# Interact with web server.
import requests

# Work with strings.
import StringIO

# Need regular expressions for pattern matching.
import re

# Parse the web server response.
import json

import sys

# Catalog of Weekly Advertising.
from Catalog import Catalog

# Details of the item for sale.
from StoreItem import *

# Parsing JSON and data structures.
from WebParsers import *


#
# Verify that the website is returning the given status.
# 
# 200: Status OK.
# 301: URL has ben permenantly moved. (For example: please update your bookmarks.)
# 302: URL has ben terporarily moved. (For example: keep your bookmark as URL may change.)
#
def urlCheckStatus(cookieSession, url, statusesExpected = [200, 301, 302]):

    # Assume the web site at the given url is not alive,
    # until we know otherwise.
    foundExpected = False

    try:
        r = cookieSession.head(url)
    except requests.exceptions.RequestException as e:
        errMsg = "Error: unable to send request to url ("
        errMsg += str(url) + ")"
        print e
        raise ValueError(errMsg)
    except:
        print "Got an unknown exception..."
        print "Unexpected error:", sys.exc_info()[0]
        

    # Verify we get the expected status.
    for statusExpected in statusesExpected:
        if r.status_code == statusExpected:
            foundExpected = True
            break

    return foundExpected


#
# Request the JSON from the given URL.
#
def urlToJson(cookieSession, url):

    # Collect the data into this JSON to process further.
    siteJson = {}

    # We are only going to process a JSON response.
    headers = {"Accept": "application/json"}

    # Get all the information about this page.
    try:
        r = cookieSession.get(url, headers=headers)
    except requests.exceptions.RequestException as e:
        errMsg = "Error: unable to send request to url ("
        errMsg += str(url) + ")"
        raise ValueError(errMsg)
    else:

        # Verify request was successful.
        EXPECTED_STATUS_CODE = 200
        if r.status_code != EXPECTED_STATUS_CODE:
            errMsg = "Error: with sending request to web server ("
            errMsg += url + ")" + "\n"
            errMsg += "Error: expected: staus code of "
            errMsg += str(EXPECTED_STATUS_CODE)
            errMsg += " but received " + str(r.status_code)
            raise ValueError(errMsg)

        # Load the response into a stable scalar.
        try:
            siteJson = r.json()
        except:
            errMsg = "Error: With sending request to web server ("
            errMsg += url + ")" + "\n"
            errMsg += "Error: Unable to convert response into a JSON."
            raise ValueError(errMsg)

    return siteJson

#
# Use the cookie session to contact the given URL and return the 
# Beautiful soup. Cookies make sure that we continue the session.
#
def urlToSoup(cookieSession, url):

    # Collect the data into this beautiful soup to process further.
    soup = {}

    try:
        # Get all the information about this page.
        r = cookieSession.get(url)
    except requests.exceptions.RequestException as e:
        errMsg = "Error: unable to send request to url ("
        errMsg += str(url) + ")"
        raise ValueError(errMsg)
    else:
        # Verify request was successful.
        EXPECTED_STATUS_CODE = 200
        if r.status_code != EXPECTED_STATUS_CODE:
            errMsg = "Error: with sending request to web server ("
            errMsg += url + ")" + "\n"
            errMsg += "Error: expected: staus code of "
            errMsg += str(EXPECTED_STATUS_CODE)
            errMsg += " but received " + str(r.status_code)
            raise ValueError(errMsg)

        # Lets make this web page beautiful soup.
        soup = BeautifulSoup(r.text, 'lxml')

    return soup


#
# Scrape the PDF content from the given URL.
#
def urlToContent(cookieSession, url):

    urlContent = ""

    try:
        # Get all the information about this page.
        r = cookieSession.get(url)
    except requests.exceptions.RequestException as e:
        errMsg = "Error: unable to send request to url ("
        errMsg += str(url) + ")"
        raise ValueError(errMsg)
    else:
        # Verify request was successful.
        EXPECTED_STATUS_CODE = 200
        if r.status_code != EXPECTED_STATUS_CODE:
            errMsg = "Error: with sending request to web server ("
            errMsg += url + ")" + "\n"
            errMsg += "Error: expected: staus code of "
            errMsg += str(EXPECTED_STATUS_CODE)
            errMsg += " but received " + str(r.status_code)
            raise ValueError(errMsg)

        # Lets keep the PDF content.
        urlContent = r.content

    return urlContent


#
# Calculate the number of store Items that are in the given
# list that are of type Product.
#
def numberOfProducts(storeItems):

    # Assume the number of products in the catalog
    # zero until we know otherwise.
    numProducts = 0

    # Consider each item in the list.
    for currentStoreItem in storeItems:
        if currentStoreItem.mType == PRODUCT:
            # Found a store item that is a Product.
            numProducts += 1

    return numProducts


#
# For each store item in the catalog pull its image content down.
#
def populateImages(cookieSession, catalog):

    # Pull down the images for each of the store items with a URL.
    for pageNumber, storeItems in catalog.iteritems():
        for currentStoreItem in storeItems:

            if currentStoreItem.mLargeImageUrl:
                try:
                    currentStoreItem.mLargeImageContent = urlToContent(cookieSession,
                                                                       currentStoreItem.mLargeImageUrl)
                except ValueError as err:
                    print err
                    continue

                
            if currentStoreItem.mXLargeImageUrl:
                try:
                    currentStoreItem.mXLargeImageContent = urlToContent(cookieSession,
                                                                        currentStoreItem.mXLargeImageUrl)  
                except ValueError as err:
                    print err
                    continue

    return

#
# For each of the URLs associated with a given web server
# process the response and place into catalogs.
# eg a single webServer can be associated with multiple
#    urls that are related to multiple locations.
#
def scrapeToCatalogs(webServer, flyers, grouping):

    # Each of the catalogs of interest.
    catalogs = {}

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Before we start processing the data lets verify the website is acutally up.
    try:
        urlCheckStatus(cookieSession, webServer)
    except ValueError as err:
        print err
        print "Error: Do you require VPN to access this site?"
        # Do not continue as the web site is currently down.
        return catalogs

    # Determine if we need VPN access for this site.
    try:
        rawSoup = urlToSoup(cookieSession, webServer)
    except ValueError as err:
        print err
        print "Error: Do you require VPN to access this site?"
        return catalogs
    else:
        if requireVpnAccess(rawSoup):
            print "Error: Do you require VPN to access this site?"
            return catalogs

    # Consider each of the locations of interest for the webserver.
    #    for location, urlPath in flyers.iteritems():
    for currentFlyer in flyers:
        store = currentFlyer["store"]
        location = currentFlyer["location"]
        urlPath = currentFlyer["url"]
    
        catalog = Catalog(location, webServer)

        # Process both Flipp sites including Walmart.
        if (grouping == "Flipp") or \
           (grouping == "FlippForVpn") or \
           (grouping == "FlippForWalmart"):

            # Need to modify the url for processing Flipp
            # because they redirect traffic via reverse proxy
            # for Google Analytics.
            url = urlPath

            try:
                rawJsonData = urlToJson(cookieSession, url)
            except ValueError as err:
                print err
                continue
            else:

                # Create an empty dictionary to populate with the current catalog.
                currentCatalog, validFrom, externalName, pdfUrl = parseFlippJson(rawJsonData)

                for pageNumber, storeItems in currentCatalog.iteritems():

                    # CVS, Walmart store item(s) need more processing.
                    if (grouping == "FlippForWalmart"):
                        # Need to check if we need to get more information
                        # about each item.
                        for currentStoreItem in storeItems:
                            # We can use the given URL to get a few more details about this store item.
                            if currentStoreItem.mFlyerItemId:
                                # Create the item details URL.
                                # https://weeklyads.walmart.com/hosted/walmart/flyer_items/212910470?locale=en
                                detailsUrl = "https://weeklyads.walmart.com/hosted/walmart/flyer_items/"
                                detailsUrl += currentStoreItem.mFlyerItemId
                                detailsUrl += "?locale=en"
                                
                                try:
                                    itemDetailsJson = urlToJson(cookieSession, detailsUrl)
                                except ValueError as err:
                                    print err
                                    continue
                                else:
                                    # Get the description for this store item.
                                    itemDescription = parseFlippJsonItemDescription(itemDetailsJson)
                                    itemPrice = parseFlippJsonItemPrice(itemDetailsJson)
                                    if itemDescription or itemPrice:
                                        if itemDescription:
                                            currentStoreItem.mDescription = itemDescription
                                        if itemPrice:
                                            currentStoreItem.mPrice = itemPrice
                                        # Need to perform the cleanse again because
                                        # we have just changed the values.
                                        currentStoreItem.cleanse()

                            if currentStoreItem.mUrl:
                                try:
                                    itemDetailsSoup = urlToSoup(cookieSession, currentStoreItem.mUrl)
                                except ValueError as err:
                                    print err
                                    continue
                                else:
                                    # Extract the finer details.
                                    itemTitle, itemDescription, itemPrice, itemCategory, itemImageUrl = parseFlippWalmartItem(itemDetailsSoup)
                                    # Save the items.
                                    # Only update when the new details are valid.
                                    if itemTitle:
                                        currentStoreItem.mTitle = itemTitle
                                    if itemDescription:
                                        currentStoreItem.mDescription = itemDescription
                                    if itemPrice:
                                        currentStoreItem.mPrice = itemPrice
                                    if itemCategory:
                                        currentStoreItem.mCategory = itemCategory
                                    # Walmart only provides a single large image.
                                    if itemImageUrl:
                                        currentStoreItem.mLargeImageUrl = ""
                                        currentStoreItem.mXLargeImageUrl = itemImageUrl

                                    # Need to perform the cleanse again because
                                    # we have just changed the values.
                                    currentStoreItem.cleanse(join=False)

                    # Found a page in the catalog that is an advert.
                    if len(storeItems) == 0:
                        # Create a blank item.
                        blankItem = StoreItem()
                        blankItem.setToBlank()

                        # Blank line for the spread sheet.
                        catalog.addPage(pageNumber, [blankItem])
                    else:

                        # Save all the items for the current page in the catalog.
                        catalog.addPage(pageNumber, storeItems)

                # Save when this catalog is valid from.
                catalog.mValidFrom = validFrom
                catalog.mPdfUrl = pdfUrl

                # Take the current catalog and download the content for each of the store item's images.
                populateImages(cookieSession, currentCatalog)

                # Populate the PDF data using the PDF URL.
                if catalog.mPdfUrl:
                    try:
                        catalog.mPdfContent = urlToContent(cookieSession, catalog.mPdfUrl)
                    except ValueError as err:
                        print err
                        continue

                # Add another catalog.
                catalogIndex = store.replace(" ","") + "-" + location + "-" 
                catalogIndex += externalName + "-" + catalog.mValidFrom

                # Save the catalog so it can be printed out.
                catalogs[catalogIndex] = catalog

        elif grouping == "Webgrocer":

            # Create the url using the web server and the path to the catalog.
            url = urlPath

            # For Web Grocer we need to have a "/" on the end of the URL.
            # Check the last character in the string.
            if urlPath[-1] != "/":
                url +=  "/"

            # Need to determine the number of pages in the catalog.
            try:
                rawSoup = urlToSoup(cookieSession, url)
            except ValueError as err:
                print err
                continue
            else:
                externalName = ""
                # Lets grab each page from the catalog.
                for pageNumber in xrange(1, parseWebgrocerSoupPageCount(rawSoup) + 1):
                    try:
                        rawSoup = urlToSoup(cookieSession, url + str(pageNumber))
                    except ValueError as err:
                        print "Unable to process the URL: " + str(url) + str(pageNumber)
                        print err
                        continue
                    else:
                        # Get the store items on this page.
                        currentStoreItems, validFrom, externalName = parseWebgrocerSoup(rawSoup)

                        # When the description is missing from the store item we have
                        # more work to do, to go and get it.
                        for currentStoreItem in currentStoreItems:

                            # Get more data if we have a data ID.
                            if currentStoreItem.mDataId:

                                # Create the item details URL.
                                detailsUrl = webServer + "/CircularDetails/Item/" + currentStoreItem.mDataId
                                try:
                                    itemDetailsSoup = urlToSoup(cookieSession, detailsUrl)
                                except ValueError as err:
                                    print err
                                    continue
                                else:
                                    # Get the description for this store item.
                                    itemDescription = parseWebgrocerSoupItemDescription(itemDetailsSoup)
                                    itemPrice = parseWebgrocerSoupItemPrice(itemDetailsSoup)
                                    itemValidFrom, itemValidTo = parseWebgrocerSoupItemValidDates(itemDetailsSoup)
                                    # Get the image URL for this store item.
                                    itemImageUrl = parseWebgrocerSoupItemImageUrl(itemDetailsSoup)
                                    
                                    if itemDescription:
                                        currentStoreItem.mDescription = itemDescription
                                        
                                    # Only update the price if we don't already have one.
                                    if itemPrice and not currentStoreItem.mPrice:
                                        currentStoreItem.mPrice = itemPrice

                                    # Need to perform the cleanse again because
                                    # we have just changed the values.
                                    if (itemDescription) or (itemPrice and not currentStoreItem.mPrice):
                                        currentStoreItem.cleanse()

                                    if itemValidFrom:
                                        if "2001" not in itemValidFrom:
                                            currentStoreItem.mStartDate = itemValidFrom.replace("_","-")
                                            if itemValidFrom > validFrom:
                                                validFrom = itemValidFrom
                                    if itemValidTo:
                                        if "2001" not in itemValidTo:
                                            currentStoreItem.mEndDate = itemValidTo.replace("_","-")

                                    if itemImageUrl:
                                        currentStoreItem.mLargeImageUrl = itemImageUrl
                                        currentStoreItem.mXLargeImageUrl = itemImageUrl
                                        try:
                                            currentStoreItem.mLargeImageContent = urlToContent(cookieSession,
                                                                                               currentStoreItem.mLargeImageUrl)
                                            currentStoreItem.mXLargeImageContent = urlToContent(cookieSession,
                                                                                               currentStoreItem.mXLargeImageUrl)
                                        except ValueError as err:
                                            print err
                                            continue
                        
                        # Save when this catalog is valid from.
                        if validFrom > catalog.mValidFrom:
                            catalog.mValidFrom = validFrom
                        
                        # Found a page in the catalog that is an advert.
                        if numberOfProducts(currentStoreItems) == 0:
                            # Blank line for the spread sheet.
                            blankStoreItem = StoreItem()
                            blankStoreItem.setToBlank()
                        
                            catalog.addPage(pageNumber, [blankStoreItem])
                        else:
                            # Save all the items for the current page in the catalog.
                            catalog.addPage(pageNumber, currentStoreItems)

                # Verify that we could find the valid from date,
                # otherwise no point saving this catalog.
                if not catalog.mValidFrom or not externalName:
                    print "Error: Has the Catalog expired?"
                    print " * External Name: " + externalName
                    print " * Valid From: " + catalog.mValidFrom
                    print "Error: Update Catalytics configuration."
                    print " * Store: " + store
                    print " * Location: " + location
                    print " * URL: " + urlPath
                    continue

                # Get the URL to the JPEG images for this Catalog so can build a PDF.
                try:
                    pdfImagesSoup = urlToSoup(cookieSession, url + "0/Print")
                except:
                    continue
                else:
                    # Extract the image URLs from the beautiful soup.
                    pdfImageUrls = parseWebgrocerSoupPdfImages(pdfImagesSoup)
                    pdfImageContent = []

                    # Get the content of the images for each page of the catalog.
                    for currentUrl in pdfImageUrls:
                        catalog.mPdfImageContent.append(urlToContent(cookieSession,
                                                                     currentUrl))

                # Add another catalog.
                catalogIndex = store.replace(" ","") + "-" + location + "-" 
                catalogIndex += externalName + "-" + catalog.mValidFrom
                    
                # Save the catalog so it can be printed out.
                catalogs[catalogIndex] = catalog

        elif grouping == "PublixForVpn":

            # Create the url using the web server and the path to the catalog.
            url = urlPath

            # Need to determine the number of pages in the catalog.
            try:
                rawSoup = urlToSoup(cookieSession, url)
            except ValueError as err:
                print err
                continue
            else:
                for pageNumber in xrange(1, parsePublixSoupPageCount(rawSoup) + 1):
                    urlPageNumber = url
                    urlPageNumber += '&pagenumber=' + str(pageNumber)
                    print urlPageNumber
                    try:
                        rawSoup = urlToSoup(cookieSession, str(urlPageNumber))
                    except ValueError as err:
                        print "Unable to process the URL: " + str(urlPageNumber)
                        print err
                        continue
                    else:
                        currentStoreItems, validFrom, externalName = parsePublixSoup(rawSoup)

                        # Save when this catalog is valid from.
                        if validFrom > catalog.mValidFrom:
                            catalog.mValidFrom = validFrom
                        
                        # Found a page in the catalog that is an advert.
                        if numberOfProducts(currentStoreItems) == 0:
                            # Blank line for the spread sheet.
                            blankStoreItem = StoreItem()
                            blankStoreItem.setToBlank()
                        
                            catalog.addPage(pageNumber, [blankStoreItem])
                        else:
                            # Save all the items for the current page in the catalog.
                            catalog.addPage(pageNumber, currentStoreItems)

                # Take the current catalog and download the content for each of the store item's images.
                populateImages(cookieSession, catalog.mPages)

                # Add another catalog.
                catalogIndex = store.replace(" ","") + "-" + location + "-" 
                catalogIndex += externalName + "-" + catalog.mValidFrom
                    
                # Save the catalog so it can be printed out.
                catalogs[catalogIndex] = catalog

        elif grouping == "SEgrocer":

            ######################################
            # TODO: Currently under development. #
            ######################################
            print "Entered processing for SE Grocer"

            url = urlPath
            print "url"
            print url

            # https://coupons.bi-lo.com/services/gco?size=10000

            # Content of the POST.
            payload = {"storeCode": "5282",
                       "isPrintedCircular": "true"}

            # Tell the web server the format of the request.
            headers = {'Content-type': 'application/json',
                       'Accept': '*/*',
                       'Transfer-Encoding':'chunked'}

            try:
                # Get all the information about this page.
                r = cookieSession.post('hurlit.com')

            except requests.exceptions.RequestException as e:
                print "Unable to send a post..."
                print e
                continue
                
            # Verify request was successful.
            EXPECTED_STATUS_CODE = 200
            if r.status_code != EXPECTED_STATUS_CODE:
                print "Error: with sending request to web server (" + \
                    url + ")"
                print "Error: expected: staus code of " + \
                    str(EXPECTED_STATUS_CODE) + \
                    " but received " + str(r.status_code)
                continue

            # Load the response into a stable scalar.
            rawJsonData = r.json()

            print rawJsonData

    return catalogs



#
# Use the store code to compute the Aldi Catalogs URLs.
#
def getAldiCatalogUrls(storeCode):

    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    aldiStoreUrl = 'https://flipp.aldi.us/flyers/aldi?type=2&store_code=' + str(storeCode)

    try:
        rawSoup = urlToSoup(cookieSession, aldiStoreUrl)
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

                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
                            catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#
def getBiloCatalogUrls(storeCode):

    catalogUrls = []

    catalogUrls.append("https://coupons.bi-lo.com/services/gco?size=10000")

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
        rawSoup = urlToSoup(cookieSession, dollarGeneralStoreUrl)
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
                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
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
        rawJson = urlToJson(cookieSession, familyDollarStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):
            currentFlyerId = flyerDetails['flyer_id']

            currentFlyerUrl = 'https://weeklyads.familydollar.com/flyer_data/' + str(currentFlyerId)
            currentFlyerUrl += '?locale=en-US'

            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
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
        rawSoup = urlToSoup(cookieSession, familyDollarStoreUrl)
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

                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
                            catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#    
def getFrescoymasCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()
    # https://www.circularhub.com/shopping_lists/available_flyers?merchant_id=4417&store_code=0243&postal_code=33012
    frescoymasStoreUrl = 'https://www.circularhub.com/shopping_lists/available_flyers?merchant_id=4417'
    frescoymasStoreUrl += '&store_code=' + str(storeCode) 
    frescoymasStoreUrl += '&postal_code=' + str(postCode)

    try:
        rawJson = urlToJson(cookieSession, frescoymasStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://www.circularhub.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
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
        rawJson = urlToJson(cookieSession, giantfoodStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://circular.giantfood.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
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
        rawJson = urlToJson(cookieSession, krogerStoreUrl)
    except ValueError as err:
        print err
    else:
        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://wklyads-krogeratlanta.kroger.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
                catalogUrls.append(currentFlyerUrl)


    # Need to try this alternative if unable to process the JSON.
    if(len(catalogUrls) == 0):

        krogerStoreUrl = "https://wklyads-krogercentral.kroger.com/flyers/krogercentral?type=2"
        krogerStoreUrl += "&store_code=" + str(storeCode)

        try:
            rawSoup = urlToSoup(cookieSession, krogerStoreUrl)
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
                        
                            # https://wklyads-krogercentral.kroger.com/flyers/krogercentral-online?flyer_run_id=270469&store_code=00850&type=2
                            currentFlyerUrl = "https://wklyads-krogeratlanta.kroger.com/flyer_data/"
                            currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                            currentFlyerUrl += "?locale=en-US"

                            # Can get URLs from this retailer that are repeated.
                            # So only add unique URLs.
                            if currentFlyerUrl not in catalogUrls:
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
    # https://weeklyad.meijer.com/flyer_selector/meijer?action=show&locale=en&show_shopping_list_integration=1&store_code=158&type=2
    meijerStoreUrl = 'https://weeklyad.meijer.com/flyer_selector/meijer?action=show&locale=en&show_shopping_list_integration=1'
    meijerStoreUrl += '&store_code=' + str(storeCode) 
    meijerStoreUrl += '&type=2'

    try:
        rawSoup = urlToSoup(cookieSession, meijerStoreUrl)
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
                        
                        currentFlyerUrl = "https://weeklyad.meijer.com/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
                            catalogUrls.append(currentFlyerUrl)

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
        rawJson = urlToJson(cookieSession, StopAndShopStoreUrl)
    except ValueError as err:
        print err
    else:
        for flyerIndex, flyerDetails in enumerate(rawJson):

            currentFlyerUrl = "https://circular.stopandshop.com/flyer_data/"
            currentFlyerUrl += str(flyerDetails['flyer_id'])
            currentFlyerUrl += "?locale=en-US"

            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
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
        rawSoup = urlToSoup(cookieSession, walgreensStoreUrl)
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

                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
                            catalogUrls.append(currentFlyerUrl)


    return catalogUrls


# https://circular.cvs.com/flyers/cvspharmacy?type=2&store_code=402&postal_code=33131&auto_locate=true
#
# Use the store code for the Catalog URLs.
#
def getCvsCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    cvsStoreUrl = 'https://circular.cvs.com/flyers/cvspharmacy?type=2'
    cvsStoreUrl += '&store_code=' + str(storeCode)
    cvsStoreUrl += '&postal_code=' + str(postCode)
    cvsStoreUrl += '&auto_locate=true'

    try:
        rawSoup = urlToSoup(cookieSession, cvsStoreUrl)
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
                        
                        currentFlyerUrl = "https://circular.cvs.com/flyer_data/"
                        currentFlyerUrl += str(currentFlyer['current_flyer_id'])
                        currentFlyerUrl += "?locale=en-US"

                        # Can get URLs from this retailer that are repeated.
                        # So only add unique URLs.
                        if currentFlyerUrl not in catalogUrls:
                            catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
# Use the store code for the Catalog URLs.
#
def getRiteAidCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    riteAidStoreUrl = 'https://weeklyad.info.riteaid.com/shopping_lists/available_flyers?merchant_id=2287'
    riteAidStoreUrl += '&store_code=' + str(storeCode)
    riteAidStoreUrl += '&postal_code=' + str(postCode)

    try:
        rawJson = urlToJson(cookieSession, riteAidStoreUrl)
    except ValueError as err:
        print err
    else:
        # Set a default invalid flyer ID.
        highestFlyerId = -1

        for flyerIndex, flyerDetails in enumerate(rawJson):
            currentFlyerId = flyerDetails['flyer_id']
            # Looking for the highest flyer ID.
            if int(currentFlyerId) > highestFlyerId:
                highestFlyerId = int(currentFlyerId)

        # Cherry pick the highest flyer ID.
        if highestFlyerId > 0:
            currentFlyerUrl = 'https://weeklyad.info.riteaid.com/flyer_data/' + str(highestFlyerId)
            currentFlyerUrl += '?locale=en-US'

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
        rawJson = urlToJson(cookieSession, walmartStoreUrl)
    except ValueError as err:
        print err
    else:

        for flyerIndex, flyerDetails in enumerate(rawJson):
            currentFlyerId = flyerDetails['id']

            currentFlyerUrl = 'https://weeklyads.walmart.com/hosted/walmart/flyers/' + str(currentFlyerId)
            currentFlyerUrl += '?locale=en'
            currentFlyerUrl += '&store_code=' + str(storeCode)
            
            # Can get URLs from this retailer that are repeated.
            # So only add unique URLs.
            if currentFlyerUrl not in catalogUrls:
                catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
# Use the store code for the Catalog URLs.
#
def getWebgrocerCatalogUrls(site, storeCode):


    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    # Get the flyer ID from the JSON returned from this URL.
    # 
    webgrocerStoreUrl = str(site) + '/Circular/'
    webgrocerStoreUrl += str(storeCode)

    try:
        rawSoup = urlToSoup(cookieSession, webgrocerStoreUrl)
    except ValueError as err:
        print err
    else:
        for currentAnchor in rawSoup.find_all('a'):
            if currentAnchor.get('class'):
                if currentAnchor.get('class')[0] == "megadrop-circular-name":

                    currentFlyerUrl = str(site)
                    currentFlyerUrl += currentAnchor.get('href')

                    # Can get URLs from this retailer that are repeated.
                    # So only add unique URLs.
                    if currentFlyerUrl not in catalogUrls:
                        catalogUrls.append(currentFlyerUrl)

    return catalogUrls


#
#
#
def getHebCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    hebStoreUrl = 'https://mydigitalpublication.com/publication/?pid=136'
    hebStoreUrl += '&co=US&current=1'
    hebStoreUrl += '&pc=' + str(storeCode)
    
    try:
        rawSoup = urlToSoup(cookieSession, hebStoreUrl)
    except ValueError as err:
        print err
    else:
        for currentScripts in rawSoup.find_all('script'):
            for currentScript in currentScripts:
                if ("window" in currentScript) and ("issue_id" in currentScript):
                    
                    stateStr = currentScript.split('var state = ', 1)[1]
                    stateStr = stateStr.split(';', 1)[0]
                    # Load the JSON into a dictionary
                    stateJson = json.loads(stateStr)

                    currentFlyerUrl = "https://mydigitalpublication.com/publication/rollover_contents.php?id_issue="
                    currentFlyerUrl += str(stateJson['issue_id'])
                    currentFlyerUrl += "&text=1&markdown=1&lily_only=1&out=json"

                    # Can get URLs from this retailer that are repeated.
                    # So only add unique URLs.
                    if currentFlyerUrl not in catalogUrls:
                        catalogUrls.append(currentFlyerUrl)

    return catalogUrls

#
#
#
def getPublixCatalogUrls(postCode, storeCode):

    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    publixStoreUrl = 'http://weeklyad.publix.com/Publix/Entry/LandingContent'
    publixStoreUrl += '?storeid=' + str(storeCode)
    publixStoreUrl += '&sneakpeek=N&listingid=0'
    
    try:
        rawSoup = urlToSoup(cookieSession, publixStoreUrl)
    except ValueError as err:
        print err
    else:

        # Get the URL to find the promotion code.
        urlForPromotionCode = parsePublixSoupLandingToPromotion(rawSoup)

        if urlForPromotionCode:
            
            try:
                promotionCodeSoup = urlToSoup(cookieSession, urlForPromotionCode)
            except ValueError as err:
                print err
            else:
                # Get the promotion code.
                promotionCode = parsePublixSoupPromotionCode(promotionCodeSoup)

                if promotionCode is not None:
                    flyerUrl = 'http://weeklyad.publix.com/Publix/BrowseByPage?promotionviewmode=1&listingid=0'
                    flyerUrl += '&storeid=' + str(storeCode)
                    flyerUrl += '&promotionid=' + str(promotionCode)

                    catalogUrls.append(flyerUrl)

    return catalogUrls

def getTargetCatalogUrls(postCode, storeCode):


    # List of catalog URLs for this store code.
    catalogUrls = []

    # Maintain cookies for interactions with retailer's website(s).
    cookieSession = requests.Session()

    targetStoreUrl = 'https://weeklyad-api.target.com/weekly_ads/v1/store_promotions'
    targetStoreUrl += '?key=360729a3d898ec130e09f7caadd8c165'
    targetStoreUrl += '?storeid=' + str(storeCode)
    
    try:
        rawJson = urlToJson(cookieSession, targetStoreUrl)
    except ValueError as err:
        print err
    else:
        print rawJson
        #for flyerIndex, flyerDetails in enumerate(rawJson):

            #currentFlyerId = flyerDetails['id']
            #
            #currentFlyerUrl = 'https://weeklyads.walmart.com/hosted/walmart/flyers/' + str(currentFlyerId)
            #currentFlyerUrl += '?locale=en'
            #currentFlyerUrl += '&store_code=' + str(storeCode)
            #
            #catalogUrls.append(currentFlyerUrl)


    return catalogUrls


#
# Scrape the catatlog from the retailer's flyer and write results.
#
def findRetailerUrl(retailer, site, postCode, storeCode):

    catalogUrls = []

    if(retailer.lower() == 'aldi'):
        catalogUrls = getAldiCatalogUrls(storeCode)
    elif(retailer.lower() == 'bilo'):
        catalogUrls = getBiloCatalogUrls(storeCode)
    elif(retailer.lower() == 'dollargeneral'):
        catalogUrls = getDollarGeneralCatalogUrls(storeCode)
    elif(retailer.lower() == 'familydollar'):
        catalogUrls = getFamilyDollarCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'foodlion'):
        catalogUrls = getFoodlionCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'frescoymas'):
        catalogUrls = getFrescoymasCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'giantfood'):
        catalogUrls = getGiantfoodCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'heb'):
        catalogUrls = getHebCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'kroger'):
        catalogUrls = getKrogerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'meijer'):
        catalogUrls = getMeijerCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'publix'):
        catalogUrls = getPublixCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'stopandshop'):
        catalogUrls = getStopAndShopCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'target'):
        catalogUrls = getTargetCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'walgreens'):
        catalogUrls = getWalgreensCatalogUrls(storeCode)
    elif(retailer.lower() == 'cvs'):
        catalogUrls = getCvsCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'riteaid'):
        catalogUrls = getRiteAidCatalogUrls(postCode, storeCode)
    elif(retailer.lower() == 'walmart'):
        catalogUrls = getWalmartCatalogUrls(storeCode)
    elif((retailer.lower() == 'acmemarkets') or
         (retailer.lower() == 'albertsons') or
         (retailer.lower() == 'safeway') or
         (retailer.lower() == 'shoprite')):
        catalogUrls = getWebgrocerCatalogUrls(site, storeCode)
    else:
        print "ERROR: Unsupported retailer found (" + str(retailer) + ")"

        
    return catalogUrls


