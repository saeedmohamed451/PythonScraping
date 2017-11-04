#!/usr/bin/python

from AzureServices import *


#
# Download the file into the given directory from Azure.
#

# So can parse input arguments.
import sys

# So can work with local files and directories.
import os

# How to use this script.
USAGE = "python downloadBlob.py <blob filename> <download directory>"

# Verify the input arguments.
if len(sys.argv) != 3:
    print "Error: Missing aruments"
    print USAGE
    exit(1)

BLOB_NAME = sys.argv[1]

# Name of directory that would like to upload.
LOCAL_DIRECTORY = sys.argv[2]

# Verify the local directory exists.
if not os.path.isdir(LOCAL_DIRECTORY):
    print "Error: Directory not found (" + LOCAL_DIRECTORY + ")"
    print USAGE
    exit(1)

# Create an Azure service.
service = createAzureService()

# Read BEFORE write any blobs.
#summaryAzure(service)

# Upload files to the container.
if isContainerInService(service, CONTAINER_NAME):
    downloadFileFromAzure(service, CONTAINER_NAME,
                          LOCAL_DIRECTORY + BLOB_NAME,
                          BLOB_NAME)

# Read AFTER write any blobs.
#summaryAzure(service)

