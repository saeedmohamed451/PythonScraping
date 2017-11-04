#!/usr/bin/python

import argparse

from AzureServices import *

#
# Remove a Blob from the Azure container.
#


parser = argparse.ArgumentParser(description='Remove Blob.')
parser.add_argument('blobName', metavar='blob', type=str, nargs=1,
                    help='Remove blob from Azure container.')
    
# Parse the input arguments.
args = parser.parse_args()

BLOB_NAME=args.blobName[0]

# Create an Azure service.
service = createAzureService()

# Read BEFORE write any blobs.
#summaryAzure(service)

# Check with human if okay to proceed?
message = "Is it okay to continue with delete ("
message += str(BLOB_NAME)
message += ") on Azure?"

#if queryYesNo(message):
# Delete blob.
if isContainerInService(service, CONTAINER_NAME["name"]):
    deleteBlobInAzure(service, CONTAINER_NAME["name"], BLOB_NAME)

#else:
#    print "Error: Delete Aborted by user"

# Read AFTER removed all blobs.
#summaryAzure(service)
