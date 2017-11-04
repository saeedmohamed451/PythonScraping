#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: Temporary code to be moved to web services.
import requests

# Work with strings.
from StringIO import StringIO

# Need regular expressions for pattern matching.
import re

# Interact with directories.
import os

# To create PDF documents.
from reportlab.pdfgen import canvas

# To create an image from a URL.
from reportlab.lib.utils import ImageReader
 
# Allow us to have exactly A4 sized PDF documents.
from reportlab.lib.pagesizes import A4
 
# Allow us to use inches.
from reportlab.lib.units import inch

# Chop two page spread into separate pages.
from pyPdf import PdfFileWriter, PdfFileReader

# Write our results to a CSV file.
import csv

# Write our results to an Excel spreadsheet.
import xlwt

# Catalog of Weekly Advertising.
from Catalog import Catalog

# Parsing strings and data structures.
from DocumentParsers import *

# Work with dates.
import datetime

# Work with directories and files.
from pathlib import Path

import subprocess

# Config Data for Spreadsheets.

# Don't let filenames get too long.
MAX_FILENAME_LENGTH = 50

# Needed to set the width of the spreedsheet columns.
POINTS_PER_CHAR_WIDTH = 256
POINTS_PER_CHAR_HEIGHT = 20

# A4 is 8.27 x 11.69 inches.
A4_WIDTH=8.27*inch
A4_HEIGHT=11.69*inch

# Create a style for the header items.
FONT_NAME = "Calibri"
FONT_SIZE = 11
HEADER_FONT_BOLD = "on"
HEADER_FONT_COLOR = "white"
HEADER_FONT = " font: name " + FONT_NAME + \
              ",      color " + HEADER_FONT_COLOR + \
              ",      bold " + HEADER_FONT_BOLD + \
              ",      height " + str(FONT_SIZE*POINTS_PER_CHAR_HEIGHT) + \
            "; "
HEADER_PATTERN = " pattern: pattern solid, fore_colour custom_grey;"
HEADER_ALIGN = " align: horiz center, vert center;"

BODY_FONT = " font: name " + FONT_NAME + \
            ",    height " + str(FONT_SIZE*POINTS_PER_CHAR_HEIGHT) + \
            "; align: vert center;"

BODY_FONT_CENTER = " font: name " + FONT_NAME + \
                   ",      height " + str(FONT_SIZE*POINTS_PER_CHAR_HEIGHT) + \
                   "; align: horiz center, vert center;"


# Titles of each spreadsheet/CSV and its column number.
TITLES = {
    "Complete Description": {"ColumnNum": 0,
                             "ColumnMaxWidth": 0,
                             "ColumnAlign": "left"},
    "Catalog Page": {"ColumnNum": 1,
                     "ColumnMaxWidth": 0},
    "Promotion Type": {"ColumnNum": 2,
                       "ColumnMaxWidth": 0},
    "Multibuy Qty": {"ColumnNum": 3,
                     "ColumnMaxWidth": 0},
    "Price": {"ColumnNum": 4,
              "ColumnMaxWidth": 0},
    "Department/Category": {"ColumnNum": 5,
                            "ColumnMaxWidth": 0},
    "Valid Start Date": {"ColumnNum": 6,
                         "ColumnMaxWidth": 0},
    "Item Type": {"ColumnNum": 7,
                        "ColumnMaxWidth": 0},
    "Description": {"ColumnNum": 8,
                    "ColumnMaxWidth": 0,
                    "ColumnAlign": "left"},
    "Details": {"ColumnNum": 9,
                "ColumnMaxWidth": 0},
    "Valid End Date": {"ColumnNum": 10,
                       "ColumnMaxWidth": 0},
    "Price Raw": {"ColumnNum": 11,
                  "ColumnMaxWidth": 0},
}


#
# Write the content to the given file path.
#
def writeContentToFile(content, filepath):

    # TODO: Abort if file already exists?
    try:
        with open(filepath, "wb") as outfile:
            outfile.write(content)
            outfile.close()
    except IOError:
        errMsg = "Unable to write to ("
        errMsg += filepath + ")"
        raise ValueError(errMsg)


#
# Write cell data to the active row in the given sheet.
#
def writeDataToSheet(currentSheet, activeRow, titlesObj, cellData, cellStyle):

    # Write to the selected style.
    currentSheet.write(activeRow, titlesObj["ColumnNum"], cellData, cellStyle)

    # Update the maximum width of this column if needed.
    titlesObj["ColumnMaxWidth"] = max(titlesObj["ColumnMaxWidth"], len(str(cellData)))

    return


