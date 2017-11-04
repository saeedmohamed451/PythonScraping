#!/usr/bin/python
# -*- coding: utf-8 -*-

# Beautiful Soup for processing.
from bs4 import BeautifulSoup

# Details of the item for sale.
from StoreItem import StoreItem

# Need regular expressions for pattern matching.
import re

# Parse the web server response.
import json

#
# Locate the page number that is associated with the given JSON item.
# If the item is spread over multiple pages we simply return the lower
# page number.
#
def itemOnPage(item, pages):

    # Assume the item is not on any of the catalog pages
    # until we know otherwise.
    pageNumber = -1

    # Loop though each of the pages.
    for page in pages:
        # Consider the item's horizontal position.
        if item["right"] < page["left"]:
            continue
        if item["left"] > page["right"]:
            continue

        # Consider the item's veritical position.
        if item["bottom"] > page["top"]:
            continue
        if item["top"] < page["bottom"]:
            continue

        # Found the page number where this item is located.
        pageNumber = page["page"]

        # No point looking any further.
        break

    return pageNumber


#
# Locate the category that is associated with the given JSON item.
#
def itemInCategory(item, categories):

    # Assume the item is any category until we know otherwise.
    categoryName = "Other"

    # Loop though each of the pages.
    for category in categories:
        # Consider the item's horizontal position.
        if item["left"] < category["left"]:
            continue
        if item["right"] > category["right"]:
            continue

        # Consider the item's veritical position.
        if item["top"] > category["top"]:
            continue
        if item["bottom"] < category["bottom"]:
            continue

        # Found the category this item belongs to.
        categoryName = category["name"]

        # No point looking any further.
        break

    return categoryName


#
# Take the Flipp Beautiful Soup for a single store
# item, and extract the item's price.
#
def parseFlippSoupItemPrice(soup):

    # Assume we have an empty description for this item
    # until we know otherwise.
    price = ""

    for currentSpan in soup.find_all('span'):
        if currentSpan.get('class'):
            if currentSpan.get('class')[0] == "big_price":
                price = str(currentSpan.get('aria-label')[0].encode('utf8'))

    return price


#
# Extract details about the Walmart store item.
#
def parseFlippWalmartItem(soup):

    # Store items to extract from Walmart soup.
    title = ""
    description = ""
    price = ""
    category = ""
    imageUrl = ""

    # Find all embedded Javascript within the beautiful soup.
    for currentScripts in soup.find_all('script'):
        # Lets look at each Javascript.
        for currentScript in currentScripts:
            # Looking of a specific Javascript.
            if "_setReduxState" in currentScript:
                # Strip out the JSON embedded within the Javascript.
                headerStr = "^var\s*\_setReduxState\s*\=\s*function"
                headerStr += "\(\)\s*\{window\.\_\_WML\_REDUX\_"
                headerStr += "INITIAL\_STATE\_\_\s*\=\s*"
                footerStr = ";};$"

                embeddedJavascript = currentScript
                embeddedJavascript = re.sub(headerStr, '', embeddedJavascript)
                embeddedJavascript = re.sub(footerStr, '', embeddedJavascript)

                # Load the JSON into a dictionary
                embeddedJson = json.loads(embeddedJavascript)
                if embeddedJson.get("product"):
                    product = embeddedJson.get("product")
                    if product.get("midasContext"):
                        midasContext = product.get("midasContext")
                        if midasContext.get("query"):
                            title = str(midasContext.get("query").encode("utf8"))
                        if midasContext.get("price"):
                            price = str(midasContext.get("price"))
                        if midasContext.get("categoryPathName"):
                            category = str(midasContext.get("categoryPathName").encode("utf8"))
                        if product.get("primaryProduct"):
                            primaryProduct = product.get("primaryProduct")
                            if product.get("products"):
                                products = product.get("products")
                                if products.get(primaryProduct):
                                    currentProduct = products.get(primaryProduct)
                                    if currentProduct.get("productAttributes"):
                                        productAttributes = currentProduct.get("productAttributes")
                                        if productAttributes.get("detailedDescription"):
                                            description = str(productAttributes.get("detailedDescription").encode("utf8"))
                            
                if embeddedJson.get("productBasicInfo"):
                    productBasicInfo = embeddedJson.get("productBasicInfo")
                    selectedProductId = productBasicInfo.get("selectedProductId")
                    selectedProduct = productBasicInfo.get(selectedProductId)
                    # Get the raw image URL.
                    rawImageUrl = selectedProduct.get("imageUrl")
                    # Sometimes we can get a empty dict for the raw image URL.
                    if type(rawImageUrl) is str or type(rawImageUrl) is unicode:
                        imageUrl = str(rawImageUrl.encode("utf8"))
                        # Strip off everything after the '?' character.
                        if '?' in imageUrl:
                            imageUrl = imageUrl.split('?')[0]


                # Don't look any further in the Javascript.
                break

    return title, description, price, category, imageUrl


