#!/usr/bin/python

# Allow us to get input from the user.
import sys

# Interact with local operating system.
import os

# Interact with local files and directories.
from os import listdir, walk

# Interact with local files and directories.
from os.path import isfile, join

# Get the non-standard python packages from the virtual environment 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../venv/Lib/site-packages')))

# Interact with Azure storage.
from azure.storage import CloudStorageAccount


# Put all of our data into this container.
CONTAINER_NAME = {"name": "retailers"}

# Prefix of directories that interested in.
# Images on a month to month basis so we 
# do not hit the 5,000 blob listing limit.
BLOB_PREFIX=['CSV/',
             'PDF/',
             'PDF_FINAL/',
             'XLSX/',
             # Images for monthly and retailer basis.
             'IMAGES/AcmeMarkets-MD_2017_08',
             'IMAGES/AcmeMarkets-MD_2017_09',
             'IMAGES/AcmeMarkets-MD_2017_10',
             'IMAGES/AcmeMarkets-NY_2017_08',
             'IMAGES/AcmeMarkets-NY_2017_09',
             'IMAGES/AcmeMarkets-NY_2017_10',
             'IMAGES/Albertsons-AZ_2017_09',
             'IMAGES/Albertsons-AZ_2017_10',
             'IMAGES/Albertsons-CA_2017_08',
             'IMAGES/Albertsons-CA_2017_09',
             'IMAGES/Albertsons-CA_2017_10',
             'IMAGES/Albertsons-OR_2017_08',
             'IMAGES/Albertsons-OR_2017_09',
             'IMAGES/Albertsons-OR_2017_10',
             'IMAGES/Albertsons-TX_2017_09',
             'IMAGES/Albertsons-TX_2017_10',
             'IMAGES/Albertsons-WA_2017_09',
             'IMAGES/Albertsons-WA_2017_10',
             'IMAGES/Aldi-CA_2017_08',
             'IMAGES/Aldi-CA_2017_09',
             'IMAGES/Aldi-CA_2017_10',
             'IMAGES/Aldi-IL_2017_08',
             'IMAGES/Aldi-IL_2017_09',
             'IMAGES/Aldi-IL_2017_10',
             'IMAGES/Aldi-TX_2017_08',
             'IMAGES/Aldi-TX_2017_09',
             'IMAGES/Aldi-TX_2017_10',
             'IMAGES/CVS-FL_2017_09',
             'IMAGES/CVS-FL_2017_10',
             'IMAGES/DollarGeneral-IL_2017_07',
             'IMAGES/DollarGeneral-IL_2017_08',
             'IMAGES/DollarGeneral-IL_2017_09',
             'IMAGES/DollarGeneral-IL_2017_10',
             'IMAGES/FamilyDollar-IL_2017_09',
             'IMAGES/FamilyDollar-IL_2017_10',
             'IMAGES/FoodLion-MD_2017_08',
             'IMAGES/FoodLion-MD_2017_09',
             'IMAGES/FoodLion-MD_2017_10',
             'IMAGES/FoodLion-PA_2017_08',
             'IMAGES/FoodLion-PA_2017_09',
             'IMAGES/FoodLion-PA_2017_10',
             'IMAGES/Frescoymas-FL_2017_09',
             'IMAGES/Frescoymas-FL_2017_10',
             'IMAGES/GiantFood-MD_2017_09',
             'IMAGES/GiantFood-MD_2017_10',
             'IMAGES/Kroger-GA_2017_08',
             'IMAGES/Kroger-GA_2017_09',
             'IMAGES/Kroger-GA_2017_10',
             'IMAGES/Kroger-IL_2017_08',
             'IMAGES/Kroger-IL_2017_09',
             'IMAGES/Kroger-IL_2017_10',
             'IMAGES/Meijer-MI_2017_08',
             'IMAGES/Meijer-MI_2017_09',
             'IMAGES/Meijer-MI_2017_10',
             'IMAGES/Publix-FL_2017_10',
             'IMAGES/RiteAid-PA_2017_09',
             'IMAGES/RiteAid-PA_2017_10',
             'IMAGES/Safeway-MD_2017_08',
             'IMAGES/Safeway-MD_2017_09',
             'IMAGES/Safeway-MD_2017_10',
             'IMAGES/ShopRite-NY_2017_08',
             'IMAGES/ShopRite-NY_2017_09',
             'IMAGES/ShopRite-NY_2017_10',
             'IMAGES/StopAndShop-NJ_2017_09',
             'IMAGES/StopAndShop-NJ_2017_10',
             'IMAGES/Walgreens-CA_2017_08',
             'IMAGES/Walgreens-CA_2017_09',
             'IMAGES/Walgreens-IL_2017_06',
             'IMAGES/Walgreens-IL_2017_09',
             'IMAGES/Walgreens-IL_2017_10',
             'IMAGES/Walmart-AR_2017_09',
             'IMAGES/Walmart-AR_2017_10']