#
# Create the path to the file to follow the naming convention
#  <output dir>/<Retailer name>-<location>_<YYYY_MM_DD>
#
def createPathToFile(outputDir, retailerName, storeLocation, catalogDate):

    # Path to file following the naming convention.
    pathToFile = str(outputDir) 
    pathToFile += str(retailerName) + "-"
    pathToFile += storeLocation + "_"
    pathToFile += catalogDate

    # Clear the whitespace.
    pathToFile = pathToFile.replace(" ", "")

    return pathToFile

#
# Check to see if this file already exists, create a new file
# name if it does.
# Example:
#  When the file Aldi_NY_2020_01_01.xls exists,
#  next valid name: Aldi_NY_2020_01_01-1.xls
#  next valid name: Aldi_NY_2020_01_01-2.xls    
#
def createFileName(pathToFile, extension):

    uniquePathToFile = pathToFile + extension

    uniqueId = None

    while Path(uniquePathToFile).is_file():
        if uniqueId is None:
            uniqueId = 1
        else:
            uniqueId += 1    

        uniquePathToFile = pathToFile + "-" + str(uniqueId) + extension
        
        
    return uniquePathToFile, uniqueId


#
# Use the output directory to check if it exists and create
# it if needed. Then create a subdirectory to place the
# scape results into, if needed.
# Returns: Path the the sub-directory.
#
def createOutputDir(outputDir, subDirs = []):


    # Get a current time stamp so that we can use this
    # to keep track of when events occurred.
    now = datetime.datetime.now()

    timeStamp = now.strftime("%Y_%b_%d/")

    # Directory paths that need to be created.
    # Originally wanted:
    # ./output/2017_Sep_15/CVS/
    # dirPaths = ["", timeStamp]
    # Now we want:
    # ./output/CVS/
    dirPaths = [""]

    # Make sure we have a slash on the end of each directory.
    for currentSubDir in subDirs:
        # Check the last character in the string.
        if currentSubDir[-1] == "/":
            dirPaths.append(currentSubDir)
        else:
            dirPaths.append(currentSubDir + "/")

    # Create each of the dir paths.
    for currentDirPath in dirPaths:

        outputDir += currentDirPath
        
        # Verify the output directory.
        try:
            # Check if the output directory already exists.
            os.stat(outputDir)
        except:
            # Create an output directory.
            os.mkdir(outputDir)  

    return outputDir



#
# Write the catalogs results in CSV format.
#
def writeCatalogsToCsv(grouping, webSiteName, catalogs, outputDir):

    # Each location is a new sheet in the overall spreadsheet.
    for currentCatalogName, currentCatalog in catalogs.iteritems():

        # Extract the details of interest to use for the file path and name.
        storeLocation = currentCatalogName.split("-")[1]
        catalogDate = currentCatalog.mValidFrom

        # Create the output dir so it has a scrape directory.
        currentOutputDir = createOutputDir(outputDir, 
                                           ["CSV",
                                            webSiteName + "-" + storeLocation])

        # Create the path to the file.
        pathToFile = createPathToFile(currentOutputDir, webSiteName,
                                      storeLocation, catalogDate)

        # Must create a new name if the file already exists.
        CSV_NAME, uniqueId = createFileName(pathToFile, ".csv")

        with open(CSV_NAME, 'wb') as csvfile:
            csvWriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)

            SORTED_TITLES = []
            # Sort the title to the CSV file but their specified column number(s).
            for currentTitle in sorted(TITLES.items(), key=lambda x: x[1]["ColumnNum"]):
                SORTED_TITLES.append(str(currentTitle[0]).replace(",",""))
                
            csvWriter.writerow(SORTED_TITLES)
            
            # Now loop through the catalog and output each store item
            # on a new line.
            for currentPage, currentItems in sorted(currentCatalog.mPages.iteritems()):
                for currentItem in currentItems:

                    # New row to add to the CSV file.
                    currentRow = []

                    # Populate the CSV file before it is written.
                    currentRow.append(cleanStringForCsv(currentItem.mTitleCleansed))
                    currentRow.append(cleanStringForCsv(currentPage))
                    currentRow.append(cleanStringForCsv(currentItem.mPromotionType))
                    currentRow.append(cleanStringForCsv(currentItem.mMultibuy))
                    # if currentItem.mPromotionType == 0:
                    #     currentRow.append(cleanStringForCsv("XXXX"))
                    # else:
                    currentRow.append(cleanStringForCsv(currentItem.mPriceCleansed))
                    currentRow.append(cleanStringForCsv(currentItem.mCategory))
                    currentRow.append(cleanStringForCsv(currentItem.mStartDate))
                    currentRow.append(cleanStringForCsv(currentItem.mType))
                    currentRow.append(cleanStringForCsv(currentItem.mTitle))
                    currentRow.append(cleanStringForCsv(currentItem.mDescription))
                    currentRow.append(cleanStringForCsv(currentItem.mEndDate))
                    currentRow.append(cleanStringForCsv(currentItem.mPrice))
                    # Only write the row if there is a valid title.
                    if currentItem.mTitleCleansed:
                        csvWriter.writerow(currentRow)

    return