#
# Take the Flipp Beautiful Soup for a single store
# item, and extract the item's description.
#
def parseFlippSoupItemDescription(soup):

    # Assume we have an empty description for this item
    # until we know otherwise.
    description = ""

    for currentDiv in soup.find_all('div'):
        if currentDiv.get('class'):
            if currentDiv.get('class')[0] == "name":
                description = str(currentDiv.text.encode('utf8'))

    return description


#
# Take the Flipp JSON for a single store
# item, and extract the item's description.
#
def parseFlippJsonItemDescription(rawJsonItemData):

    # Assume we have an empty description for this item
    # until we know otherwise.
    description = ""

    if rawJsonItemData.get("description"):
        description += rawJsonItemData.get("description").encode("utf8")

    if rawJsonItemData.get("disclaimer_text"):
        description += rawJsonItemData.get("disclaimer_text").encode("utf8")


    return description


#
# Take the Flipp JSON for a single store
# item, and extract the item's price.
#
def parseFlippJsonItemPrice(rawJsonItemData):

    # Assume we have an empty price for this item
    # until we know otherwise.
    price = ""

    if rawJsonItemData.get("current_price"):
        price += rawJsonItemData.get("current_price").encode("utf8")
    elif rawJsonItemData.get("price_text"):
        price += rawJsonItemData.get("price_text").encode("utf8")


    return price