#
# Connect to the Azure account using the configuration settings.
#
def connectAzureAccount():

    # Assume the account is none, until we know otherwise.
    account = None

    try:
        import AzureConfiguration as config
    except:
        raise ValueError("Missing settings in AzureConfiguration.py.")

    if config.IS_EMULATED:
        account = CloudStorageAccount(is_emulated=True)
    else:
        # Note that account key and sas should not both be included
        ACCOUNT_NAME = config.STORAGE_ACCOUNT_NAME
        ACCOUNT_KEY = config.STORAGE_ACCOUNT_KEY
        SAS = config.SAS
        account = CloudStorageAccount(account_name=ACCOUNT_NAME, 
                                  account_key=ACCOUNT_KEY, 
                                  sas_token=SAS)

    return account

#
#
#
def createAzureService():

    # Connect to the Azure account using the Azure configuration.
    account = connectAzureAccount()

    # Get Azure Storage Service for the given account.
    service = account.create_block_blob_service()

    return service

#
#
#
def getFileNamesAndSizes(service, prefix='CSV'):

    allFiles = {}

    # Only interested in the files in the main container.
    blobs = list(service.list_blobs(CONTAINER_NAME["name"], prefix))

    # Extract out the names and sizes of the files.
    for currentBlob in blobs:
        allFiles[currentBlob.name] = {"name": currentBlob.name,
                                      "size": currentBlob.properties.content_length,
                                      "maxId": None}

    return allFiles

#
#  Provide a summary of the current Azure Service.
#
def summaryAzure(service):

    PAGE_BREAK = "---"

    print(PAGE_BREAK)
    print("Summary of Containers, Blobs and Files:")


    for currentPrefix in BLOB_PREFIX:

        # Now tell us about a the blobs in the current container.
        blobs = getFileNamesAndSizes(service, currentPrefix)

        blobsCount = len(blobs)

        if blobsCount > 4000:
            print "WARNING: Getting close to limit of 5000 blobs for API"
        
        print "->For prefix (" + str(currentPrefix) + " ->Found " + str(blobsCount) + " blobs"

        for blobName, blobObj in blobs.iteritems():
            print "->Blob: " + str(blobName)


    print(PAGE_BREAK)

#
# Return TRUE if the given container name is found with in the
# given Azure storage account.
#
def isContainerInService(service, containerName):

    containerExists = False

    # List every container in your account.
    containers = list(service.list_containers())
    
    for container in containers:
        if containerName == container.name:
            containerExists = True
            break

    return containerExists


def downloadFileFromAzure(service, containerName, localFilename, downloadFile):

    try:
        service.get_blob_to_path(containerName, downloadFile, localFilename)
    except Exception as e:
        print e
        print "Error: Problem with downloading"
        print "File: " + str(localFilename)
        print "Blob: " + str(downloadFile)

#
# Upload the given list of files to the given container within
# the Azure account.
#
def uploadFilesToAzure(service, containerName, localDirectory, uploadFiles):

    for currentFile in uploadFiles:
        # Create blob name and strip off the scrap.
        currentBlob = currentFile.replace(localDirectory, "./")

        # When blob already exists it is simply overwritten.
        exists = service.exists(containerName, currentBlob)

        # Verify the blob does not already exist as don't
        # want to overwrite it.
        if not exists:
            # Create a blob within the container.
            service.create_blob_from_path(containerName,
                                          currentBlob,
                                          currentFile)
        else:
            warningMsg = "Warning: Blob ("
            warningMsg += str(currentBlob)
            warningMsg += ")already exists."
            print warningMsg


#
# Remove all the blobs within the given container for the
# Azure account.
#
def deleteAllBlobsInAzure(service, containerName):

    # List every container in your account.
    containers = list(service.list_containers())
    
    for container in containers:
        if containerName == container.name:
            # Now tell us about a the blobs in the current container.
            blobs = list(service.list_blobs(container.name))

            for blob in blobs:
                service.delete_blob(containerName, blob.name)
            
            break

#
#
#
def deleteBlobInAzure(service, containerName, blobName):
    service.delete_blob(containerName, blobName)


#
#
#
def queryYesNo(question, default="no"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