#
# Write the catalogs to the spreadsheet.
# Each sheet in the spread sheet corresponds
# to a location's catalog.
# eg The catalog for Dallas, Texas is one of
#    the sheet within the overall spreadsheet.
#
def writeCatalogsToSpreadsheet(grouping, webSiteName, catalogs, outputDir):

    # Each location is a new sheet in the overall spreadsheet.
    for currentCatalogName, currentCatalog in catalogs.iteritems():

        # Extract the details of interest to use for the file path and name.
        storeLocation = currentCatalogName.split("-")[1]
        catalogDate = currentCatalog.mValidFrom

        # Create the output dir so it has a scrape directory.
        currentOutputDir = createOutputDir(outputDir, 
                                           ["XLSX",
                                            webSiteName + "-" + storeLocation,])

        # Create the path to the file.
        pathToFile = createPathToFile(currentOutputDir, webSiteName,
                                      storeLocation, catalogDate)

        # Must create a new name if the file already exists.
        SPREAD_SHEET_NAME, uniqueId = createFileName(pathToFile, ".xls")

        # Store the unique ID so that we can place all the images for this
        # catalog into same directory.
        currentCatalog.mUniqueId = uniqueId

        # Create a new work book.
        book = xlwt.Workbook(encoding="utf8")

        # Might be nice to create a nice colour.
        xlwt.add_palette_colour("custom_grey", 0x21)
        book.set_colour_RGB(0x21, 128, 128, 128)

        # Styles to be used in spreadsheet.
        headerStyle = xlwt.easyxf(HEADER_FONT + \
                                  HEADER_PATTERN + \
                                  HEADER_ALIGN)
        bodyStyle = xlwt.easyxf(BODY_FONT)
        bodyStyleCenter = xlwt.easyxf(BODY_FONT_CENTER)

        # Spreadsheet has a limit of 31 characters for a sheet's name.
        currentSheetName = currentCatalogName.split("-")[0] + currentCatalogName.split("-")[1]
        currentSheet = book.add_sheet(currentSheetName[:31])

        # Keep track of the current active row in the spreadsheet.
        activeRow = 0

        # Write out the Title information.
        for titleName, titleDetails in TITLES.iteritems():
            # Populate the title text.
            currentSheet.write(activeRow, titleDetails["ColumnNum"], titleName.upper(), headerStyle)

            # Set the header to be a little wider 25% than just the title.
            titleDetails["ColumnMaxWidth"] = int(len(titleName) * 1.25)

            # Set the title row height. (Magic 2 for a fuller effect)
            currentSheet.row(activeRow).height = POINTS_PER_CHAR_HEIGHT * FONT_SIZE * 2

        # Write out the catalog items for each page in the catalog.
        for currentPage, currentItems in sorted(currentCatalog.mPages.iteritems()):
            # Sort items from left most pixel postion to right most pixel position. 
            # If two store times at the same left pixel position then sort from
            # top most pixel postion to bottom most pixel position.
            for currentItem in sorted(currentItems, key = lambda x: (-x.mTop, x.mLeft)):
            
                # Only write the row if there is a valid title.
                if not currentItem.mTitleCleansed:
                    continue

                # Price of current item.
                itemPrice = 0

                # Bump the current active row just before we write.
                activeRow += 1

                # Set the height of the row.
                currentSheet.row(activeRow).height = int(POINTS_PER_CHAR_HEIGHT * FONT_SIZE * 1.5)


                # Write data for the current data item to the current spreadsheet page.
                # Customer wanted to call the JSON title as the description, so renamed it here.
                writeDataToSheet(currentSheet, activeRow, 
                                 TITLES["Complete Description"], currentItem.mTitleCleansed, bodyStyle)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Catalog Page"], currentPage, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Promotion Type"], currentItem.mPromotionType, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Multibuy Qty"], currentItem.mMultibuy, bodyStyleCenter)
                #                if currentItem.mPromotionType == 0:
                #                    writeDataToSheet(currentSheet, activeRow,
                #                                     TITLES["Price"], "XXXX", bodyStyle)
                #                else:
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Price"], currentItem.mPriceCleansed, bodyStyle)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Department/Category"], currentItem.mCategory, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Valid Start Date"], currentItem.mStartDate, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Item Type"], currentItem.mType, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow, 
                                 TITLES["Description"], currentItem.mTitle, bodyStyle)
                # Customer wanted to calle the JSON description as the details, so renamed it here.
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Details"], currentItem.mDescription, bodyStyle)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Valid End Date"], currentItem.mEndDate, bodyStyleCenter)
                writeDataToSheet(currentSheet, activeRow,
                                 TITLES["Price Raw"], currentItem.mPrice, bodyStyle)

        # Update the width of the columns.
        for titleName, titleDetails in TITLES.iteritems():
            # Don't let the columns get too wide, as it does not look very nice.
            COL_WIDTH = 50
            if TITLES[titleName]["ColumnMaxWidth"] < COL_WIDTH:
                currentSheet.col(TITLES[titleName]["ColumnNum"]).width = 256 * TITLES[titleName]["ColumnMaxWidth"]
            else:
                currentSheet.col(TITLES[titleName]["ColumnNum"]).width = 256 * COL_WIDTH

        # Save out workbook to disk.
        book.save(SPREAD_SHEET_NAME)


    return