#
# Parse the JSON from Flipp site and convert to catalog.
#
def parseFlippJson(rawJsonData):

    currentCatalog = {}
    validFrom = ""
    externalName = ""
    pdfUrl = ""

    # Populate each of the pages with their indexes.
    for pageNumber in xrange(1, len(rawJsonData["pages"])+1):
        currentCatalog[pageNumber] = []

    # Save when this catalog is valid from.
    validFrom = rawJsonData["valid_from"].split("T")[0].replace("-","_")

    # Save the URL path to the catalog's PDF.
    pdfUrl = rawJsonData["pdf_url"]

    # Save the external name of this flyer.
    # For some Flipp sites the external name can be found in
    # multiple possible locations within the JSON.
    if rawJsonData.get("flyer_run_external_name"):
        externalName = rawJsonData.get("flyer_run_external_name")
    elif rawJsonData.get("flyer_type_name"):
        externalName = rawJsonData.get("flyer_type_name")
    
    # Clean up the external name.
    if externalName:
        externalName.replace(" ", "")

    # Now populate the items into the catalog.
    for currentItem in rawJsonData["items"]:

        # Advertised item in the store.
        storeItem = StoreItem()

        pageNumber =  itemOnPage(currentItem,
                                 rawJsonData["pages"])

        # Dont bother if this item is not in the catalog.
        if pageNumber <= 0:
            continue

        storeItem.mCategory = itemInCategory(currentItem,
                                             rawJsonData["categories"])


        # The name of the store Item can be found in multiple possible locations
        # within the JSON.
        if currentItem.get("display_name"):
            storeItem.mTitle = str(currentItem.get("display_name").encode("utf8"))
        elif currentItem.get("name"):
            storeItem.mTitle = str(currentItem.get("name").encode("utf8"))

        if currentItem.get("description"):
            storeItem.mDescription = str(currentItem.get("description").encode("utf8"))

        # Price is set to the current price or price text.
        if currentItem.get("current_price"):
            storeItem.mPrice = str(currentItem.get("current_price").encode("utf8"))
        elif currentItem.get("price_text"):
            storeItem.mPrice += " " + str(currentItem.get("price_text").encode("utf8"))

        # Add pre-price text to beginning of raw price.
        if currentItem.get("pre_price_text"):
            storeItem.mPrice = str(currentItem.get("pre_price_text").encode("utf8")) + " " + storeItem.mPrice

        # Add post-price text onto the end of the raw price.
        if currentItem.get("post_price_text"):
            storeItem.mPrice += " " + str(currentItem.get("pre_price_text").encode("utf8"))

        # Add story onto the end of raw price.
        if currentItem.get("sale_story"):
            storeItem.mPrice += " " + str(currentItem.get("sale_story").encode("utf8"))

        # Add disclaimer onto the end of raw price.
        if currentItem.get("disclaimer_text"):
            disclaimer = str(currentItem.get("disclaimer_text").encode("utf8"))
            disclaimer = disclaimer.replace("\n"," ")
            storeItem.mPrice += " " + disclaimer

        # Range of dates for this item.
        if currentItem.get("valid_from"):
            storeItem.mStartDate = str(currentItem.get("valid_from").encode("utf8"))
        if currentItem.get("valid_to"):
            storeItem.mEndDate = str(currentItem.get("valid_to").encode("utf8"))

        # Get the flyer item where can get additional information about this item.
        if currentItem.get("flyer_id"):
            storeItem.mFlyerId = str(currentItem.get("flyer_id"))
        if currentItem.get("flyer_item_id"):
            storeItem.mFlyerItemId = str(currentItem.get("flyer_item_id"))

        # Get the URL to the images for this store item.
        if currentItem.get("large_image_url"):
            storeItem.mLargeImageUrl = str(currentItem.get("large_image_url"))
        if currentItem.get("x_large_image_url"):
            storeItem.mXLargeImageUrl = str(currentItem.get("x_large_image_url"))

        # Get the URL to more detailed information a for this store item.
        if currentItem.get("url"):
            storeItem.mUrl = str(currentItem.get("url"))

        # Get the pixel location within the catalog.
        if currentItem.get("top"):
            storeItem.mTop = currentItem.get("top")
        if currentItem.get("bottom"):
            storeItem.mBottom = currentItem.get("bottom")
        if currentItem.get("left"):
            storeItem.mLeft = currentItem.get("left")
        if currentItem.get("right"):
            storeItem.mRight = currentItem.get("right")

        # Cleanse the store item before we append it.
        storeItem.cleanse()

        currentCatalog[pageNumber].append(storeItem)

    return currentCatalog, validFrom, externalName, pdfUrl

#
# Expecting a US date in the form (month, day, year(2 digits))
#
def convertUsToAusDate(usDate):

    # Assume australian date until we know otherwise.
    ausDate = "2001_01_01"

    # Must have 3 elements in list for month, day and year.
    if len(usDate) == 3:

        month = usDate[0]
        day = usDate[1]
        year = "2001"

        # Extract the year, month and day from US format,
        # to Australian date format.
        if len(usDate[2]) == 2:
            year = str(20) + usDate[2]
        elif len(usDate[2]) == 4:
            year = usDate[2]

        # Format needed for Australian date format.
        ausDate = year + "_" + month + "_" + day

    return ausDate


#
# Take the Web Grocer Beautiful soup for a single store
# item, and extract the item's valid from date.
#
def parseWebgrocerSoupItemValidDates(soup):

    # Valid date that the Store Item's price is valid from.
    # Enter a default value, until we know otherwise.
    validFrom = "2001_01_01"
    validTo = "2001_01_01"

    # Consider the paragraphs in the Beautiful soup.
    for currentParagraph in soup.find_all('p'):
        if currentParagraph.get('class'):
            # Find the paragraph with the valid date information in it.
            if currentParagraph.get('class')[0] == "valid-dates":
                # Extract the valid dates from the Beautiful soup.
                validDates = str(currentParagraph.text.encode('utf8'))

                # Possible formats for the valid date are:
                # eg Valid 08/13/17 - 08/19/17
                # eg Prices valid 08/13/17 - 08/19/17
                # Create a pattern match for the dates.
                patternValidDates = re.compile('(\d+\/\d+\/\d+)\s*\-\s*(\d+\/\d+\/\d+)',
                                               re.IGNORECASE)
                matchValidDates = patternValidDates.findall(validDates)

                # Now extract out the valid date from information.
                if len(matchValidDates) >= 1:
                    matchDateFrom = matchValidDates[0][0].split("/")
                    matchDateTo = matchValidDates[0][1].split("/")
                    validFrom = convertUsToAusDate(matchDateFrom)
                    validTo = convertUsToAusDate(matchDateTo)

    return validFrom, validTo

