#!/usr/bin/bash

echo "Generate code coverage for Catalytics."
coverage run --source Catalog.py,DataCleanse.py,DocumentParsers.py,DocumentServices.py,driveCatalytics.py,StoreItem.py,WebParsers.py,WebServices.py -m pytest

echo "Generate the Catalytics HTML code coveage report."
coverage html --title=Catalytics