#
# For each of the store items in a catalog, write these to disk.
#
def writeCatalogsImagesToDisk(grouping, webSiteName, catalogs, outputDir):

    for currentCatalogName, currentCatalog in catalogs.iteritems():

        # Extract the details of interest to use for the file path and name.
        storeLocation = currentCatalogName.split("-")[1]
        catalogDate = currentCatalog.mValidFrom
        catalogUniqueId = currentCatalog.mUniqueId
        imageDirectoryName = webSiteName + "-" + storeLocation + "_" + catalogDate

        # Match the directory of images to the same name as the spreadsheet.
        if catalogUniqueId is not None:
            imageDirectoryName += "-" + str(catalogUniqueId)

        # Create the output dir so it has a scrape directory.
        currentOutputDir = createOutputDir(outputDir, 
                                           ["IMAGES",
                                            imageDirectoryName])

        # Write out the catalog items for each page in the catalog.
        for currentPage, currentItems in sorted(currentCatalog.mPages.iteritems()):
            for currentItem in currentItems:

                # Only create image filename if we need one.
                if currentItem.mLargeImageUrl or currentItem.mXLargeImageUrl:

                    # Cannot continue if there is not name for the images.
                    if not currentItem.mTitleCleansed:
                        errMsg = "Error: Unable to get image name for ("
                        if currentItem.mLargeImageUrl:
                            errMsg += str(currentItem.mLargeImageUrl)
                        elif currentItem.mXLargeImageUrl:
                            errMsg += str(currentItem.mXLargeImageUrl)
                        errMsg +=")"
                        print errMsg
                        continue

                    # Ignore all the characters that are not ascii.
                    # Need to create a filename without special characters in it.
                    titleShort = "".join(i for i in currentItem.mTitleCleansed if ord(i)<128)
                
                    # Strip out all white spaces, tabs and new lines.
                    titleShort = "".join(titleShort.split())

                    # Remove all commas and dots and special symbols.
                    titleShort = re.sub(r'[\W+/g]', '', titleShort)

                    # Now prepend the path to the file.
                    filename = currentOutputDir + titleShort[:MAX_FILENAME_LENGTH]

                    if currentItem.mLargeImageUrl:
                        largeImageFilename, uniqueId = createFileName(filename, ".jpg")
                        writeContentToFile(currentItem.mLargeImageContent,
                                           largeImageFilename)

                    if currentItem.mXLargeImageUrl:
                        xLargeImageFilename, uniqueId = createFileName(filename, ".jpg")
                        writeContentToFile(currentItem.mXLargeImageContent,
                                           xLargeImageFilename)


    return