#
# Take the Web Grocer Beautiful soup for a single store
# item, and extract the item's description.
#
def parseWebgrocerSoupItemDescription(soup):

    # Assume we have an empty description for this item
    # until we know otherwise.
    description = ""

    for currentParagraph in soup.find_all('p'):
        if currentParagraph.get('class'):
            if currentParagraph.get('class')[0] == "description":
                description = str(currentParagraph.text.encode('utf8'))

    return description


#
# Take the Web Grocer Beautiful soup for a single store
# item, and extract the item's price.
#
def parseWebgrocerSoupItemPrice(soup):

    # Assume we have an empty price for this item
    # until we know otherwise.
    price = ""

    for currentParagraph in soup.find_all('p'):
        if currentParagraph.get('class'):
            if currentParagraph.get('class')[0] == "price":
                price = str(currentParagraph.text.encode('utf8'))

    return price


#
# Take the Web Grocer Beautiful soup for a single store
# item, and extract the URLs to each page of the PDF.
#
def parseWebgrocerSoupPdfImages(soup):

    pdfImageUrls = []

    for currentImage in soup.find_all('img'):
        if currentImage.get('class'):
            if currentImage.get('class')[0] == "circular-print-image":
                currentImageUrl = currentImage.get('src')
                pdfImageUrls.append(currentImageUrl)

    return pdfImageUrls


#
# Take the Web Grocer Beautiful soup for a single store
# item, and extract the item's description.
#
def parseWebgrocerSoupItemImageUrl(soup):

    # Assume we have an empty image URL for this item
    # until we know otherwise.
    imageUrl = ""

    for currentDiv in soup.find_all('div'):
        if currentDiv.get('id'):
            if currentDiv.get('id') == "QuicklookLeft":
                currentImg = currentDiv.find('img')
                imageUrl = currentImg['src']
                break

    return imageUrl

#
# Take the Web Grocer Beautiful soup and return then number of
# pages in this catalog.
#
def parseWebgrocerSoupPageCount(soup):

    # Assume no pages, until we know otherwise.
    pageCount = 0

    # Looks for the span as this has the page counts.
    for currentSpan in soup.find_all('span'):
        if currentSpan.get('class'):
            if currentSpan.get('class')[0] == "pages":
                # Find the maximum page count.
                if int(currentSpan.text) > pageCount:
                    pageCount = int(currentSpan.text)

    # Finally try and get the page count
    if pageCount == 0:
        for img in soup.find_all('img'):
            if img.get('id') == 'PageImage':
                if img.get('data-current-page'):
                    pageCount = int(img.get('data-current-page'))

    return pageCount


#
#
#
def parsePublixSoupLandingToPromotion(soup):

    urlForpromotionCode = ""

    for currentDiv in soup.find_all('div'):
        if currentDiv.get('class'):
            if currentDiv.get('class')[0] == 'posViewDealsBtn':
                for currentAnchor in currentDiv.find_all('a'):
                    if currentAnchor.get('class'):
                        if((currentAnchor.get('class')[0] == "btn") and
                           (currentAnchor.get('class')[1] == "btn-large") and
                           (currentAnchor.get('class')[2] == "action-tracking-nav")):
                            urlForPromotionCode = 'http://weeklyad.publix.com/'
                            urlForPromotionCode += str(currentAnchor.get('href'))

    return urlForPromotionCode


def parsePublixSoupPromotionCode(soup):

    promotionCode = None

    # look for div with this class 'mobileBBPSliderXofY'
    for currentDiv in soup.find_all('div'):
        if currentDiv.get('class'):
            if currentDiv.get('class')[0] == 'mobileBBPSliderXofY':
                if currentDiv.get('data-promotionid'):
                    promotionCode = currentDiv.get('data-promotionid')

    return promotionCode


