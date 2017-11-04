#!/usr/bin/python
# -*- coding: utf-8 -*-

# Work with dates.
import datetime

class Catalog(object):

    #
    #
    #
    def __init__(self, location, webserver):

        # Keep track of where the location of this
        # catalog was retrieved from.
        self.mLocation = location
        self.mWebserver = webserver

        # Current time that this object is created.
        now = datetime.datetime.now()
        self.mYear = now.strftime("%Y")
        self.mMonth = now.strftime("%b")
        self.mDay = now.strftime("%d")
        self.mDate = now.strftime("%Y_%b_%d")

        self.mValidFrom = ""

        # URL to find the catalog's PDF.
        self.mPdfUrl = ""

        # Content of the catalog's PDF.
        self.mPdfContent = ""

        # Content of each page of the catalog's PDF.
        self.mPdfImageContent = []

        # Each page number is its key.
        self.mPages = {}

    #
    # Add a page to the pages in the catalog and referenced
    # by the page number for ease of retrieve.
    #
    def addPage(self, pageNumber, page):
        # Use the page number as the key.
        self.mPages[pageNumber] = page
    
    #
    # Helpful for debugging purposes.
    #
    def debug(self):
        print "---"
        print "Location: " + self.mLocation
        print "Web Server: " + self.mWebserver
        print "Date: " + self.mDate
        print "Num of Pages: " + str(len(self.mPages.keys()))
        for currentPageNumber, currentPage in self.mPages.iteritems():
            print " Page-" + str(currentPageNumber) + ":"
            print currentPage
        
