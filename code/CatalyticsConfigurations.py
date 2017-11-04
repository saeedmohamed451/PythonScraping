#!/usr/bin/python

#
# Configuration of the retailer's web sites of interest.
#  - Currently x9 different catagories:
#    -1- Flipp
#    -2- Flipp for VPN
#    -3- Flipp for Walmart
#    -4- My Web Grocer
#    -5- SE Grocer
#    -6- Stand Alone - Target 
#    -7- Stand Alone - HEB
#    -8- Stand Alone - Publix
#    -9- Stand Alone - Wholefoods
#


#
# Process the Flipp Category.
#
FLIPPS = {
    ##################################################
    "Aldi":
    {"site": "https://www.aldi.us",
     "flyers": [
         # 30Aug-05Sep Weekly Ad.
         {"store": "72543 HighwayPalm Desert",
          "location": "CA", # 92260
          "url":"https://flipp.aldi.us/flyer_data/1270367?locale=en-US"},
         # 30Aug-05Sep Preview Ad.
         {"store": "72543 HighwayPalm Desert",
          "location": "CA", # 92260
          "url":"https://flipp.aldi.us/flyer_data/1259795?locale=en-US"},
         # 30Aug-05Sep Weekly Ad.
         {"store": "1836 N ClybournChicago",
          "location": "IL", # 60614
          "url":"https://flipp.aldi.us/flyer_data/1270344?locale=en-US"},
         # 30Aug-05Sep Preview Ad.
         {"store": "1836 N ClybournChicago",
          "location": "IL", # 60614
          "url":"https://flipp.aldi.us/flyer_data/1259793?locale=en-US"},
         # 30Aug-05Sep Weekly Ad.
         {"store": "13548 Preston RdDallas",
          "location": "TX", # 75240
          "url":"https://flipp.aldi.us/flyer_data/1270349?locale=en-US"},
         # 30Aug-05Sep Preview Ad.
         {"store": "13548 Preston RdDallas",
          "location": "TX", # 75240
          "url":"https://flipp.aldi.us/flyer_data/1259790?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
    "DollarGeneral":
    # { Authorization: "Basic d2lzZS51c2VyOlIzc2VhcmNo" }
    {"site": "https://www.google.com",
     "flyers": [
         # 27Aug-2Sep Aug Weekly Ad.
         {"store": "549 E Pershing Rd,Chicago",
          "location": "IL", # 60653
          "url":"https://weeklyads.familydollar.com/flyer_data/1284199?locale=en-US"},
         # 06 Aug 04 Sep Hot Summer Deals Ad.
         {"store": "549 E Pershing Rd,Chicago",
          "location": "IL", # 60653
          "url":"https://weeklyads.familydollar.com/flyer_data/1251992?locale=en-US"},
         # 05 Jul 04 Sep Back to School Savings
         {"store": "549 E Pershing Rd,Chicago",
          "location": "IL", # 60653
          "url":"https://weeklyads.familydollar.com/flyer_data/1272194?locale=en-US"},
         # 25 Jul 01 Oct Beauty Cents Fall 2017
         {"store": "549 E Pershing Rd,Chicago",
          "location": "IL", # 60653
          "url":"https://weeklyads.familydollar.com/flyer_data/1241769?locale=en-US"},
         # 20Aug-23Sep Weekly Wireless Specials
         {"store": "549 E Pershing Rd,Chicago",
          "location": "IL", # 60653
          "url":"https://weeklyads.familydollar.com/flyer_data/1270892?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
    "FoodLion":
    {"site": "https://www.foodlion.com",
     "flyers": [
         # 30Aug-05Sep Weekly Ad.
         {"store": "7280 Mason Dixen Highway,Meyersdale",
          "location": "PA", # 15552
          "url":"https://ad.foodlion.com/flyer_data/1282042?locale=en-US"},
         # 30Aug-05Sep Weekly Ad.
         {"store": "3200 Old Washingtion Rd,Waldorf",
          "location": "ML", # 20602
          "url":"https://ad.foodlion.com/flyer_data/1282006?locale=en-US"}
     ],
     "grouping": "Flipp"},
    ##################################################
    "GiantFood":
    {"site": "https://giantfood.com",
     "flyers": [
         # 1-7 Sep Weekly Circular
         {"store": "3297 Crain HighwayWaldorf",
          "location": "ML", # 20603
          "url":"https://circular.giantfood.com/flyer_data/1278716?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
    "Kroger":
    # TODO: Need to change to the correct www.kroger.com or www.kroger.com.edgekey.net?
    {"site": "https://www.google.com",
     "flyers": [
         # 30Aug-05Sep Weekly Ad.
         {"store": "800 Glenwood Av,Atlanta",
          "location": "GA", # 30316
          "url":"https://wklyads-krogeratlanta.kroger.com/flyer_data/1278133?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
    "Meijer":
    {"site": "https://www.meijer.com",
     "flyers": [
         #  27Aug-2Sep Weekly Ad.
         {"store": "1997 E Beltline GrandRapids",
          "location": "MI", # 49525
          "url":"https://weeklyad.meijer.com/flyer_data/1274398?locale=en-US"},
         # 27Aug-2Sep Meal Kits.
         {"store": "1997 E Beltline GrandRapids",
          "location": "MI", # 49525
          "url":"https://weeklyad.meijer.com/flyer_data/1279350?locale=en-US"},
         # 20Aug-9Sep Automotive Ad.
         {"store": "1997 E Beltline GrandRapids",
          "location": "MI", # 49525
          "url":"https://weeklyad.meijer.com/flyer_data/1265827?locale=en-US"},
         # 27Aug-2Sep Back to School Ad.
         {"store": "1997 E Beltline GrandRapids",
          "location": "MI", # 49525
          "url":"https://weeklyad.meijer.com/flyer_data/1284846?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
    "StopAndShop":
    {"site": "https://stopandshop.com",
     "flyers": [
         # 1-7Sep Weekly Circular.
         {"store": "801 Newark Av,Elizabeth",
          "location": "NJ", # 07208
          "url":"https://circular.stopandshop.com/flyer_data/1278762?locale=en-US"}
     ],
     "grouping": "Flipp"},
    ##################################################
    "Walgreens":
    {"site": "https://www.walgreens.com",
     "flyers": [
         # 27Aug-2Sep Weekly Ad.
         {"store": "1500 E GAGE AVE,LA",
          "location": "CA", # 90001
          "url":"https://flyer.walgreens.com/flyer_data/1264261?locale=en-US"},
         # 27Aug-30Sep Aug Savings Book.
         {"store": "1500 E GAGE AVE,LA",
          "location": "CA", # 90001
          "url":"https://flyer.walgreens.com/flyer_data/1233968?locale=en-US"},
     ],
     "grouping": "Flipp"},
    ##################################################
}


#
# Process the Flipp Catagory for websites that use geo-blocking.
#
FLIPPS_FOR_VPN = {
    ##################################################
    "CVS":
    {"site": "https://www.cvs.com",
     "flyers": [
         # 27Aug-2Sep Weekly Ad.
         {"store": "170 SE 3RD Ave",
          "location": "FL", # 33131
          "url": "https://circular.cvs.com/flyer_data/1263578?locale=en-US",
          "itemsUrl": "https://circular.cvs.com/flyer_item/"},
     ],
     "grouping": "FlippForVpn"},
    ##################################################
    "RiteAid":
    {"site": "https://www.riteaid.com",
     "flyers": [
         # 27Aug-2Sep Weekly Ad.
         {"store": "1430 Baltimore Street",
          "location": "PA", # 17331
          "url": "https://weeklyad.info.riteaid.com/flyer_data/1264890?locale=en-US",
          "itemsUrl": "https://weeklyad.info.riteaid.com/flyer_item/tabbed/"},
     ],
     "grouping": "FlippForVpn"}
    ##################################################
}


#
# Process the Flipp Category for the Walmart retailer.
#
FLIPPS_FOR_WALMART = {
    ##################################################
   "Walmart":
   {"site": "https://www.walmart.com",
    "flyers": [
        # 13-31Aug Weekly Ads
        {"store": "205 N Main Street",
         "location": "AR", # 72712
         "url": "https://weeklyads.walmart.com/hosted/walmart/flyers/1251820?locale=en&store_code=3164"},
    ],
    "grouping": "FlippForWalmart"},
    ##################################################
}


#
# Process the 'Web Grocer' Category.
# (Takes about 6 minutes to get 15 catalogs.)
#
WEB_GROCERS = {
    ##################################################
   "AcmeMarkets":
   {"site": "http://acmemarkets.mywebgrocer.com",
    "flyers": [
        # 25-31Aug Online Weekly Ad.
        {"store": "114 S Talbot St Saint Michaels",
         "location": "ML", # 21663 
         "url": "/Circular/Saint-Michaels/879773084/Weekly/3/"},
        # 25Aug-21Sep Online Big Book.
        {"store": "114 S Talbot St Saint Michaels",
         "location": "ML", # 21663 
         "url": "/Circular/Saint-Michaels/879773084/Other/4/"},
        # 25-31Aug Online Weekly Ad.
        {"store": "13 North Avenue Pleasant Valley",
         "location": "NY", # 12569 
         "url": "/Circular/Pleasant-Valley/D6E3128197/Weekly/3/"},
        # 25Aug-21Sep Online Big Book.
        {"store": "13 North Avenue Pleasant Valley",
         "location": "NY", # 12569 
         "url": "/Circular/Pleasant-Valley/D6E3128197/Other/4/"},
    ],
    "grouping": "Webgrocer"},
    ##################################################
    "Albertsons":
    {"site": "http://albertsons.mywebgrocer.com",
     "flyers": [
         # 30Aug-5Sep Online Weekly Ad.
         {"store": "1500 NH Street",
          "location": "CA", # 93436 
          "url": "/Circular/Lompoc/0AA3128436/Weekly/2/"},
         # 1-4Sep 4 Day Sale.
         {"store": "1500 NH Street",
          "location": "CA", # 93436 
          "url": "/Circular/Lompoc/0AA3128436/Other/2/"},
         # 30Aug-26Sep Big Book of Savings.
         {"store": "1500 NH Street",
          "location": "CA", # 93436 
          "url": "/Circular/Lompoc/0AA3128436/Other/3/"},
     ],
     "grouping": "Webgrocer"},
    ##################################################
    "Safeway":
    {"site": "http://plan.safeway.com",
     "flyers": [
         # 30Aug-5Sep Weekly Ads. 
         {"store": "10335 Reisterstown Rd Owings Mills",
          "location": "ML", # 21117 
          "url": "/Circular/Owings-Mills-10335-Reisterstown-Rd-/CA9574582/Weekly/3/"},
         # 30Aug-26Sep Big Book of Savings.
        {"store": "10335 Reisterstown Rd Owings Mills",
         "location": "ML", # 21117 
         "url": "/Circular/Owings-Mills-10335-Reisterstown-Rd-/CA9574582/Other/5/"},
     ],
     "grouping": "Webgrocer"},
    ##################################################
    "ShopRite":
    {"site": "http://plan.shoprite.com",
     "flyers": [
         {"store": "258 Main StreetNew Paltz",
          "location": "NY", # 12561 
          "url": "/Circular/ShopRite-of-New-Paltz/EDBF635/Weekly/1/"},
         {"store": "258 Main StreetNew Paltz",
          "location": "NY", # 12561
          "url": "/Circular/ShopRite-of-New-Paltz/EDBF635/Other/1/"},
     ],
     "grouping": "Webgrocer"}
    ##################################################
}


#
# Process the SE Grocers Category.
#
# TODO: Not yet implemented.
#             
# Note: BiLo: server at: coupons.bi-lo.com
#             data from: https://coupons.bi-lo.com/
#                         services/gco?size=10000
#
# Note: Winn-Dixie: server at: coupons.winndixie.com
#                   data from: https://coupons.winndixie.com/
#                               services/gco?size=10000
SE_GROCERS = {
#    "coupons.bi-lo.com":
#    {"urls":
#     {"Colombia South Carolina": "https://coupons.bi-lo.com/services/gco?size=10000"},
#     "grouping": "SEgrocer"}
}

#
# Process the Stand Alone Category.
#
# TODO: Not yet implemented.
#
# Note: Publix: server at: weeklyad.publix.com
#               data from: http://weeklyad.publix.com/
#                           Publix/ListingDetail?IsPartial=Y&
#                           StoreID=2500566&
#                           ListingID=-2029316545&
#                           SneakPeek=N
#
# Note: Target: server at: weeklyad.target.com
#               data from: https://weeklyad-api.target.com/
#                           weekly_ads/v1/promotions/2799-20170806?
#                           key=360729a3d898ec130e09f7caadd8c165
#
# Note: HEB: server at: https://www.heb.com/weekly-ads/weekly-deals/426
#            data from: 
STANDALONES_TARGET = {}
STANDALONES_HEB = {}
STANDALONES_PUBLIX = {}
STANDALONES_WHOLEFOODS = {}