def parseWebgrocerSoupExternalCatalogName(soup, catalogId):

    externalName = ""

    # Look through all the anchors.
    for currentAnchor in soup.find_all('a'):
        currentAnchorClass = currentAnchor.get('class')
        if currentAnchorClass:
            # Interested in specific anchors.
            if currentAnchorClass[0] == "megadrop-circular-name":
                # eg "3 Day Sale - 2022025"
                currentAnchorLabel = currentAnchor.get('data-clientanalyticslabel')
                if catalogId in currentAnchorLabel:
                    externalName = currentAnchorLabel.split('-')[0].replace(" ","")
                    # Found the external name of this catalog.
                    break


    return externalName


#
#
#
def parsePublixSoupPageCount(soup):

    # Assume no pages, until we know otherwise.
    pageCount = 0

    for currentSelect in soup.find_all('select'):
        if currentSelect.get('class') and currentSelect.get('id'):
            if ((currentSelect.get('class')[0]  == "selectSpinnerMobile") and 
                (currentSelect.get('class')[1]  == "action-mobile-page-picker") and
                (currentSelect.get('id') == "MobilePagePickerScroller")):

                for currentOption in currentSelect.find_all('option'):
                    pageCount += 1

    return pageCount


#
#
#
def parsePublixSoup(soup):

    storeItems = []
    validFrom = ""
    validTo = ""
    externalName = "WeeklyAd"

    # Determine the valid from and to date(s).
    for currentParagraph in soup.find_all('p'):
        if currentParagraph.get('class'):
            if((currentParagraph.get('class')[0] == 'mobile') and
               (currentParagraph.get('class')[1] == 'IDP_validDates')):

                validDates = str(currentParagraph.text.encode('utf8'))
                # Clean up the date.
                validDates = validDates.replace(' ','')
                validDates = validDates.replace('\r','')
                validDates = validDates.replace('\n','')
                # They use a '-' character between the valid from and to date.
                validFrom = validDates.split('\xe2\x80\x93')[0].split('Effective')[1]
                validTo = validDates.split('\xe2\x80\x93')[1]

                validFromMonth = validFrom.split('/')[0]
                validFromDay = validFrom.split('/')[1]
                validFrom = '2017_' + validFromMonth + '_' + validFromDay

                validToMonth = validTo.split('/')[0]
                validToDay = validTo.split('/')[1]
                validTo = '2017_' + validToMonth + '_' + validToDay

                break

    # Get the store items.
    for currentInput in soup.find_all('input'):
        if currentInput.get('class'):
            if ((currentInput.get('class')[0]  == "shoppingListButton") and 
                (currentInput.get('class')[1]  == "action-shoppinglist-toggle") and
                (currentInput.get('class')[2]  == "addToShoppingListBtn") and
                (currentInput.get('class')[3]  == "excludeFromMobile")  and
                (currentInput.get('class')[4]  == "action-tracking-nav")):

                # Advertised item in the store.
                storeItem = StoreItem()

                # TODO: storeItem.mCategory, storeItem.mUrl

                if currentInput.get('data_description'):
                    storeItem.mDescription = str(currentInput.get('data_description').encode("utf8"))
                if currentInput.get('data_title'):
                    storeItem.mTitle = str(currentInput.get('data_title').encode("utf8"))

                if currentInput.get('data_price'):
                    storeItem.mPrice = str(currentInput.get('data_price').encode("utf8"))
                elif currentInput.get('data_finalprice'):
                    storeItem.mPrice = str(currentInput.get('data_finalprice').encode("utf8"))

                # Convert to the correct format.
                startDateYear = validFrom.split('_')[0]
                startDateMonth = validFrom.split('_')[1]
                startDateDay = validFrom.split('_')[2]

                storeItem.mStartDate = startDateYear + '-' + startDateMonth + '-' + startDateDay

                endDateYear = validTo.split('_')[0]
                endDateMonth = validTo.split('_')[1]
                endDateDay = validTo.split('_')[2]

                storeItem.mEndDate = endDateYear + '-' + endDateMonth + '-' + endDateDay

                # Publix only provides a single image
                if currentInput.get('data-image'):
                    storeItem.mXLargeImageUrl = 'http:' + currentInput.get('data-image')

                # Cleanse the store item before we append it.
                storeItem.cleanse()
                storeItems.append(storeItem)

    return storeItems, validFrom, externalName