#
def movePdf(pdfSource, pdfDest):

    os.rename(pdfSource, pdfDest)


#
# Spit double spread pages into multiple pages.
# Expect pages to be the size of pageWidth.
#
def chopPdf(inputPdf, outputPdf, pageWidth, checkFirstPage=True):

    # Now lets read the cropped image into memory and have a look at its dimensions.
    # Two pass read because can't perform a deep copy on internal objects.
    origInputPdfFirstPass = PdfFileReader(file(inputPdf, "rb"))
    origInputPdfSecondPass = PdfFileReader(file(inputPdf, "rb"))
    chopPdfOutput = PdfFileWriter()

    # Need total number of pages so can deal with one page at a time.
    numPages = origInputPdfFirstPass.getNumPages()

    # Assume this is not the correct catalog until we know otherwise.
    foundCorrectCatalog = False
    
    # Dont need to check the first page for one page catalogs for a 5-day sale, say.
    if not checkFirstPage:
        foundCorrectCatalog = True

    # Consider each page, chop it up if it is a two page spread.
    for currentPageNumber in range(numPages):
        # DEBUG:
        # print "currentPage: " + str(currentPageNumber)

        currentPage = origInputPdfFirstPass.getPage(currentPageNumber)

        currentWidth = currentPage.mediaBox.getUpperRight_x()
        currentHeight =currentPage.mediaBox.getUpperRight_y()
        # DEBUG:
        # print "Width: " + str(currentWidth)
        # print "Height: " + str(currentHeight)

        # The front page of the catalog must be within buffer mm
        # of the expected page width.
        BUFFER_MM = 50.0
        if(checkFirstPage and 
           ((currentPageNumber == 0) and 
            (currentWidth > (pageWidth - BUFFER_MM)) and 
            (currentWidth < (pageWidth + BUFFER_MM)))):

            foundCorrectCatalog = True

        # Need to split page up when we have a 2 page spread.
        # Assume two page spread once gone over 50 of next A4 page.
        if((foundCorrectCatalog == True) and 
           (currentWidth > (pageWidth * 1.5))):

            # Need to chop this page into two.
            currentPageLeft = currentPage
            currentPageRight = origInputPdfSecondPass.getPage(currentPageNumber)

            currentPageLeft.cropBox.lowerLeft = (0, 0)
            currentPageLeft.cropBox.upperRight = (pageWidth, currentHeight)
            chopPdfOutput.addPage(currentPageLeft)
            currentPageRight.cropBox.lowerLeft = (pageWidth, 0)
            currentPageRight.cropBox.upperRight = (currentWidth, currentHeight)
            chopPdfOutput.addPage(currentPageRight)

        else:
            # Normal scenario where page is no wider than a normal A4 page.
            chopPdfOutput.addPage(currentPage)

    # Create a stream handle to write out the results.
    outputStream = file(outputPdf, "wb")
    # Dump the chopped PDF results to disk.
    chopPdfOutput.write(outputStream)
    # Close the stream handle.
    outputStream.close()

    return foundCorrectCatalog



