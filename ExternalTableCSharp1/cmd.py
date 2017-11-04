#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

import os
import json
import sys

import datetime
print "Imported packages"
# Get the non-standard python packages from the virtual environment 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../venv/Lib/site-packages')))
print "set up path"
# Get the source code for Catalytics.
sys.path.insert(0, '../code/')
print "Import source code"
# TODO: Remove this... Beautiful Soup for processing.
from bs4 import BeautifulSoup
print "Found soup"
# TODO: Remove this... Interact with Azure storage.

# Service to Azure storage and read from containers.
#from azure.storage.blob import BlockBlobService
#print "Got storage service"
# Push into the Azure container.
#from azure.storage.blob import ContentSettings
#print "Asure settings"
# TODO: Add this later as the way run in Azure cloud is different to laptop.
#from AzureServices import *

#
#
#
def main():

    print "Entered main() for cmd.py!!"
    print str(os.getcwd())
    #
    # Connect to Azure and list 
    # all blobs in all containers.
    #
#    block_blob_service = BlockBlobService(account_name='scrapingoutput',
#                                          account_key='YZXB3G4hf2M6x8cIT8Jjsd7KYCv9eEFF0iMvLhmcBaWIr8SorIg+MQCId13KLcj5ZC7ZEDqUTZbB3wPmfwrpJA==')
#
#
#    # List all blobs.
#    generator = block_blob_service.list_blobs('retailers')
#    for blob in generator:
#        print blob.name

#    # Create an Azure service.
#    service = createAzureService()
#
#    # List all blobs.
#    summaryAzure(service)

    localFilename = 'D:/local/somefile.txt'

    # Lets write to local disk.
    with open(localFilename, 'a') as the_file:
        now = datetime.datetime.now()
        the_file.write('Able to write to this file on Azure at (' + str(now) + ').\n')

#    # Push this local file to the Azure container.
#    block_blob_service.create_blob_from_path('retailers', localFilename, localFilename)
    
#
#
#
if __name__ == '__main__':
    main()