#
#
#
def requireVpnAccess(soup):

    requireVpn = False

    VPN_UNAVAILABLE = "Sorry, our site is unavailable "
    VPN_UNAVAILABLE += "in your country right now."

    for currentDiv in soup.find_all('div'):
        if currentDiv.get('class'):
            if currentDiv.get('class')[0] == "top":
                for currentH1 in currentDiv.find_all('h1'):
                    if VPN_UNAVAILABLE == currentH1.text:
                        requireVpn = True

    return requireVpn


#
# Take the Web Grocer Beautiful soup and return a list of the store items.
#
def parseWebgrocerSoup(soup):

    # All the items on the current Catalog page.
    storeItems = []
    validFrom = ""
    externalName = "weekly"
    
    # Link to the mapping area for the current displayed Catalog page.
    pageMapId = None
    
    # Find the Catalog page with special ID called "PageImage"
    for img in soup.find_all('img'):
        if img.get('id') == 'PageImage':
            # Get the source of this image ID.
            pageMapId = str(img.get('usemap').replace('#',''))
            catalogId = str(img.get('data-circular-id'))
            externalName = parseWebgrocerSoupExternalCatalogName(soup, catalogId)

            # Find the mouse over maps.
            for currentMap in soup.find_all('map'):
                # Get the ID of the current mouse over map.
                currentMapId = str(currentMap.get('name'))

                # Only interested in the mouse over map for current page of the catalog.
                if(currentMapId != pageMapId):
                    continue

                # Found the mouse over map!
                for currentArea in currentMap.find_all('area'):
    
                    # Keep the store item and need to encode as utf-8 
                    storeItem = StoreItem()
    
                    # Get the data for this point target.
                    dataId = currentArea.get('data-id')

                    # Possible some of this data is available.
                    dataTitle = currentArea.get('data-title')
                    dataDescription = currentArea.get('data-description')
                    dataPrice = currentArea.get('data-price-string')
                    dataType = currentArea.get('data-type')
                    dataStartDate = currentArea.get('data-valid-start-text')
                    dataEndDate = currentArea.get('data-valid-end-text')

                    if dataId:
                        storeItem.mDataId = str(dataId.encode('utf8'))
                    if dataTitle:
                        storeItem.mTitle = str(dataTitle.encode('utf8'))
                    if dataDescription:
                        storeItem.mDescription = str(dataDescription.encode('utf8'))
                    if dataPrice:
                        storeItem.mPrice = str(dataPrice.encode('utf8'))
                    if dataType:
                        storeItem.mType = str(dataType.encode('utf8'))
                    if dataStartDate:
                        storeItem.mStartDate = str(dataStartDate.encode('utf8'))
                        # Only process the date if it is not dummy data.
                        if storeItem.mStartDate != "01/01/01":
                            day = str(storeItem.mStartDate.split("/")[1])
                            month = str(storeItem.mStartDate.split("/")[0])
                            year = str(20) + str(storeItem.mStartDate.split("/")[2])
                            # Convert from american date format to Australian date format.
                            validFrom = year + "_" + month + "_" + day
                    if dataEndDate:
                        storeItem.mEndDate = str(dataEndDate.encode('utf8'))

                    # Price information is all hidden.
                    if dataId and not storeItem.mPrice:
                        for currentDiv in soup.find_all('div'):
                            if(currentDiv.get('id') == "CircularItem-" + str(dataId)):
                                storeItem.mPrice = currentDiv.find('p', {"class": "itemPrice"})
                                storeItem.mTitle = currentDiv.find('p', {"class": "itemTitle"})
    
                                # Strip out the text from the paragraph.
                                if storeItem.mPrice is not None:
                                    storeItem.mPrice = str(storeItem.mPrice.getText().encode('utf8'))
                                if storeItem.mTitle is not None:
                                    storeItem.mTitle = str(storeItem.mTitle.getText().encode('utf8'))

                                break



                    # Cleanse the store item before we append it.
                    storeItem.cleanse()

                    # Save what we were able to scrape.
                    storeItems.append(storeItem)

    return storeItems, validFrom, externalName
