#!/usr/bin/python

from AzureServices import *

#
# Connect to Azure and list 
# all blobs in all containers.
#

# Create an Azure service.
service = createAzureService()

# List all blobs.
summaryAzure(service)

