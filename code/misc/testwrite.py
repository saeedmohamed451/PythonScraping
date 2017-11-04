#!/usr/bin/python

# Catalog of Weekly Advertising.
from Catalog import Catalog

# Services to work with documents.
import DocumentServices

grouping = "testgrouping"
retailer = "testretailer"
catalog = Catalog("testLocation", "testWeb")
catalog.mValidFrom = "2017_01_01"
catalogs = {"testStore-testLocation-externalName-2017_01_01": catalog}

outputDir = "./testoutput/"
print("  -> Write Catalogs to XLSX")
DocumentServices.writeCatalogsToSpreadsheet(grouping,
                                            retailer,
                                            catalogs,
                                            outputDir)
print("  -> Write Catalogs to CSV")
DocumentServices.writeCatalogsToCsv(grouping,
                                    retailer,
                                    catalogs,
                                    outputDir)

print("  -> Write Catalogs to PDF")
DocumentServices.writeCatalogsToPdf(grouping,
                                    retailer,
                                    catalogs,
                                    outputDir)




print("  -> Write Catalogs Images to Disk")
DocumentServices.writeCatalogsImagesToDisk(grouping,
                                           retailer,
                                           catalogs,
                                           outputDir)
