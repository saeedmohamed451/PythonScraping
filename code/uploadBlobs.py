#!/usr/bin/python

from AzureServices import *


#
# Upload the files in the given directory to Azure.
# If the files already exist DO NOT over write them.
#

# So can parse input arguments.
import sys

# So can work with local files and directories.
import os

# How to use this script.
USAGE = "python uploadBlobs.py <upload directory>"

# Verify the input arguments.
if len(sys.argv) != 2:
    print "Error: Missing aruments"
    print USAGE
    exit(1)

# Name of directory that would like to upload.
LOCAL_DIRECTORY = sys.argv[1]

# Verify the local directory exists.
if not os.path.isdir(LOCAL_DIRECTORY):
    print "Error: Directory not found (" + LOCAL_DIRECTORY + ")"
    print USAGE
    exit(1)


# List of file that shall be uploaded to Azure.
localFiles = []

# Walk through local directory to get path to each
# of the files would like to upload.
for path, subdirs, files in walk(LOCAL_DIRECTORY):
    for name in files:
        localFiles.append(join(path, name))

# Create an Azure service.
service = createAzureService()

# Read BEFORE write any blobs.
#summaryAzure(service)

# Upload files to the container.
if isContainerInService(service, CONTAINER_NAME["name"]):
    uploadFilesToAzure(service, CONTAINER_NAME["name"],
                       LOCAL_DIRECTORY, localFiles)

# Read AFTER write any blobs.
#summaryAzure(service)