#
# Write the catalog's PDF data to file and crop any white space. 
#
def writeCatalogsToPdf(grouping, webSiteName, catalogs, outputDir):

    # Write the PDF and the cropped PDF to disk.
    for currentCatalogName, currentCatalog in catalogs.iteritems():
        
        # No PDF url found for this catalog.
        # No images found for each page of this catalog.
        if (not currentCatalog.mPdfUrl) and (len(currentCatalog.mPdfImageContent) == 0):
            continue

        # Extract the details of interest to use for the file path and name.
        storeLocation = currentCatalogName.split("-")[1]
        catalogDate = currentCatalog.mValidFrom

        # Create the output dir so it has a scrape directory.
        currentOutputDir = createOutputDir(outputDir, 
                                           ["PDF",
                                            webSiteName + "-" + storeLocation])

        currentOutputDirCropped = createOutputDir(outputDir, 
                                                  ["PDF_FINAL",
                                                   webSiteName + "-" + storeLocation])

        currentOutputDirChopped = createOutputDir(outputDir, 
                                                  ["PDF_CHOPPED",
                                                   webSiteName + "-" + storeLocation])

        # Create the path to the file.
        pathToFile = createPathToFile(currentOutputDir, webSiteName,
                                      storeLocation, catalogDate)
        pathToFileCropped = createPathToFile(currentOutputDirCropped, webSiteName,
                                             storeLocation, catalogDate)
        pathToFileChopped = createPathToFile(currentOutputDirChopped, webSiteName,
                                             storeLocation, catalogDate)
        
        # Now prepend the path to the file.
        # Must create a new name if the file already exists.
        pdfFilename, uniqueId = createFileName(pathToFile, ".pdf")
        pdfCroppedFilename, uniqueId = createFileName(pathToFileCropped, ".pdf")
        pdfChoppedFilename, uniqueId = createFileName(pathToFileChopped, ".pdf")

        # We have a PDF URL for this Catalog.
        if currentCatalog.mPdfUrl:

            # Write the PDF to save the content.
            writeContentToFile(currentCatalog.mPdfContent, pdfFilename)

        # We have muliple images for each page of this Catalog.
        elif len(currentCatalog.mPdfImageContent) > 0:

            # Create a PDF document canvas.
            c = canvas.Canvas(pdfFilename,
                              pagesize= A4)

            c.setTitle(webSiteName + "-" + storeLocation)
 
            # Move the origin to bottom left hand side.
            c.translate(0,0)
 
            # Write each image onto a new page in the PDF.
            for currentImage in currentCatalog.mPdfImageContent:

                # Write the image of the current page to the PDF.
                origW, origH = c.drawImage(ImageReader(StringIO(currentImage)),
                                           0, 0,
                                           width=A4_WIDTH,
                                           height=A4_HEIGHT,
                                           preserveAspectRatio=True,
                                           anchor='s')


                # Create a new page.
                c.showPage()

            # Save the result.
            c.save()


        # Crop the PDF to remove white-space.
        cmd = "pdf-crop-margins "
        # Use Ghostview to calculate the bounding box.
        cmd += "-gs  "
        # Keep borders to 0 pixels.
        cmd += "-p 0  "
        # Input filename.
        cmd += pdfFilename + "  "
        # Output filename.
        cmd += "-o  " + pdfCroppedFilename

        # Send command to shell.
        try:
            result = subprocess.check_output(cmd, shell=True)
        except:
            errMsg = "Error: Unable to run command (" 
            errMsg += cmd +")"
            print errMsg

        # Now need to deal with two page spreads after have cropped the margins.
        if(webSiteName.lower() == "kroger"):
            KROGER_PAGE_WIDTH = 974.99816
            # Only perform the chop operation for the given retailers.
            chopPdf(pdfCroppedFilename, pdfChoppedFilename, KROGER_PAGE_WIDTH)
            movePdf(pdfChoppedFilename, pdfCroppedFilename)
        elif(webSiteName.lower() == "aldi"):
            ALDI_PAGE_WIDTH = [
                # Aldi Insider Catalog.
                1514.38059,
                # Alid Weekly Ad.
                1746.99944]
            # Only perform the chop operation for the given retailers.
            for currentPageWidth in ALDI_PAGE_WIDTH:
                # Stop when we have found the correct catlog to chop.
                if chopPdf(pdfCroppedFilename, pdfChoppedFilename, currentPageWidth):
                    break
            movePdf(pdfChoppedFilename, pdfCroppedFilename)
        elif(webSiteName.lower() == "familydollar"):
            FAMILY_DOLLAR_PAGE_WIDTH = 1283.5201
            # Deal with 5-day sale where first page needs to be chopped.
            chopPdf(pdfCroppedFilename, pdfChoppedFilename, FAMILY_DOLLAR_PAGE_WIDTH, False)
            movePdf(pdfChoppedFilename, pdfCroppedFilename)

    return


#
#
#
def writeCatalogs(grouping, retailer, catalogs, outputDir):

    if len(catalogs) == 0:
        # No point trying to generate a spreadsheet or PDF.
        print("Error: no weekly advertisement data found from (" + \
              str(retailer) + ")")
        return
        
    print("  -> Write Catalogs to XLSX")
    writeCatalogsToSpreadsheet(grouping, retailer, catalogs, outputDir)

    print("  -> Write Catalogs to CSV")
    writeCatalogsToCsv(grouping, retailer, catalogs, outputDir)

    print("  -> Write Catalogs to PDF")
    writeCatalogsToPdf(grouping, retailer, catalogs, outputDir)

    print("  -> Write Catalogs Images to Disk")
    writeCatalogsImagesToDisk(grouping,
                                               retailer,
                                               catalogs,
                                               outputDir)
