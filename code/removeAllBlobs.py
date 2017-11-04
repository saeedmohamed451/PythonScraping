#!/usr/bin/python

from AzureServices import *

#
# Remove all Blobs from the Azure container.
#

# Create an Azure service.
service = createAzureService()

# Read BEFORE write any blobs.
summaryAzure(service)

# Check with human if okay to proceed?
if queryYesNo("Is it okay to continue with delete on Azure?"):
    # Delete all blobs.
    if isContainerInService(service, CONTAINER_NAME):
        deleteAllBlobsInAzure(service, CONTAINER_NAME)

else:
    print "Error: Delete Aborted by user"

# Read AFTER removed all blobs.
summaryAzure(service)
