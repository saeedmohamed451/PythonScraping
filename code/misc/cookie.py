#!/usr/bin/python

import requests

s = requests.Session()

print "Hello World"

url = 'http://plan.shoprite.com/Circular/ShopRite-of-New-Paltz/EDBF635/Weekly/1'

response = s.get(url)

url2 = 'http://plan.shoprite.com/CircularDetails/Item/2082069'

response2 = s.post(url2)

print response2.content

