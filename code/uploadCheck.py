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

# Regular expressions library.
import re

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

# Details of files that shall are proposed to be uploaded to Azure.
localFiles = {}
localCsvFiles = {}

# Walk through local directory to get path to each
# of the files would like to upload.
for path, subdirs, files in walk(LOCAL_DIRECTORY):
    for name in files:

        # Relative path to the file to be uploaded including its filename.
        currentFile = join(path, name)

        # Keep the file's size, to the byte level.
        localFiles[currentFile] = {
            # Name of this local file on disk.
            "name": currentFile,
            # Size of this file.
            "size": os.path.getsize(currentFile)}

        if '/CSV/' in path:
            localCsvFiles[currentFile] = {
                # Name of this local file on disk.
                "name": currentFile,
                # Size of this file.
                "size": os.path.getsize(currentFile),
                # Upload until we know otherwise.
                "upload": True,
                # Name of the local file when push up to Azure cloud.
                # Change to the alias when this local file name 
                # already exists on the Azure cloud.
                "alias": None}


# Create an Azure service.
service = createAzureService()

# Read BEFORE write any blobs.
#summaryAzure(service)

# DEBUG.
#print "Local Files are:"
#print localFiles.keys()

# Get a full list of all CSVs in the Azure Bucket.
bucketFiles = getFileNamesAndSizes(service)
#print "What is in the cloud?"
#print bucketFiles.keys()

# Determine the current maximum Unique ID for each date that a catalog started on.
# Example: Aldi-CA_2017_01_01-3.csv would have maxId = 3.
for currentBucketFile, currentBucketObj in bucketFiles.iteritems():

    # Strip off the unique numbering as the order may have changed.
    matchId = re.findall('\-(\d+)?\.csv', currentBucketFile)
    if len(matchId) > 0:
        currentUniqueId = int(matchId[0])
        
        # Example: Aldi-CA_2017_01_01-3.csv => Aldi-CA_2017_01_01.csv
        uniqueIdSub = re.compile('(\-\d+)?', re.IGNORECASE)
        currentBucketFileBasename = uniqueIdSub.sub('', currentBucketFile)

        if bucketFiles[currentBucketFileBasename]["maxId"] is None:
            bucketFiles[currentBucketFileBasename]["maxId"] = int(currentUniqueId)
        elif currentUniqueId > bucketFiles[currentBucketFileBasename]["maxId"]:
            bucketFiles[currentBucketFileBasename]["maxId"] = currentUniqueId

# So now we need to look through each catalog item on the local disk and
# determine if they need to be uploaded or not.

# Look at the size of files in the cloud to determine if these files already exist.
for currentLocalCsvFile, currentLocalCsvFileObj in localCsvFiles.iteritems():
    
    # Strip off the prefix directory.
    # Example: directory/Aldi-CA_2017_01_01-3.csv => Aldi-CA_2017_01_01-3.csv
    currentLocalCsvFileBasename =  os.path.basename(currentLocalCsvFile)

    # Strip off the unique numbering as the order may have changed.
    # Example: Aldi-CA_2017_01_01-3.csv => Aldi-CA_2017_01_01
    uniqueId = re.compile('(\-\d+)?\.csv', re.IGNORECASE)
    currentLocalCsvFileBasename = uniqueId.sub('', currentLocalCsvFileBasename)

    # Now lets see if there are any blobs in the cloud that are the same size.
    for currentBucketFile, currentBucketObj in bucketFiles.iteritems():
        if currentLocalCsvFileBasename in currentBucketFile:
            if currentLocalCsvFileObj["size"] == currentBucketObj["size"]:

                # Do not upload this file as it is already in the cloud.
                currentLocalCsvFileObj["upload"] = False
                break

# Look at the names of the files in the cloud to determine if we need a new alias.    
for currentLocalCsvFile, currentLocalCsvObj in localCsvFiles.iteritems():
    if currentLocalCsvObj["upload"]:

        # Strip off the prefix directory.
        # Example: directory/Aldi-CA_2017_01_01-3.csv => Aldi-CA_2017_01_01-3.csv
        currentLocalCsvFileBasename =  os.path.basename(currentLocalCsvFile)

        # Now lets see if there are any blobs in the cloud with the same name.
        for currentBucketFile, currentBucketObj in bucketFiles.iteritems():

            if currentLocalCsvFileBasename == os.path.basename(currentBucketFile):

                print "Local: " + str(currentLocalCsvFile)
                print "This name is currently being used in the cloud"

                print "Bucket: " + str(currentBucketFile)

                # Example: Aldi-CA_2017_01_01-3.csv => Aldi-CA_2017_01_01.csv
                uniqueIdSub = re.compile('(\-\d+)?', re.IGNORECASE)
                currentBucketFileBasename = uniqueIdSub.sub('', currentBucketFile)

                if bucketFiles[currentBucketFileBasename]["maxId"] is None:
                    # Update the maximum ID.
                    bucketFiles[currentBucketFileBasename]["maxId"] = 1
                else:
                    # Update the maximum ID.
                    bucketFiles[currentBucketFileBasename]["maxId"] += 1
                
                # Create the new alias.
                currentAlias = currentLocalCsvFile.replace('.csv',
                                                           '-' + str(bucketFiles[currentBucketFileBasename]["maxId"]) + '.csv')

                localCsvFiles[currentLocalCsvFile]["alias"] = currentAlias


# DEBUG: What do we need to upload?
for currentLocalCsvFile, currentLocalCsvObj in localCsvFiles.iteritems():
    
    # print currentLocalCsvFile, currentLocalCsvObj

    if currentLocalCsvObj["upload"]:
        currentLocalCsvFileSize = localCsvFiles[currentLocalCsvFile]["size"]
        if currentLocalCsvObj["alias"] is None:
            print "---"
            print "Need to upload: " + str(currentLocalCsvFile) + " " + str(currentLocalCsvFileSize)
        else:
            print "---"
            print "Need to rename before upload"
            print "From: " + str(currentLocalCsvFile) + " " + str(currentLocalCsvFileSize)
            print "To: " + str(currentLocalCsvObj["alias"])


    
    

# Upload files to the container.
#if isContainerInService(service, CONTAINER_NAME):
#    uploadFilesToAzure(service, CONTAINER_NAME,
#                       LOCAL_DIRECTORY, localFiles.keys())

# Read AFTER write any blobs.
#summaryAzure(service)

