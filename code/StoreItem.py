#!/usr/bin/python
# -*- coding: utf-8 -*-

# Need regular expressions for pattern matching.
import re

# Work with dates.
import datetime

# Need the bespoke dictionary of string replacements.
from DataCleanse import *

# Types of Store Items.
# A store item is a 'PRODUCT' when has price information.
PRODUCT = "Product"
# A store item is 'INFORMATION' when it has no price information.
INFORMATION = "Information"
# Used for store item when whole page of catalog has no store items.
BLANK = "BLANK"


#
# Each item in the retailer's store can be
# represented by this object so that we can 
# know its title, price, desription, etc.
#
class StoreItem(object):

    def __init__(self):

        # To get more beautiful soup information about this
        # store item, if needed.
        self.mDataId = ""

        # Name of the catalog/flyer that this store item came from.
        self.mFlyerId = ""

        # To get more JSON information about this store item,
        # if needed.
        self.mFlyerItemId = ""

        # Brief description about the item for sale.
        self.mTitle = ""
        self.mTitleCleansed = ""
        
        # Details about this item.
        self.mDescription = ""

        # Dollar price of item. 
        # If conditional includes the conditions.
        self.mPrice = ""
        self.mPriceCleansed = "0.0"

        # eg Homewares, Groceries etc.
        self.mCategory = ""

        # eg Product or Information
        self.mType = PRODUCT

        # When this item can be purchased
        # at the given price.
        self.mStartDate = ""

        # When this item can no longer be purchased
        # at the given price.
        self.mEndDate = ""

        # eg 2 for $8 then multibuy shall be 2.
        # Better price when we purhase multiple items.
        self.mMultibuy = ""

        # eg 'Loyalty Card', 'Half Price',
        #    'BOGOF' - Buy One Get One Free
        #    '3 for 2'.
        # Assume price reduction until we know otherwise.
        self.mPromotionType = PRICE_REDUCTION

        # URL to find the store item's images.
        self.mLargeImageUrl = ""
        self.mXLargeImageUrl = ""

        # Content of the store item's images.
        self.mLargeImageContent = ""
        self.mXLargeImageContent = ""

        # URL to get more information about this store item.
        self.mUrl = ""

        # Keep track of the pixel location in the catalog.
        self.mTop = 0
        self.mBottom = 0
        self.mLeft = 0
        self.mRight = 0


    #
    # Sometimes a whole page in a catalog is filled with an
    # Advertisement in which case there are no actual store
    # item information on this page.
    # A blank product store item represents this.
    #
    def setToBlank(self):

        self.mTitle = BLANK
        self.mTitleCleansed = BLANK
        self.mDescription = BLANK
        self.mCategory = BLANK
        self.mPromotionType = BLANK
        self.mPrice = 0.0
        self.mPriceCleansed = 0.0
        self.mType = INFORMATION

    #
    # Perform a data clean of the Price.
    #
    def cleansePrice(self):

        # Initialise the clean price.
        if self.mPrice:
            self.mPriceCleansed = self.mPrice

        # Strip out all white spaces, tabs and new lines.
        self.mPriceCleansed = "".join(str(self.mPriceCleansed).split())
        
        # Lets perform the pattern matching.
        # Starting with the longest patterns first.
        for currentPattern in sorted(PRICE_PATTERNS,
                                     key=len, reverse=True):
            replacePattern = PRICE_PATTERNS[currentPattern]
            patternCleanse = re.compile(currentPattern, re.IGNORECASE)
            matchCleanse = patternCleanse.findall(self.mPriceCleansed)

            if len(matchCleanse) >= 1:
                # DEBUG.
                # print "Price Cleanse: Pattern MATCH: " + str(currentPattern)
                if replacePattern:
                    # TODO: What is a better way of adding these smarts?
                    if replacePattern == "div 100":
                        self.mPriceCleansed = float(matchCleanse[0][0])/100.0
                    elif replacePattern == "div 20":
                        self.mPriceCleansed = float(matchCleanse[0][0])/20.0                    
                    elif replacePattern == "div 12":
                        self.mPriceCleansed = float(matchCleanse[0][0])/12.0                    
                    elif replacePattern == "div 10":
                        self.mPriceCleansed = float(matchCleanse[0][0])/10.0                    
                    elif replacePattern == "div 6":
                        self.mPriceCleansed = float(matchCleanse[0][0])/6.0                    
                    elif replacePattern == "div 5":
                        self.mPriceCleansed = float(matchCleanse[0][0])/5.0
                    elif replacePattern == "div 4":
                        self.mPriceCleansed = float(matchCleanse[0][0])/4.0                    
                    elif replacePattern == "div 3":
                        self.mPriceCleansed = float(matchCleanse[0][0])/3.0                    
                    elif replacePattern == "div 2":
                        self.mPriceCleansed = float(matchCleanse[0][0])/2.0
                    elif replacePattern == "mpy 2":
                        self.mPriceCleansed = float(matchCleanse[0][0])*2.0
                    else:
                        self.mPriceCleansed = replacePattern
                else:
                    self.mPriceCleansed = matchCleanse[0][0]
                # Don't bother looking any further as we have a 
                # matching pattern.
                break

        # Finally perform the symbolic replacements.
        # TODO: This could be replaced to remove all symbols.
        for before in sorted(SYMBOLIC_REPLACEMENTS, 
                             key=len, reverse=True):

            # What the string should look like after the replacement.
            after = SYMBOLIC_REPLACEMENTS[before]

            # String replacement.
            self.mPriceCleansed = str(self.mPriceCleansed).replace(before, after)

        try:
            # Keep accuracy of two decimal places,
            # for number of cents in dollar.
            self.mPriceCleansedFloat = round(float(self.mPriceCleansed), 2)
        except ValueError:
            # Not a float more work to do.
            pass
        else:
            # Successfully converted to a float so lets keep it.
            self.mPriceCleansed = self.mPriceCleansedFloat


    #
    # Perform a data clean of the Multibuy.
    #
    def cleanseMultibuy(self):

        # Initialise the price for multibuy.
        priceForMultibuy = ""

        # Initialise the clean price.
        if self.mPrice:
            priceForMultibuy = self.mPrice

        # Strip out all white spaces, tabs and new lines.
        priceForMultibuy = "".join(priceForMultibuy.split())

        # Look for specific patterns for each of the promotion
        # types we are interested in.
        for currentPattern in sorted(MULTIBUY_PATTERNS,
                                     key=len, reverse=True):

            replacePattern = MULTIBUY_PATTERNS[currentPattern]
            patternCleanse = re.compile(currentPattern, re.IGNORECASE)
            matchCleanse = patternCleanse.findall(priceForMultibuy)

            if len(matchCleanse) >= 1:
                # DEBUG.
                # print "Multibuy Cleanse: Pattern MATCH: " + str(currentPattern)
                self.mMultibuy = replacePattern
                break


    #
    # Perform a data clean of the Promotion Type.
    #
    def cleansePromotionType(self):

        # Initialise the price for promotion.
        priceForPromotion = ""

        # Initialise the clean price.
        if self.mPrice:
            priceForPromotion = self.mPrice

        # Strip out all white spaces, tabs and new lines.
        priceForPromotion = "".join(priceForPromotion.split())

        for currentPromotionPatterns in PROMOTION_PRIORITY_PATTERNS:
            # Look for specific patterns for each of the promotion
            # types we are interested in.
            for currentPattern in sorted(currentPromotionPatterns,
                                         key=len, reverse=True):

                replacePattern = currentPromotionPatterns[currentPattern]
                patternCleanse = re.compile(currentPattern, re.IGNORECASE)
                matchCleanse = patternCleanse.findall(priceForPromotion)

                if len(matchCleanse) >= 1:
                    # DEBUG.
                    # print "PromoType Cleanse: Pattern MATCH: " + str(currentPattern)
                    self.mPromotionType = replacePattern
                    break
            else:
                continue

            # Exit outer loop because inner loop found match.
            break


    #
    # Perform a data clean of the Title.
    #
    def cleanseTitle(self, join=True):

        # Update the default value if we found a title.
        if self.mTitle: 
            self.mTitleCleansed = self.mTitle

        # Initialise the title by joining the title and description.
        if join:
            # Only append the description if it exists.
            if self.mDescription:
                self.mTitleCleansed += " " + self.mDescription

        # Deal with raw strings, ugh.
        self.mTitleCleansed = self.mTitleCleansed.decode('string-escape')

        # Remove the dirty tabs and new lines.
        dirtyNewLine = re.compile('\n+', re.IGNORECASE)
        self.mTitleCleansed = dirtyNewLine.sub(' ',  self.mTitleCleansed)
        dirtyTab = re.compile('\t+', re.IGNORECASE)
        self.mTitleCleansed = dirtyTab.sub(' ',  self.mTitleCleansed)
        # Deal with very special characters and replace with something within
        # normal range of the character set.
        dirtyHyphen = re.compile('\–', re.IGNORECASE)
        self.mTitleCleansed = dirtyHyphen.sub('\-',  self.mTitleCleansed)
        dirtyCharacter_a = re.compile('\ä', re.IGNORECASE)
        self.mTitleCleansed = dirtyCharacter_a.sub('a',  self.mTitleCleansed)
        dirtyCharacter_e = re.compile('\é', re.IGNORECASE)
        self.mTitleCleansed = dirtyCharacter_e.sub('e',  self.mTitleCleansed)
        dirtyCharacter_e = re.compile('\”', re.IGNORECASE)
        self.mTitleCleansed = dirtyCharacter_e.sub('"',  self.mTitleCleansed)
        dirtyCharacter_u = re.compile('\ú', re.IGNORECASE)
        self.mTitleCleansed = dirtyCharacter_u.sub('u',  self.mTitleCleansed)
        dirtyCharacter_o = re.compile('\Ô', re.IGNORECASE)
        self.mTitleCleansed = dirtyCharacter_o.sub('o',  self.mTitleCleansed)

        # Remove the dirty symbols.
        for currentPattern in sorted(DIRTY_SYMBOLS_PATTERNS,
                                     key=len, reverse=True):

            replacePattern = DIRTY_SYMBOLS_PATTERNS[currentPattern]
            patternCleanse = re.compile(currentPattern, re.IGNORECASE)
            # Replace the successful pattern match.
            self.mTitleCleansed = patternCleanse.sub(replacePattern, self.mTitleCleansed)

        # Remove the dirty words.
        for currentPattern in sorted(DIRTY_WORD_PATTERNS,
                                     key=len, reverse=True):

            replacePattern = DIRTY_WORD_PATTERNS[currentPattern]
            patternCleanse = re.compile(currentPattern, re.IGNORECASE)
            # Replace the successful pattern match.
            self.mTitleCleansed = patternCleanse.sub(replacePattern, self.mTitleCleansed)

        # Remove the dirty extra white space.
        dirtyExtraWhitespace = re.compile('\s+', re.IGNORECASE)
        self.mTitleCleansed = dirtyExtraWhitespace.sub(' ',  self.mTitleCleansed)

        # Capitalise each word.
        self.mTitleCleansed = self.mTitleCleansed.title()

        # All units in lowercase.
        for currentPattern in sorted(DIRTY_ABBREVIATIONS_PATTERNS,
                                     key=len, reverse=True):

            replacePattern = DIRTY_ABBREVIATIONS_PATTERNS[currentPattern]
            patternCleanse = re.compile(currentPattern, re.IGNORECASE)
            # Replace the successful pattern match.
            self.mTitleCleansed = patternCleanse.sub(replacePattern, self.mTitleCleansed)
            

    #
    # Multiple raw date formats need to be converted to
    # Australian format of dd/mm/yyyy.
    #
    def cleanDate(self, rawDate):

        # Return the original date, until we know otherwise.
        cleanedDate = rawDate

        # Set to true if we are able to process date format.
        cleanDone = False

        # Heading of CSV file.
        if((rawDate.lower() == "valid start date") or
           (rawDate.lower() == "valid end date")):
            cleanDone = True

        if not rawDate:
            cleanDone = True

        # Example: 01/01/2001
        #          dd/mm/yyyy
        matches = re.findall(r"^(\d\d?)\/(\d\d?)\/(\d\d\d\d)$", rawDate)
        if len(matches) == 1:
            # Nothing to do already in correct format!
            cleanDone = True


        # Example: 01/01/01
        #          dd/mm/yy
        matches = re.findall(r"^(\d\d)\/(\d\d)\/(\d\d)$", rawDate)
        if len(matches) == 1:
            cleanDone = True
            day = str(matches[0][0])
            month = str(matches[0][1])
            year = '20' + str(matches[0][2])
            cleanedDate = '%s/%s/%s' % (day, month, year)

        # Example: 2017-08-25
        #          yyyy-mm-dd
        matches = re.findall(r"^(\d\d\d\d)\-(\d\d?)\-(\d\d?)$", rawDate)
        if len(matches) == 1:
            cleanDone = True
            year = str(matches[0][0])
            month = str(matches[0][1])
            day = str(matches[0][2])
            cleanedDate = '%s/%s/%s' % (day, month, year)
        
        # Example: 2017-09-16T00:00:00-05:00
        #          yyyy-mm-dd
        matches = re.findall(r"^(\d\d\d\d)\-(\d\d?)\-(\d\d?)T", rawDate)
        if len(matches) == 1:
            cleanDone = True
            year = str(matches[0][0])
            month = str(matches[0][1])
            day = str(matches[0][2])
            cleanedDate = '%s/%s/%s' % (day, month, year)
        
        if not cleanDone:
            print "Warning: Unable to clean date (" + str(rawDate) + ")"

        return cleanedDate

    #
    # Clean up the date format to be consistent for both the
    # Start and end dates of the store item.
    #
    def cleanseDates(self):

        self.mStartDate = self.cleanDate(self.mStartDate)
        self.mEndDate = self.cleanDate(self.mEndDate)


    #
    # Update the Type of store item.
    #
    def updateType(self):

        # No raw price was able to be scraped.
        # Must be information about the store.
        if not self.mPrice:
            self.mType = INFORMATION
            self.mPromotionType = ""
        else:
            self.mType = PRODUCT
            self.mPromotionType = PRICE_REDUCTION

    #
    # Perform the data cleanse on the dirty data.
    #
    def cleanse(self, join=True):

        # Update the type of this item.
        self.updateType()

        # Clean the price data.
        self.cleansePrice()

        # Clean the multibuy data.
        self.cleanseMultibuy()

        # Clean the promotion type data.
        self.cleansePromotionType()

        # Clean the title data.
        self.cleanseTitle(join)

        # Clean the start and end dates.
        # Australian date format of DD/MM/YYYY.
        self.cleanseDates()


    #
    # Helpful for debugging purposes.
    #
    def debug(self): # pragma: no cover
        print "---"
        print "Title: " + str(self.mTitle) + " Cleansed: " + str(self.mTitleCleansed)
        print "Description: " + str(self.mDescription)
        print "Price: " + str(self.mPrice) + " Cleansed: " + str(self.mPriceCleansed)
        print "Multibuy: " + str(self.mMultibuy)
        print "Promotion: " + str(self.mPromotionType)
        print "Category: " + str(self.mCategory)
        print "Type: " + str(self.mType)
        print "Start Date: " + str(self.mStartDate)
        print "End Date: " + str(self.mEndDate)
        print "Large Image URL: " + str(self.mLargeImageUrl)
        print "XLarge Image URL: " + str(self.mXLargeImageUrl)
        print "Details URL: " + str(self.mUrl)
        print "Data ID: " + str(self.mDataId)
        print "Flyer ID: " + str(self.mFlyerId)
        print "Flyer Item ID: " + str(self.mFlyerItemId)
        print "Top: " + str(self.mTop)
        print "Bottom: " + str(self.mBottom)
        print "Left: " + str(self.mLeft)
        print "Right: " + str(self.mRight)
