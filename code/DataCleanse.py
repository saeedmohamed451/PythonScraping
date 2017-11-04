#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# This file contains the pattern matches we need to convert a raw price
# to a cleansed:
# - Complete Description
# - Price
# - Multibuy quantity
# - Promotion type
#

#######
# QnA #
#######

# Q: Why are there so many pattern matches?
#
# A: Each of these pattern matches are specific to raw price strings
#    that have been scraped off the retailer's web sites.
#
#    Once we understand these patterns across multiple retailers these
#    pattern matches can be made generic by replacing 'words' with '\S'.
#
#    These reduced pattern matches can then be used as a ground-truth
#    training set for supervised machine learning.
#
#    A neural network can then be used to perform the raw price
#    conversions for new retailers or existing retailers than change
#    their raw price strings over time.
#    


# Symbolic replacements.
SYMBOLIC_REPLACEMENTS = {
    "$": "",
    "\$": "",
    "¢": "",
}

# Generic string replacements, that are case sensitive.
# Dont want to do any string replacements but use pattern matches
# As this is more correct.
STRING_REPLACEMENTS = {
}

REMOVE_WHITE_SPACE = {" ": ""}

# String replacements specific to Price.
PRICE_STRING_REPLACEMENTS = {}
PRICE_STRING_REPLACEMENTS.update(STRING_REPLACEMENTS)
PRICE_STRING_REPLACEMENTS.update(REMOVE_WHITE_SPACE)

#####################
# Pattern matching. #
#####################

# Price patterns.
# Note: Reserve value in dictionary for future use.
PRICE_PATTERNS = {

    ################
    # Single Items #
    ################
    # 4.99 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "((\d+)(\.\d+)?)\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend": "",
    # 27.99 PLUS $1.00 manufacturer's coupon in most Sunday newspapers** **Coupons from Sunday newspaper must be presented at time of purchase.
    "((\d+)(\.\d+)?)\s*PLUS\s*\$*\d+\.*\d*\s*manufacturer's\s*coupon\s*in\s*most\s*Sunday\s*newspapers\**\s*\**Coupons\s*from\s*Sunday\s*newspaper\s*must\s*be\s*presented\s*at\s*time\s*of\s*purchase\.*": "",
    # 0.88 ⟡Plus deposit where requires.
    "((\d+)(\.\d+)?)\s*\⟡\s*Plus\s*deposit\s*where\s*requires\.*": "",
    # 2.44 ⟡ plus deposit where required by law.
    "((\d+)(\.\d+)?)\s*\⟡\s*plus\s*deposit\s*where\s*required\s*by\s*law\.*": "",
    # 1.99 (excludes Fiber One).
    "((\d+)(\.\d+)?)\s*\(*excludes\s*Fiber\s*One\)*\.*": "",
    # 2.98 save/ahorre $3.01
    "((\d+)(\.\d+)?)\s*save\s*\/\s*ahorre\s*\$\d+\.*\d*": "",
    # 4.98 save/ahorre $2.01 lb.
    "((\d+)(\.\d+)?)\s*save\s*\/\s*ahorre\s*\$\d+\.*\d*\s*lb\.*": "",
    # 1.28 save/ahorre 72¢
    "((\d+)(\.\d+)?)\s*save\s*\/\s*ahorre\s*\d+\¢": "",
    # 0.48 save from /ahorre entre 21-51¢
    "((\d+)(\.\d+)?)\s*save\s*\s*from\s*\/\s*ahorre\s*entre\s*\d+\-\d+\¢": "",
    # 4.98 save from/ahorre entre $1.01-2.01
    "((\d+)(\.\d+)?)\s*save\s*\s*from\s*\/\s*ahorre\s*entre\s*\$\d+\.*\d*\-\d+\.*\d*": "",
    # NOW/AHORA 0.75
    "NOW\s*\/\s*AHORA\s*((\d+)(\.\d+)?)": "",
    # 2.89 buy 5 & save
    "((\d+)(\.\d+)?)\s*buy\s*\d+\s*\&\s*save": "",
    # get both for 7.0 buy one
    "get\s*both\s*for\s*((\d+)(\.\d+)?)\s*buy\s*one": "",
    # 1.0 EXTRA hot price
    "((\d+)(\.\d+)?)\s*EXTRA\s*hot\s*price": "",
    # 9.99 While Supplies Last
    "((\d+)(\.\d+)?)\s*While\s*Supplies\s*Last": "",
    # 10.99 Order Online, by Phone or in Person!
    "((\d+)(\.\d+)?)\s*Order\s*Online\,*\s*by\s*Phone\s*or\s*in\s*Person": "",
    # $29.99 to $49.99
    "^\s*\$*((\d+)(\.\d+)?)\s*to\s*\$*\d+\.*\d*": "",
    # $1.49 MFR with Price Plus Card
    "\$*((\d+)(\.\d+)?)\s*MFR\s*with\s*Price\s*Plus\s*Card": "",
    # 5.95 Fees and limits apply
    "((\d+)(\.\d+)?)\s*Fees\s*and\s*limits\s*apply": "",
    # 5.99 Must bring coupon to get advertised discount
    "((\d+)(\.\d+)?)\s*Must\s*bring\s*coupon\s*to\s*get\s*advertised\s*discount": "",
    # 24.99 buy one Wonder Woman DVD
    "((\d+)(\.\d+)?)\s*buy\s*one\s*Wonder\s*Woman\s*DVD": "",
    # 59.99 Date Subject to change
    "((\d+)(\.\d+)?)\s*Date\s*Subject\s*to\s*change": "",
    # 21.99 $2.00 mfr's coupon in most Sunday newspapers**
    "((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*mfr\'s\s*coupon\s*in\s*most\s*Sunday\s*newspapers\**": "",
    # 5.99 (excludes trial/travel sizes).
    "((\d+)(\.\d+)?)\s*\(*excludes\s*trial\/travel\s*sizes\)*\.*": "",
    # 13.99 $5.00 mfr's mail-in rebate
    "((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*mfr\'s\s*mail\-in\s*rebate": "",
    # $1, See description for details
    "\$*((\d+)(\.\d+)?)\,*\s*See\s*description\s*for\s*details": "",
    # 0.88 May Vary by Store
    "((\d+)(\.\d+)?)\s*May\s*Vary\s*by\s*Store": "",
    # 6.99 Where Available
    "((\d+)(\.\d+)?)\s*Where\s*Available": "",
    # 5.99 Some Exclusions Apply
    "((\d+)(\.\d+)?)\s*Some\s*Exclusions\s*Apply": "",
    # 0.79 Not all items available in all stores.
    "((\d+)(\.\d+)?)\s*Not\s*all\s*items\s*available\s*in\s*all\s*stores\.*": "",
    # 0.99 USE DIGITAL COUPON UP TO 5X IN THE SAME TRANSACTION
    "((\d+)(\.\d+)?)\s*USE\s*DIGITAL\s*COUPON\s*UP\s*TO\s*\d+X\s*IN\s*THE\s*SAME\s*TRANSACTION": "",
    # 18.99 BONUS 3000=$3 reward when you buy 2
    "((\d+)(\.\d+)?)\s*BONUS\s*\d+\=\$*\d+\s*reward\s*when\s*you\s*buy\s*\d+": "",
    # 5.99 Bonus point 2000 = $2 reward When you buy 2
    "((\d+)(\.\d+)?)\s*Bonus\s*point\s*\d+\s*\=*\s*\$*\d+\s*reward\s*When\s*you\s*buy\s*\d+": "",
    # 6.99  $1 less coupon online or in store
    "((\d+)(\.\d+)?)\s*\$*\d+\s*less\s*coupon\s*online\s*or\s*in\s*store": "",
    # 8.99 $5 mail-in rebate on 2Ω
    "((\d+)(\.\d+)?)\s*\$*\d+\s*mail\-in\s*rebate\s*on\s*\d*\s*\Ω*": "",
    # 16.99 $3 mail-in rebateΩ
    "((\d+)(\.\d+)?)\s*\$*\d+\s*mail\-in\s*rebate\Ω*": "",
    # 5.99 HOT DEAL
    "((\d+)(\.\d+)?)\s*HOT\s*DEAL": "",
    # coupon savings 19.99
    "coupon\s*savings\s*((\d+)(\.\d+)?)": "",
    # 9.99 +Only available on in-store purchases.
    "((\d+)(\.\d+)?)\s*\+*Only\s*available\s*on\s*in\-store\s*purchases\.*": "",
    # 5.99 BONUS POINTS 3000=$3 reward when you spend $10
    "((\d+)(\.\d+)?)\s*BONUS\s*POINTS\s*\d+\=\$*\d+\s*reward\s*when\s*you\s*spend\s*\$*\d+": "",
    # 10.0 Select stores only.
    "((\d+)(\.\d+)?)\s*Select\s*stores\s*only\.*": "",
    # FINAL PRICE 5.5
    "FINAL\s*PRICE\s*((\d+)(\.\d+)?)": "",
    # 6.99 EARN 2,000 IN PLENTY POINTS WORTH
    "((\d+)(\.\d+)?)\s*EARN\s*\d+\,*\d*\s*IN\s*PLENTY\s*POINTS\s*WORTH": "",
    # 6.99 EARN 2,000 IN PLENTI POINTS WORTH
    "((\d+)(\.\d+)?)\s*EARN\s*\d+\,*\d*\s*IN\s*PLENTI\s*POINTS\s*WORTH": "",
    # 5.99 (excludes Rite Aid Aspirin)  WITH CARD
    "((\d+)(\.\d+)?)\s*\(excludes\s*Rite\s*Aid\s*Aspirin\)\s*WITH\s*CARD": "",
    # Reg. Price 5.0
    "Reg\.*\s*Price\s*((\d+)(\.\d+)?)": "",
    # 20.0 Airtime sold separately.
    "((\d+)(\.\d+)?)\s*Airtime\s*sold\s*separately\.*": "",
    # 15.0 Selection may vary by store.
    "((\d+)(\.\d+)?)\s*Selection\s*may\s*vary\s*by\s*store\.*": "",
    # 0.99 Money-saving WEEKLY DEALS in every aisle
    "((\d+)(\.\d+)?)\s*Money\-*saving\s*WEEKLY\s*DEALS\s*in\s*every\s*aisle": "",
    # 5.0 Only with your Giant card
    "((\d+)(\.\d+)?)\s*Only\s*with\s*your\s*Giant\s*card": "",
    # NOW 1.39
    "NOW\s*((\d+)(\.\d+)?)": "",
    # SALE 5.5
    "SALE\s*((\d+)(\.\d+)?)": "",
    # sale 20% off
    "^sale\s*((\d+)(\.\d+)?)\s*\%\s*off": "-1.0",
    # now 7.49 sale 25% off
    "now\s*((\d+)(\.\d+)?)\s*sale\s*\d+\%\s*off": "",
    # 99¢
    "((\d+)(\.\d+)?)\¢": "div 100",
    # 99¢ lb.
    "((\d+)(\.\d+)?)\¢\s*lb\.*": "div 100",
    # 89¢ ea
    "((\d+)(\.\d+)?)\¢\s*ea\.*": "div 100",
    # 99¢ SALE
    "((\d+)(\.\d+)?)\¢\s*SALE": "div 100",
    # 99¢ EA. Club Price
    "((\d+)(\.\d+)?)\¢\s*ea\.*\s*Club\s*Price": "div 100",
    # 97¢ with Price QPlus Car
    "((\d+)(\.\d+)?)\¢\s*with\s*Price\s*QPlus\s*Car": "div 100",
    # YOUR CHOICE $2.99
    "YOUR\s*CHOICE\s*\$*((\d+)(\.\d+)?)": "",
    # Your Choice! $1.99
    "YOUR\s*CHOICE\s*\!*\s*\$*((\d+)(\.\d+)?)": "",
    # Every Day 79¢
    "Every\s*Day\s*((\d+)(\.\d+)?)\¢": "div 100",
    # Every Day $1.99
    "Every\s*Day\s*\$((\d+)(\.\d+)?)": "",
    # FINAL PRICE $2.99
    "FINAL\s*PRICE\s*\$((\d+)(\.\d+)?)": "",
    # Reg. 1.75
    "Reg\.*\s*((\d+)(\.\d+)?)": "",
    # Sale Price 0.88
    "Sale\s*Price\s*((\d+)(\.\d+)?)": "",
    # As Low As 19.99
    "As\s*Low\s*As\s*((\d+)(\.\d+)?)": "",
    # YOUR CHOICE 2.88
    "YOUR\s*CHOICE\s*((\d+)(\.\d+)?)": "",
    # 3.99 Excludes Organic
    # 2.99 (excludes Organic)
    "((\d+)(\.\d+)?)\s*\(*Excludes\s*Organic\)*": "",
    # Starting at 20.0
    "Starting\s*at\s*((\d+)(\.\d+)?)": "",
    # Starting at 5.0 Selection varies by store
    "Starting\s*at\s*((\d+)(\.\d+)?)\s*Selection\s*varies\s*by\s*store": "",
    # 3.5 Selection varies by store
    "((\d+)(\.\d+)?)\s*Selection\s*varies\s*by\s*store": "",
    # 1.99 Sizes Vary by Store
    "((\d+)(\.\d+)?)\s*Sizes\s*Vary\s*by\s*Store": "",
    # 0.49 Each
    "((\d+)(\.\d+)?)\s*Each": "",
    # 79¢ ea with card
    "((\d+)(\.\d+)?)\¢\s*ea\s*with\s*card": "div 100",
    # 97¢ with Price Plus Card
    "((\d+)(\.\d+)?)\¢\s*with\s*Price\s*Plus\s*Card": "div 100",
    # $5 with your club card
    "\$*((\d+)(\.\d+)?)\s*with\s*your\s*club\s*card": "",
    # 0.44 lb OR 0.49 /lb.
    "((\d+)(\.\d+)?)\s*\/*lb\.*": "",
    # 0.29 Per Lb. OR 
    "((\d+)(\.\d+)?)\s*Per\s*Lb\.*": "",
    # 1.59 Per Lb. SAVE 15%
    "((\d+)(\.\d+)?)\s*Per\s*Lb\.\s*SAVE\s*\d+\%": "",
    # 0.33 /ea. OR 14.49 EA OR 1.99 ea. OR 2.99 /ea OR 5.99 EA.
    "((\d+)(\.\d+)?)\s*\/*ea\.*": "",
    # $4.99 Every Day
    "\$*((\d+)(\.\d+)?)\s*Every\s*Day": "",
    # 10.0 Low Price every day
    "((\d+)(\.\d+)?)\s*Low\s*Price\s*every\s*day": "",
    # 5.0 WOW Price Every Day
    "((\d+)(\.\d+)?)\s*WOW\s*Price\s*Every\s*Day": "",
    # 0.99 EA Low Price every Day
    "((\d+)(\.\d+)?)\s*EA\s*Low\s*Price\s*every\s*Day": "",
    # 0.52 EA WOW Price Every Day
    "((\d+)(\.\d+)?)\s*EA\s*WOW\s*Price\s*Every\s*Day": "",
    # 1.29 LB WOW Price every day
    "((\d+)(\.\d+)?)\s*LB\s*WOW\s*Price\s*every\s*day": "",
    # 0.5 Hot Price!
    "((\d+)(\.\d+)?)\s*Hot\s*Price\!": "",
    # 10.0 HOT SALE
    "((\d+)(\.\d+)?)\s*HOT\s*SALE": "",
    # 0.9 EA HOT SALE
    "((\d+)(\.\d+)?)\s*EA\s*HOT\s*SALE": "",
    # 1.99 LB HOT SALE OR 2.99 LB. HOT SALE
    "((\d+)(\.\d+)?)\s*LB\.*\s*HOT\s*SALE": "",
    # 0.5 PER WING HOT SALE
    "((\d+)(\.\d+)?)\s*PER\s*WING\s*HOT\s*SALE": "",
    # 10.0 Floral not included.
    "((\d+)(\.\d+)?)\s*Floral\s*not\s*included\.*": "",
    # 0.49 Limit 4
    "((\d+)(\.\d+)?)\s*Limit": "",
    # "3.99 Limit 2 offers per transaction.
    "((\d+)(\.\d+)?)\s*Limit\s*\d+\s*offers\s*per\s*transaction": "",
    # "9.99 *Lesser quantities
    "((\d+)(\.\d+)?)\s*\**Lesser\s*quantities": "",
    # 5.0 See Tag for Details
    "((\d+)(\.\d+)?)\s*See": "",
    # 16.0 Cover not included
    "((\d+)(\.\d+)?)\s*Cover": "",
    # 1.99 Sizes Vary by Store
    "((\d+)(\.\d+)?)\s*Sizes": "",
    # 12.91 Backpack Not Included
    "((\d+)(\.\d+)?)\s*Backpack": "",
    # 3.99 Accessories not included.
    "((\d+)(\.\d+)?)\s*Accessories": "",
    # 12.0 Available in Most Stores.
    "((\d+)(\.\d+)?)\s*Available": "",
    # 5.0 Excludes Pantene Gold Series
    "((\d+)(\.\d+)?)\s*Excludes": "",
    # 25.0 Phone and Plan Sold Separately
    "((\d+)(\.\d+)?)\s*Phone": "",
    # 1.0 prices not valid in the City of Philadelphia, PA, or Cook County, IL
    "((\d+)(\.\d+)?)\s*prices": "",
    # FINAL PRICE 0.99 $1.00 off. SAVE $5 when you buy 5 participating products
    "FINAL\s*PRICE\s*((\d+)(\.\d+)?)\s*\$*\d+\.\d+\s*off\.*\,*\s*SAVE\s*\$\d+\s*When\s*You\s*Buy\s*\d+\s*Participating\s*Products": "",
    # Final price 2/ 4.0 DIGITAL COUPON $1.00 OFF 2
    "FINAL\s*price\s*2\/\s*((\d+)(\.\d+)?)\s*DIGITAL\s*COUPON\s*\$\d+\.*\d*\s*OFF\s*\d*": "div 2",
    # FINAL PRICE 2/ 4.0 $1.00 OFF 2 DIGITAL COUPON Limit 1
    "FINAL\s*PRICE\s*2\/\s*((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*OFF\s*\d+\s*DIGITAL\s*COUPON\s*Limit": "div 2",
    # FINAL PRICE 2/ 3.0 DIGITAL COUPON $2.00 OFF 2 Limit 1
    "FINAL\s*PRICE\s*2\/\s*((\d+)(\.\d+)?)\s*DIGITAL\s*COUPON\s*\$*\d+\.*\d*\s*OFF\s*\d+\s*Limit\s*\d+": "div 2",
    # Final price 3/ 7.0 $5.00 OFF 3 DIGITAL COUPON
    "FINAL\s*PRICE\s*3\/\s*((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*OFF\s*\d+\s*DIGITAL\s*COUPON": "div 3",
    # FINAL PRICE 3/ 9.0 $5.00 when you buy 3 with coupon in most sunday papers
    "FINAL\s*PRICE\s*3\/\s*((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*when\s*you\s*buy": "div 3",
    # FINAL PRICE 3/ 9.0 -$2.00 off of 3 WITH COUPON IN MOST SUNDAY PAPERS Limit 1
    "FINAL\s*PRICE\s*3\/\s*((\d+)(\.\d+)?)\s*\-*\$*\d+\.*\d*\s*off\s*of\s*\d+\s*WITH\s*COUPON\s*IN\s*MOST\s*SUNDAY\s*PAPERS": "div 3",
    # FINAL PRICE 5/ 5.0 -$5.00 WHEN YOU BUY 5 DIGITAL COUPON
    "FINAL\s*PRICE\s*5\/\s*((\d+)(\.\d+)?)\s*\-*\$*\d+": "div 5",
    # 5.99 Plus Deposit Where Applicable
    "((\d+)(\.\d+)?)\s*Plus\s*Deposit": "",
    # 0.99 ◊Plus deposit where required. Limit 3 items.
    "((\d+)(\.\d+)?)\s*\◊*\s*Plus\s*deposit\s*where\s*required": "",
    # 2.44 ✧Plus deposit where required.
    "((\d+)(\.\d+)?)\s*\✧*\s*Plus\s*deposit\s*where\s*required": "",
    # 10.0 Free When you buy Panera soup
    "((\d+)(\.\d+)?)\s*Free": "",
    # 39.99 Valid week of August 23
    "((\d+)(\.\d+)?)\s*Valid\s*week\s*of": "",
    # 1.99 Weekly sale price without digital coupon
    "((\d+)(\.\d+)?)\s*Weekly\s*sale\s*price\s*without\s*digital\s*coupon": "",
    # FREE BANANAS UP TO $3 VALUE when you spend $10 
    "FREE\s*BANANAS\s*UP\s*TO\s*\$*\d+\s*VALUE\s*when\s*you\s*spend\s*\$*((\d+)(\.\d+)?)": "",
    # 1.77 *Other quantities 2/$5
    "((\d+)(\.\d+)?)\s*\**Other\s*quantities": "",
    # SPEND $3, See description for details
    "SPEND\s*\$*((\d+)(\.\d+)?)\,*\s*See\s*description\s*for\s*details": "",
    # 11.99 Ω Manufacturer coupon available in most Sunday papers "or at Walgreens.com/Coupons. 
    "((\d+)(\.\d+)?)\s*\Ω*\s*Manufacturer\s*coupon": "",
    # 2.99 REGISTER REWARDS® $3 OFF with card on next purchase when you buy 2
    "((\d+)(\.\d+)?)\s*REGISTER\s*REWARDS\®*\s*\$*\d+\s*OFF\s*with\s*card\s*on\s*next\s*purchase\s*when\s*you\s*buy\s*2": "div 2",
    # 3.99 BONUS POINTS 1000 = $1 reward when you buy 2
    # 2.49 BONUS POINTS 1000 = $1 reward when you buy 2
    "((\d+)(\.\d+)?)\s*BONUS\s*POINTS\s*\d+\s*\=\s*\$*\d+\s*reward\s*when\s*you\s*buy\s*2": "",
    # 88¢ Plus deposit where required
    # 79¢ Plus deposit where required
    "((\d+)(\.\d+)?)\¢\s*Plus\s*deposit\s*where\s*required": "div 100",
    # 79¢, See description for details
    "((\d+)(\.\d+)?)\¢\,*\s*See\s*description\s*for\s*details": "div 100",
    # 2.99 RED HOT SPECIAL Valid week of August 30
    "((\d+)(\.\d+)?)\s*RED\s*HOT\s*SPECIAL": "",
    # 5.77 4 DAYS ONLY! Limit 4 Lobsters
    "((\d+)(\.\d+)?)\s*\d+\s*DAYS\s*ONLY\!*": "",
    # SALE 2 for 6.0 2 DAYS ONLY!
    "SALE\s*2\s*for\s*((\d+)(\.\d)?)\s*\d\s*DAYS\s*ONLY\!*": "div 2",
    # SALE 2 for 1.0 SAVE 70¢ WHEN YOU BUY 2 Must purchase 2 to get discount price
    "SALE\s*2\s*for\s*((\d+)(\.\d)?)\s*SAVE\s*70\¢\s*WHEN\s*YOU\s*BUY\s*\d+\s*Must\s*purchase\s*\d+\s*to\s*get\s*discount\s*price": "div 2",
    # 3.99 CUT FRESH IN-STORE DAILY
    "((\d+)(\.\d+)?)\s*CUT\s*FRESH": "",
    # 19.99 Participating Varieties and Sizes May Vary by Store
    "((\d+)(\.\d+)?)\s*Participating\s*Varieties\s*and\s*Sizes\s*May\s*Vary\s*by\s*Store": "",
    # 3.77 LIMIT 1 WITHOUT COUPON
    "((\d+)(\.\d+)?)\s*LIMIT\s*\d+\s*WITHOUT\s*COUPON": "",
    # 0.97 LIMIT 5 LBS.
    "((\d+)(\.\d+)?)\s*LIMIT\s*\d+\s*LBS\.*": "",
    # 3.44 Brand may vary by store. ◊Plus deposit where required.
    "((\d+)(\.\d+)?)\s*Brand\s*may\s*vary\s*by\s*store": "",
    # 2.99 (excludes Baked).
    "((\d+)(\.\d+)?)\s*\(*\s*excludes\s*Baked\s*\)*\.*": "",
    # 9.99 $1.00 coupon savings in our app** **Coupons from Sunday newspaper must be presented at time of purchase.
    # 2.94 $1.00 coupon savings in our app
    "((\d+)(\.\d*)?)\s*\$\d+\.*\d*\s*coupon\s*savings\s*in\s*our\s*app\**": "",
    # 0.99 $1.00 instant coupon at coupon center
    "((\d+)(\.\d*)?)\s*\$\d+\.*\d*\s*instant\s*coupon\s*at\s*coupon\s*center": "",
    # 13.99 $5 mfr's mail-in rebate
    "((\d+)(\.\d*)?)\s*\$\d+\s*mfr\'s\s*mail\-in\s*rebate": "",
    # 9.99 $1 mfr's coupon in most Sunday newspapers
    "((\d+)(\.\d*)?)\s*\$\d+\s*mfr\'s\s*coupon\s*in\s*most\s*Sunday\s*newspapers": "",
    # 8.99 $2 ExtraBucks® Rewards for next purchase ExtraBucks® Rewards offer limit of
    # 4.99 $2 ExtraBucks® Rewards for next purchase ExtraBucks® Rewards
    # 8.99 $2 ExtraBucks® Rewards for next purchase ExtraBucks® Rewards
    # 9.99 $9.99 ExtraBucks® Rewards for next purchase ExtraBucks® Rewards
    "((\d+)(\.\d*)?)\s*\$\d+\.*\d*\s*ExtraBucks\®\s*Rewards\s*for\s*next\s*purchase": "",
    # 2.99 $5 ExtraBucks® Rewards when you spend $20
    # 6.99 $5 ExtraBucks® Rewards when you spend $20
    # 4.99 $5 ExtraBucks® Rewards when you spend $20
    "((\d+)(\.\d*)?)\s*\$\d+\.*\d*\s*ExtraBucks\®\s*Rewards\s*when\s*you\s*spend\s*\$*\d+": "",
    # 34.99 PLUS $5 ExtraBucks Rewards Manufacturers
    "((\d+)(\.\d*)?)\s*PLUS\s*\$*\d+\s*ExtraBucks\s*Rewards\s*Manufacturers": "",
    # 11.99 BUY 2 GET $5 ExtraBucks® Rewards ExtraBucks®
    # 14.99 BUY 2 GET $5 ExtraBucks® Rewards ExtraBucks
    "((\d+)(\.\d*)?)\s*BUY\s*\d+\s*GET\s*\$*\d+\s*ExtraBucks\®\s*Rewards\s*ExtraBucks\®": "",
    # regular retail of 14.99 HP, Canon or Epson ink cartridges
    "regular\s*retail\s*of\s*((\d+)(\.\d*)?)\s*HP\,*\s*Canon\s*or\s*Epson\s*ink\s*cartridges": "",
    # 9.99 Earn 100 Plenti points* When you buy 2
    "((\d+)(\.\d*)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*When\s*you\s*buy\s*\d+": "",
    # 7.99 (*Children Cough and Cold Category, ProVoice 2017)
    "((\d+)(\.\d*)?)\s*\(*\s*\**\s*Children\s*Cough": "",
    # 21.99 (*Excludes Mucinex D)
    "((\d+)(\.\d*)?)\s*\(*\s*\**\s*Excludes\s*Mucinex": "",
    # 0.1 Same day pickup FREE
    "((\d+)(\.\d*)?)\s*Same\s*day\s*pickup\s*FREE": "",
    # 28.89 Was $41.29. Save $12.40
    # 38.19 Was $49.99. Save $11.80.
    # 16.99 Was $24.49. Save $7.50.
    "((\d+)(\.\d*)?)\s*Was\s*\$*\d+\.*\d*\.*\s*Save\s*\$*\d+\.*\d*": "",
    # 5.99 REGULAR RETAIL
    "((\d+)(\.\d*)?)\s*REGULAR\s*RETAIL": "",
    # 1.99 SPEND $9 GET $3 ExtraBucks® Rewards ExtraBucks® Rewards
    "((\d+)(\.\d*)?)\s*SPEND\s*\$*\d+\s*GET\s*\$*\d+\s*ExtraBucks\®*\s*Rewards\s*ExtraBucks\®*\s*Rewards": "",
    # 4.0 PLUS! Earn 300 Plenti points Worth $3.00 WITH CARD
    "((\d+)(\.\d*)?)\s*PLUS\!*\s*Earn\s*\d+\s*Plenti\s*points\s*Worth\s*\$*\d+\.*\d*\s*WITH\s*CARD": "",
    # 10.49 Earn 500 Plenti points* Worth $5.00 When you buy
    "((\d+)(\.\d*)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*\s*When\s*you\s*buy": "",
    # 6.99 Earn 400 Plenti points* when you buy
    "((\d+)(\.\d*)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*When\s*you\s*buy": "",
    
    ################
    # Loyalty Card #
    ################

    # $1.99 Club Price
    "\$*((\d+)(\.\d+)?)\s*Club\s*Price": "",
    # $7.99 Card Price
    "\$*((\d+)(\.\d+)?)\s*Card\s*Price": "",
    # 0.49 with card
    "((\d+)(\.\d+)?)\s*with\s*card": "",
    # 0.59 Ea. With Card
    "((\d+)(\.\d+)?)\s*Ea\.*\s*With\s*Card": "",
    # $2.49 with Price Plus Card
    "\$*((\d+)(\.\d+)?)\s*with\s*Price\s*Plus\s*Card": "",
    # 3.0 or $1.79 ea. with card 25¢ off online coupon◊
    "\d+\.\d+\s*or\s*\$((\d+)(\.\d+)?)\s*ea\.*\s*with\s*card\s*\d+\¢\s*off\s*online\s*coupon\◊*": "",
    # 4.99 with card $2 off online coupon◊
    "((\d+)(\.\d+)?)\s*with\s*card\s*\$\d+\s*off\s*online\s*coupon\◊*": "",
    # 0.88 lb With Card
    "((\d+)(\.\d+)?)\s*lb\s*With\s*Card": "",
    # 2.5 and up with card
    "((\d+)(\.\d+)?)\s*and\s*up\s*with\s*card": "",
    # 0.75 ‡
    "((\d+)(\.\d+)?)\s*\‡": "",
    # 6.0 *
    "((\d+)(\.\d+)?)\s*\*": "",
    # 0.99 Per 16-oz. Pkg.
    "((\d+)(\.\d+)?)\s*Per\s*\d+\-*oz\.*\s*Pkg\.*": "",
    # 14.99 Save $5 OR 2.99 Save $1. OR 109.99 * Save $20
    "((\d+)(\.\d+)?)\s*\**\s*Save\s*\$*\d+\.*": "",
    # 1.19 Per 4-Pack
    "((\d+)(\.\d+)?)\s*Per\s*\d+\-Pack": "",
    # 1.29 Per Pack
    "((\d+)(\.\d+)?)\s*Per\s*Pack": "",
    # 1.69 Per Pint
    "((\d+)(\.\d+)?)\s*Per\s*Pint": "",
    # 2.49 Per Dry Pint
    "((\d+)(\.\d+)?)\s*Per\s*Dry\s*Pint": "",
    # 3.69 Per Dozen
    "((\d+)(\.\d+)?)\s*Per\s*Dozen": "",
    # 4.95 3 Pack + 1 FREE
    "((\d+)(\.\d+)?)\s*\d+\s*Pack\s*\+*\s*\d+\s*FREE": "",
    # 7.75 3 Pack + 1 FREE Kids' Underwear
    "((\d+)(\.\d+)?)\s*\d+\s*Pack\s*\+*\s*\d+\s*FREE\s*Kids\'*\s*Underwear": "",
    # 1.99 /ea. 3 day sale !
    "((\d+)(\.\d+)?)\s*\/*ea\.*\s*\d+\s*day\s*sale\s*\!*": "",
    # 3.0 3 day sale!
    "((\d+)(\.\d)?)\s*\d\s*day\s*sale\s*\!*": "",
    # 10.0 MIX & MATCH OR 4.0 * Mix & Match!
    "((\d+)(\.\d+)?)\s*\**\s*MIX\s*\&\s*MATCH\!*": "",
    # SALE 3 for 6.0 Mix & Match!
    "SALE\s*3\s*for\s*((\d+)(\.\d+)?)\s*Mix\s*\&\s*Match\!*": "div 3",
    # 1.19 Per 1-lb. Pkg.
    "((\d+)(\.\d+)?)\s*Per\s*\d+\-*lb\.*\s*Pkg\.*": "",
    # 1.69 Per 3-lb. Bag
    "((\d+)(\.\d+)?)\s*Per\s*\d*\-*lb\.*\s*Bag": "",
    # 3.49 Per 12-oz. Bag.
    "((\d+)(\.\d+)?)\s*Per\s*\d*\-*oz\.*\s*Bag\.*": "",
    # 5.0 SWAP & SAVE!
    "((\d+)(\.\d+)?)\s*SWAP\s*\&\s*SAVE\!*": "",
    # 10.0 SAVE $5 when you spend $20 on participating products*
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*products\**": "",
    # 2.79 SAVE $5 when you spend $20 participating products*
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*participating\s*products*": "",
    # 34.99 Save $5.
    # 299.99 Save $50
    "((\d+)(\.\d+)?)\s*Save\s*\$\d+\.*": "",
    # 24.99 Save 5.01-15.01.
    "((\d+)(\.\d+)?)\s*Save\s*\d+\.\d+\-\d+\.\d+\.*": "",
    # 24.99 $10 off
    "((\d+)(\.\d+)?)\s*\$\d+\s*off": "",
    # 7.49 - $52.49 25% off
    "((\d+)(\.\d+)?)\s*\-\s*\$*\d+\.\d+\s*\d+\%\s*off": "",
    # 5.0 $1 OFF* INSTANTLY
    "((\d+)(\.\d+)?)\s*\$\d+\s*OFF\**\s*INSTANTLY": "",
    # 1.5 50¢ OFF INSTANTLY AT REGISTER
    "((\d+)(\.\d)?)\s*\d\d\¢\s*OFF\s*INSTANTLY\s*AT\s*REGISTER": "",
    # When You Buy 3 FINAL COST 1.77
    "When\s*You\s*Buy\s*\d+\s*FINAL\s*COST\s*((\d+)(\.\d*)?)": "",
    # 5.0 Save An Additional $3* with DG Digital Coupons
    "((\d+)(\.\d*)?)\s*Save\s*An\s*Additional\s*\$*\d+\**\s*with\s*DG\s*Digital\s*Coupons": "",
    # 3.5 $2 OFF INSTANTLY AT REGISTER
    "((\d+)(\.\d+)?)\s*\$\d+\s*OFF\s*INSTANTLY\s*AT\s*REGISTER": "",
    # 0.8 Final Price With Coupon* Save 10¢ with DG DIGITAL COUPONS
    "((\d+)(\.\d+)?)\s*Final\s*Price\s*With\s*Coupon\**\s*Save\s*\d+\¢\s*with\s*DG\s*DIGITAL\s*COUPONS": "",
    # 2.0 Final Price With Coupon* Save $1 With DG DIGITAL COUPONS
    "((\d+)(\.\d+)?)\s*Final\s*Price\s*With\s*Coupon\**\s*Save\s*\$\d+\s*With\s*DG\s*DIGITAL\s*COUPONS": "",
    # 1.95 DG DIGITAL COUPONS Save an additional $1*
    "((\d+)(\.\d+)?)\s*DG\s*DIGITAL\s*COUPONS\s*Save\s*an\s*additional\s*\$\d+\**": "",
    # 2.75 DG DIGITAL COUPONS Save an additional 25¢*
    "((\d+)(\.\d+)?)\s*DG\s*DIGITAL\s*COUPONS\s*Save\s*an\s*additional\s*\d+\¢\**": "",
    # 2.25 Save an additional $1* When you buy 2 with DG DIGITAL COUPONS
    "((\d+)(\.\d+)?)\s*Save\s*an\s*additional\s*\$\d+\**\s*When\s*you\s*buy\s*\d+\s*with\s*DG\s*DIGITAL\s*COUPONS": "",
    # 4.0 Save an additional 50¢*
    "((\d+)(\.\d+)?)\s*Save\s*an\s*additional\s*\d+\¢*\**": "",
    # 10.99 $1.00 DIGITAL COUPON
    # 3.99 -$1.00 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*\-*\$\d+\.\d+\s*DIGITAL\s*COUPON": "",
    # 1.49 DIGITAL COUPON - $1.00
    # 3.99 DIGITAL COUPON -$1.00
    "((\d+)(\.\d+)?)\s*DIGITAL\s*COUPON\s*\-*\s*\$\d+\.\d+": "",
    # 4.99 /lb. DIGITAL COUPON -$1.00
    "((\d+)(\.\d+)?)\s*\/*lb\.*\s*DIGITAL\s*COUPON\s*\-*\s*\$\d+\.\d+": "",
    # 5.99 /lb. $1.00 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*\/*lb\.*\s*\$\d+\.\d+\s*DIGITAL\s*COUPON": "",
    # 4.0 DIGITAL COUPON -$1.00 OFF 2
    "((\d+)(\.\d+)?)\s*DIGITAL\s*COUPON\s*\-*\s*\$\d+\.\d+\s*OFF\s*\d+": "",
    # 4.0 - $1.00 OFF 2 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*\-*\s*\$\d+\.\d+\s*OFF\s*\d+\s*DIGITAL\s*COUPON": "",
    # 1.49 $1.00 off DIGITAL COUPON
    # 6.0 $1.00 OFF 2 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*\$\d+\.\d+\s*off\s*DIGITAL\s*COUPON": "",
    # 12.0 WITH AIRTIME PURCHASE
    "((\d+)(\.\d+)?)\s*WITH\s*AIRTIME\s*PURCHASE": "",
    # 12.0 WITH ANY TRACFONE AIRTIME PURCHASE
    "((\d+)(\.\d+)?)\s*WITH\s*ANY\s*TRACFONE\s*AIRTIME\s*PURCHASE": "",
    # 10.39 - $103.99 20% off
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*\d+\%\s*off": "",
    # 1.11 - $12.74 sale 25% off
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*sale\s*\d+\%\s*off": "",
    # 7.99 sale $2 off
    "((\d+)(\.\d+)?)\s*sale\s*\$\d+\s*off": "",
    # 12.91 pre-tax
    "((\d+)(\.\d+)?)\s*pre\-*tax": "",
    # 1.25 - $5.00
    # 4.0 - $8
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.*\d*": "",
    # 3.0 - $8.00 $1 OFF
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*\$\d+\s*OFF": "",
    # 10.0 - $50.00 30-50% off women's handbags and select jewelry*
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*\d+\-\d+\%\s*off\s*women\'s\s*handbags\s*and\s*select\s*jewelry\**": "",
    # 3.49 +CRV
    "((\d+)(\.\d+)?)\s*\+*CRV": "",
    # 1.0 +CA CRV or deposit where applicable
    "((\d+)(\.\d+)?)\s*\+CA\s*CRV\s*or\s*deposit\s*where\s*applicable": "",
    # 10.0 ‡ +CA CRV or deposit where applicable
    "((\d+)(\.\d+)?)\s*\‡*\s*\+*CA\s*CRV\s*or\s*deposit\s*where\s*applicable": "",
    # 5.0 Buy Both Trueliving Lamp Shade Trueliving® Lamp Base Get GE® Halogen Bulbs Assorted 72W 2 pk. Free
    # 12.0 Buy Both trueliving® Lamp Shade And trueliving® Lamp Base Get Halogen Bulbs Assorted 72W 2 pk.FREE
    "((\d+)(\.\d+)?)\s*Buy\s*Both\s*trueliving": "",
    # 149.99 plus $50 off your next shopping trip via Custom Coupon at checkout when you buy one of the TVs featured above*
    "((\d+)(\.\d+)?)\s*plus\s*\$\d+\s*off\s*your\s*next\s*shopping\s*trip": "",
    # 59.99 * Save $10 on your next shopping trip via Custom Coupon at checkout when you buy one Madden NFL 18 Edition
    # 59.99 * Save $10 on your next shopping trip via Custom Coupon at checkout when you buy one PS4 or Xbox One Madden NFL 18 Standard Edition
    "((\d+)(\.\d+)?)\s*\**\s*Save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy": "",
    # 2 for 50.50 save $5 on your next shopping trip via Custom Coupon at checkout when you buy 
    "2\s*for\s*((\d+)(\.\d+)?)\s*\**\s*Save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy": "div 2",
    # 599.99 Save $100 plus $50 off your next shopping trip via Custom Coupon at checkout when you buy one of the TVs featured above*
    "((\d+)(\.\d+)?)\s*Save\s*\$\d+\s*plus\s*\$\d+\s*off\s*your\s*next\s*shopping\s*trip": "",
    # 399.99 Save $20 plus $50 via Custom Coupon at checkout when you buy one of the TVs featured above*
    "((\d+)(\.\d+)?)\s*Save\s*\$\d+\s*plus\s*\$\d+\s*via\s*Custom\s*Coupon\s*at\s*": "",
    
    # 6.0 or $3.79 ea. with card $1 off coupon online or in store on 2‡
    "\d+\.\d+\s*or\s*((\d+)(\.\d+)?)\s*ea\.*\s*with\s*card\s*\$\d+\s*off\s*coupon\s*online\s*or\s*in\s*store\s*on\s*\d+\‡*": "",
    # 16.99 with card $2 off coupon online or in store‡
    "((\d+)(\.\d+)?)\s*with\s*card\s*\$\d+\s*off\s*coupon\s*online\s*or\s*in\s*store\‡*": "",
    # 17.79 get $4 off instantly** when you buy $20 or more of Tide Downy Bounce or Gain Products*
    "((\d+)(\.\d+)?)\s*get\s*\$\d+\s*off\s*instantly\**\s*when\s*you\s*buy\s*\$\d+\s*or\s*more": "",
    # 17.99 EA W/ SAVINGS CENTER COUPON $2.00 OFF 1
    "((\d+)(\.\d+)?)\s*EA\s*W\/\s*SAVINGS\s*CENTER\s*COUPON\s*\$\d+\.\d+\s*OFF\s*\d+": "",
    # 4.0 W/ SAVINGS CENTER COUPON -1.00 OFF 2
    # 4.0 W/ SAVINGS CENTER COUPON $1.00 OFF 2
    "((\d+)(\.\d+)?)\s*W\/*\s*SAVINGS\s*CENTER\s*COUPON\s*\-*\$*\d+\.\d+\s*OFF\s*\d+": "",
    # 19.0 WITH ANY TOTAL WIRELESS SERVICE PLAN PURCHASE
    "((\d+)(\.\d+)?)\s*WITH\s*ANY\s*TOTAL\s*WIRELESS\s*SERVICE\s*PLAN\s*PURCHASE": "",
    # 49.0 WITH ANY SIMPLE MOBILE SERVICE PLAN PURCHASE
    "((\d+)(\.\d+)?)\s*WITH\s*ANY\s*SIMPLE\s*MOBILE\s*SERVICE\s*PLAN\s*PURCHASE": "",
    # 199.0 buy one Boost iPhone 6 get one free* $50 Prepaid Boost Airtime Card
    "((\d+)(\.\d+)?)\s*buy\s*one\s*Boost\s*iPhone\s*\d+\s*get\s*one\s*free\**\s*\$\d+\s*Prepaid\s*Boost\s*Airtime\s*Card": "",
    # 19.99 Average cost less than $7.00/month*
    "((\d+)(\.\d+)?)\s*Average\s*cost\s*less\s*than\s*\$\d+\.\d+\/month\**": "",
    # 1.99 EA W/O MVP Card regular retail
    "((\d+)(\.\d+)?)\s*EA\s*W\/O\s*MVP\s*Card\s*regular\s*retail": "",
    # MVP 0.89 W/O MVP Card 99¢ EA
    "MVP\s*((\d+)(\.\d+)?)": "",
    # MVP 1.79 W/O MVP Card Regular Retail
    "MVP\s*((\d+)(\.\d+)?)\s*W\/O\s*MVP\s*Card\s*\d+\¢\s*EA": "",
    # MVP 7.29 W/O MVP Card $8.99 EA
    "MVP\s*((\d+)(\.\d+)?)\s*W\/O\s*MVP\s*Card\s*\$\d+\.*\d*\s*EA": "",
    # 2.69 buy theirs get ours free*
    "((\d+)(\.\d+)?)\s*buy\s*theirs\s*get\s*ours\s*free\**": "",
    # 3.29 buy their get ours free* *When purchased in a single t
    "((\d+)(\.\d+)?)\s*buy\s*their\s*get\s*ours\s*free\**": "",
    # 0.99 25¢ MFR coupon in our app
    "((\d+)(\.\d\d)?)\s*\d\d\¢\s*MFR\s*coupon\s*in\s*our\s*app": "",
    # 11.99 $2 MFR coupon in our app** **Coupons from Sunday newspaper must be presented at time of purchase.
    "((\d+)(\.\d+)?)\s*\$*\d+\s*MFR\s*coupon\s*in\s*our\s*app\**": "",
    # 2.99 EA W/ MFR. DISCOUNT COUPON -2.00 OFF 1
    "((\d+)(\.\d+)?)\s*EA\s*W\/*\s*MFR\.*\s*DISCOUNT\s*COUPON\s*\-*\d+\.\d+\s*OFF\s*\d+": "",
    # 4.0 W/ MFR. DISCOUNT COUPON $2.00 OFF 2
    "((\d+)(\.\d+)?)\s*W\/*\s*MFR\.*\s*DISCOUNT\s*COUPON\s*\-*\$*\d+\.\d+\s*OFF\s*\d+": "",
    # 5.0 Get $5 off instantly when you buy $15 or more in participating General Mills Box Tops for Education Products*
    "((\d+)(\.\d+)?)\s*Get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*\$\d+\s*or\s*more\s*in\s*participating\s*General\s*Mills\s*Box\s*Tops\s*for\s*Education\s*Products\**": "",
    # 1.95 with $2 Smart Coupon
    "((\d+)(\.\d+)?)\s*with\s*\$\d+\s*Smart\s*Coupon": "",
    # 5.0 PRICE DROP
    "((\d+)(\.\d+)?)\s*PRICE\s*DROP": "",
    # 3.75 PRICE DROP!
    "((\d+)(\.\d+)?)\s*PRICE\s*DROP\s*\!*": "",
    # 10.0 SAVE MORE! OFF $2 with Smart Coupon
    "((\d+)(\.\d+)?)\s*SAVE\s*MORE\!*\s*OFF\s*\$\d+\s*with\s*Smart\s*Coupon": "",
    # 4.0 SAVE MORE! $2 OFF with Smart Coupon
    "((\d+)(\.\d+)?)\s*SAVE\s*MORE\s*\!*\s*\$\d+\s*OFF\s*with\s*Smart\s*Coupon": "",
    # $5 OFF YOUR OF $25 OF RITE AID BRAND
    "\$*\d+\s*OFF\s*YOUR\s*OF\s*\$*((\d+)(\.\d+)?)\s*OF\s*RITE\s*AID\s*BRAND": "",
    # SPEND $25 GET $5 ExtraBucks® Rewards
    # SPEND $30 GET $10 ExtraBucks® Rewards ExtraBucks
    "SPEND\s*\$*((\d+)(\.\d+)?)\s*GET\s*\$*\d+\s*ExtraBucks\®*\s*Rewards": "-1.0",
    # 3.99 Brands may vary by store.
    "((\d+)(\.\d+)?)\s*Brands": "",
    # 3.99 † Only available on in-store purchases.
    "((\d+)(\.\d+)?)\s*\†*\s*Only": "",
    # SALE: $3.39 to $6.79 EA. with Price Plus Card
    "SALE\:*\s*\$((\d+)(\.\d+)?)\s*to\s*\$*\d+\.*\d*\s*EA\.*\s*with\s*Price\s*Plus\s*Card": "",
    # 1.79 $2.00 Instant Coupon at coupon center Must be an ExtraCare
    "((\d+)(\.\d+)?)\s*\$\d+\.*\d*\s*Instant\s*Coupon\s*at\s*coupon\s*center\s*Must\s*be\s*an\s*ExtraCare": "",
    # 0.99 75¢ ExtraBucks® Rewards for next purchase ExtraBucks® Rewards offer
    "((\d+)(\.\d\d)?)\s*\d+\¢\s*ExtraBucks\®*\s*Rewards\s*for\s*next\s*purchase\s*ExtraBucks\®*\s*Rewards\s*offer": "",
    # 6.99 buy 2, get $4 OR buy 3, get $8 ExtraBucks® Rewards
    "((\d+)(\.\d\d)?)\s*buy\s*\d+\,*\s*get\s*\$*\d+\s*OR\s*buy\s*\d+\,*\s*get\s*\$*\d+\s*ExtraBucks\®*\s*Rewards": "",
    # Template.
    # "((\d+)(\.\d+)?)": "",

    ##################
    # Multibuy Items #
    ##################
    # 2 bags for 0.98
    "2\s*bags\s*for\s*((\d+)(\.\d+)?)": "div 2",
    # 2/ 7.0 buy theirs get ours free*
    "2\s*\/\s*((\d+)(\.\d+)?)\s*buy\s*theirs\s*get\s*ours\s*free\**": "div 2",
    # 2/ 8.0 Where Available While Supplies Last
    "2\s*\/\s*((\d+)(\.\d+)?)\s*Where\s*Available\s*While\s*Supplies\s*Last": "div 2",
    # 2/ 10.0 Participating Varieties and Sizes May Vary by Store
    "2\s*\/\s*((\d+)(\.\d+)?)\s*Participating\s*Varieties\s*and\s*Sizes\s*May\s*Vary\s*by\s*Store": "div 2",
    # 2/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "2\s*\/\s*((\d+)(\.\d+)?)\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend": "div 2",
    # 2 FOR 4.0 PRICE DROP
    "2\s*FOR\s*((\d+)(\.\d+)?)\s*PRICE\s*DROP": "div 2",
    # 2 FOR 5.0 EARN 2,000 IN PLENTI POINTS WORTH
    "2\s*FOR\s*((\d+)(\.\d+)?)\s*EARN\s*\d+\,*\d*\s*IN\s*PLENTI\s*POINTS\s*WORTH": "div 2",
    # 2/ 10.0 $5 ExtraBucks® Rewards when you spend $20
    "2\/\s*((\d+)(\.\d+)?)\s*\$*\d+\s*ExtraBucks\®*\s*Rewards\s*when\s*you\s*spend\s*\$*\d+": "div 2",
    # 2 FOR 3.0 OR $1.99 EA. WITH CARD
    "2\s*FOR\s*((\d+)(\.\d+)?)\s*OR\s*\$*\d+\.*\d*\s*EA\.*\s*WITH\s*CARD": "div 2",
    # MVP 2/ 6.0 - $1.00 OFF 2
    "MVP\s*2\/\s*((\d+)(\.\d+)?)\s*\-\s*\$*\d+\.*\d*\s*OFF\s*\d*": "div 2",
    # MVP 2/ 3.0 SAVE $2 INSTANTLY WHEN YOU BUY
    "MVP\s*2\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*INSTANTLY\s*WHEN\s*YOU\s*BUY": "div 2",
    # Sale Reg. 3.6 BUY 2 GET 1 50% OFF*
    "Sale\s*Reg\.*\s*((\d+)(\.\d+)?)\s*BUY\s*\d+\s*GET\s*\d+\s*\d*\%*\s*OFF": "",
    # 2/ 3.0 ◊Plus deposit where required.
    "2\/\s*((\d+)(\.\d+)?)\s*\◊*Plus\s*deposit\s*where\s*required\.*": "div 2",
    # 2/ 2.0 $2.00 instant coupon on 2 at coupon center
    "2\/\s*((\d+)(\.\d+)?)\s*\$*\d+\.*\d*\s*instant\s*coupon\s*on\s*\d+\s*at\s*coupon\s*center": "div 2",
    # 2/ 5.0 SAVE $5 when you spend $15 on participating products
    "2\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*spend\s*\$*\d+\s*on\s*participating\s*products": "div 2",
    # 2/ 6.0 SAVE $3 when you buy any 10 participating
    "2\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*buy\s*any\s*\d+\s*participating": "div 2",
    # 2/ 5.0 SPEND $20 GET $5 ExtraBucks® Rewards ◊Plus deposit where required.  ExtraBucks® Rewards offer limit of 1 per household with card. (20003615331)
    "2\/\s*((\d+)(\.\d+)?)\s*SPEND\s*\$*\d+\s*GET\s*\$*\d+\s*ExtraBucks\®*\s*Rewards\s*\◊*Plus\s*deposit\s*where\s*required": "div 2",
    # 2 FOR 4.0 Earn 100 Plenti points
    # 2 FOR 7.0 Earn 400 Plenti points
    # 2 FOR 5.0 Earn 100 Plenti points
    "2\s*for\s*((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$\d+\.*\d*\s*when\s*you\s*buy\s*\$*\d+\s*of\s*these\s*items": "div 2",
    "2\s*for\s*((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*when\s*you\s*buy\s*\$*\d+\s*of\s*these\s*items": "div 2",
    # 2 FOR 6.0 Earn 100 Plenti Worth $1.00 points
    "2\s*for\s*((\d+)(\.\d+)?)\s*Earn\s*\d*\s*Plenti\s*Worth": "div 2",
    # 2 FOR 6.0 (excludes Lay's Kettle)
    "2\s*for\s*((\d+)(\.\d+)?)\s*\(*\s*excludes": "div 2",
    # 2 FOR 7.0 PLUS! Earn 200 Plenti points* Worth $2.00 When you buy 2 of these items
    "2\s*for\s*((\d+)(\.\d+)?)\s*PLUS\!*\s*Earn\s*\d*\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*\s*When\s*you\s*buy": "div 2",
    # 3/ 6.0 $3.00 instant coupon on 3 Manufacturers coupon in most Sunday newspapers
    "3\/\s*((\d+)(\.\d+)?)\s*\$\d+\.*\d*\s*instant\s*coupon\s*on\s*\d+\s*Manufacturers\s*coupon\s*in\s*most\s*Sunday\s*newspapers": "div 3",
    # 3/ 10.0 ◊Plus deposit where required
    "3\/\s*((\d+)(\.\d+)?)\s*\◊*Plus\s*deposit\s*where\s*required\.*": "div 3",
    # 3/ 6.0 SAVE $5 when you spend $15 on participating products
    "3\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*spend\s*\$*\d+\s*on\s*participating\s*products": "div 3",
    # 4/ 5.0 Participating Varieties and Sizes May Vary by Store
    "4\/\s*((\d+)(\.\d+)?)\s*Participating\s*Varieties\s*and\s*Sizes\s*May\s*Vary\s*by\s*Store": "div 4",
    # 4/ 6.0 SAVE $5 when you spend $15 on participating products
    "4\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*spend\s*\$*\d+\s*on\s*participating\s*products": "div 4",
    # 4/ 5.0 SAVE $3 when you buy any 10 participating products
    "4\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*buy\s*any\s*\d+\s*participating\s*products": "div 4",
    # 4/ 11.0 Limit 2 offers per transaction.
    "4\/\s*((\d+)(\.\d+)?)\s*Limit\s*\d+\s*offers\s*per\s*transaction\.*": "div 4",
    # 4/ 10.0 *Other quantities
    "4\/\s*((\d+)(\.\d+)?)\s*\**Other\s*quantities": "div 4",
    # 4/ 10.0 *Other quantities 3/$10 Limit 2 offers per transaction
    "4\/\s*((\d+)(\.\d+)?)\s*\**Other\s*quantities\s*3\/\$*\d+\s*Limit\s*\d+\s*offers\s*per\s*transaction": "div 4",
    # 5/ 10.0 Where Available While Supplies Last *In a single transaction
    "5\/\s*((\d+)(\.\d+)?)\s*Where\s*Available\s*While\s*Supplies\s*Last\s*\**In\s*a\s*single\s*transaction": "div 5",
    # 5/ 10.0 *Other quantities 2/$6 Where Available While Supplies Last
    "5\/\s*((\d+)(\.\d+)?)\s*\**Other\s*quantities\s*\d+\/\$\d+\s*Where\s*Available\s*While\s*Supplies\s*Last": "div 5",
    # 5/ 11.0 *Other quantities $2.99/ea. 
    "5\/\s*((\d+)(\.\d+)?)\s*\**Other\s*quantities\s*\$*\d+\.*\d*\/*ea\.*": "div 5",
    # 10/ 10.0 SAVE $3 when you buy any 10 participating products
    "10\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*buy\s*any\s*\d+\s*participating\s*products": "div 10",
    # 10/ 10.0 SAVE $5 When you spend $15 on participating products
    "10\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*When\s*you\s*spend\s*\$*\d+\s*on\s*participating\s*products": "div 10",
    # 10 patties or links for $10
    "10\s*patties\s*or\s*links\s*for\s*\$((\d+)(\.\d+)?)": "div 10",
    # 2 FREE when you buy 10* *Other quantities 10/$10 Limit 2 offers per transaction
    "2\s*FREE\s*when\s*you\s*buy\s*10\**\s*\**Other\s*quantities\s*10\/\$*((\d+)(\.\d+)?)\s*Limit\s*\d+\s*offers\s*per\s*transaction": "div 12",
    # SALE 2 for 7.0 SAVE $5 on your next purchase when you
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d*\s*on\s*your\s*next\s*purchase\s*when\s*you": "div 2",
    # SALE 2 for 4.0 MIX & MATCH *
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)\s*MIX\s*\&*\s*MATCH\s*\**": "div 2",
    # SALE 4 for 4.0 SAVE $4 WHEN YOU BUY 4 Must purchase 4 to get discount price
    "SALE\s*4\s*for\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*WHEN\s*YOU\s*BUY\s*\d+\s*Must\s*purchase\s*\d+\s*to\s*get\s*discount\s*price": "div 4",
    # PICK 10 PAY ONLY 77¢ EA. with Price Plus Card
    "PICK\s*\d+\s*PAY\s*ONLY\s*((\d+)(\.\d+)?)\¢\s*EA\.*\s*with\s*Price\s*Plus\s*Card": "div 100",
    # 3 FOR $3 with Price Plus Card
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*with\s*Price\s*Plus\s*Card": "div 3",
    # 3 for $9 when you BUY 6 or more
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*\d+\s*or\s*more": "div 3",
    # 3 for $12 WHEN YOU BUY 3 LIMIT 3 TOTAL
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*\d+\s*LIMIT\s*\d+\s*TOTAL": "div 3",
    # 4 for $10 WHEN YOU BUY 4 with coupon on pg. 4 Limit 1 offer.
    "4\s*for\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*\d+\s*": "div 4",
    # 4/ 10.0 Plus Deposit Where Applicable
    "4\s*\/\s*((\d+)(\.\d+)?)\s*Plus\s*Deposit": "div 4",
    # 4 packages for $19.99 PLUS, many more in store
    "4\s*packages\s*for\s*\$*((\d+)(\.\d+)?)\s*PLUS\,*\s*many\s*more\s*in\s*store": "div 4",
    # 5 for $10 WHEN YOU BUY 5
    "5\s*for\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*\d+\s*": "div 5",
    # 5 for 10.0
    "5\s*for\s*((\d+)(\.\d+)?)": "div 5",
    # 5 for 10.0 2 DAYS ONLY! where available Must purchase
    "5\s*for\s*((\d+)(\.\d+)?)\s*2\s*DAYS\s*ONLY\!*\s*where\s*available\s*Must\s*purchase": "div 5",
    # When You Buy 2 FINAL COST 4.00 When you buy multiples of 2 in the same transaction with Card
    "When\s*You\s*Buy\s*2\s*FINAL\s*COST\s*((\d+)(\.\d+)?)\s*When\s*you\s*buy\s*multiples\s*of\s*2": "div 2",
    # When You Buy 2 FINAL COST 6.00 When you buy in multiples of 2
    "When\s*You\s*Buy\s*2\s*FINAL\s*COST\s*((\d+)(\.\d+)?)\s*When\s*you\s*buy\s*in\s*multiples\s*of\s*2": "div 2",
    # When You Buy 4 FINAL COST 8.0 When you buy 4
    "When\s*You\s*Buy\s*4\s*FINAL\s*COST\s*((\d+)(\.\d+)?)\s*When\s*you\s*buy\s*4": "div 4",
    # SAVE $1 On Little Debbie Zebra Cakes 7.38
    "SAVE\s*\$*\d+\s*On\s*Little\s*Debbie\s*Zebra\s*Cakes\s*((\d+)(\.\d+)?)": "",
    # Reg. 1.95 BUY 2, GET 1 FREE* *Offers With Like Items Cannot Be Combined Must purchase 3 to get discount price"
    "Reg\.*\s*((\d+)(\.\d+)?)\s*BUY\s*2\,*\s*GET\s*1\s*FREE": "mpy 2",
    # Reg. 4.0 BUY 1, GET 1 50% OFF* Equal or lesser value 2 Day Only! Must purchase 2 to get discount price
    "Reg\.*\s*((\d+)(\.\d+)?)\s*BUY\s*1\,*\s*GET\s*1": "",
    # sale 2 for 5.0 get $2 off instantly when you buy
    "sale\s*2\s*for\s*((\d+)(\.\d+)?)\s*get\s*\$*\d+\s*off\s*instantly\s*when\s*you\s*buy": "div 2",
    # 2 for $10 Plus deposit where required
    "2\s*for\s*\$*((\d+)(\.\d+)?)\s*Plus\s*deposit\s*where\s*required": "div 2",
    # 2 for $11 WHEN YOU BUY 2
    # 2 for $22.00 WHEN YOU BUY 2
    "2\s*for\s*\$*((\d+)(\.\d+)?)\s*WHEN\s*YOU\s*BUY\s*2": "div 2",
    # BUY 2 GET $8 ExtraBucks® Rewards
    "(BUY\s*\d+\s*GET\s*\$*\d+\s*ExtraBucks\®*\s*Rewards)": "-1.0",
    # 31.99 * buy one Mobil 1 Full Synthetic Oil 5 qt. jug and one Mobil 1 Oil Filter
    "((\d+)(\.\d+)?)\s*\**\s*buy\s*one\s*Mobil\s*\d+\s*Full\s*Synthetic\s*Oil\s*\d+\s*qt\.*\s*jug\s*and\s*one\s*Mobil\s*\d+\s*Oil\s*Filter": "",
    # 9.99 with card BONUS POINTS 2000=$2 reward when you buy 2††
    "((\d+)(\.\d+)?)\s*with\s*card\s*BONUS\s*POINTS\s*\d+\=\$\d+\s*reward\s*when\s*you\s*buy\s*\d+\†*": "",
    # 4.99 with card $1 off online coupon◊ BONUS POINTS 1000=$1 reward when you buy 2††
    "((\d+)(\.\d+)?)\s*with\s*card\s*\$\d+\s*off\s*online\s*coupon\◊*\s*BONUS\s*POINTS\s*\d+\=\$\d+\s*reward\s*when\s*you\s*buy\s*\d+\†*": "",
    # 3.99 SAVE $3 when you buy 3 participating Horizon products*
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*Horizon\s*products\**": "",
    # 3.89 /ea. Save $3 when you buy 2 Tribe Hummus*
    "((\d+)(\.\d+)?)\s*\/*ea\.*\s*Save\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*Tribe\s*Hummus\**": "",
    # 1.49 when you buy 5 participating products with your card. $1.00 off SAVE $5 when you buy 5 participating products*
    "((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*\d+\s*participating\s*products\s*with\s*your\s*card": "",
    # 1.49 when you buy any 5 participating products with your card. $1.00 Off SAVE $5 when you buy 5 participating products*
    # 1.49 when you buy any 5 participating products with your card. $1.00 Off. SAVE $5 when you buy 5 participating products*
    # 0.99 when you buy any 5 participating products with your card. $1.00 OFF SAVE $5 when you buy 5 participating products*
    # 1.49 when you buy any 5 participating products with your card -$1.00 off SAVE $5 when you buy 5 on participating products*
    # 1.49 when you buy any 5 participating products with your card - $1.00 off SAVE $5 when you buy 5 participating products*
    # 1.49 when you buy any 5 participating products with your card - $1.00 OFF. SAVE $5 when you buy 5 participating products*
    # 11.99 when you buy any 3 participating products with your card SAVE $15 WHEN YOU BUY ANY 3 PARTICIPATING PRODUCTS & SAVE $5 OFF EACH
    # 1.49 when you buy any 5 participating products with your card -$1.00 off SAVE $5 when you buy 5 participating products*
    # 1.49 when you buy any 5 participating products with your card - $1.00 off SAVE $5 When you buy 5 participating products*
    # 1.5 when you buy any 7 participating products with your card $1.00 Off SAVE $7 when you buy 7 participating products*
    # 1.49 when you buy any 5 participating products with your card. $1.00 off SAVE $5 when you buy 5 participating products*
    # 0.99 when you buy any 5 participating products with your card -$1.00 off SAVE $5 when you buy 5 participating products*
    # 0.99 when you buy any 5 participating products with your card. $1.00 OFF SAVE $5 when you buy 5 participating products*
    "((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*any\s*\d+\s*participating\s*products\s*with\s*your\s*card": "",
    # 1.5 /ea. WHEN YOU BUY 3 FINAL PRICE $1.00 WHEN YOU BUY 3 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*\/ea\.\s*WHEN\s*YOU\s*BUY\s*\d+\s*FINAL\s*PRICE\s*\$\d+\.\d+\s*WHEN\s*YOU\s*BUY\s*\d+\s*DIGITAL\s*COUPON": "",
    # 1.5 when you buy 3 -$1.00 WHEN YOU BUY 3 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*\d+\s*\-*\s*\$\d+\.\d+\s*WHEN\s*YOU\s*BUY\s*\d+\s*DIGITAL\s*COUPON": "",
    # 0.69 /ea. when you buy 5*
    "((\d+)(\.\d+)?)\s*\/ea\.\s*when\s*you\s*buy\s*\d+\*": "",
    # 7.99 FREE DASANI SPARKLING 8 Pack when you buy 2 Dasani Water 24 Packs or Powerade 8 Packs*
    "((\d+)(\.\d+)?)\s*FREE\s*DASANI\s*SPARKLING\s*\d+\s*Pack": "",
    # 8.0 FREE BABY CARROTS 2 lb. bag when you buy 2 Sabra Hummus or Guacamole Singles*
    "((\d+)(\.\d+)?)\s*FREE\s*BABY\s*CARROTS\s*\d+\s*lb\.*\s*bag\s*when\s*you\s*buy\s*\d+\s*Sabra\s*Hummus\s*or\s*Guacamole\s*Singles\**": "",
    # 10.0 when you buy 5* OR 6.0 when you buy 3
    "^\s*((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*\d+\**": "",
    # 2/ 6.0 SAVE $6 when you buy 6 participating products
    # 2/ 9.0 SAVE $4 when you buy 4 participating products
    # 2/ 8.0 SAVE $4 when you buy 4 participating products
    "^2\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products": "div 2",
    # 2/ 5.0 SAVE $10 INSTANTLY when you spend $30 on
    "2\/\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*INSTANTLY\s*when\s*you\s*spend\s*\$*\d+\s*on": "div 2",
    # 2/ 5.0 WOW Price Every Day
    "2\/\s*((\d+)(\.\d+)?)\s*WOW\s*Price\s*Every\s*Day": "div 2",
    # 2/ 6.0 HOT SALE W/O MVP Card $4.09 EA
    "2\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 2",
    # 3/ 3.0 WOW Price Every Day
    "3\/\s*((\d+)(\.\d+)?)\s*WOW\s*Price\s*Every\s*Day": "div 3",
    # 0.95 Ea. When You Buy 3
    "((\d+)(\.\d+)?)\s*Ea\.*\s*When\s*You\s*Buy\s*\d+": "",
    # 7.99 /lb. when you buy 3 pkgs. or more*
    "((\d+)(\.\d+)?)\s*\/*lb\.*\s*when\s*you\s*buy\s*\d+\s*pkgs\.*\s*or\s*more\**": "",
    # .99 /lb. when you buy 3 pkgs. or more*
    "\.(\d+)\s*\/*lb\.*\s*when\s*you\s*buy\s*\d+\s*pkgs\.*\s*or\s*more\**": "",
    # 10.79 ea WHEN YOU BUY ANY 6 With Card
    "((\d+)(\.\d+)?)\s*ea\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*With\s*Card": "",
    # 0.99 when you buy any 5 participating products with your card -$1.00 off SAVE $5 when you buy 5 participating products*
    # 1.0 when you buy any 7 participating products with your card - $1.00 off SAVE $7 When you buy 7 participating products*
    # 0.99 when you buy any 5 participating products with your card. $1.00 OFF SAVE $5 when you buy 5 participating products*
    "((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*any\s*\d+\s*participating\s*products\s*with\s*your\s*card": "",
    # 2.5 SAVE $4 when you buy 4 participating products*
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products\**": "",
    # 4.99 SAVE $4 when you buy 4 on participating products*
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*on\s*participating\s*products\**": "",
    # 3.99 /ea. SAVE $6 when you buy 6 participating products*
    "((\d+)(\.\d+)?)\s*\/*ea\.*\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products\**": "",
    # 2.29 ea WHEN YOU BUY 1 WITH CARD & DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*ea\s*WHEN\s*YOU\s*BUY\s*\d+\s*WITH\s*CARD\s*\&\s*DIGITAL\s*COUPON": "",
    # 7.99 Earn 300 Plenti points* Worth $3.00 when you buy 2 of these items. WITH CARD *Limit 2 offers per customer.
    # 7.99 Earn 300 Plenti points* Worth $3.00 when you buy 2 of these items. WITH CARD  *Limit 2 offers per customer."
    "((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$\d+\.*\d*\s*when\s*you\s*buy\s*\d+\s*of\s*these\s*items": "",
    # 16.99 Earn 200 Plenti points* Worth $2.00 WITH CARD
    "^((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$\d+\.*\d*": "",
    # 12.0 WHEN YOU BUY 2 WITH CARD & DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*WHEN\s*YOU\s*BUY\s*\d+\s*WITH\s*CARD\s*\&\s*DIGITAL\s*COUPON": "div 2",
    # 2 FOR 3.0 OR 1.99 EA. WITH CARD
    "2\s*FOR\s*\$*((\d+)(\.\d+)?)\s*OR\s*\d+\.*\d*\s*EA\.*\s*WITH\s*CARD": "div 2",
    # 2 FOR 8.0 (excludes PM)  OR 4.29 EA. WITH CARD
    "2\s*FOR\s*((\d+)(\.\d+)?)\s*\(excludes\s*PM\)\s*\s*OR\s*\d+\.*\d*\s*EA\.*\s*WITH\s*CARD": "div 2",
    # 2 FOR $22.00 with Price Plus Card
    "2\s*FOR\s*\$*((\d+)(\.\d+)?)\s*with\s*Price\s*Plus\s*Card": "div 2",
    # 2/ 4.0
    "2\s*\/\s*\$*((\d+)(\.\d+)?)": "div 2",
    # 2/ 4.0 Some Exclusions Apply
    "2\s*\/\s*\$*((\d+)(\.\d+)?)\s*Some\s*Exclusions\s*Apply": "div 2",
    # 2/ 4.0 Plus deposit or CRV where required
    "2\s*\/\s*\$*((\d+)(\.\d+)?)\s*Plus\s*deposit": "div 2",
    # 2/ 8.0 Excludes Gluten Free
    "2\s*\/\s*((\d+)(\.\d+)?)\s*Excludes\s*Gluten\s*Free": "div 2",
    # MVP 2/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*2\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 2",
    # 2 FOR 8.0
    "2\s*FOR\s*\$*((\d+)(\.\d+)?)": "div 2",
    # 2 FOR $7 Club Price
    "2\s*FOR\s*\$*((\d+)(\.\d+)?)\s*Club\s*Price": "div 2",
    # 2 FOR 10.0 Earn 500 Plenti points* Worth $5.00 When you buy $25 of these items. 
    "2\s*FOR\s*((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*": "div 2",
    # SALE 2 for 5.0 Must purchase 2 to get discount price  *Offers With Like Items Cannot Be Combined   †Prices not valid in the City of Philadelphia, PA Or Cook Country, IL"
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)\s*Must\s*purchase\s*2\s*to\s*get\s*discount\s*price": "div 2",
    # SALE 2 for 9.0 *Offers With Like Items Cannot Be Combined   Must purchase 2 to get discount price
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)\s*\**\s*Offers\s*With\s*Like\s*Items\s*Cannot\s*Be\s*Combined": "div 2",
    # SALE 2 for 3.0 SAVE $1 WHEN YOU BUY 2
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*WHEN\s*YOU\s*BUY\s*2": "div 2",
    # SALE 2 for 90.0
    "SALE\s*2\s*for\s*((\d+)(\.\d+)?)": "div 2",
    # SALE 3 for 6.0 Must purchase 3 to get discount price
    "SALE\s*3\s*FOR\s*((\d+)(\.\d+)?)\s*Must\s*purchase\s*3\s*to\s*get\s*discount\s*price": "div 3",
    # SALE 3 for 2.40
    "SALE\s*3\s*FOR\s*((\d+)(\.\d+)?)": "div 3",
    # 3 FOR 9.99 Must bring coupon to get advertised discount. 
    # 3 for $9 when you BUY 6 or more
    "3\s*FOR\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*d+\s*or\s*more": "div 3",
    # 3 for 3.0
    "3\s*FOR\s*\$*((\d+)(\.\d+)?)": "div 3",
    # 3 FOR 9.99 Must bring coupon to get advertised discount
    "3\s*FOR\s*\$*((\d+)(\.\d+)?)\s*Must\s*bring\s*coupon\s*to\s*get\s*advertised\s*discount": "div 3",
    # 3 for $3 Plus deposit where required
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*Plus\s*deposit\s*where\s*required": "div 3",
    # 3 for $9 WHEN YOU BUY 3 Limit 1 offer.
    # 3 for $9 WHEN YOU BUY 3 Limit 1 offer.
    # 3 for $12 WHEN YOU BUY 3 Limit 1 offer.
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*WHEN\s*YOU\s*BUY\s*3\s*Limit\s*1\s*offer\.*": "div 3",
    # 3 for $6.00 WHEN YOU BUY 3
    "3\s*for\s*\$*((\d+)(\.\d+)?)\s*WHEN\s*YOU\s*BUY\s*3": "div 3",
    # 3/ 9.0
    "3\s*\/\s*\$*((\d+)(\.\d+)?)": "div 3",
    # 3/ 6.0 *Other quantities 2/$5
    "3\s*\/\s*\$*((\d+)(\.\d+)?)\s*\**Other\s*quantities\s*\d+\s*\/\s*\$*\d+": "div 3",
    # 3/ 6.0 Plus Deposit Where Applicable
    "3\s*\/\s*\$*((\d+)(\.\d+)?)\s*Plus\s*Deposit\s*Where\s*Applicable": "div 3",
    # 3/ 5.0 SAVE $2 when you buy 4 participating products
    "3\s*\/\s*\$*((\d+)(\.\d+)?)\s*SAVE\s*\$*\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products": "div 3",
    # 3/ 9.0 - $6.00 when you buy 3 with coupon in most sunday papers
    "3\s*\/\s*\d+\.*\d*\s*\-\s*\$*((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*3\s*with\s*coupon": "div 3",
    # 3/ 6.0 $3 ExtraBucks® Rewards when you spend $12 on ANY of the products listed here
    "3\/\s*((\d+)(\.\d+)?)\s*\$*\d+\s*ExtraBucks\®*\s*Rewards\s*when\s*you\s*spend\s*\$*\d+\s*on\s*ANY\s*of\s*the\s*products\s*listed\s*here": "div 3",
    # MVP 3/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*3\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 3",
    # SALE 4 for 44.0 Must purchase 4 to get discount price
    "SALE\s*4\s*FOR\s*((\d+)(\.\d+)?)\s*Must\s*purchase\s*4\s*to\s*get\s*discount\s*price": "div 4",
    # 4 FOR 6.0 OR 1.79 EA. WITH CARD
    "4\s*FOR\s*((\d+)(\.\d+)?)\s*OR\s*\d+\.*\d*\s*EA\.*\s*WITH\s*CARD": "div 4",
    # 4 FOR 2.0 Earn 100 Plenti points* Worth $1.00 when you buy 4 of these items. OR 99¢ EA. WITH CARD *Limit 2 offers per customer.
    "4\s*FOR\s*((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*\s*when\s*you\s*buy\s*\d+\s*of\s*these\s*items": "div 4",
    # SALE 5 for 10.0 Must purchase 5 to get discount price  *Offers With Like Items Cannot Be Combined   ‡ Prices not valid in the City of Philadelphia, PA, or Cook Country, IL
    "SALE\s*5\s*for\s*((\d+)(\.\d+)?)\s*Must\s*purchase\s*5\s*to\s*get\s*discount\s*price": "div 5",
    # 4/ 12.0
    "4\s*\/\s*\$*((\d+)(\.\d+)?)": "div 4",
    # 4/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "4\s*\/\s*((\d+)(\.\d+)?)\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend": "div 4",
    # 4 for 12.0
    "4\s*for\s*\$*((\d+)(\.\d+)?)": "div 4",
    # 4 FOR $10.00 with Price Plus Card
    "4\s*for\s*\$*((\d+)(\.\d+)?)\s*with\s*Price\s*Plus\s*Card": "div 4",
    # 4/ 12.0 *Other quantities $5.99/ea. 
    "4\/\s*((\d+)(\.\d+)?)\s*\**Other\s*quantities": "div 4",
    # MVP 4/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*4\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 4",
    # 5.0 when you buy 5 $5.00 WHEN YOU BUY 5 DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*\d+\s*\$\d+\.\d+\s*WHEN\s*YOU\s*BUY\s*\d+\s*DIGITAL\s*COUPON": "div 5",
    # 5/ 55.0
    "5\s*\/\s*\$*((\d+)(\.\d+)?)": "div 5",
    # 5 FOR $5 with Price Plus Card
    "5\s*FOR\s*\$*((\d+)(\.\d+)?)\s*with\s*Price\s*Plus\s*Card": "div 5",
    # 5/ 10.0 FREE NATURE's PROMISE ORGANIC SALAD MIX when you spend
    "5\s*\/\s*\$*((\d+)(\.\d+)?)\s*FREE\s*NATURE\'s\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend": "div 5",
    # 5 for 55.0
    "5\s*for\s*\$*((\d+)(\.\d+)?)": "div 5",
    # 5/ 55.0 Plus Deposit Where Applicable
    "5\s*\/\s*((\d+)(\.\d+)?)\s*Plus\s*Deposit\s*Where\s*Applicable": "div 5",
    # MVP 5/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*5\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 5",
    # SALE 6 for 120.0 *Offers With Like Items Cannot Be Combined
    "SALE\s*6\s*for\s*((\d+)(\.\d+)?)\s*\**\s*Offers\s*With\s*Like\s*Items\s*Cannot\s*Be\s*Combined": "div 6",
    # 6/ 12.0
    "6\s*\/\s*\$*((\d+)(\.\d+)?)": "div 6",
    # 6 for 12.0
    "6\s*for\s*\$*((\d+)(\.\d+)?)": "div 6",
    # MVP 6/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*6\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 6",
    # 10 for 110.0
    "10\s*for\s*\$*((\d+)(\.\d+)?)": "div 10",
    # 10/ 100.0
    "10\s*\/\s*\$*((\d+)(\.\d+)?)": "div 10",
    # 10/ 10.0 Excludes Beef
    "10\s*\/\s*((\d+)(\.\d+)?)\s*Excludes\s*Beef": "div 10",
    # 10 patties/ 10.0
    "10\s*patties\s*\/\s*((\d+)(\.\d+)?)": "div 10",
    # MVP 10/ 4.0 HOT SALE W/O MVP Card $2.19 EA
    "MVP\s*10\s*\/\s*((\d+)(\.\d+)?)\s*HOT\s*SALE": "div 10",
    # MVP 10/ 10.0 W/O MVP Card $1.19 EA
    "MVP\s*10\s*\/\s*((\d+)(\.\d+)?)\s*W\/O\s*MVP\s*Card": "div 10",
    # 10/ 10.0 Low Price Every Day
    "10\s*\/\s*((\d+)(\.\d+)?)Low\s*Price\s*Every": "div 10",
    # 10/ 10.0 Plus Deposit Where Applicable
    "10\s*\/\s*((\d+)(\.\d+)?)\s*Plus\s*Deposit": "div 10",
    # 10 for 10.0
    "10\s*for\s*\$*((\d+)(\.\d+)?)": "div 10",
    # 20/ 10.0 Excludes Greek
    "20\s*\/\s*((\d+)(\.\d+)?)\s*Excludes\s*Greek": "div 20",
    # 20/ 10.0
    "20\s*\/\s*((\d+)(\.\d+)?)": "div 20",
    # 20 for 10.0
    "20\s*for\s*\$*((\d+)(\.\d+)?)": "div 20",
    # 13.99 10% off Wine Purchase of 4 or More Bottles 750 ml and/or 1.5 liter.
    "((\d+)(\.\d+)?)\s*\d+\%\s*off\s*Wine\s*Purchase\s*of\s*\d+\s*or\s*More\s*Bottles\s*\d+\s*ml\s*and\/or\s*\d+\.\d+\s*liter\.": "",
    # 10.0 10% off Wine Purchase of 4 or More Bottles 750 ml and/or 1.5 liter. Excludes clearance. Mix or match bottle sizes.
    "((\d+)(\.\d+)?)\s*\d+\%\s*off\s*Wine\s*Purchase\s*of\s*\d+\s*or\s*More\s*Bottles\s*\d+\s*ml\s*and\/or\s*\d+\.\d+\s*liter\.\s*Excludes\s*clearance\.\s*Mix\s*or\s*match\s*bottle\s*sizes\.": "",
    # 10.0 buy four Select General Mills Quaker or Kellogg's Products get one of equal or lesser value free*
    "((\d+)(\.\d+)?)\s*buy\s*four\s*Select\s*General\s*Mills": "",
    # 1.99 buy four Select General Mills Quaker or Kellogg's Items get one of equal or lesser value free*
    "((\d+)(\.\d+)?)\s*buy\s*four\s*Select\s*General\s*Mills": "",
    # 10.0 or $4.29 ea. with card
    "\d+\.\d+\s*or\s*\$((\d+)(\.\d+)?)\s*ea\.*\s*with\s*card": "",
    # 5.99 to $11.99 with card
    "((\d+)(\.\d+)?)\s*to\s*\$\d+\.\d+\s*with\s*card": "",
    # 0.99 ea WHEN YOU BUY 1 WITH CARD & DIGITAL COUPON
    "((\d+)(\.\d+)?)\s*ea\s*WHEN\s*YOU\s*BUY\s*\d+\s*WITH\s*CARD\s*\&\s*DIGITAL\s*COUPON": "",
    # 6.59 get $3 off instantly when you buy two* Limit one offer per transaction.
    "((\d+)(\.\d+)?)\s*get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*\**\s*Limit\s*one\s*offer\s*per\s*transaction\.*": "",
    # 15.99 get $5 off instantly when you buy two Select Bounty or Charmin Products*
    "((\d+)(\.\d+)?)\s*get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*Select\s*Bounty\s*or\s*Charmin\s*Products\**": "",
    # 3.99 with card REGISTER REWARDS® $6 OFF on next purchase when you buy 4**
    "((\d+)(\.\d+)?)\s*with\s*card\s*REGISTER\s*REWARDS\®\s*\$\d+\s*OFF\s*on\s*next\s*purchase\s*when\s*you\s*buy\s*\d+\**": "",
    # 5.0 BUY TWO Red Lobster Cheddar Bay Biscuit Mix & GET ONE FREE Food Lion Shredded Cheese
    "((\d+)(\.\d+)?)\s*BUY\s*TWO\s*Red\s*Lobster\s*Cheddar\s*Bay\s*Biscuit\s*Mix\s*\&\s*GET\s*ONE\s*FREE\s*Food\s*Lion\s*Shredded\s*Cheese": "",
    # 10.0 BUY TWO & GET 6 Pack .5 Liter Bottles select Varieties Propel Water
    "((\d+)(\.\d+)?)\s*BUY\s*TWO\s*\&\s*GET\s*6\s*Pack\s*\.5\s*Liter\s*Bottles\s*select\s*Varieties\s*Propel\s*Water": "",
    # Price Raw
    "(Price\s*Raw)": "-1.0",
    # $8.10 when you BUY 6 or more
    "\$*((\d+)(\.\d+)?)\s*when\s*you\s*BUY\s*\$*\d+": "",
    # SALE 3 for 12.75 Save 25¢ with DG DIGITAL COUPONS
    "SALE\s*3\s*for\s*((\d+)(\.\d+)?)\s*Save\s*\d+\¢\s*with\s*DG\s*DIGITAL\s*COUPONS": "div 3",
    # 3.0 Save -$1 DG DIGITAL COUPONS Excludes Hardest Working 
    "((\d+)(\.\d+)?)\s*Save\s*\-*\$*\d*\s*DG\s*DIGITAL\s*COUPONS": "",

    ########################
    # BUY ONE GET ONE FREE #
    ########################
    # BUY ONE GET ONE FREE*  EARN 2,000 IN PLENTI POINTS WORTH
    "(BUY\s*ONE\s*GET\s*ONE\s*FREE\**\s*EARN\s*\d+\,*\d*\s*IN\s*PLENTI\s*POINTS\s*WORTH)": "-1.0",
    # buy 1 get 1 free* with card
    # BUY 1 GET 1 FREE WITH CARD
    "(buy\s*\d+\s*get\s*\d+\s*free\**\s*with\s*card)": "-1.0",
    # BUY 1 GET 1* 50% OFF WITH CARD. SPEND $30 GET $10 ExtraBucks
    "(BUY\s*\d+\s*GET\s*\d+\**\s*\d+\%\s*OFF\s*WITH\s*CARD\.*\s*SPEND\s*\$*\d+\s*GET\s*\$*\d+\s*ExtraBucks)": "-1.0",
    # BUY 1 GET 1 FREE SAVE UP TO $3.99 WITH CARD
    "(BUY\s*1\s*GET\s*1\s*FREE\s*SAVE\s*UP\s*TO\s*\$\d+\.\d+\s*WITH\s*CARD)": "-1.0",
    # buy 1 get 1 free* with card + coupon savings online or in most Sunday papersΩ
    "(buy\s*\d+\s*get\s*\d+\s*free\**\s*with\s*card\s*\+*\s*coupon\s*savings\s*online\s*or\s*in\s*most\s*Sunday\s*papers\Ω*)": "-1.0",
    # FREE BUY ONE GET ONE
    "(FREE\s*BUY\s*ONE\s*GET\s*ONE)": "-1.0",
    # MVP 2.18 BUY TWO & GET ONE FREE DEL MONT
    "MVP\s*((\d+)(\.\d+)?)\s*BUY\s*TWO\s*\&\s*GET\s*": "",
    # Sale Reg. 2.0 BUY 1, GET 1 FREE* Equal or lesser
    "Sale\s*Reg\.*\s*((\d+)(\.\d+)?)\s*BUY\s*1\,*\s*GET\s*1\s*FREE\**": "",
    # MVP BUY ONE GET ONE FREE SINGLE ITEM HALF PRICE W/O MVP Card $7.99 ea
    "(MVP\s*BUY\s*ONE\s*GET\s*ONE\s*FREE\s*SINGLE\s*ITEM\s*HALF\s*PRICE\s*W/O\s*MVP\s*Card\s*\$*\d+\.*\d*\s*ea)": "-1.0",

    ##############
    # Half price #
    ##############
    # BUY ONE GET ONE 50% OFF  EARN 2,000 IN PLENTI POINTS* WORTH
    "(BUY\s*ONE\s*GET\s*ONE\s*\d+\%*\s*OFF\s*\s*EARN\s*\d+\,*\d*\s*IN\s*PLENTI\s*POINTS\**\s*WORTH)": "-1.0",
    # 4.49 50% off
    "((\d+)(\.\d+)?)\s*50\%\s*off": "",
    # BUY 1, GET 1 50% OFF* Equal or lesser value Must purchase 2 to get discount price
    "(BUY\s*1\,*\s*GET\s*1\s*50\%*\s*OFF\**\s*Equal\s*or\s*lesser\s*value\s*Must\s*purchase\s*\d+\s*to\s*get\s*discount\s*price)": "-1.0",
    # BUY 1, GET 1 50% OFF* Equal or lesser value Excludes multi-packs Must purchase 2 to get discount price
    "(BUY\s*1\,*\s*GET\s*1\s*50\%*\s*OFF\**\s*Equal\s*or\s*lesser\s*value\s*Excludes\s*multi-packs\s*)": "-1.0",
    # 1.0 - $12.00 BUY 1 GET 1 50% OFF*
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*BUY\s*\d+\s*GET\s*\d+\s*\d+\%\s*OFF\**": "",
    # 12.5 - $28.00 BUY 1 GET 1 50% OFF* Equal or lesser valuew
    "((\d+)(\.\d+)?)\s*\-\s*\$\d+\.\d+\s*BUY\s*\d+\s*GET\s*\d+\s*\d+\%\s*OFF\**\s*Equal\s*or\s*lesser\s*value": "",
    # 25.0 BUY 1 GET 1 50% OFF* Equal or lesser value
    "((\d+)(\.\d+)?)\s*BUY\s*\d+\s*GET\s*\d+\s*50\%\s*OFF\**\s*Equal\s*or\s*lesser\s*value": "",
    # buy 1 get 1 50% off*
    "(buy\s*\d+\s*get\s*\d+\s*50\%\s*off\**)": "-1.0",
    # buy 1 get 1 50% off* with card
    # Buy 1 get 1 50% % off* with card
    "(buy\s*\d+\s*get\s*\d+\s*50\%\s*\%*\s*off\**\s*with\s*card)": "-1.0",
    # buy 1 get 1 0.50% off* with card
    "(buy\s*\d+\s*get\s*\d+\s*0\.50\%\s*\%*\s*off\**\s*with\s*card)": "-1.0",
    # buy one get one 50% off of equal or lesser value
    # buy one get one 50% off* of equal or lesser value
    "(buy\s*one\s*get\s*one\s*\d+\%\s*off\**\s*of\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # buy one, get one 50%* off of equal or lesser value
    "(buy\s*one\,*\s*get\s*one\s*\d+\%\**\s*off\s*of\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # FREE BUY ONE GET ONE SINGLE ITEM HALF PRICE
    "(FREE\s*BUY\s*ONE\s*GET\s*ONE\s*SINGLE\s*ITEM\s*HALF\s*PRICE)": "-1.0",
    
    # BUY 1, GET 1* 50% OFF WITH CARD.
    "(BUY\s*1\,*\s*GET\s*1\**\s*50\%*\s*OFF\s*WITH\s*CARD\.*)": "-1.0",
    # BUY 1, GET 1* 50% OFF + SPEND $25, GET $8 ExtraBucks® Rewards
    "(BUY\s*\d+\,*\s*GET\s*\d+\**\s*\d+\%*\s*OFF\s*\+*\s*SPEND\s*\$*\d+\,*\s*GET\s*\$*\d+\s*ExtraBucks)": "-1.0",
    # Buy 1 Get 1* 50% WITH CARD
    "(BUY\s*1\,*\s*GET\s*1\**\s*50\%*\s*WITH\s*CARD)": "-1.0",
    # 2.99 Earn 100 Plenti points* Worth $1.00/ 1/2 PRICE WITH CARD  *Limit 2 offers per customer.
    "((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*\/*\s*1\/2\s*PRICE\s*WITH\s*CARD\s*\**Limit\s*\d+\s*offers\s*per\s*customer\.*": "",
    # 2.99 1/2 PRICE! WITH CARD  Selection may vary by store
    "((\d+)(\.\d+)?)\s*1\/2\s*PRICE\!*\s*WITH\s*CARD\s*Selection\s*may\s*vary\s*by\s*store": "",

    #############
    # No prices #
    #############
    # FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "(^\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend)": "-1.0",
    # 2 FREE when you buy 1
    "(^\s*2\s*FREE\s*when\s*you\s*buy\s*1)": "-1.0",
    # SAVE $3 when you spend $10 on participating Dove products* Only with your Stop & Shop card. *In a single transaction. Participating Varieties and Sizes May Vary by Store
    "(^\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*Dove\s*products\**)": "-1.0",
    # SAVE $1 When you buy any TWO Must buy two qualifying items to receive discount.
    "(^\s*SAVE\s*\$\d+\s*When\s*you\s*buy\s*any\s*TWO\s*Must\s*buy\s*two\s*qualifying\s*items\s*to\s*receive\s*discount\.*)": "-1.0",
    # Manufacturers coupon in most Sunday newspapers
    "(^\s*Manufacturers\s*coupon\s*in\s*most\s*Sunday\s*newspapers)": "-1.0",
    # save $10 on your next shopping trip when you buy 2
    "(^\s*save\s*\$*\d+\s*on\s*your\s*next\s*shopping\s*trip\s*when\s*you\s*buy\s*\d+)": "-1.0",
    # COMING SOON
    "(^\s*COMING\s*SOON)": "-1.0",
    # SAVE AT CHECKOUT $3.00 MUST BUY both To Receive Discount
    "(^\s*SAVE\s*AT\s*CHECKOUT\s*\$*\d+\.*\d*\s*MUST\s*BUY\s*both\s*To\s*Receive\s*Discount)": "-1.0",
    # buy five, get one of equal or lesser value free
    "(^\s*buy\s*five\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy two Libby's 100% Pure Pumpkin
    "(^\s*buy\s*two\s*Libby\'s\s*\d+\%\s*Pure\s*Pumpkin)": "-1.0",
    # save $10 via Custom Coupon at checkout
    "(^\s*save\s*\$*\d+\s*via\s*Custom\s*Coupon\s*at\s*checkout)": "-1.0",
    # buy three, get one of equal or lesser value free
    "(buy\s*three\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy one Softsoap Body Wash get one
    "(buy\s*one\s*Softsoap\s*Body\s*Wash\s*get\s*one)": "-1.0",
    # Mix & match any participating items
    "(Mix\s*\&\s*match\s*any\s*participating\s*items)": "-1.0",
    # BUY 2 Gatorade GET 5 PROPEL FREE
    "(BUY\s*\d+\s*Gatorade\s*GET\s*\d+\s*PROPEL\s*FREE)": "-1.0",
    # © 2017 by CVS/pharmacy®. Prices, promotions, styles and availability may vary by store
    "(^\s*\©\s*2017\s*by\s*CVS\/pharmacy\®\.*\s*Prices\,*\s*promotions\,*\s*styles\s*and\s*availability\s*may\s*vary\s*by\s*store)": "-1.0",
    # Available in select stores.
    "(^\s*Available\s*in\s*select\s*stores\.*)": "-1.0",
    # Exclusions apply. See store for details.
    "(^\s*Exclusions\s*apply\.*\s*See\s*store\s*for\s*details\.*)": "-1.0",
    # FREE KRAFT SHREDDED CHEESE 6.67-8 OZ. PKG
    "(^\s*FREE\s*KRAFT\s*SHREDDED\s*CHEESE)": "-1.0",
    # See description for details
    "(^\s*See\s*description\s*for\s*details)": "-1.0",
    # 3000 BONUS points = $3 reward†† when you spend $15 or more on participating
    "(^\s*\d+\s*BONUS\s*points\s*\=\s*\$*\d+\s*reward\†\†\s*when\s*you\s*spend\s*\$*\d+\s*or\s*more\s*on\s*participating)": "-1.0",
    # BONUS 3000 points when you spend $15 or more on participating
    "(^\s*BONUS\s*\d+\s*points\s*when\s*you\s*spend\s*\$*\d+\s*or\s*more\s*on\s*participating)": "-1.0",
    # BONUS POINTS 2000= $2 reward when you buy participating products
    "(^\s*BONUS\s*POINTS\s*2000\=\s*\$*\d+\s*reward\s*when\s*you\s*buy\s*participating\s*products)": "-1.0",
    # $8 REGISTER REWARDS® on next purchase when you spend $15 or more on participating products
    "(^\s*\$*\d+\s*REGISTER\s*REWARDS\®\s*on\s*next\s*purchase\s*when\s*you\s*spend\s*\$*\d+\s*or\s*more\s*on\s*participating\s*products)": "-1.0",
    # † Only available on-in store purchases.
    "(^\s*\†*\s*Only\s*available\s*on\-in\s*store\s*purchases\.*)": "-1.0",
    # See gift card for terms, conditions and applicable fees.
    "(^See\s*gift\s*card\s*for\s*terms\,*\s*conditions\s*and\s*applicable\s*fees\.*)": "-1.0",
    # WITH CARD
    "(WITH\s*CARD)": "-1.0",
    # buy three, get one free
    "(buy\s*three\,*\s*get\s*one\s*free)": "-1.0",
    # save $50 on your next shopping trip via Custom at checkout when you buy one of
    "(save\s*\$*\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*at\s*checkout\s*when\s*you\s*buy\s*one\s*of)": "-1.0",
    # Buy two, get two free
    "(Buy\s*two\,*\s*get\s*two\s*free)": "-1.0",
    # FREE INSTANTLY!, See description for details
    "(FREE\s*INSTANTLY\!*\,*\s*See\s*description\s*for\s*details)": "-1.0",
    # FREE* with purchase, See description for details
    "(FREE\**\s*with\s*purchase\,*\s*See\s*description\s*for\s*details)": "-1.0",
    # Support right from the start, made for your pregnancy journey.
    "(Support\s*right\s*from\s*the\s*start\,*\s*made\s*for\s*your\s*pregnancy\s*journey\.*)": "-1.0",
    # 50¢ off. Save $5 when you buy any 5 participating
    "(50\¢\s*off\.*\s*Save\s*\$*\d+\s*when\s*you\s*buy\s*any\s*\d+\s*participating)": "-1.0",
    # retailer: We will reimburse you the face value of this coupon
    "(retailer\:*\s*We\s*will\s*reimburse\s*you\s*the\s*face\s*value\s*of\s*this\s*coupon)": "-1.0",
    # Buy Any 2 Osem Cake 8.8 oz. get Bamba 1 oz. free
    "(Buy\s*Any\s*2\s*Osem\s*Cake\s*\d+\.*\d*\s*oz\.*\s*get\s*Bamba\s*\d+\s*oz\.*\s*free)": "-1.0",
    # $3 ExtraBucks® Rewards when you spend $10
    "(\$*\d+\s*ExtraBucks\®*\s*Rewards\s*when\s*you\s*spend\s*\$*\d+)": "-1.0",
    # $3 ExtraBucks® Rewards for next purchase
    "(\$*\d+\s*ExtraBucks\®*\s*Rewards\s*for\s*next\s*purchase)": "-1.0",
    # buy 2, get $6 OR buy 3, get $12 ExtraBucks® Rewards
    "(buy\s*\d+\,*\s*get\s*\$*\d+\s*OR\s*buy\s*\d+\,*\s*get\s*\$*\d+\s*ExtraBucks\®*\s*Rewards)": "-1.0",
    # 25% OFF  PLUS! Earn 2,000 Plenti points
    "(25\%\s*OFF\s*\s*PLUS\!*\s*Earn\s*\d+\,*\d*\s*Plenti\s*points)": "-1.0",
    # BUY ONE GET ONE 50% OFF  Earn 1,000 Plenti points
    "(BUY\s*ONE\s*GET\s*ONE\s*50\%\s*OFF\s*Earn\s*\d+\,*\d*\s*Plenti\s*points)": "-1.0",
    # BUY ONE GET ONE 50% OFF  PLUS! Earn 1,000 Plenti points
    "(BUY\s*ONE\s*GET\s*ONE\s*50\%\s*OFF\s*PLUS\!*\s*Earn\s*\d+\,*\d*\s*Plenti\s*points)": "-1.0",
    # BUY ONE GET ONE FREE*  !Earn 1,000 Plenti points
    "(BUY\s*ONE\s*GET\s*ONE\s*FREE\**\s*\!*\s*Earn\s*\d+\,*\d*\s*Plenti\s*points)": "-1.0",
    # BUT TWO GET THIRD ONE FREE!  Selection may
    "(BUT\s*TWO\s*GET\s*THIRD\s*ONE\s*FREE)": "-1.0",
    # © 2016 by CVS/pharmacy®. Not all advertised items available in all
    "(\©*\s*2016\s*by\s*CVS\/*pharmacy\®*\.*\s*Not\s*all\s*advertised\s*items\s*available\s*in\s*all)": "-1.0",
    # SPEND $15 GET $5 ExtraBucks® Rewards ExtraBucks®
    # SPEND $20 GET $10 ExtraBucks® Rewards ExtraBucks®
    "(SPEND\s*\$*\d+\s*GET\s*\$*\d+\s*ExtraBucks\®*\s*Rewards\s*ExtraBucks\®*)": "-1.0",
    # SPEND $20 GET $4 ExtraBucks Rewards WITH CARD
    "(SPEND\s*\$*\d+\s*GET\s*\$*\d+\s*ExtraBucks\s*Rewards\s*with\s*card)": "-1.0",
    # SPEND $10 $5 GET extrabucks® rewards
    "(SPEND\s*\$*\d+\s*\$*\d+\s*GET\s*ExtraBucks\®*\s*Rewards)": "-1.0",
    # Save 50¢ Manufacturer's Coupon Consumer
    "(Save\s*\d+\¢\s*Manufacturer's\s*Coupon\s*Consumer)": "-1.0",
    # SAVE $1 Instantly when you buy 4 in a single transaction
    "(SAVE\s*\$*\d+\s*Instantly\s*when\s*you\s*buy\s*\d*\s*in\s*a\s*single\s*transaction)": "-1.0",
    # SAVE $2.00 INSTANTLY on any
    "(^\s*SAVE\s*\$*\d+\.*\d*\s*Instantly\s*on\s*any)": "-1.0",
    # SAVE $1 Instantly on the purchase of
    "(^\s*SAVE\s*\$*\d+\.*\d*\s*Instantly\s*on\s*the\s*purchase\s*of)": "-1.0",
    # FREE!*, See description for details
    "(FREE\!*\**\,*\s*See\s*description\s*for\s*details)": "-1.0",
    # FREE! INSTANTLY, See description for details
    "(FREE\!*\s*INSTANTLY,\s*See\s*description\s*for\s*details)": "-1.0",
    # SAVE MORE! 25¢ OFF with Smart Coupon
    "(SAVE\s*MORE\!*\s*25\¢*\s*OFF\s*with\s*Smart\s*Coupon)": "-1.0",
    # FINAL PRICE $9.00 off when you buy any
    "(FINAL\s*PRICE\s*\$*\d+\.*\d*\s*off\s*when\s*you\s*buy\s*any)": "-1.0",
    # 40¢ off
    "((\d+)(\.\d+)?)\¢\s*off": "-1.0",
    # buy 1, get 1 of equal or lesser value
    "(buy\s*1\,*\s*get\s*1\s*of\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # buy 1, get 1 of free equal or lesser value
    "(buy\s*1\,*\s*get\s*1\s*of\s*free\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # 75¢ off
    "(\d+\¢*\s*off)": "-1.0",
    # See Circular Page for Price
    "(See\s*Circular\s*Page\s*for\s*Price)": "-1.0",
    # Purchase one at a time or all at once
    "(Purchase\s*one\s*at\s*a\s*time\s*or\s*all\s*at\s*once)": "-1.0",
    # $1 OFF INSTANTLY AT REGISTER
    "(\$*\d+\s*OFF\s*INSTANTLY\s*AT\s*REGISTER)": "-1.0",
    # $10 REGISTER REWARDS®  on next purchase when you buy 
    "(\$*\d+\s*REGISTER\s*REWARDS\®*\s*on\s*next\s*purchase\s*when\s*you\s*buy)": "-1.0",
    # BONUS POINTS 10,000 = $10 reward when you spend $50
    "(BONUS\s*POINTS\s*\d+\,*\d*\s*\=*\s*\$*\d*10\s*reward\s*when\s*you\s*spend)": "-1.0",
    # BUY 1 Kingsford or.. AND GET 1 Kingsford BBQ Sauce FREE w/CARD
    "(BUY\s*\d+\s*Kingsford\s*or\.*\s*AND\s*GET\s*\d+\s*Kingsford\s*BBQ\s*Sauce\s*FREE)": "-1.0",
    # FREE with Purchase
    "(FREE\s*with\s*Purchase)": "-1.0",
    # BUY 2... AND GET 1... FREE with Price Plus Card
    # BUY 3...AND GET 1...FREE with Price Plus Card
    "(BUY\s*\d*\.*\s*AND\s*GET\s*\d*\.*\s*FREE\s*with\s*Price\s*Plus\s*Card)": "-1.0",
    # FREE*, See description for details
    "(FREE\**\,*\s*See\s*description\s*for\s*details)": "-1.0",
    # save $4 WITH CARD
    # save $3.50 WITH CARD
    "(save\s*\$*\d+\.*\d*\s*WITH\s*CARD)": "-1.0",
    # SAVE $1.50 WITH COUPON
    "(SAVE\s*\$*\d+\.*\d*\s*WITH\s*COUPON)": "-1.0",
    # SAVE MORE! OFF $1 with Smart Coupon
    "(SAVE\s*MORE\!\s*OFF\s*\$\d+\s*with\s*Smart\s*Coupon)": "-1.0",
    # SAVE MORE! $2 OFF with Smart Coupon
    "(SAVE\s*MORE\!*\s*\$\d+\s*OFF\s*with\s*Smart\s*Coupon)": "-1.0",
    # additional $2 off coupon online or in store‡
    "(additional\s*\$\d+\s*off\s*coupon\s*online\s*or\s*in\s*store\‡*)": "-1.0",
    # GREAT LOW PRICE
    "(GREAT\s*LOW\s*PRICE)": "-1.0",
    # GREAT LOW PRICE with card
    "(GREAT\s*LOW\s*PRICE\s*with\s*card)": "-1.0",
    # Price Raw
    "(Price\s*Raw)": "-1.0",
    # Save 50¢
    "(Save\s*\d+\¢)": "-1.0",
    # SAVE $6 when you spend $20 on participating product*
    "(SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*product\**)": "-1.0",
    # SAVE $3 when you spend $10 on participating products*
    "(SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*products\**)": "-1.0",
    # 20¢ off SAVE $5 when you spend $15 on participating products*
    "(\d+\¢\s*off\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*products\**)": "-1.0",
    # 25¢ off SAVE $4 when you buy 4 participating products*
    # 25¢ off. SAVE $4 when you buy 4 participating products*
    "(25\¢\s*off\.*\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products\**)": "-1.0",
    # $1.00 off SAVE $4 when you buy 4 participating products* OR
    # $1.00 off. SAVE $4 when you buy 4 participating products*
    "($\d+\.*\d*\s*off\.*\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating)": "-1.0",
    # SAVE $5 WHEN YOU SPEND $20 ON ALL HEALTH & BEAUTY PRODUCTS
    "(SAVE\s*\$*\d+\s*WHEN\s*YOU\s*SPEND\s*\$*\d+\s*ON\s*ALL\s*HEALTH\s*\&*\s*BEAUTY\s*PRODUCTS)": "-1.0",
    # Save $1 OFF
    "(Save\s*\$\d+\s*OFF)": "-1.0",
    # $1.50 off
    "(\$\d+\.\d+\s*off)": "-1.0",
    # $3 off OR $3 off†
    "(\$*\d+\s*off\†*)": "-1.0",
    # $1 off◊
    "(\$*\d+\s*off\◊*)": "-1.0",
    # $2 off
    "(\$*\d+\s*off)": "-1.0",
    # 50¢ off
    "(\d+\¢\s*off)": "-1.0",
    # 50% off
    "(\d+\%\s*off)": "-1.0",
    # $2 off with card
    "(\$\d+\s*off\s*with\s*card)": "-1.0",
    # $1 OFF with caard
    "(\$\d+\s*OFF\s*with\s*caard)": "-1.0",
    # $2 OFF with card (with purchase of 2)
    "(\$\d+\s*OFF\s*with\s*card\s*\(with\s*purchase\s*of\s*\d+\))": "-1.0",
    # $1.50 OFF with card
    "(\$\d+\.\d+\s*OFF\s*with\s*card)": "-1.0",
    # $5 OFF with card Limit one coupon per customer per offer.
    "(\$*\d+\.*\d*\s*OFF\s*with\s*card\s*Limit\s*one\s*coupon\s*per\s*customer\s*per\s*offer)": "-1.0",
    # $1.50 OFF with card (with purchase of 2)
    "(\$\d+\.\d+\s*OFF\s*with\s*card\s*\(with\s*purchase\s*of\s*2\))": "-1.0",
    # $2 off with cards
    "(\$\d+\s*off\s*with\s*cards)": "-1.0",
    # 30-40% off
    "(\d+\-\d+\%\s*off)": "-1.0",
    # $5 off Automotive Dept. Purchase of $30 or More
    "(\$\d+\s*off\s*Automotive\s*Dept\.*\s*Purchase\s*of\s*\$\d+\s*or\s*More)": "-1.0",
    # 0.50 off. SAVE $5 when you spend $15 on participating products*
    "(\d+\.\d+\s*off\.*\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*products\**)": "-1.0",
    # 30¢ off. SAVE $5 when you spend $15 on participating products*
    "(\d+\¢\s*off\.*\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*on\s*participating\s*products\**)": "-1.0",
    # 30¢ off SAVE $5 when you spend $15 participating products*
    # 40¢ off. SAVE $5 when you spend $15 participating products*
    "(\d+\¢\s*off\.*\s*SAVE\s*\$\d+\s*when\s*you\s*spend\s*\$\d+\s*participating\s*products\**)": "-1.0",
    # $10.00 OFF when you buy 2
    "(\$\d+\.\d+\s*OFF\s*when\s*you\s*buy\s*\d+)": "-1.0",
    # BUY 1 GET 1 FREE Equal or lesser value • Must purchase 2 to get discount price
    "(\s*BUY\s*\d+\s*GET\s*\d+\s*FREE\s*Equal\s*or\s*lesser\s*value)": "-1.0",
    # buy one get one free
    # buy one, get one free
    "(\s*buy\s*one\,*\s*get\s*one\s*free)": "-1.0",
    # BUY ONE GET ONE FREE Single Item Half Price
    "(BUY\s*ONE\s*GET\s*ONE\s*FREE\s*Single\s*Item\s*Half\s*Price)": "-1.0",
    # buy one get one of equal or lesser value 25% off
    # buy one get one of equal or lesser value 50% off*
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*\d+\%\s*off\**)": "-1.0",
    # buy 1 get 1 free of equal or lesser value
    # buy 1 get 2 free of equal or lesser value
    # buy 2, get 1 free of equal or lesser value
    "(buy\s*\d+\s*\,*\s*get\s*\d+\s*free\s*of\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # buy 1, get 1 free of equal or lesser value MIX OR MATCH
    "(buy\s*d+\,*\s*get\s*\d+\s*free\s*of\s*equal\s*or\s*lesser\s*value\s*MIX\s*OR\s*MATCH)": "-1.0",
    # BONUS POINTS 2000=$2 reward when you buy pariticipating products††
    "(BONUS\s*POINTS\s*\d+\=\$\d+\s*reward\s*when\s*you\s*buy\s*pariticipating\s*products\†*)": "-1.0",
    # buy 1 get 1 50% off* with card + BONUS POINTS 5000 = $5 reward when you spend $20††
     "(buy\s*\d+\s*get\s*\d+\s*\d+\%\s*off\*\s*with\s*card\s*\+\s*BONUS\s*POINTS\s*\d+\s*\=\s*\$\d+\s*reward\s*when\s*you\s*spend\s*\$\d+\†*)": "-1.0",
    #  BUY 2 GET 1 FREE SAVE UP TO $19.44 WITH CARD
    "(BUY\s*\d+\s*GET\s*\d+\s*FREE\s*SAVE\s*UP\s*TO\s*\$\d+\.\d+\s*WITH\s*CARD)": "-1.0",
    # Buy 2 get 3rd FREE* hair care mix & match
    "(Buy\s*\d+\s*get\s*\d+rd\s*FREE\**\s*hair\s*care\s*mix\s*\&\s*match)": "-1.0",
    # buy 5 get 1 free buy of equal or lesser value
    "(buy\s*\d+\s*get\s*\d+\s*free\s*buy\s*of\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # buy one Febreze One Starter Kit 10.1 oz. get one Febreze One Refill free*
    "(buy\s*one\s*Febreze\s*One\s*Starter\s*Kit\s*\d+\.\d+\s*oz\.*\s*get\s*one\s*Febreze\s*One\s*Refill\s*free\**)": "-1.0",
    # buy one get one 50% off* of equal or lesser value offers cannot mix or match
    "(buy\s*one\s*get\s*one\s*\d+\%\s*off\**\s*of\s*equal\s*or\s*lesser\s*value\s*offers\s*cannot\s*mix\s*or\s*match)": "-1.0",
    # buy one get one get one of equal or lesser value 50% off
    "(buy\s*one\s*get\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*\d+\%\s*off)": "-1.0",
    # buy one get one of equal or lesser value 50% offers cannot mix or match off*
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*\d+\%\s*offers\s*cannot\s*mix\s*or\s*match\s*off\**)": "-1.0",
    # buy one get one of equal or lesser value 50% off* offers cannot mix or match off
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*\d+\%\s*off\**\s*offers\s*cannot\s*mix\s*or\s*match\s*off)": "-1.0",
    # buy one get one of equal or lesser value 50% off* offers cannot mix or match
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*\d+\%\s*off\**\s*offers\s*cannot\s*mix\s*or\s*match)": "-1.0",
    # buy one get one of equal or lesser value for $1
    # buy one, get one of equal or lesser value for $1
    "(buy\s*one\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*for\s*\$\d+)": "-1.0",
    # buy one, get one for $1 of equal or lesser value
    "(buy\s*one\,*\s*get\s*one\s*for\s*\$\d+\s*of\s*equal\s*or)": "-1.0",
    # buy one get one or equal or lesser value
    "(buy\s*one\s*get\s*one\s*or\s*equal\s*or\s*lesser\s*value)": "-1.0",
    # buy one get one of equal or lessor value 50% off*
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lessor\s*value\s*\d+\%\s*off\**)": "-1.0",
    # buy two Automotive Air Fresheners get one of equal or lesser value free*
    "(buy\s*two\s*Automotive\s*Air\s*Fresheners\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free\**)": "-1.0",
    # buy two get one of equal or lesser value free
    "(buy\s*two\s*\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy two, get one of equal or lesser free
    "(buy\s*two\s*\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*free)": "-1.0",
    # buy five, get five of equal or lesser value free
    "(buy\s*five\,*\s*get\s*five\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy two Pampers Super Pack Diapers get one Dreft Liquid Laundry Detergent 40-50 oz. free*
    "(buy\s*two\s*Pampers\s*Super\s*Pack\s*Diapers\s*get\s*one\s*Dreft\s*Liquid\s*Laundry\s*Detergent\s*\d+\-\d+\s*oz\.*\s*free\**)": "-1.0",
    # SAVE $2 INSTANTLY when you spend $10 on Lysol Disinfecting
    "(SAVE\s*\$*\d+\s*INSTANTLY\s*when\s*you\s*spend\s*\$*\d+)": "-1.0",
    # get $10 off instantly when you buy two Pennzoil Full Synthetic or High Mileage Full Synthetic Oil*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*Pennzoil\s*Full\s*Synthetic\s*or\s*High\s*Mileage\s*Full\s*Synthetic\s*Oil\**)": "-1.0",
    # get $10 off when you buy two Pennzoil Full Synthetic or instantly High Mileage Full Synthetic Oil*
    "(get\s*\$\d+\s*off\s*when\s*you\s*buy\s*two\s*Pennzoil\s*Full\s*Synthetic\s*or\s*instantly\s*High\s*Mileage\s*Full\s*Synthetic\s*Oil\**)": "-1.0",
    # get $1 off instantly when you buy two AXE Premium Deodorant*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*AXE\s*Premium\s*Deodorant\**)": "-1.0",
    # get $1 off instantly when you buy two Old Spice Products or Olay Bar Soap or Body Wash*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*Old\s*Spice\s*Products\s*or\s*Olay\s*Bar\s*Soap\s*or\s*Body\s*Wash\**)": "-1.0",
    # get $3 off instantly when you buy $10 of Dove Personal Care Products*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*\$\d+\s*of\s*Dove\s*Personal\s*Care\s*Products\**)": "-1.0",
    # get $3 off instantly when you buy $13
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*\$\d+)": "-1.0",
    # get $3 off instantly when you buy three
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*three)": "-1.0",
    # get $3 off instantly when you buy two Claritin Allergy Products*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*Claritin\s*Allergy\s*Products\**)": "-1.0",
    # get $3 off instantly when you Fram Air Cabin Air or Oil Filters*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you)": "-1.0",
    # get $3 off when you buy two instantly Pennzoil Conventional Oil*
    "(get\s*\$\d+\s*off\s*when\s*you\s*buy\s*two\s*instantly\s*Pennzoil\s*Conventional\s*Oil\**)": "-1.0",
    # get $4 off instantly when you buy $20 of Robitussin Centrum Emergen-C or Advil Sinus Congestion Products*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*\$\d+\s*of\s*Robitussin\s*Centrum\s*Emergen\-C\s*or\s*Advil\s*Sinus\s*Congestion\s*Products\**)": "-1.0",
    # get $5 off instantly when you buy one Gillette Razor System and one Refill*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*one\s*Gillette\s*Razor\s*System\s*and\s*one\s*Refill\**)": "-1.0",
    # get $5 off instantly when you buy two Pennzoil High Mileage Oil*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*Pennzoil\s*High\s*Mileage\s*Oil\**)": "-1.0",
    # get $5 off when you buy two instantly Pennzoil High Mileage Oil*
    "(get\s*\$\d+\s*off\s*when\s*you\s*buy\s*two\s*instantly\s*Pennzoil\s*High\s*Mileage\s*Oil\**)": "-1.0",
    # get $7 off instantly when you buy two AutoQuest Full Synthetic Oil*
    "(get\s*\$\d+\s*off\s*instantly\s*when\s*you\s*buy\s*two\s*AutoQuest\s*Full\s*Synthetic\s*Oil\**)": "-1.0",
    # save $10 on your next shopping trip via Custom Coupon at checkout when you buy two Enfamil 28-33.2 oz. Gerber 30.6-32 oz. or Similac Powder Formulas* 1.86-2 lbs.
    "(save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy\s*two\s*Enfamil\s*\d+\-\d+\.*\d+\s*oz\.*\s*Gerber\s*\d+\.\d+\-\d+\s*oz\.*\s*or\s*Similac\s*Powder\s*Formulas\**\s*\d+\.\d+\-\d+\s*lbs\.*)": "-1.0",
    # save $10 on your next shopping trip via Custom Coupon at checkout when you buy two Luvs Big Value or Stock-Up Packs*
    "(save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy\s*two\s*Luvs\s*Big\s*Value\s*or\s*Stock\-Up\s*Packs\**)": "-1.0",
    # save $1 on your next shopping trip via Custom Coupon at checkout when you buy ten Gerber Baby Food 2 pk./2.5-5 oz. or Organic Pouches*
    "(save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy\s*ten\s*Gerber\s*Baby\s*Food\s*\d+\s*pk\.\/\d+\.\d+\-\d+\s*oz\.*\s*or\s*Organic\s*Pouches\**)": "-1.0",
    # SAVE $5 For every $15 you spend on participating beauty items
    # SAVE $5 For every $15 you spend on participating beauty items.
    "(SAVE\s*\$\d+\s*For\s*every\s*\$\d+\s*you\s*spend\s*on\s*participating\s*beauty\s*items\.*)": "-1.0",
    # SAVE $5 when you buy 3 Hallmark cards*
    "(SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*Hallmark\s*cards\**)": "-1.0",
    # save $7 on your next shopping trip via Custom Coupon at checkout when you buy $30 or more of Huggies Diapers Wipes Pull-Ups or GoodNites Products*
    "(save\s*\$\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon)": "-1.0",
    # save $75 on your next shopping trip when you buy one iPad *While supplies last. No rainchecks or substitutions.
    "(save\s*\$*\d+\s*on\s*your\s*next\s*shopping\s*trip\s*when\s*you\s*buy\s*one)": "-1.0",
    # BUY 1 GET 1 25% OFF* Equal or lesser value
    "(BUY\s*1\s*GET\s*1\s*\d+\%\s*OFF\**\s*Equal\s*or\s*lesser\s*value)": "-1.0",
    # BUY 1 GET 1 OF EQUAL OR LESSER VALUE FREE
    # BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE
    "(BUY\s*\d+\,*\s*GET\s*\d+\s*OF\s*EQUAL\s*OR\s*LESSER\s*VALUE\s*FREE)": "-1.0",
    # BUY 1 GET 1 OF EQUAL OR LESSER VALUE FREE WITH CARD
     #BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE WITH CARD
    "(BUY\s*\d+\,*\s*GET\s*\d+\s*OF\s*EQUAL\s*OR\s*LESSER\s*VALUE\s*FREE\s*WITH\s*CARD)": "-1.0",
    # BUY 2 GET 1 FREE*
    "(\s*BUY\s*\d+\s*GET\s*\d+\s*FREE\**)": "-1.0",
    # BUY 2, GET 1 FREE*
    "(\s*BUY\s*\d+\,*\s*GET\s*\d+\s*FREE\**)": "-1.0",
    # buy one get one of equal or lesser value free
    # buy one, get one of equal or lesser value free
    "(buy\s*one\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy two, get one of equal or lesser value free
    "(buy\s*two\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": "-1.0",
    # buy one Xbox One 1TB Console get one free
    "(buy\s*one\s*Xbox\s*One\s*1TB\s*Console\s*get\s*one\s*free)": "-1.0",
    # 10% OFF* Gift Cards
    "(\d+\%\s*OFF\**\s*Gift\s*Cards)": "-1.0",
    # $1 off† buy 2 get 3rd FREE
    # $1 off† buy 2 get 3rd FREE§
    "(\$*\d+\s*off\†*\s*buy\s*\d+\s*get\s*\d+rd\s*FREE\§*)": "-1.0",
    # $1 Off◊ buy 2 get 3rd FREE§
    "(\$\d+\s*Off\◊*\s*buy\s*\d+\s*get\s*\d+rd\s*FREE\§*)": "-1.0",
    # $20 OFF your first online order plus 60 days FREE delivery.
    "(\$\d+\s*OFF\s*your\s*first\s*online\s*order\s*plus\s*\d+\s*days\s*FREE\s*delivery\.*)": "-1.0",
    # BONUS POINTS 5000 = $5 reward when you spend $10 or more on participating products††
    "(\s*BONUS\s*POINTS\s*\d+\s*\=\s*\$\d+\s*reward\s*when\s*you\s*spend\s*\$\d+\s*or\s*more\s*on\s*participating\s*products\†*)": "-1.0",
    # BONUS POINTS 5000 = $5 reward when you spend $20 or more on participating products†† $5 off online coupon◊
    "(\s*BONUS\s*POINTS\s*5000\s*\=\s*\$\d+5\s*reward\s*when\s*you\s*spend\s*\$\d+\s*or\s*more\s*on\s*participating\s*products\†*\s*\$\d+\s*off\s*online\s*coupon\◊*)": "-1.0",
    # BONUS POINTS =$5 reward when you $15 or more on participating products†† $2 off online coupon on 2◊
    "(\s*BONUS\s*POINTS\s*\=\$\d+\s*reward\s*when\s*you\s*\$\d+\s*or\s*more\s*on\s*participating\s*products\†*\s*\$*)": "-1.0",
    # BUY 1, GET 1 FREE WITH CARD
    "(BUY\s*\d+\,*\s*GET\s*\d+\s*FREE\s*WITH\s*CARD)": "-1.0",
    # SAVE 50% SHELF TAG REFLECTS SAVINGS WITH CARD
    "(SAVE\s*\d+\%\s*SHELF\s*TAG\s*REFLECTS\s*SAVINGS\s*WITH\s*CARD)": "-1.0",
    # SAVE $3 when you buy 3 participating Horizon products*
    "(SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*Horizon\s*products\**)": "-1.0",
    # 33% off, SAVE $5 when you buy 5 participating products
    "(\d+\%\s*off\,*\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+\s*participating\s*products)": "-1.0",
    # SAVE $2 when you buy 2
    "SAVE\s*\$((\d+)(\.\d+)?)\s*when\s*you\s*buy\s*\d+": "-1.0",
    # 1.5 SAVE $4 when you buy 4
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*when\s*you\s*buy\s*\d+": "",
    # 11.99 SAVE $10 INSTANTLY when you spend
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*INSTANTLY\s*when\s*you\s*spend": "",
    # 4.0 Save $2 with DG DIGITAL COUPONS
    "((\d+)(\.\d+)?)\s*SAVE\s*\$\d+\s*with\s*DG\s*DIGITAL\s*COUPONS": "",
    # FINAL PRICE 0.75 DIGITAL COUPON -25¢ Limit 1
    "FINAL\s*PRICE\s*((\d+)(\.\d+)?)\s*DIGITAL\s*COUPON\s*\-*\d+\¢*\s*Limit\s*\d+": "",
    # Earn 500 Plenti points* Worth $5.00 WITH CARD  
    "Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\d*\s*WITH\s*CARD": "-1.0",

    # BUY 1 GET 1
    "(BUY\s*1\s*GET\s*1)": "-1.0",

    # 1.00 off. SAVE $3 When You Buy 2 Participating Products
    # 1.00 off, SAVE $3 When You Buy 2 Participating Products
    # $1.00 off SAVE $3 When You Buy 2 Participating Products
    "(\$*\d+\.\d+\s*off\.*\,*\s*SAVE\s*\$\d+\s*When\s*You\s*Buy\s*\d+\s*Participating\s*Products)": "-1.0",
    # SAVE $4.00 ON 2 WITH COUPON
    "(SAVE\s*\$\d+\.*\d*\s*ON\s*\d+\s*WITH\s*COUPON)": "-1.0",

    ###########
    # 3 for 2 #
    ###########
    # BUY 2 GET 3rd FREE* WITH CARD
    "(BUY\s*\d+\s*GET\s*\d+rd\s*FREE\**\s*WITH\s*CARD)": "-1.0",
    # Buy 2 Get 1 free or Equal or lesser value
    "(\s*Buy\s*\d+\s*Get\s*\d+\s*free\s*or\s*Equal\s*or\s*lesser\s*value)": "-1.0",
    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§§
    "(buy\s*\d+\s*get\s*\d+rd\s*FREE\§*)": "-1.0",
    # buy 2 get 3rd FREE* * Card required for promotional pricing.
    "(buy\s*\d+\s*get\s*\d+rd\s*FREE\**)": "-1.0",
    # 1.95 BUY 2 GET 1 FREE*
    "((\d+)(\.\d+)?)\s*BUY\s*\d+\s*GET\s*\d+\s*FREE\**": "",
    # 5.0 BUY TWO Smart Balance & GET ONE FREE of Lender Bagels 17 Oz Select Varieties
    "((\d+)(\.\d+)?)\s*BUY\s*TWO\s*Smart\s*Balance\s*\&\s*GET\s*ONE\s*FREE\s*of\s*Lender\s*Bagels\s*\d+\s*Oz\s*Select\s*Varieties": "",
    # 2.99 FREE STOP & SHOP Grade A Large 12 ct. White or Brown Eggs when you buy 2*
    "((\d+)(\.\d+)?)\s*FREE\s*STOP\s*\&\s*SHOP\s*Grade\s*A\s*Large\s*\d+\s*ct\.*\s*White\s*or\s*Brown\s*Eggs\s*when\s*you\s*buy\s*d+\**": "",
    # 5.0 FREE Giant Grade A Large 12ct. White or Brown Eggs when you buy 2*
    "((\d+)(\.\d+)?)\s*FREE\s*Giant\s*Grade\s*A\s*Large\s*\d+ct\.*\s*White\s*or\s*Brown\s*Eggs\s*when\s*you\s*buy\s*\d+\**": "",
    # buy two get one free*
    "(\s*buy\s*two\s*get\s*one\s*free\**)": "-1.0",
    # buy two, get one free*
    "(\s*buy\s*two\,\s*get\s*one\s*free\**)": "-1.0",
    # Earn 100 Plenti points* Worth $1.00 When you buy 2 of these items.
    # Earn 800 Plenti points* Worth $8.00 When you buy $50 of these items.
    "(Earn\s*\d+\s*Plenti\s*points\**\s*worth\s*\$*\d+\.*\d*\s*when\s*you\s*buy)": "-1.0",
    # 16.99 Earn 200 Plenti points* Worth $2.00 WITH CARD
    "((\d+)(\.\d+)?)\s*Earn\s*\d+\s*Plenti\s*points\**\s*Worth\s*\$*\d+\.*\s*\s*WITH\s*CARD": "",
    # Earn 200 Plenti points* When you buy 2 of these items.
    "(Earn\s*\d+\s*Plenti\s*points\**\s*when\s*you\s*buy\s*\d+)": "-1.0",
    # BUY TWO GET THIRD FREE!
    "(BUY\s*TWO\s*GET\s*THIRD\s*FREE)": "-1.0",

    # Template.
    # "()": "-1.0",
}

# Promotion Type Categories.

BUY_ONE_GET_ONE_FREE = "BOGOF"
BUY_ONE_GET_ONE_HALF_PRICE = "BOGO50%"
BUY_TWO_GET_ONE_FREE = "B2G1F"
BUY_THREE_FOR_TWO = "3for2"
HALF_PRICE = "Half Price"
# Purchase 2 or more.
MULTIBUY = "Multibuy"

# Require to be a store loyalty member.
LOYALTY_CARD = "Loyalty Card"
# For dollar amount(s) off.
PRICE_REDUCTION = "Price Reduction"
# For percentage amounts off.
PERCENT_OFF = "% Off"

PROMOTION_MULTIBUY_PATTERNS = {
    # 2 bags for 0.98
    "(2\s*bags\s*for)": MULTIBUY,
    # get both for
    "(get\s*both\s*for)": MULTIBUY,
    # 0.99 /ea. when you buy 4*
    # 7.99 /lb. when you buy 3 pkgs. or more*
    "(when\s*you\s*buy\s*\d+)": MULTIBUY,
    # Sale Reg. 3.6 BUY 2 GET 1 50% OFF
    "(Sale\s*Reg\.*\s*\d+\.*\d*\s*BUY\s*2\s*GET\s*1\s*50\%*\s*OFF)": MULTIBUY,
    # buy 5 get 1 free buy of equal or lesser value
    "(get\s*1\s*free)": MULTIBUY,
    # buy 1 get 2 free of equal or lesser value
    "(buy\s*1\s*get\s*2\s*free)": MULTIBUY,
    # 1.0 each 10 for $10, mix or match 10,get the 11th free*
    "(\d+\s*for)": MULTIBUY,
    # $1.00 off SAVE $3 When You Buy 2 Participating Products
    "(buy\s*2)": MULTIBUY,
    # buy 5 & save $5 instantly
    "(buy\s*5)": MULTIBUY,
    # $5 OFF with card (with purchase of 2)
    "(with\s*purchase\s*of\s*d+)": MULTIBUY,
    # buy 1 get 2 free of equal or lesser value
    "(buy\s*1\s*get\s*\d+\s*free)": MULTIBUY,
    # 7.99 /lb. when you buy 3 pkgs. or more*
    # 0.99 /ea. when you buy 4*
    # 7.0 SAVE $5 when you buy 5 participating products*
    # buy 5 get 1 free buy of equal or lesser value
    "(buy\s*d+)": MULTIBUY,
    # 11.99 when you buy any 3 participating products
    # 3.99 SAVE $4 when you buy any 4 participating products
    "(buy\s*any\s*\d+)": MULTIBUY,
    # 12.99 10% off Wine Purchase of 4 or More Bottles 750 ml and/or 1.5 liter.
    "(of\s*4\s*or)": MULTIBUY,
    # 0.99 when you buy any 7 participating products with your card $1.00 Off SAVE $7 when you buy 7 participating products*
    "(when\s*you\s*buy\s*any\s*\d+)":MULTIBUY,
    # SAVE $4.00 ON 2 WITH COUPON
    "(ON\s*2)": MULTIBUY,
    # Buy two, get two free
    "(Buy\s*two\,*\s*get)": MULTIBUY,
    # 2 FREE when you buy 1
    "(2\s*FREE\s*when\s*you\s*buy\s*1)": MULTIBUY,
    # MVP 2/ 3.0
    "(MVP\s*\d+\/\s*\d+\.*\d*)": MULTIBUY,
    # 4.0 W/ MFR. DISCOUNT COUPON $2.00 OFF 2
    "(\$*\d+\.*\d*\s*OFF\s*2)": MULTIBUY,
    # buy three, get one free
    "(buy\s*three\,*\s*get)": MULTIBUY,
    # 3/ 9.0
    "(^\d+\s*\/\s*\d+)": MULTIBUY,
    # FINAL PRICE 3/ 9.0
    "(^FINAL\s*PRICE\s*\d+\s*\/\s*\d+)": MULTIBUY,
    # Must purchase 3 to get discount
    "(Must\s*purchase\s*\d+)": MULTIBUY,
    # 10 patties/ 10.0
    "(\d+\s*patties\s*\/\s*\d+)": MULTIBUY,
    # 10 patties or links for $10
    "(\d+\s*patties\s*or\s*links\s*for)": MULTIBUY,
    # buy one, get one for $1 of equal or lesser value 
    "(buy\s*one\,*\s*get\s*one\s*for\s*\$\d+)": MULTIBUY,
    # buy two Libby
    "(buy\s*two\s*Libby)": MULTIBUY,
    # buy five, get five of equal or lesser value free
    "(buy\s*five\,*\s*get\s*five\s*of\s*equal\s*or\s*lesser\s*value\s*free)": MULTIBUY,
    # BUY 3...AND GET 1...FREE with Price Plus Card
    "(BUY\s*3\.*AND\s*GET\s*1\.*FREE)": MULTIBUY,
    # buy five, get one of equal or lesser value free
    "(^\s*buy\s*five\,*\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*free)": MULTIBUY,
    # PICK 10 PAY ONLY 77¢ EA. with Price Plus Card
    "(PICK\s*\d+\s*PAY\s*ONLY)": MULTIBUY,
    # MVP 2/ 4.0 HOT SALE
    "(MVP\s*\d+\s*\/\s*\d+\.*\d*\s*HOT\s*SALE)": MULTIBUY,
    # MVP 10/ 10.0 W/O MVP Card $1.19 EA
    "(MVP\s*\d+\s*\/\s*\d+\.*\d*\s*W\/O\s*MVP)": MULTIBUY,
    # 4 packages for $19.99
    "(\d+\s*packages\s*for\s*\$*\d+\.*\d*)": MULTIBUY,

    # Exclusions
    # buy 2, get $4 OR buy 3, get $8 ExtraBucks® Rewards
    "(buy\s*\d+\,*\s*get\s*\$*\d+\s*OR\s*buy\s*\d+\,*\s*get\s*\$*\d+\s*ExtraBucks\®*\s*Rewards)": LOYALTY_CARD,

}

PROMOTION_LOYALTY_CARD_PATTERNS = {
    # Any raw Price string with the words to get loyalty card.
    "(with\s*card)": LOYALTY_CARD,
    "(with\s*your\s*card)": LOYALTY_CARD,
    # BONUS POINTS 5000 = $5 reward when you spend $10 or more on participating products††
    "(BONUS\s*POINT)": LOYALTY_CARD,
    # Earn 800 Plenti points* Worth $8.00 When you buy $50 of these items.
    "(Earn\s*\d+\s*Plenti\s*points)": LOYALTY_CARD,
    # MVP 1.79 W/O MVP Card Regular Retail
    "(MVP\s*Card)": LOYALTY_CARD,
    # Giant card
    "(Giant\s*card)": LOYALTY_CARD,
    # Price Plus Card
    "(Price\s*Plus\s*Card)": LOYALTY_CARD,
    # Stop & Shop card
    "(Stop\s*\&\s*Shop\s*card)": LOYALTY_CARD,
    # Stop and Shop card
    "(Stop\s*and\s*Shop\s*card)": LOYALTY_CARD,
    # club card
    "(club\s*card)": LOYALTY_CARD,
    # Club Price
    "(Club\s*Price)": LOYALTY_CARD,
    # Card Price
    "(Card\s*Price)": LOYALTY_CARD,
}

PROMOTION_BUY_ONE_GET_ONE_FREE_PATTERNS = {
    # BUY 1, GET 1 FREE WITH CARD
    "(BUY\s*1\,*\s*GET\s*1\s*FREE)": BUY_ONE_GET_ONE_FREE,
    # BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE WITH CARD
    # BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE
    "(BUY\s*1\,*\s*GET\s*1\s*OF)": BUY_ONE_GET_ONE_FREE,
    # buy one, get one of equal or lesser value free
    "(buy\s*one\,*\s*get\s*one\s*of)": BUY_ONE_GET_ONE_FREE,
    # MVP 3.29 BUY ONE & GET ONE FREE JIF OR JIF
    "(buy\s*one\s*\&*\s*get\s*one\s*free)": BUY_ONE_GET_ONE_FREE,
    # buy one Xbox One 1TB Console get one free
    "(buy\s*one\s*Xbox\s*One\s*1TB\s*Console\s*get\s*one\s*free)": BUY_ONE_GET_ONE_FREE,
    # buy one get one or equal or lesser value
    "(buy\s*one\s*get\s*one\s*or\s*equal\s*or\s*lesser\s*value)": BUY_ONE_GET_ONE_FREE,
    # BUY 1 GET 1
    "(^BUY\s*1\,*\s*GET\s*1$)": BUY_ONE_GET_ONE_FREE,
    # buy 1, get 1 of equal or lesser value
    "(^BUY\s*1\,*\s*GET\s*1\s*of\s*equal\s*or\s*lesser\s*value)": BUY_ONE_GET_ONE_FREE,
    # BUY 1 Kingsford or.. AND GET 1 Kingsford BBQ Sauce FREE
    "(BUY\s*1\s*Kingsford\s*or\.*\s*AND\s*GET\s*1\s*Kingsford\s*BBQ\s*Sauce\s*FREE)": BUY_ONE_GET_ONE_FREE,
    # When you Buy 1 Kibbles 'n Bits® Dog Food GET 1 FREE*
    "(When\s*you\s*Buy\s*1\s*Kibbles\s*\'n\s*Bits\®\s*Dog\s*Food\s*GET\s*1\s*FREE\**)": BUY_ONE_GET_ONE_FREE,
    # BUY 1 GET 1 FREE Equal or lesser value
    #"(BUY\s*1\s*GET\s*1\s*FREE\s*Equal\s*or\s*lesser\s*value)": BUY_ONE_GET_ONE_FREE,
    
}

PROMOTION_BUY_ONE_GET_ONE_HALF_PRICE_PATTERNS = {
    # 1.0 - $12.00 BUY 1 GET 1 50% OFF*
    # 12.5 - $28.00 BUY 1 GET 1 50% OFF* Equal or lesser valuew
    # 25.0 BUY 1 GET 1 50% OFF* Equal or lesser value
    "(BUY\s*1\,*\s*GET\s*1\s*50\%\s*OFF)": BUY_ONE_GET_ONE_HALF_PRICE,
    # buy 1 get 1 50% off*
    # buy 1 get 1 50% off* with card
    "(buy\s*1\,*\s*get\s*1\**\s*50\%\s*off)": BUY_ONE_GET_ONE_HALF_PRICE,
    # buy one get one 50% off of equal or lesser value
    # buy one get one 50% off* of equal or lesser value
    # buy one, get one 50%* off
    "(buy\s*one\,*\s*get\s*one\s*50\%\**\s*off)": BUY_ONE_GET_ONE_HALF_PRICE,
    # Buy 1 get 1 50% % off* with card
    "(Buy\s*1\,*\s*get\s*1\**\s*50\%\s*\%\s*off)": BUY_ONE_GET_ONE_HALF_PRICE,
    # buy 1 get 1 0.50% off* with card
    "(buy\s*1\,*\s*get\s*1\**\s*0.50\%\s*off)": BUY_ONE_GET_ONE_HALF_PRICE,
    # Buy 1 Get 1* 50% WITH CARD
    "(Buy\s*1\,*\s*Get\s*1\**\s*50\%\s*WITH\s*CARD)": BUY_ONE_GET_ONE_HALF_PRICE,
    # BUY ONE GET ONE FREE Single Item Half Price
    # BUY ONE GET ONE FREE SINGLE ITEM HALF PRICE
    "(BUY\s*ONE\,*\s*GET\s*ONE\s*FREE\s*Single\s*Item\s*Half\s*Price)": BUY_ONE_GET_ONE_HALF_PRICE,
    # buy one get one of equal or lessor value 50% off*
    # buy one get one of equal or lessor value 50% off*
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lessor\s*value\s*50\%\s*off\**)": BUY_ONE_GET_ONE_HALF_PRICE,
    
    # Buy one get one Of Equal Or Lesser value 50% off*
    "(buy\s*one\s*get\s*one\s*of\s*equal\s*or\s*lesser\s*value\s*50\%\s*off\**)": BUY_ONE_GET_ONE_HALF_PRICE,
    # Reg. 4.0 BUY 1, GET 1 50% OFF* Equal or lesser value,
    "(Reg\.*\s*\d+\.*\d*\s*BUY\s*1\,*\s*GET\s*1\s*50\%\s*OFF\**\s*Equal\s*or\s*lesser\s*value\,*)": BUY_ONE_GET_ONE_HALF_PRICE,

}

PROMOTION_HALF_PRICE_PATTERNS = {
    # SAVE 50% SHELF TAG REFLECTS SAVINGS WITH CARD
    "(SAVE\s*50\%)": HALF_PRICE,
    # BUY ONE GET ONE FREE Single Item Half Price
    "(Half\s*Price)": HALF_PRICE,
    # 4.49 50% off
    "(50\%\s*off)": HALF_PRICE,
    # 2.99 Earn 100 Plenti points* Worth $1.00/ 1/2 PRICE WITH CARD  *Limit 2 offers per customer.
    "(1\/2\s*PRICE)": HALF_PRICE,

    # Exclusion:
    # Sale Reg. 3.6 BUY 2 GET 1 50% OFF
    "(Sale\s*Reg\.*\s*\d+\.*\d*\s*BUY\s*2\s*GET\s*1\s*50\%*\s*OFF)": MULTIBUY, 
   
}

# For dollar amount(s) off.
PROMOTION_PRICE_REDUCTION_PATTERNS = {
    # 4.0 SAVE MORE! $2 OFF with Smart Coupon
    "(Coupon)": PRICE_REDUCTION,
    # $1.00 off
    # 1.00 off, SAVE $3 When You Buy 2 Participating Products
    "(\$*\d+\.*\d*\s*off)": PRICE_REDUCTION,
    # 40¢ off
    "(\d+\¢\s*off)": PRICE_REDUCTION,
    # 3.89 /ea. Save $3 when you buy 2 Tribe Hummus*    
    "(Save\s*\$\d+)": PRICE_REDUCTION,
    # SAVE MORE! OFF $1 with Smart Coupon
    "(OFF\s*\$\d+)": PRICE_REDUCTION,
    # 3.75 PRICE DROP!
    "(PRICE\s*DROP)": PRICE_REDUCTION,
    # 2.69 buy theirs get ours free*
    "(get\s*ours\s*free)": PRICE_REDUCTION,
}

# For percentage amounts off.
PROMOTION_PERCENT_OFF_PATTERNS = {
    # 1.59 Per Lb. SAVE 15%
    "(SAVE\s*\d+\%)": PERCENT_OFF,
    # 33% OFF
    "(\d+\%\s*OFF)": PERCENT_OFF,
    # BUY 1 GET 1 25% OFF
    "(BUY\s*1\s*GET\s*\d+\%\s*OFF)": PERCENT_OFF,

}

PROMOTION_BUY_TWO_GET_ONE_FREE_PATTERNS = {
    # BUY 2... AND GET 1... FREE with Price Plus Card
    "(BUY\s*2\.*\s*AND\s*GET\s*1\.*\s*FREE\s*with\s*Price\s*Plus\s*Card)": BUY_TWO_GET_ONE_FREE,
    # Buy 2 Get 1 free or Equal or lesser value
    # buy 2, get 1 free of equal or lesser value
    "(Buy\s*2\,*\s*Get\s*1)": BUY_TWO_GET_ONE_FREE,
    # buy two get one free OR buy two get one free*
    # buy two, get one of equal or lesser value free
    "(buy\s*two\,*\s*get\s*one)": BUY_TWO_GET_ONE_FREE,
    # 5.0 BUY TWO Smart Balance & GET ONE FREE of Lender Bagels 17 Oz Select Varieties
    "(BUY\s*TWO\s*Smart\s*Balance\s*\&\s*GET\s*ONE\s*FREE)": BUY_TWO_GET_ONE_FREE,
    # MVP 2.18 BUY TWO & GET ONE FREE DEL M
    "(BUY\s*TWO\s*\&\s*GET\s*ONE\s*FREE)": BUY_TWO_GET_ONE_FREE,

    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§§
    "(buy\s*2\s*get\s*3rd)": BUY_TWO_GET_ONE_FREE,
    # BUY TWO GET THIRD FREE!
    "(BUY\s*TWO\s*GET\s*THIRD\s*FREE)": BUY_TWO_GET_ONE_FREE,
    # BUT TWO GET THIRD ONE FREE!  Selection may
    "(BUT\s*TWO\s*GET\s*THIRD\s*ONE\s*FREE)": BUY_TWO_GET_ONE_FREE,
    

    # TODO: Need a smarter pattern match for...
    # 5.0 BUY TWO Smart Balance & GET ONE FREE of Lender Bagels 17 Oz Select Varieties
    # 2.99 FREE STOP & SHOP Grade A Large 12 ct. White or Brown Eggs when you buy 2*
    # 5.0 FREE Giant Grade A Large 12ct. White or Brown Eggs when you buy 2*
}

PROMOTION_BUY_THREE_FOR_TWO_PATTERNS = {

}


# Consider the promotional patterns in the priority order.
# Highest priority first.
PROMOTION_PRIORITY_PATTERNS = [
    PROMOTION_BUY_ONE_GET_ONE_HALF_PRICE_PATTERNS,
    PROMOTION_BUY_ONE_GET_ONE_FREE_PATTERNS,
    PROMOTION_HALF_PRICE_PATTERNS,
    PROMOTION_BUY_TWO_GET_ONE_FREE_PATTERNS,
    PROMOTION_BUY_THREE_FOR_TWO_PATTERNS,
    PROMOTION_MULTIBUY_PATTERNS,
    PROMOTION_PERCENT_OFF_PATTERNS,
    PROMOTION_LOYALTY_CARD_PATTERNS,
    PROMOTION_PRICE_REDUCTION_PATTERNS,
]

MULTIBUY_PATTERNS = {

    #########
    # BOGOF #
    #########
    # buy 1 get 1 50% off* with card
    "(buy\s*1\,*\s*get\s*1\s*50)": "",
    # BUY 1, GET 1 FREE WITH CARD
    "(buy\s*1\,*\s*get\s*1)": "",
    # BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE WITH CARD
    # BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE
    "(BUY\s*1\,*\s*GET\s*1\s*OF)": "",
    # BUY ONE GET ONE FREE SINGLE
    "(BUY\s*ONE\s*GET\s*ONE\s*FREE)": "",
    # buy one, get one of equal or lesser value free
    "(buy\s*one\,*\s*get\s*one\s*of)": "",
    # FREE BUY ONE GET ONE
    "(FREE\s*BUY\s*ONE\s*GET\s*ONE)": "",
    # BUY 1, GET 1 FREE* Equal or lesser value Must purchase 2 to get discount price
    "(BUY\s*1\,*\s*GET\s*1\s*FREE\**\s*Equal\s*or\s*lesser\s*value\s*Must\s*purchase\s*\d+\s*to\s*get\s*discount\s*price)": "",
    # When you Buy 1 Kibbles 'n Bits® Dog Food GET 1 FREE*
    "(When\s*you\s*Buy\s*1\s*Kibbles\s*\'n\s*Bits\®\s*Dog\s*Food\s*GET\s*1\s*FREE\**)": "",
    # Reg. 4.0 BUY 1, GET 1 50% OFF* Equal or lesser value,
    "(Reg\.*\s*\d+\.*\d*\s*BUY\s*1\,*\s*GET\s*1\s*50\%\s*OFF\**\s*Equal\s*or\s*lesser\s*value\,*)": "",
    # BUY 1 GET 1 FREE Equal or lesser value
    "(BUY\s*1\s*GET\s*1\s*FREE\s*Equal\s*or\s*lesser\s*value)": "",

    ###########
    # 3 FOR 2 #
    ###########
    # BUY 2... AND GET 1... FREE with Price Plus Card
    "(BUY\s*2\.*\s*AND\s*GET\s*1\.*)": 3,
    # Buy 2 Get 1 free or Equal or lesser value
    # buy 2, get 1 free of equal or lesser value
    "(Buy\s*2\,*\s*Get\s*1)": 3,
    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§
    # buy 2 get 3rd FREE§§
    "(buy\s*2\s*get\s*3rd)": 3,
    # buy two get one free OR buy two get one free*
    # buy two, get one of equal or lesser value free
    "(buy\s*two\,*\s*get\s*one)": 3,
    # 5.0 BUY TWO Smart Balance & GET ONE FREE of Lender Bagels 17 Oz Select Varieties
    "(BUY\s*TWO\s*Smart\s*Balance\s*\&\s*GET\s*ONE\s*FREE)": 3,
    # BUY TWO GET THIRD FREE!
    "(BUY\s*TWO\s*GET\s*THIRD\s*FREE)": 3,
    # MVP 2.18 BUY TWO & GET ONE FREE DEL
    "(BUY\s*TWO\s*\&\s*GET\s*ONE\s*FREE)": 3,

    #############
    # Multi Buy #
    #############
    # 2 bags for 0.98
    "(2\s*bags\s*for)": 2,
    # get both for 7.0
    "(get\s*both\s*for)": 2,
    # Must purchase 2 to get discount
    "(Must\s*purchase\s*2\s*to\s*get\s*discount)": 2,
    # $1.00 off SAVE $3 When You Buy 2 Participating Products
    "(buy\s*2)": 2,
    # Buy two, get two free
    "(buy\s*two)": 2,
    # 2/ 4.0
    "(^\s*2\s*\/\s*)": 2,
    # MVP 2/ 3.0 
    "(^\s*MVP\s*2\s*\/\s*)": 2,
    # 2/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "(^\s*2\s*\/\s*\d+\.*\d*\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend)": 2,
    # SAVE $4.00 ON 2 WITH COUPON
    "(on\s*2)": 2,
    # 2 FOR 10.0 Earn 500 Plenti points* Worth $5.00 When you buy $25 of these items. 
    "(2\s*for)": 2,
    # 2/ 2.0 $2.00 instant coupon
    "(2\/\s*\d+\.*\d*\s*\$*\d+\.*\d*\s*instant\s*coupon)": 2,
    # $5 OFF with card (with purchase of 2)
    "(with\s*purchase\s*of\s*2)": 2,
    # 4.0 W/ MFR. DISCOUNT COUPON $2.00 OFF 2
    "(OFF\s*2)": 2,
    # buy one, get one for $1 of equal or lesser value 
    "(buy\s*one\,*\s*get\s*one\s*for\s*\$\d+)": 2,
    # 2 FREE when you buy 1
    "(2\s*FREE\s*when\s*you\s*buy\s*1)": 3,
    # 3 FOR 9.99 Must bring coupon to get advertised discount. 
    "(3\s*for)": 3,
    # buy 1 get 2 free of equal or lesser value
    "(buy\s*1\s*get\s*2\s*free)": 3,
    # 3/ 33.0
    "(3\s*\/\s*)": 3,
    # 3/ 6.0 *Other quantities 2/$5
    "(3\s*\/\s*\d+\.*\d*\s*\**Other\s*quantities\s*\d+\s*\/\s*\$\d+)": 3,
    # buy three, get one free
    "(buy\s*three\,*\s*get)": 3,
    # 3/ 6.0 $3.00 instant coupon
    "(3\s*\/\s*\d+\.*\d*\s*\$*\d+\.*\d+\s*instant\s*coupon)": 3,
    # 7.99 /lb. when you buy 3 pkgs. or more*
    "(buy\s*3)": 3,
    # 11.99 when you buy any 3 participating products
    "(buy\s*any\s*3)": 3,
    # Must purchase 3 to get discount
    "(Must\s*purchase\s*3\s*to\s*get\s*discount)": 3,
    # BUY 3...AND GET 1...FREE
    "(BUY\s*3\.*\s*AND\s*GET\s*1\.*\s*FREE)": 4,
    # 4/ 4.0
    "(^\s*4\s*\/\s*)": 4,
    # MVP 4/ 12.0
    "(^\s*MVP\s*4\s*\/\s*)": 4,
    # 4/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend
    "(4\s*\/\s*\d+\.*\d*\s*FREE\s*NATURE\'S\s*PROMISE\s*ORGANIC\s*SALAD\s*MIX\s*when\s*you\s*spend)": 4,
    # 4 FOR 6.0 OR 1.79 EA. WITH CARD
    # 4 FOR 2.0 Earn 100 Plenti points* Worth $1.00 when you buy 4 of these items. OR 99¢ EA. WITH CARD *Limit 2 offers per customer.
    "(4\s*for)": 4,
    # 0.99 /ea. when you buy 4*
    "(buy\s*4)": 4,
    # 3.99 SAVE $4 when you buy any 4 participating products
    "(buy\s*any\s*4)": 4,
    # 12.99 10% off Wine Purchase of 4 or More Bottles 750 ml and/or 1.5 liter.
    "(of\s*4\s*or)": 4,
    # 4 packages for $19.99 PLUS, many more in store
    "(4\s*packages\s*for\s*\$*\d+\.*\d*)": 4,
    # 4/ 10.0 *Other quantities 3/$10 Limit 2 offers per transaction.
    "(4\/\s*\d+\.*\d*\s*\**Other\s*quantities\s*\d+\/\$*\d+\s*Limit\s*\d+\s*offers\s*per\s*transaction\.*)": 4,
    # 5/ 55.0
    "(^\s*5\s*\/\s*)": 5,
    # 5/ 10.0 *Other quantities
    "(5\s*\/\s*\d+\.*\d*\s*\**Other\s*quantities)": 5,
    # 5/ 10.0 *Other quantities 2/$6 Where Available While Supplies Last
    "(5\s*\/\s*\d+\.*\d*\s*\**Other\s*quantities\s*\d+\/\$\d+\s*Where\s*Available\s*While\s*Supplies\s*Last)": 5,
    # 7.0 SAVE $5 when you buy 5 participating products*
    "(buy\s*5)": 5,
    "(buy\s*any\s*5)": 5,
    # SALE 5 for 10.0 Must purchase 5 to get discount price
    "(5\s*for)": 5,
    # buy five, get five of equal or lesser value free
    "(buy\s*five)": 5,
    # MVP 5/ 5.0 HOT SALE
    "(MVP\s*5\/\s*\d+\.*\d*\s*HOT\s*SALE)": 5,
    # 6/ 33.0
    "(6\s*\/\s*)": 6,
    # buy 5 get 1 free buy of equal or lesser value
    "(buy\s*6)": 6,
    "(buy\s*any\s*6)": 6,
    "(buy\s*5\s*get\s*1)": 6,
    # when you BUY 6 or more
    "(when\s*you\s*BUY\s*6\s*or\s*more)": 6,
    # SALE 6 for 120.0 *Offers With Like Items Cannot Be Combined
    "(6\s*for)": 6,
    # 0.99 when you buy any 7 participating products with your card $1.00 Off SAVE $7 when you buy 7 participating products*
    "(buy\s*7)": 7,
    "(buy\s*any\s*7)": 7,
    "(when\s*you\s*buy\s*any\s*7)": 7,
    "(buy\s*8)": 8,
    "(buy\s*any\s*8)": 8,
    "(when\s*you\s*buy\s*any\s*8)": 8,
    # 1.0 each 10 for $10, mix or match 10,get the 11th free*
    "(^\s*\d+\.*\d*\s*each\s*10\s*for)": 10,
    "(^\s*10\s*for)": 10,
    # 10/ 30.0
    "(^\s*10\s*\/\s*)": 10,
    # MVP 10/ 30.0
    "(^\s*MVP\s*10\s*\/\s*)": 10,
    # 10 patties/ 10.0
    "(^\s*10\s*patties\s*\/)": 10,
    # 10 patties or links for $10
    "(^\s*10\s*patties\s*or\s*links\s*for)": 10,
    # PICK 10 PAY ONLY 77¢ EA. with Price Plus Card
    "(PICK\s*10\s*PAY\s*ONLY)": 10,
    # 2 FREE when you buy 10* *Other quantities 10/$10
    "(2\s*FREE\s*when\s*you\s*buy\s*10\**\s*\**Other\s*quantities)": 12,
    # 20/ 10.0 Excludes Greek
    "(20\s*\/\s*)": 20,

    # Exclusions:
    # 1.77 *Other quantities 2/$5
    "(\d+\.*\d*\s*\**Other\s*quantities\s*\d+\/\$\d+)": "",
    # Purchase one at a time or all at once
    "(Purchase\s*one\s*at\s*a\s*time\s*or\s*all\s*at\s*once)": "",
    # Offer valid 9/3/17
    "(Offer\s*valid\s*\d+\/\d+\/\d+)": "",
    # buy 2, get $4 OR buy 3, get $8 ExtraBucks® Rewards
    "(buy\s*\d+\,*\s*get\s*\$*\d+\s*OR\s*buy\s*\d+\,*\s*get\s*\$*\d+\s*ExtraBucks\®*\s*Rewards)": "",

}

# Dirty words to remove from the cleansed description.
DIRTY_WORD_PATTERNS = {

    # <Pattern looking for> : <replace pattern with this string>
    "(\.\.+)" : "",
    "(4\s*Day\s*Sale)" : "",
    "(ACME\s*BIG\s*BOOK\s*OF\s*XTRAsavings)" : "",
    "(ACME\s*Celebrate\s*LABOR\s*DAY)" : "",
    "(ACME\s*Stock\s*up\s*for\s*LABOR\s*DAY)" : "",
    "(ACME\s*XTRA)" : "",
    "(Action\s*Figure\s*Items\s*shown\s*plus\s*more)" : "",
    "(Additional\s*\d+\s*off\s*coupon\s*in\s*most\s*Sunday\s*papers)" : "",
    "(Additional\s*or\s*lesser\s*quantities\s*will\s*scan\s*at\s*\d+\.*\d*\s*ea\.*)" : "",
    "(AFTER\s*INSTANT)" : "",
    "(Albertsons\s*big\s*book\s*of\s*savings)" : "",
    "(All\s+Flavors\.*)" : "",
    "(All\s*Natural\,*)" : "",
    "(All\s*props\s*sold\s*separately\.*)" : "",
    "(All\s*Sizes\s*All\s*Varieties\s*WASHINGTON)" : "",
    "(ALL\s*THREE\s*FOR\s*\d+\.*\d*)" : "",
    "(All\s+Varieties\.*)" : "",
    "(ALWAYS\s*IN\s*SEASON\.*)" : "",
    "(and\s*hairs\s*moisture\s*balance\s*making\s*it\s*dry\s*and\s*dull)" : "",
    "(and\s*Larger)" : "",
    "(and\s*Select\s*Young\s*Men\'s\s*Apparel)" : "",
    "(Annie\'s\s*HOMEGROWN)" : "",
    "(an\s*itchy\s*nose\s*due\s*to\s*a\s*hay\s*fever\s*or\s*other\s*upper\s*respiratory\s*allergies)" : "",
    "(ANTIBIOTIC\s*FREE)" : "",
    "(antibiotic\s*free\s*all\s*natural\.*)" : "",
    "(antibiotic\s*free\s*meats\s*\&*\s*rBst\s*free\s*cheeses\.*)" : "",
    "(^ANY)" : "",
    "(Any\s+Flavor\.*)" : "",
    "(Any\s+Variety\.*)" : "",
    "(\(*a\s*\$\d+\.*\d*\s*value\)*)" : "",
    "(As\s*a\s*part\s*of\s*the\s*new\s*Dove\s*DermaCare\s*Scalp\s*series\s*we\s*created)" : "",
    "(As\s*measured\s*in\s*blood\s*samples\s*in\s*a\s*clinical\s*study)" : "",
    "(Assorted\s*counts)" : "",
    "(Assorted\s+Flavors\.*)" : "",
    "(Assorted\s*scents)" : "",
    "(Assorted\s*styles)" : "",
    "(Assorted\s+Varieties\.*)" : "",
    "(A\s*specially\s*crafted\s*blend\s*of\s*Vitamin\s*C\s*\+*\s*9\s*Vitamins\,*\s*Mineral\s*\&*\s*Herbs)" : "",
    "(Available\s*Hot)" : "",
    "(Available\s*in\s*Multiple\s*Colors)" : "",
    "(Available\s*in\s*our\s*Bakery\.*)" : "",
    "(Available\s*in\s*our\s*Deli\.*)" : "",
    "(Available\s*in\s*our\s*produce\s*department)" : "",
    "(available\s*in\s*produce)" : "",
    "(Available\s*in\s*Selected\s*Stores\.*)" : "",
    "(available\s*in\s*select\s*locations)" : "",
    "(Available\s*in\s*select\s*stores)" : "",
    "(available\s*in\s*the\s*bakery)" : "",
    "(Available\s*in\s*the\s*butcher\s*block)" : "",
    "(AVAILABLE\s*IN\s*THE\s*DELI)" : "",
    "(available\s*in\s*the\s*service\s*deli\.*)" : "",
    "(Baby\s*Dept\.*)" : "",
    "(Back\s*to\s*School\.*)" : "",
    "(Baked\s*In\s*Store)" : "",
    "(Baked\s*in\-store\.*)" : "",
    "(barrel\s*excludes\s*pub\s*mix\s*poker\s*mix\s*\&*\s*gourmet\s*popcorn\s*cluster\.*)" : "",
    "(bbq\s*bourbon\s*general)" : "",
    "(Beans\s*or\s*Vegetables\.*)" : "",
    "(beef$)" : "",
    "(beef\s*or\s*chicken)" : "",
    "(beef\s*turkey\s*or\s*chicken\.*)" : "",
    "(Best\s*of\s*all\s*No\s*sharpening\s*necessary\.*)" : "",
    "(Be\s*You\.*\s*SM)" : "",
    "(beverage$)" : "",
    "(blueberry\s*or\s*corn)" : "",
    "(Boar\’*s\s*Head\s*\&*\s*CARRY\s*OUT\s*CUISINE\.*)" : "",
    "(Brands\s*may\s*vary\s*by\s*store\.*)" : "",
    "(Breakfast\s*Club\s*\d+\s*OFF\s*when\s*you\s*buy\s*\d+\s*on)" : "",
    "(Breakfast\s*Club\s*\$*\d+\s*OFF\s*when\s*you\s*buy\s*\$*\d+\s*or\s*more\s*on\s*participating\s*products\s*in\s*a\s*single\s*transaction)" : "",
    "(b\s*LA\s*BREA\s*BAKERY\s*\d+)" : "",
    "(buffalo\s*jalapeo\s*or\s*sriracha)" : "",
    "(BUY\s*ANY\s*\d+\s*SAVE\s*\d+\s*EA\.*)" : "",
    "(Buy\s*any\s*\d+\s*select\s*Annie\’s\,*\s*Mountain\s*High\s*or\s*Cascadian\s*Farm\s*products\s*and\s*get\s*\d+\s*of\s*equal\s*or\s*lesser\s*value\,*\s*FREE\.*)" : "",
    "(BUY\s*\d+\s*GET\s*\d+\s*FREE\s*EQUAL\s*OR\s*LESSER\s*VALUE)" : "",
    "(BUY\s*\d+\s*GET\s*\d+\s*FREE\s*EQUAL\s*OR\s*LESSER\s*VALUE\s*Club\s*Price)" : "",
    "(BUY\s*\d+\s*of\s*these\**\s*Gatorade\s*Sports\s*Drink\s*\d+\-pk\.*\,*\s*\d+\s*fl\.*\s*oz\.*\s*btls\.*\s*and\s*GET\s*\d+\s*of\s*these\s*Propel\s*Fitness\s*Water\s*\d+\s*fl\.*\s*oz\.*\s*btl\.*)" : "",
    "(BUY\s*\s+\,*\s*GET\s*\s+\s*FREE)" : "",
    "(CA$)" : "",
    "(CALIFORNIA\s*NATURAL)" : "",
    "(Cannot\s*be\s*doubled\s*tripled\s*quadrupled\s*or\s*exchanged\s*for\s*cash\.*)" : "",
    "(Can\s*be\s*used\s*with\s*lights\s*or\s*candles\.*)" : "",
    "(Cape\s*included\s*with\s*Blu-ray\.*)" : "",
    "(Cascadian\s*Farm\s*ORGANIC)" : "",
    "(Celebrate\s*LABOR\s*DAY)" : "",
    "(CELEBRATE\s*with\s*SHRIMP)" : "",
    "(Certified\s*Angus\s*Beef\s*Boneless\s*Strip\s*Loin\s*Sold\s*whole\s*in\s*Cryovac\.*)" : "",
    "(Cheers\s*to\s*SAVINGS)" : "",
    "(Cheese\s*Italian\s*Vegetable\s*or\s*Meat)" : "",
    "(chocolate\s*chip\s*peanut\s*butter\s*oatmeal\s*raisin\s*candy\s*or\s*brownie)" : "",
    "(chocolate\s*chunk\s*cranberry\s*raisin\s*oatmeal\s*rainbow\s*or\s*snickerdoodle)" : "",
    "(CHOICE\s*Meat\s*\.*)" : "",
    "(Choose\s*from\s*one\s*or\s*more\s*select\s*varieties\s*of\s*our\s*\d+\.*\d*\s*single\s*bottle\s*beers\.*)" : "",
    "(Chunk\s*Light\s*In\s*Water)" : "",
    "(cinnamon\s*chip\s*or\s*caramel\s*pecanbon)" : "",
    "(CLIP\s*AND\s*REDEEM\s*BY)" : "",
    "(CLIP\s*AND\s*REDEEM\s*BY\s*\d+\s*ADDITIONAL\s*QUANTITIES\s*OR\s*PRICE\s*WITHOUT\s*MyMixx\s*DIGITAL\s*COUPON\s*\d+\s*FOR\s*\d+\s*DOWNLOAD\s*EXTRA)" : "",
    "(Clip\s*or\s*CLICK)" : "",
    "(Club\s*Price\.*)" : "",
    "(Club\s*Size\.*)" : "",
    "(Club\s*Sizes\.*)" : "",
    "(CLUB\s*SIZE\s*Savings\.*)" : "",
    "(Club\s*Sizes\s*GREAT\s*VALUES\.*)" : "",
    "(\"Color\s*May\s*Vary\")" : "",
    "(Colors\s*may\s*vary\s*by\s*store\.*)" : "",
    "(Color\s*Varies)" : "",
    "(COOLER\s*Savings)" : "",
    "(COUPON\s*CANNOT\s*BE\s*DOUBLED\.*)" : "",
    "(Coupon\s*in\s*MostSunday\s*Papers)" : "",
    "(coupon\s*savings\s*in\s*most\s*Sunday\s*papers)" : "",
    "(coupon\s*savings\s*online\s*or\s*in\s*most\s*Sunday\s*papers)" : "",
    "(Coupon\s*valid\s*thru\s*\d+\/\d+\/\d+\.*)" : "",
    "(CRV$)" : "",
    "(CRV\s*Max\s*Value\s*\d+\.*\d*)" : "",
    "(Customer\s*is\s*responsible\s*for\s*CRV\s*Items\s*must\s*be\s*purchased)" : "",
    "(Customer\s*is\s*responsible\s*for\s*tax\.*)" : "",
    "(CUT\s*FRESH\s*IN\-STORE\s*)" : "",
    "(Date\:*\s*September\s*\d+\,*\s*\d+)" : "",
    "(Date\s*subject\s*to\s*changed\:*\s*Limit\s*\d+)" : "",
    "(Date\s*subject\s*to\s*change\.*\s*limit\s*\d+\.*)" : "",
    "(\.+\$*\d+\.+\d+)" : "",
    "(\$*\d+\.*\d*\-*\d+\%\s*OFF)" : "",
    "(\d+\-\d+\.\d+\s*oz\.\,\s*Frozen)" : "",
    "(\d+\.*\d*\s*EA\.*)" : "",
    "(\d+\.*\d*\s*ea\.*\-*\d+\s*ea\.*)" : "",
    "(\$*\d+\.*\d*\s*EA\.*\s*Club\s*Price\s*Limit\s*\d+)" : "",
    "(\d+\.*\d*\s*OFF\s*with\s*at\s*shoprite\.com)" : "",
    "(debi\s*lilly\s*design)" : "",
    "(deli\s*\&*\s*CARRY\s*OUT\s*CUISINE\.*)" : "",
    "(Did\s*you\s*know\s*that\s*aggressive\s*washing\s*and\s*harsh\s*products\s*could\s*take\s*away\s*your\s*scalps\s*nutrients)" : "",
    "(DIGITAL\s*COUPON)" : "",
    "(Digital\s*Only\s*Just\s*for\s*u\.*)" : "",
    "(Dinner\s*Includes\:*\s*\(*\d+\)*\s*\d*\s*Piece\s*Fried\s*or\s*Baked\s*Chicken\s*or\s*\(*\d+\)*\s*Rotisserie\s*Chicken)" : "",
    "(discount\s*taken\s*at\s*register)" : "",
    "(DIY\s*Dept\.*)" : "",
    "(does\s*not\s*include\s*seasoned\s*pork\s*or\s*back\s*ribs)" : "",
    "(DOWNLOAD\s*EXTRA)" : "",
    "(Dryness\s*and\s*Itch\s*Relief\s*Conditioner\s*that\s*helps\s*nourish\s*and\s*sooth\s*itchy\s*and\s*dry\s*scalp.)" : "",
    "(\d+\%\s*ALL\s*NATURAL)" : "",
    "(\d+\s*day\s*Fight\s*Night\s*Savings)" : "",
    "(\d+\s*DAY\s*SALE)" : "",
    "(\d+\s*Fetzer\s*Vineyards\s*Hopland\s*Mendocino\s*Co\.*)" : "",
    "(\d+\s*FOR\s*\$*\d+)" : "",
    "(\d+\s*FOR\s*\$*\d+\s*Club\s*Price)" : "",
    "(\d+\s*FOR\s*\$*\d+\s*Club\s*Price\s*Limit\s*\d+)" : "",
    "(\d+\s*FREE\s*Lucerne\s*Milk)" : "",
    "(\d+\s*FRIDAY\s*Friday\s*September\s*\d+th)" : "",
    "(\d+\s*Hours\s*of\s*congestion\s*relief\s*with\s*just\s*one\s*tablet)" : "",
    "(\d+\%\s*Lean\,*)" : "",
    "(Fresh\s*Ground\s*Beef\s*\d+\%\s*Lean\.*\s*\d+\.\d+\s*lb\.*)" : "",
    "(\d+\%\s*OFF\s*All\s*\d+\s*ml\.*)" : "",
    "(\d+\s*off\s*coupon\s*in\s*most\s*Sunday\s*papers)" : "",
    "(\d+\s*off\s*coupon\s*online\s*or\s*in\s*most\s*Sunday\s*papers)" : "",
    "(\d+\s*PACK\s*\d+\s*a\s*can\.*)" : "",
    "(\d+\%\s*Real\s*Dairy\.*)" : "",
    "(\d+\s*Unilever)" : "",
    "(Eat\s*Smart)" : "",
    "(Enter\s*Promo\s*Code\:*\s*\w+)" : "",
    "(equal\s*or\s*lesser\s*value\s*item\s*free)" : "",
    "(equal\s*or\s*lesser\s*value\s*items\s*free\.*)" : "",
    "(Every\s*Day\s*\d+\s*AM\s*\-\s*\d+\s*PM\s*or\s*its\s*FREE)" : "",
    "(Excludes\s*activewear\,*\s*basics\s*and\s*The\s*Find\.*)" : "",
    "(Excludes\s*adidas\s*and\s*Skechers\.*)" : "",
    "(Excludes\s*Always\s*Discreet\s*Boutique\.*)" : "",
    "(excludes\s*angus\s*beef\s*franks\.*)" : "",
    "(Excludes\s*bath\s*poufs\.*)" : "",
    "(excludes\s*Birds\s*Eye\s*Selects\s*\&*\s*Protein\s*Blends)" : "",
    "(Excludes\s*clearance\.*)" : "",
    "(Excludes\s*custom\s*fit\s*orthotics\.*)" : "",
    "(excludes\s*decaf\.*)" : "",
    "(Excludes\s*Greek\.*)" : "",
    "(excludes\s*lasagna\s*jumbo\s*shells\s*and\s*manicotti\.*)" : "",
    "(excludes\s*lasagna\s*tri\-color\s*oven\s*ready\s*jumbo\s*shells\s*pot\s*pie\s*squares\s*whole\s*grain\s*super\s*greens\s*organic\s*and\s*gluten\s*free\.*)" : "",
    "(excludes\s*organic\s*\d*\s*fruit\s*\&*\s*veggie\s*and\s*super\-*v\s*\d+\.*\d*\s*ea\.*\-*\d*\s*ea\.*)" : "",
    "(excludes\s*peanut\s*butter\s*pretzels\s*\&*\s*pretzel\s*rods\.*)" : "",
    "(Excludes\s*pseudoephedrine\s*products\.*)" : "",
    "(Excludes\s*Rotisserie\s*Chicken\.*)" : "",
    "(excludes\s*San\s*Marzano\.*)" : "",
    "(Excludes\s*travel\s*and\s*trial\s*size\.*)" : "",
    "(Excludes\s*travel\s*and\s*trial\s*size\.*)" : "",
    "(Excludes\s*twin\s*packs\.*)" : "",
    "(Excludes\s*Wet\s*Brush\.*)" : "",
    "(Excluding\s*Coffee\s*House\s*\&*\s*Swiss\s*Miss\s*Newmans\s*Donut\s*Shop\s*Krispy\s*Kreme\s*Revv\s*SAVE\s*UP\s*TO\s*\d+\.*\d*)" : "",
    "(Excluding\s*Decaf)" : "",
    "(Excluding\s*Intense\s*Chocolate\s*\&*\s*Holiday)" : "",
    "(Excluding\s*Nourish\s*Granola\s*\&*\s*Pumpkin)" : "",
    "(Exclusively\s*at\s*ACME\.*)" : "",
    "(EZ\s*peel\s*frozen\s*sold\s*in\s*a\s*\d+\s*lb\.*\s*bag\s*for\s*\d+\.*\d*\s*lesser\s*quantities\s*\d+\.*\d*\s*lb\.*)" : "",
    "(FAB5\s*SALE)" : "",
    "(Fall\s*into\s*for\s*a\s*healthier\s*you)" : "",
    "(Fall\s*into\s*savings\s*for\s*a\s*healthier\s*you)" : "",
    "(Fall\s*\&*\s*Regular\s*Scents)" : "",
    "(FAMILY\s*SIZE)" : "",
    "(Family\s*Size\s*Non\s*GMO\s*Gluten\s*Free)" : "",
    "(Family\s*Size\s*\-*\s*Hot\s*All\s*hot\s*deli\s*items\s*are\s*Available\s*\d+\-*\d+pm\s*daily)" : "",
    "(FEEL\s*GOOD\.*)" : "",
    "(fettuccine\s*linguine\s*or\s*angel\s*hair)" : "",
    "(Fight\s*Night\s*Fiesta)" : "",
    "(Final\s*Price)" : "",
    "(Final\s*Price\s*\d+\s*for\s*\d+\.*\d*\s*with\s*Manufacturers\s*In\s*Ad\s*Coupon\.*)" : "",
    "(Fishermans\s*Net\.)" : "",
    "(for\s*all\s*occasions)" : "",
    "(For\s*Immune\s*Support)" : "",
    "(for\s*the\s*Family\**)" : "",
    "(FOSTER\s*FARMS\s*Family\s*Owned\s*Since\s*\d+)" : "",
    "(FOUNDED\s*IN\s*SKAGIT\s*VALLEY\,*\s*WA)" : "",
    "(Free\s*From\s*Antibiotics\,*)" : "",
    "(FREE\!*\s*INSTANTLY)" : "",
    "(FREE\s*INSTANTLY\s*up\s*to\s*\d+\.*\d*\s*value)" : "",
    "(free\s*Signature\s*Cafe\s*Whole\s*Roasted\s*Chicken\s*per\s*customer\s*per\s*visit\.*)" : "",
    "(Freshly\s*Ground\s*In\-Store\s*Daily)" : "",
    "(Fresh\s*Dairy\s*\&\s*Frozen\s*Grocery)" : "",
    "(fresh\s*ground\s*in\-*store\s*daily)" : "",
    "(Fresh\,*\s*No\s*Antibiotics\s*Ever\,*)" : "",
    "(fresh\s*to\s*go\.*)" : "",
    "(fresh\s*to\s*go\.*)" : "",
    "(Friday\-*Monday)" : "",
    "(FRIDAY\s*SEPTEMBER\s*\d+ST\s*THRU\s*MONDAY\s*SEPTEMBER\s*\d+TH\.*)" : "",
    "(FRIDAY\s*SEPTEMBER\s*\d+TH\s*THRU\s*MONDAY\s*SEPTEMBER\s*\d+TH)" : "",
    "(Fri\.*\-Sun\.*)" : "",
    "(From\s*Mexico)" : "",
    "(frozen\s*meat)" : "",
    "(frozen\s*meat$)" : "",
    "(frozen\s*strips\s*tenders\s*or\s*nuggets\.*\s*meat)" : "",
    "(fudgy\s*brownies\s*topped\s*with\s*chocolate\s*chip\s*candy\s*brownie\s*or\s*peanut\s*butter\s*cookies\.*)" : "",
    "(GAME\s*ON\s*PARTICIPATING\s*ITEM)" : "",
    "(GAME\s*ON\s*READY\s*SET\s*WIN)" : "",
    "(gaps\s*in\s*immune\s*function\s*between\s*formula\-fed\s*and\s*breast\-fed\s*infants\.*)" : "",
    "(Get\s*1\s*Pringles\s*INSTANTLY)" : "",
    "(Get\s*\d+\s*FREE\s*Gallon\s*White\s*Milk\s*INSTANTLY\!*)" : "",
    "(Get\s*\d+\s*FREE\s*Gatorade\s*flow\s*INSTANTLY)" : "",
    "(Get\s*\d+\s*FREE\s*Signature\s*SELEct\s*Salsa\s*INSTANTLY)" : "",
    "(Get\s*\d+\s*FREE\s*Signature\s*SELECT\s*Salsa\s*INSTANTLY\!*)" : "",
    "(Get\s*FREE\s*Bakery\s*Cookies\s*INSTANTLY\!*)" : "",
    "(get\s*your\s*favorite\s*FROZEN\s*TREATS\.*)" : "",
    "(get\s*your\s*favorite\s*FROZEN\s*TREATS\.*)" : "",
    "(Giant\s*Size\s*\-\s*Original)" : "",
    "(goes\s*on\s*invisible\s*to\s*help\s*protect\s*against\s*sweat\s*and\s*odor\.*)" : "",
    "(GOOD\s*HUMOR)" : "",
    "(GO\s*TEXAN\.*)" : "",
    "(Great\s*for\s*a\s*quick\s*and\s*easy\s*dinner)" : "",
    "(Great\s*for\s*snacking\s*Cheese\s*of\s*the\s*Month)" : "",
    "(grocery\s*\&*\s*snack)" : "",
    "(Ground\s*fresh\s*daily\s*in\s*store\.*)" : "",
    "(Grown\s*in\s*Castroville)" : "",
    "(GROWN\s*IN\s*TULARE\s*COUNTY)" : "",
    "(Guaranteed\s*FRESHNESS\s*QUALITY)" : "",
    "(Hand\s*Made\.*)" : "",
    "(Happy\s*LABOR\s*DAY)" : "",
    "(Hatfield\.)" : "",
    "(Health\s*\&\s*Beauty\s*Care\s*Dept\.*)" : "",
    "(health\s*\&*\s*home\s*savings)" : "",
    "(healthy\s*\&*\s*sustainable\.*)" : "",
    "(helps\s*strengthen\s*your\s*babys\s*immune\s*system\s*to\s*be\s*more\s*like\s*a\s*breastfed\s*baby\s*than\s*ever\s*before\.*)" : "",
    "(hickory\s*or\s*spicy\.*)" : "",
    "(high\s*protein\s*snacks\.*)" : "",
    "(Home\s*Dept\.*)" : "",
    "(Home\s*SAVINGS)" : "",
    "(homestyle\s*white\s*wheat\s*or\s*\d+\s*grain)" : "",
    "(hot\s*or\s*mild\s*Meat)" : "",
    "(How\s*Similac\s*with\s*\d+\-FL\s*helps\s*support\s*babys\s*developing\s*immune\s*system\s*by\s*closing\s*multiple)" : "",
    "(Includes\s*\d+\s*Breasts\,*\s*\d+\s*Wings\,*\s*\d+\s*Thighs\,*\s*\d+\s*Drumsticks\,*\s*\(*\d+\)*\s*\d+\s*oz\s*Sides\s*\&*\s*\(*\d+\)*\s*\d+\-Pack\s*King\'s\s*Hawaiian\s*Rolls)" : "",
    "(includes\s*Naturals\.*)" : "",
    "(Includes\s*Signature\s*Cafe\s*Whole\s*Roasted\s*Chicken\s*Signature\s*CAFE)" : "",
    "(Individual\s*Price\s*\d+\.*\d*\s*ea\.*)" : "",
    "(Individual\s*Price\s*d+\.*\d*\s*ea\.*)" : "",
    "(Individual\s*Price\s*\d+\s*ea\.*)" : "",
    "(Individual\s*Price\s*\d+\s*for\s*\d+\s*CASE\s*SALE\.*)" : "",
    "(Individual\s*Price\s*\d+\s*for\s*\d+\s*CASE\s*SALE\.*)" : "",
    "(in\s*a\s*single\s*transaction\.)" : "",
    "(In\s*a\s*single\s*transaction\s*VALID\s*\d+\/\d+\/\d+\s*\-\s*\d+\/\d+\/\d+\s*\d*\s*Smithfield\.*)" : "",
    "(In\s*Store\s*Daily)" : "",
    "(INSTANT\s*SAVINGS\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+)" : "",
    "(INSTANT\s*SAVINGS\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*OR\s*MORE)" : "",
    "(INSTANT\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*SAVE\s*\d+\s*INSTANTLY\s*)" : "",
    "(INSTANT\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*SAVE\s*\d+\s*INSTANTLY\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+)": "",
    "(is\s*previously\s*frozen\.*)" : "",
    "(Item\s*of\s*the\s*Week)" : "",
    "(Items\s*must\s*be\s*purchased\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(It\s*goes\s*on\s*invisible\s*to\s*help\s*reduce\s*white\s*marks\s*on\s*skin\s*or\s*clothing\.*)" : "",
    "(It\s*keep\s*you\s*feeling\s*fresh\s*for\s*\d+\s*hours\.*)" : "",
    "(Its\s*got\s*a\s*specially\s*designed\s*self\-sharpener\s*inside\.*)" : "",
    "(Its\s*mild\s*pH\s*balanced\s*formula\s*helps\s*to\s*gently\s*care\s*for\s*hair\.*)" : "",
    "(Jericho\s*NY\s*\d+)" : "",
    "(JOHN\s*BRAND\s*SINCE\s*\d+)" : "",
    "(just\s*for\s*u\.*)" : "",
    "(k\-cups\s*GAME\s*ON\s*PARTICIPATING\s*ITEM)" : "",
    "(LABOR\s*DAY)" : "",
    "(Lancaster\s*BRAND$)" : "",
    "(Lancaster\s*BRAND\.)" : "",
    "(Lancaster\s*BRAND\s*deli\s*\&*\s*CARRY\s*OUT\s*CUISINE\.*)" : "",
    "(Lancaster\s*BRAND\s*PERDUE\.)" : "",
    "(Lancaster\s*BRAND\s*PREMIUM\s*BEEF)" : "",
    "(lasagna\s*tri\-color\s*oven\-ready\s*jumbo\s*shells\s*pot\s*pie\s*squares\s*whole\s*grain\s*super\s*greens\s*organic\s*and\s*gluten\s*free\.*)" : "",
    "(Late\s*July)" : "",
    "(less\s*than\s*half\s*price\.*)" : "",
    "(Let\'*s\s*Face\s*It\s*Dirt\s*\&*\s*oil\s*in\s*your\s*pores\s*can\s*clog\s*them\s*leading)" : "",
    "(Limited\s*edition\.*)" : "",
    "(Limit\s*\d+\.*)" : "",
    "(Limit\s*\d+\s*Offers)" : "",
    "(LIMIT\s*\d+\s*PER\s*CUSTOMER\.*)" : "",
    "(Limit\s*\d+\s*Per\s*Variety)" : "",
    "(Limit\s*one\s*coupon\s*per\s*offer\.*)" : "",
    "(Limit\s*ONE\s*offer\s*per\s*transaction\.*)" : "",
    "(Limit\s*two\s*coupons\s*per)" : "",
    "(Limit\s*two\s*coupons\s*per\s*offer\.*)" : "",
    "(Live\s*Healthy\.*)" : "",
    "(LOCAL\s*FARMER)" : "",
    "(LOCAL\.*\s+Rosh\s*Hashanah)" : "",
    "(Look\s*for\s*\d+\.*\d*\s*OFF)" : "",
    "(LOOK\s*GOOD\.*)" : "",
    "(LOOK\s*WHAT\'S\s*New\.*)" : "",
    "(LOOK\s*WHATS\s*New\.*)" : "",
    "(LOWER\s*Prices\s*ON\s*WHAT\s*YOU\s*BUY\s*MOST)" : "",
    "(low\s*Low\s*Iron)" : "",
    "(Lysol\s*Disinfecting\s*Spray\s*kills\s*\d+\.*\d*\%*\s*of\s*bacteria\s*and\s*viruses)" : "",
    "(Machine\s*Wash\s*Cold\s*Wash\s*with\s*like\s*colors)" : "",
    "(Made\s*fresh\s*in\s*the\s*deli)" : "",
    "(made\s*fresh\s*in\-store\s*daily)" : "",
    "(Made\s*in\-store\.*)" : "",
    "(Make\s*Your\s*Holidays\s*More\s*Festive)" : "",
    "(Max\s*Value\:*\s*\$*\d+\.*\d*)" : "",
    "(Max\s*Value\s*\d+\.*\d*)" : "",
    "(Max\s*Value\s*Up\s*To\:*\s*\$*\d+\s*When\s*You\s*Buy\s*\d+\s*Starbucks\s*Coffee\s*\d+\-*\d*\s*oz\.*\s*bags\s*or\s*\d+\-*\d*\s*ct\.*\s*k\-*cups)" : "",
    "(May\s*not\s*be\s*used\s*in\s*combination\s*with\s*any\s*other\s*offer\.*)" : "",
    "(meat$)" : "",
    "(medium\s*size\s*cereal)" : "",
    "(MFR\s*Coupon\s*in\s*MostSunday\s*Papers)" : "",
    "(min\.*\s*\d+)" : "",
    "(Mix\s*and\s*Match)" : "",
    "(Mix\s*or\s*Match)" : "",
    "(MIX\s*OR\s*MATCH)" : "",
    "(MIX\s*\&\s*MATCH)" : "",
    "(MOUNTAIN\s*HIGH\s*The\s*Natural\s*Choice\s*in\s*Yoghurt)" : "",
    "(Multiple\s*Colors)" : "",
    "(MUSTBUY\s*\d*)" : "",
    "(MUST\s*BUY\s*\d+)" : "",
    "(MVP\s*SAVINGS\s*CENTER)" : "",
    "(NATHANS\s*FAMOUS\s*is\s*a\s*registered\s*trademark\s*used\s*under\s*license\s*from\s*Nathans\s*Famous\s*Systems\s*Inc\.*)" : "",
    "(never\s*frozen)" : "",
    "(NEW\s*LOWER\s*PRICE)" : "",
    "(New\s*you\.*)" : "",
    "(NON\s*GMO\s*Project)" : "",
    "(NO\s*COUPON\s*NECESSARY)" : "",
    "(No\s*Discomfort\s*Lactaid\s*ENJOY\s*DAIRY\s*AGAIN)" : "",
    "(No\s*Membership\s*Fees)" : "",
    "(No\s*visible\s*flakes\s*with\s*regular\s*use)" : "",
    "(Not\s*From\s*Concentrate\.*)" : "",
    "(Not\s*valid\s*toward\s*previous\s*purchase\.*)" : "",
    "(now\s*\d+\.*\d*\-*\d+\.*\d*)" : "",
    "(offer\.*)" : "",
    "(Offers)" : "",
    "(Offers\s*cannot\s*mix\s*or\s*match\.*)" : "",
    "(Offer\s*valid\s*in\s*one\s*transaction\s*between\s*\d+\/\d+\/\d+\s*\&*\s*\d+\/\d+\/\d+\.*)" : "",
    "(Offer\s*valid\s*with\s*Card\s*and\s*Coupon\.*)" : "",
    "(OFFICIAL\s*TAILGATING\s*HEADQUARTERS)" : "",
    "(Off\s*the\s*HOOK)" : "",
    "(olive\s*oil\s*roasted\s*garlic\s*or\s*rainin\s*grain\.*)" : "",
    "(One\s*coupon\s*per\s*customer\s*per\s*transaction\.*)" : "",
    "(ONE\s*offer\s*per\s*transaction\.*)" : "",
    "(ONLY\s*\d+\.*\d*\s*PER\s*lb\.*)" : "",
    "(Only\s*non\-chlorine\s*bleach\s*when\s*needed)" : "",
    "(on\s*all\s*your\s*pantry\s*favorites)" : "",
    "(original\s*buffalo\s*cheesy\s*or\s*honey\s*BBQ)" : "",
    "(original\s*garlic\s*or\s*whole\s*grain\.*)" : "",
    "(Original\s*or\s*Cinnamon)" : "",
    "(Original\,*\s*Spicy\s*or\s*Hatch\s*available\s*in\s*produce\.*)" : "",
    "(Original\,*\s*Whole\s*Grain\,*\s*Honey\s*Wheat\s*or\s*Cinnamon\s*Raisin\,*)" : "",
    "(or\s*larger\.*)" : "",
    "(or\s*more)" : "",
    "(or\s*more\s*BONELESS)" : "",
    "(or\s*more\s*Meat\s*\.*)" : "",
    "(Or\s*Organic\s*Strawberries\,*\s*\d+\s*oz\s*\$*\d+\.*\d*)" : "",
    "(O\s*organics$)" : "",
    "(O\s*organics\.)" : "",
    "(Other\s*Airborne\s*and\s*Digestive\s*Advantage\s*Products\.*\s*\d+\%\s*off)" : "",
    "(Other\s*Select\s*Crock\-Pot\s*Slow\s*Cookers)" : "",
    "(Other\s*Vicks\s*Products\.*\s*\d+\%\s*off)" : "",
    "(out\s*pore\-clogging\s*dirt\s*and\s*oil\s*then\s*cools\s*leaving\s*skin\s*tightly\s*smooth\s*\&*\s*refreshed\.*)" : "",
    "(OVER\s*\d+\.*)" : "",
    "(participating\s*products\s*in\s*a\s*single\s*transaction\.*)": "",
    "(Peeled\s*and\s*Deveined\.*)" : "",
    "(peeled\s*\&*\s*deveined\s*frozen\s*\d+\s*lb\.*\s*bag\s*\d+\.*\d*)" : "",
    "(peel\s*frozen\s*sold\s*in\s*a\s*\d+\s*lb\.*\s*bag\s*for\s*\d+\.*\d*\s*lesser\s*quantities\s*\d+\.*\d*\s*lb\.*\s*JUMBO)" : "",
    "(Pet$)" : "",
    "(petite\s*brownies\s*madeleines\s*duets\s*or\s*palmiers\s*Signature\s*SELEct)" : "",
    "(Plain\s*or\s*with\s*nuts\.*)" : "",
    "(Please\s*drink\s*it\s*responsibly\.*)" : "",
    "(Plus\s*deposit\s*fee\s*and\s*tax\s*where\s*applicable\.*)" : "",
    "(Plus\s*deposit\s*where\s*applicable\.*)" : "",
    "(Plus\s*deposit\s*where\s*available\.*)" : "",
    "(Plus\s*deposit\s*where\s*required\.*)" : "",
    "(Plus\s*deposit\s*where\s*required\s*Individual\s*Price\s*\d+\.*\d*\s*ea\.*)" : "",
    "(Plus\s*Dep\.*\s*or\s*Fee)" : "",
    "(Plus\s*Save\s*an\s*additional\s*\d+\%\s*when\s*you\s*buy\s*\d+\s*or\s*more\s*\d+\s*ml\.*)" : "",
    "(Portioned\s*for\s*easy\s*preparation)" : "",
    "(PREPARED\s*in\s*our\s*STORE)" : "",
    "(Previously\s*frozen)" : "",
    "(Previously\s*frozen\s*CELEBRATE\s*with\s*SHRIMP)" : "",
    "(Previously\s*Frozen\s*or\s*Boneless\s*Pork\s*Tenderloin)" : "",
    "(PRICE\s*AFTER)" : "",
    "(PRICE\s*AFTER\s*MyMixx\s*DIGITAL\s*COUPON)" : "",
    "(PRIMO\s*TAGLIO\s*FIRST\s*CUT\s*QUALITY\s*SAY\s*PREE\-MO\s*TAHL\-YO\s*GAME\s*ON\s*PARTICIPATING\s*ITEM)" : "",
    "(Print\s*In\-*Store\s*Coupon\s*and\s*Save\s*\$*\d+)" : "",
    "(Product\s*of\s*U\.S\.A\.\d+\%\s*Lean\s*Ground\s*Beef\s*Patty\s*Unseasoned\.*\s*\d+\.\d+\s*lb)" : "",
    "(Promo\s*Code\:*\s*\w+)" : "",
    "(Provides\s*\d+\s*hr\s*relief\s*of\s*nasal\s*congestion\s*sneezing\s*a\s*runny\s*nosy)" : "",
    "(Pumpkin\s*Season\s*is\s*here)" : "",
    "(Pumpkin\s*Variety\s*Available)" : "",
    "(Purchase\s*must\s*be\s*made\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(Quality\s*Guaranteed)" : "",
    "(RABBIT\s*OF\s*APPROVAL)" : "",
    "(Ready\s*to\s*Cook)" : "",
    "(reflect\s*\d+\%\s*off)" : "",
    "(reflect\s*\d+\s*off)" : "",
    "(Refrigerated)" : "",
    "(reg\.*retails\s*\d+\.*\d*\-\d+\.*\d*\s*\.*)" : "",
    "(Reg\.*\s*\d+\.*\d*)" : "",
    "(Reg\.*\s+\d+\.+\d+\.*)" : " ",
    "(Reg\.*\s+\d+\.+\d+\.+\d+\.+\d+\.*)" : " ",
    "(Reg\.*\s+\d+\.+\d+\s*ea\.*)" : " ",
    "(Reg\.*\s+\d+\.+\d+\s*or\s*more\.*)" : " ",
    "(Reg\.*\s+\d+\.+\d+\s*\-\s*\d+\.+\d+\.*)" : " ",
    "(Reg\.*\s+\d+\.+\d+\s*\-\s*\d+\.+\d+\.*\s+ea\.*)" : " ",
    "(Reg\.*\s+\d+\s*\-\s*\d+\.*)" : " ",
    "(Reg\.*\s+\d+\s*-\s*\d+\.+\d+\.*)" : " ",
    "(reg\.*\s*retails\s*\d+\.*\d*\-\d+\.*\d*)" : "",
    "(reg\.*\s*retails\s*\d+\.*\d*\s*lb\.*\-*\d+\.*\d*\s*lb\.*)" : "",
    "(Regular\s*or\s*LIght\.*)" : "",
    "(Regular\s*or\s*lite)" : "",
    "(Regular\s*or\s*lite)" : "",
    "(Regular\s*Retail\s*\d+\.*\d*)" : "",
    "(Regular\s*Retail\s*\d+\.*\d*\s*BUY\s*ANY\s*\d+\s*SAVE\s*\d+\s*EA\.*)" : "",
    "(regular\s*retails\s*\d+\.*\d*\-\d+\.*\d*\s*lb)" : "",
    "(RESPONSIBLE\s*CHOICE)" : "",
    "(REST\s*OF\s*WEEK\s*\d+\/\$*\d+)" : "",
    "(REST\s*OF\s*WEEK\s*\d+\¢\s*EA\s*MVP)" : "",
    "(Roasted\s*or\s*baked\s*in\-store\s*daily\.*)" : "",
    "(Roast\,*\s*Butcher\s*Shop\,*\s*U\.S\.D\.A\.\s*Choice\s*or\s*Ground\s*Beef\,*\s*\d+\%\s*Fat\,\s*Value\s*Pack)" : "",
    "(ROCKY$)" : "",
    "(Rosh\s*Hashanah$)" : "",
    "(Rosh\s*Hashanah\s*\d+)" : "",
    "(Sale\s*Price\s*\$*\d+\.*\d*\s*ea\.*)" : "",
    "(Sale\s*price\s*only\s*valid\s*during\s*4\s*Day\s*Sale\s*dates)" : "",
    "(Sale\s*price\s*only\s*valid\s*during\s*\d+\s*Day\s*Sale\s*dates\.*)" : "",
    "(sale\s*retails\s*\d+\.*\d*\-\d+\.*\d*)" : "",
    "(sale\s*retails\s*\d+\-*\d+\.*\d*\s*lb\.*)" : "",
    "(Same\s*Day\s*Pickup)" : "",
    "(SAVE\s*BIG\.*)" : "",
    "(SAVE\s*\$*\d+\s*INSTANTLY\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*PARTICIPATING\s*PRODUCTS\s*IN\s*A\s*SINGLE\s*TRANSACTION\.*)" : "",
    "(SAVE\s*\d+\s*INSTANTLY\s*WHEN\s*YOU\s*BUY\s*\d+\s*OF\s*EACH)" : "",
    "(SAVE\s*\d+\s*INSTANTLY\s*when\s*you\s*buy\s*\d+\s*participating\s*products\s*in\s*this\s*section\s*in\s*a\s*single\s*transaction)" : "",
    "(SAVE\s*\$*\d+\s*INSTANTLY\s*when\s*you\s*buy\s*FOUR\s*\(*\d+\)*\s*participating)" : "",
    "(Save\s*\d+\%\s*Off\s*Your\s*Grocery\s*Purchase\s*Of\s*\$*\d+\s*Or\s*More)" : "",
    "(Save\s*\$*\d+\s*on\s*your\s*next\s*shopping\s*trip\s*via\s*Custom\s*Coupon\s*at\s*checkout\s*when\s*you\s*buy\s*\$*\d+)" : "",
    "(Save\s*on\s*products\s*from\s*Rosa\.*)" : "",
    "(Save\s*Some\s*More\s*On\s*Smores)" : "",
    "(SAVINGS)" : "",
    "(SCORE\s*GREAT\s*DEALS\s*PARTICIPATING\s*ITEM)" : "",
    "(SEAFOOD\s*fest)" : "",
    "(See\s*store\s*display\s*and\s*packaging\s*for\s*full\s*details\.*)" : "",
    "(\**See\s*Store\s*For\s*Exclusions\s*Albertsons\s*Coupon\s*Effective\s*\d+\/\d+\/\d+\s*\-\s*\d+\/\d+\/\d+)" : "",
    "(^Select)" : "",
    "(Selected\s+Flavors\.*)" : "",
    "(Selected\s*sizes\s*and\s*varieties\.*)" : "",
    "(Selected\s*sizes\s*\&*\s*varieties)" : "",
    "(Selected\s*stores\.*)" : "",
    "(Selected\s*varietals)" : "",
    "(Selected\s*varietals\s*Single\s*Price\s*\d+\.*\d*)" : "",
    "(Selected\s*varieties)" : "",
    "(Selected\s+Varieties\.*)" : "",
    "(Selected\s*varieties\s*FREE)" : "",
    "(Selection\s*and\s*pricing\s*may\s*vary\s*in\s*our\s*Kosher\s*Parve\s*Bakery\s*locations\.*)" : "",
    "(Selection\s*varies\s*by\s*store\.*)" : "",
    "(Select\s*Flavors\.*)" : "",
    "(Select\s*Stylers)" : "",
    "(Select\s*Styles\s*\&*\s*Sizes)" : "",
    "(Select\s*Varieties\.*)" : "",
    "(sending\s*us\s*looking\s*for\s*anti-dandruff\s*products\.)" : "",
    "(Sept\.*\s*\d+\-Sept\.*\s*\d+\,*\s*\d*)" : "",
    "(Sept\s*\d+\-Sept\s*\d+\s*\d*)" : "",
    "(SEPT\.*\s*\d+\s*THRU\s*SEPT\.*\s*\d+\,*\s*\d*)" : "",
    "(Series\s*\d+\s*or\s*Series\s*\d+)" : "",
    "(Served\s*hot\s*from\s*the\s*Deli\s*Case\.*)" : "",
    "(shelf\s*retails)" : "",
    "(ShopRite\s*Fresh\s*Bake\s*Shop)" : "",
    "(ShopRite\s*Sale\s*Price\s*\d+\.*\d*\s*lb\s*\-\d+\.*\d*\s*lb\s*\-lb)" : "",
    "(Side\s*Dish\,*)" : "",
    "(Side\s*Dishes\,*)" : "",
    "(Similacs\s*biggest\s*breakthrough\s*in\s*nearly\s*a\s*decade\s*comes\s*in\s*two\s*gentle\s*formulas\s*Similac\s*Pro\-Advance\s*and\s*Pro\-Sensitive\.*)" : "",
    "(SINCE\s*\d+)" : "",
    "(SINGLE\s*BOTTLE\s*\$*\d+\.*\d*\-*\d+\%\s*OFF\s*\d+)" : "",
    "(Single\s*Price\s*\d+\.*\d*)" : "",
    "(\,*\s*In\s*the\s*Bakery)" : "",
    "(Sliced\s*free\s*\.*\s*\d+\.\d+\s*lb)" : "",
    "(Sliced\s*fresh\s*to\s*order)" : "",
    "(Sliced\s*fresh\s*to\s*order\s*available\s*in\s*the\s*service\s*deli)" : "",
    "(Sliced\s*fresh\s*to\s*order\s*in\s*your\s*Service\s*Deli)" : "",
    "(Sold\s*by\s*the\s*Pound\,*)" : "",
    "(Sometimes\s*little\s*flakes\s*on\s*the\s*shoulders\s*can\s*make\s*us\s*feel\s*self\-conscious)" : "",
    "(So\s*you\s*always\s*get\s*the\s*pointperfectly\.*)" : "",
    "(SPEND\s*\d+\s*SAVE\s*\d+\s*When\s*purchasing\s*any\s*Carando\s*Eckrich\s*Nathans\s*Famous\s*or\s*Smithfield\s*products\.*)" : "",
    "(Spicy\s*Pico\s*over\s*Guacamole\s*or\s*Black\s*Bean\s*over\s*Guacamole)" : "",
    "(Sporting\s*Goods\s*Dept\.*)" : "",
    "(\s*\-*\s*Assorted)" : "",
    "(\s*\-*\s*Assorted\s*Cool\s*Gear)" : "",
    "(\s*\-*\s*Fully\s*Cooked)" : "",
    "(\s*\-+\s*Select\s*varieties\.*)" : "",
    "(start\s*your\s*day\s*off\s*RIGHT)" : "",
    "(Start\s*your\s*morning\s*with\s*a\s*fresh\s*sweat\s*fighting\s*spray\s*that\s*helps\s*keep\s*you\s*protected\s*all\s*day\.*)" : "",
    "(Stayfree\s*Pads\.*)" : "",
    "(stock\s*up\s*on\s*SNACKS\.*)" : "",
    "(stock\s*up\s*\&*\s*SAVE\.*)" : "",
    "(Strawberry\s*Blueberry\s*and\s*Peach)" : "",
    "(Swagger\s*scent\s*is\s*the\s*smell\s*of\s*cedarwood\s*lime\s*and\s*confidence\.*)" : "",
    "(Teams\s*may\s*vary\s*by\s*store\.*)" : "",
    "(Texas\s*smoked\s*or\s*tuscan\.*)" : "",
    "(That\'*s\s*long\s*enough\s*to\s*build\s*a\s*small\s*house\s*or\s*navigate\s*an\s*especially\s*large\s*lake\.*)" : "",
    "(Thawed\s*for\s*Your\s*Convenience)" : "",
    "(The\s*formulation\s*cleanses\s*itchy\s*and\s*dry\s*scalp\s*while\s*leaving\s*hair\s*flake\s*free\s*smooth\s*and\s*less\s*frizzy\.*)" : "",
    "(Thin\s*Cut\s*for\s*Steak\s*rolls\s*or\s*Chipped\s*Steak\s*for\s*Sandwiches)" : "",
    "(This\s*anti\s*dandruff\s*conditioner\s*is\s*formulated\s*with\s*active\s*Pyrithione\s*Zinc)" : "",
    "(This\s*coupon\s*cannot\s*be\s*used\s*unless\s*the\s*purchase\s*is\s*\$*\d+\s*or\s*more\s*after\s*deducting\s*all\s*manufacturer\s*coupons\s*and\s*store\s*coupons\s*and\s*without\s*including\s*money\s*orders\s*lottery\s*tickets\s*gift\s*cards\s*alcohol\s*tobacco\s*prescriptions\s*stamps\s*and\s*other\s*products\s*prohibited\s*by\s*law\.*)" : "",
    "(This\s*coupon\s*must\s*be\s*presented\s*at\s*time\s*of\s*purchase\.*)" : "",
    "(This\s*eyeliner\s*pencil\s*gives\s*you\s*control\s*and\s*versatility\.*)" : "",
    "(This\s*unique\s*formula\s*heats\s*on\s*contact\s*with\s*water\s*to\s*open\s*pores\s*\&*\s*draw)" : "",
    "(to\s*effectively\s*tackle\s*dandruff\s*in\s*a\s*formula\s*to\s*help\s*solve\s*dryness\s*and\s*itch\s*experienced\s*by\s*dandruff\-prone\s*scalp\.*)" : "",
    "(to\s*skin\s*problems\s*but\s*you\s*don\'*t\s*always\s*have\s*time\s*for\s*a\s*deep\s*cleaning\s*mask\s*treatment\.*)" : "",
    "(TRIMMED\s*\&*\s*READY)" : "",
    "(Tumble\s*dry)" : "",
    "(Unilever\s*Ice\s*Cream\s*products)" : "",
    "(Unlike\s*other\s*formulas\s*Similac\s*has\s*\d+\-FL\s*HMO\s*a\s*prebiotic\s*that\s*circulates\s*throughout\s*the\s*body\.*)" : "",
    "(Up\s*to\s*a\s*\$*\d+\.*\d*\s*value\.*)" : "",
    "(U\.S\.D\.A\.\s*CHOICE\.*)" : "",
    "(USDA\s*CHOICE)" : "",
    "(USDA\s*ORGANIC\.*)" : "",
    "(Value\s*pack$)" : "",
    "(Value\s*pack\s*FOSTER\s*FARMS\s*Family\s*Owned\s*Since\s*\d+)" : "",
    "(Variety\s*of\s*flavors)" : "",
    "(VERIFIED\s*nongmoproject\.*org)" : "",
    "(Void\s*if\s*copied\s*or\s*transferred\s*in\s*the\s*event\s*of\s*return\s*coupon\s*savings\s*may\s*be\s*deducted\s*from\s*refund\.*)" : "",
    "(WAKE\s*UP\s*with)" : "",
    "(Walmart\s*Exclusive\s*Pack)" : "",
    "(Want\s*a\s*precise\s*line\s*It\s*glides\s*on\s*easily\.*)" : "",
    "(Want\s*to\s*soften\s*a\s*bit\s*There\'*s\s*a\s*soft\s*smudger\s*tip\.*)" : "",
    "(Water\s*added\.*)" : "",
    "(Weather\s*permitting)" : "",
    "(We\s*make\s*our\s*wine\s*responsibly\.*)" : "",
    "(we\s*will\s*never\s*forget\s*NEVER\s*FORGOTTEN\s*\d+\s*\d*\.*\d*\s*\d+)" : "",
    "(What\s*It\s*Does\s*Biore\s*Self\s*Heating\s*One\s*Minute\s*Mask\s*gives\s*you\s*purified\s*pores\s*in\s*just\s*\d+\s*minute\.*)" : "",
    "(WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*participating\s*products\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(When\s*You\s*Buy\s*\d+\s*Cheez\-It\s*Crackers\s*\d+\-\d+\.*\d*\s*oz\s*FREE\s*Items\s*must\s*be\s*purchased)" : "",
    "(When\s*You\s*Buy\s*\d+\s*El\s*Monterey\s*Burritos\s*\d+\s*ct\.*\,*)" : "",
    "(When\s*You\s*Buy\s*\d+\s*El\s*Monterey\s*Burritos\s*\d+\s*ct\s*frozen\s*Items\s*must\s*be\s*purchased)" : "",
    "(When\s*You\s*Buy\s*\d+\s*Gatorade\s*\d+\s*pack\s*\d+\s*oz\s*btls)" : "",
    "(when\s*you\s*buy\s*\d+\s*participating\s*Kelloggs\s*Cereal\s*\d+\.\d+\-\d+\.\d+\s*oz\s*pkg\s*or\s*Keebler\s*Cookies\s*or\s*Snacks\s*\d+\.\d+\-\d+\.\d+\s*oz\s*pkg)" : "",
    "(when\s*you\s*buy\s*\(*\d+\)*\s*participating\s*Kellogg\’s\s*Cereal\,*\s*\d+\.*\d*\-\d+\.*\d*\s*oz\.*\s*pkg\.*\s*or\s*Keebler\s*Cookies\s*or\s*Snacks\,*\s*\d+\.*\d*\-\d+\.*\d*\s*oz\.*\s*pkg\.*\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(When\s*You\s*Buy\s*\d+\s*Post\s*Cereal)" : "",
    "(WINE\s*OR\s*CHAMPAGNE)" : "",
    "(win\s*Buy\s*a\s*\"GIRLS\s*NIGHT\s*DVD\"\s*and\s*get\s*\d+\.*\d*\s*off\s*FETZER\s*wine\s*with\s*mail\-in\s*rebate\s*VALID\s*\d+\/\d+\s*\-\s*\d+\/\d+\s*with\s*Club\s*Card\.*)" : "",
    "(With\s*flavored\s*butter\s*TAKE\s*BAKE\s*or\s*GRILL)" : "",
    "(With\s*your\s*PricePlus\s*club\s*card\.*)" : "",
    "(XTRA)" : "",
    "(xtreme\s*value\.*)" : "",
    "(Your\s*Choice\s*of\s*either\:*\s*\d+\s*lb\.*\s*Potato\s*Salad\,*\s*Macaroni\s*Salad\s*or\s*Cole\s*Slaw\s*and\s*\d+\s*Kings\s*Hawaiian\s*Rolls)" : "",
    "(Your\s*favorites)" : "",
    "(YOU\s*SAVE\s*\d+\.*\d*)" : "",

    # New patterns.
    "(\s*\-\s*\$*\d+\.*\d*\s*with\s*card)" : "",
    "(Gillette\s*Shave\s*Needs)" : "Gillette Shave",
    "(Select\s*Cartridges)" : "Cartridges",
    "(Select\s*Tablets)" : "Tablets",
    "(Select\s*Underwear)" : "Underwear",
    "(Select\s*Pads)" : "Pads",
    "(Select\s*Wal-Zan)" : "Wal-Zan",
    "(Lansoprazole\s*Omeprazole\s*Omeprazole)" : "Lansoprazole Omeprazole",
    "(Select\s*Qunol)" : "Qunol",
    "(Move\s*Free)" : "",
    "(Select\s*Ibuprofen)" : "Ibuprofen",
    "(All\s*Day)" : "",
    "(\$*\d+\s*Off\s*Coupon\s*In\s*Most\s*Sunday\s*Paperst)" : "",
    "(\$*\d+\.*\d+\s*less\s*coupon\s*in\s*most\s*Sunday\s*papers)" : "",
    "(\$*\d+\s*off\s*coupon\s*on\s*\d+\s*in\s*most\s*Sunday\s*papers)" : "",
    "(Items\s*shown\s*plus\s*more)" : "",
    "(GREAT\s*SAVINGS\s*DOWN\s*EVERY\s*AISLE)" : "",
    "(\$*\d+\s*FRIDAY\s*SEPTEMBER\s*\d+TH)" : "",
    "(ONE\s*DAY\s*ONLY)" : "",
    "(Discount\s*When\s*You\s*Buy\s*\d+)" : "",
    "(\-\d+\%)" : "",
    "(\-\d+\.\d\d)" : "",
    "(Valid\s*Friday\s*only\s*\d+\-\d+\-\d+)" : "",
    "(donut\s*friday)" : "",
    "(THIS\s*WEEKS\s*FEATURED\s*ORGANIC\s*ITEMS)" : "",
    "(USDA\s*ORGANIC\s*WE\s*PROUDLY\s*OFFER\s*OVER\s*\d+\s*VARIETIES\s*OF\s*ORGANIC\s*PRODUCTS\.*)" : "",
    "(Makes\s*a\s*Great\s*Lunch\s*Hot\s*\&\s*Fresh)" : "",
    "(candy\s*\d+\.\d+\s*lb\.*)" : "candy",
    "(Delicious$)" : "",
    "(QUICK\s*\&\s*EASY)" : "",
    "(Open\s*Nature$)" : "",
    "(No\s*Antibiotics\s*or\s*Added\s*Hormones)" : "",
    "(No\s*Antibiotics\s*or\s*Addezd\s*Hormones)" : "",
    "(Vegetarian\s*Fed)" : "",
    "(Vegertarian\s*Fed)" : "",
    "(Signature\s*Farms$)" : "",
    "(Signature\s*Farms\s*Quality\s*Guaranteed$)" : "",
    "(Subject\s*to\s*Availability\s*wild)" : "",
    "(The\s*product\s*is\s*a\s*natural\s*food\s*because\s*it\s*contains\s*no\s*artificial\s*ingredients\s*and\s*is\s*only\s*minimally\s*processed\.*)" : "",
    "(Signature\s*CAFE$)" : "",
    "(Made\s*Fresh\s*Daily)" : "",
    "(RESER\'S\s*FINE\s*FOODS$)" : "",
    "(Sliced\s*Fresh\s*in\s*the\s*Deli)" : "",
    "(Sale\s*Price)" : "",
    "(Rewards\s*Per\s*Transaction)" : "",
    "(Sold\s*in\s*Packages\s*of\s*\d+\s*lb\.*\s*or\s*More\s*in\s*the\s*Meat\s*Case)" : "",
    "(GROUND\s*FRESH\s*in\s*Store\s*Daily)" : "",
    "(Reg\.*\s*Retail)" : "",
    "(up\s*to\s*\d+\.\d+\s*lb\.*\s*Equal\s*or\s*Lesser\s*Value)" : "",
    "(Sold\s*Out\s*of\s*Our\s*Fresh\s*Butcher\s*Block\s*Fresh\s*Never\s*Frozen)" : "",
    "(Hot\s*\&\s*Fresh)" : "",
    "(Reward\s*Per\s*Transaction)" : "",
    "(Select\s*Varieties\s*Additional)" : "",
    "(FIRST\s*CUT\s*QUALITY)" : "",
    "(SAY\s*PREE-MO\s*TAHL-YO)" : "",
    "(Valid\s*Only\s*Friday\s*September\s*\d+\s*\d\d\d\d)" : "",
    "(Plus\s*deposit\s*in\s*Oregon\.*)" : "",
    "(Sale)" : "",
    "(WHEN\s*YOU\s*BUY\s*\d+)" : "",
    "(Buy\s*any\s*\d+\s*select\s*Annies\s*Mountain\s*High\s*or\s*Cascadian\s*Farm\s*products\s*and\s*get\s*\d+\s*of\s*equal\s*or\s*lesser\s*value\s*FREE\.*)" : "",
    "(BUY\s*\d+\s*GET\s*\d+\s*FREE\s*MOUNTAIN\s*HIGH\s*The\s*Natural\s*Choice\s*in\s*Yoghurt\s*Cascadian\s*Farm\s*ORGANIC\s*FOUNDED\s*IN\s*SKAGIT\s*VALLEY\s*WA\s*SINCE\s*\d+\s*Annie\'s\s*HOMEGROWN\s*RABBIT\s*OF\s*APPROVAL)" : "",
    "(Sold\s*in\s*the\s*bag)" : "",
    "(Grown\s*In\s*Tulare\s*County)" : "",
    "(Selected\s*vareities\.*)" : "",
    "(Single\s*Price\s*\d+\.\d+\s*ea\.*)" : "",
    "(Delicious\s*served\s*warm\.*)" : "",
    "(SCORE\s*BIG\.*)" : "",
    "(In\s*beautiful\s*Fall\s*Colors\.*)" : "",
    "(Hot\s*at\s*\d+ p\.*m\.*)" : "",
    "(Tomatoes\s*On\s*The\s*Vine\s*Tomatoes\s*On\s*The\s*Vine)" : "Tomatoes on the Vine",
    "(Large\s*Navels\s*Minneola\s*Tangelos\s*or\s*Cara\s*Cara\s*Oranges\s*Large\s*Navels\s*Minneola\s*Tangelos\s*or\s*Cara\s*Cara\s*Oranges)" : "Large Navels Minneola Tangelos or Cara Cara Oranges",
    "(Northwest\s*Grown)" : "Northwest",
    "(BUY\s*\d+\s*\&\s*SAVE)" : "",
    "(Clip\s*Or\s*Click\.*)" : "",
    "(Just\s*For\s*U\.*)" : "",
    "(cash\s*in\s*your\s*quarters)" : "",
    "(Savour\s*The\s*Sea)" : "",
    "(Select\s*Varietals)" : "",
    "(BUY\s*\d+\s*OR\s*MORE\s*\&\s*SAVE\s*FAB)" : "",
    "(SAVE\s*FAB)" : "",
    "(SAVINGS\s*DOWN\s*EVERY\s*AISLE)" : "",
    "(\d+\s*Blue\s*Friday\s*PRICES\s*IN\s*THIS\s*SECTION\s*VALID\s*FRIDAY\s*SEPTEMBER\s*\d+ND\s*ONLY)" : "",
    "(\d+\s*SALE)" : "",
    "(Fresh\s*Picked)" : "Fresh",
    "(\d+\.\d\d\s*lb\.*\s*Wild\s*Caught)" : "",
    "(\d+\.\d\d\s*lb\.*\s*Savour\s*The\s*Sea)" : "",
    "(OWN\s*IT\s*ON\s*SEPTEMBER\s*\d+\s*\d\d\d\d)" : "",
    "(\s*AND\s*GET\s*FREE\s*OFFER\s*VALID\s*\d+\/\d+\/\d+\-\d+\/\d+\/\d+\s*ONE\s*\d+\s*Trolli\s*SourBrite\s*Crawlers\s*Originalor\s*Bites\s*Assorted\s*\d+\.\d+\s*\-\s*\d+oz\.*\s*Standup\s*Bag\s*\d+\s*Ferrara\s*Candy\s*Company)" : "",
    "(Participating\s*items\s*must\s*be\s*purchased\s*in\s*a\s*single\s*transaction\s*with\s*Club\s*Card\s*\.*)" : "",
    "(Limit\s*one\s*Blu\-ray\s*Combo\s*Pack\s*or\s*DVD\s*per\s*transaction\.*)" : "",
    "(Discount\s*taken\s*at\s*the\s*register\.*)" : "",
    "(Customer\s*pays\s*tax\s*and\s*CRV\s*where\s*applicable\.*)" : "",
    "(Not\s*all\s*varietiesavailable\s*in\s*all\s*stores\.*)" : "",
    "(Online\s*and\s*in\-store\s*prices\s*offers\s*and\s*discounts\s*may\s*differ\.*)" : "",
    "(\d+\s*DreamWorks\s*Animation\s*LLC\.*)" : "",
    "(All\s*Rights\s*Reserved\.*)" : "",
    "(TWENTIETH\s*CENTURY\s*FOX\s*FOX\s*and\s*associated\s*logos\s*are\s*trademarks\s*of\s*Twentieth\s*Century\s*Fox\s*Film\s*Corporation\s*and\s*its\s*related\s*entities\.*)" : "",
    "(Captain\s*Underpants\s*the\s*First\s*Epic\s*Movie\s*Captain\s*Underpants\s*the\s*First\s*Epic\s*Movie)" : "Captain Underpants the First Epic Movie",
    "(No\s*hormones\.)" : "",
    "(No\s*hormones\s*added\.)" : "",
    "(BUY\s*\d+\s*Gatorade)" : "",
    "(GET\s*\d+\s*FREE\s*Propel\s*\d+\-oz\.*\s*bottles\.*)" : "",
    "(Valid\s*Thru\s*\d+\/\d+\/\d\d)" : "",
    "(Signature\s*Farms\s*BaconSold\s*in\s*a)" : "",
    "(Only\s*\d+\.*\d*\s*ea\.*\d+\.\d+\s*LB\.*)" : "",
    "(COUPON\s*CANNOT\s*BE\s*DOUBLED\s*or\s*combined\s*with\s*digital\s*coupon\.*)" : "",
    "(Signature\s*Farms\s*Bacon\s*Signature\s*Farms\s*Bacon)" : "Signature Farms Bacon",
    "(Fresh\s*Ground\s*Beef\s*Fresh\s*Ground\s*Beef)" : "Fresh Ground Beef",
    "(Club\s*Price\s*Limit\s*\d+\s*Pks\.*)" : "",
    "(Club\s*Price\s*Limit\s*\d+\s*Pkgs\.*)" : "",
    "(Value\s*Pack\.*\s*\d+\.\d+\s*LB)" : "",
    "(USDA\s*Choice\s*Beef\s*Loin\s*New\s*York\s*Strip\s*Steak\s*Bone\-in\.*)" : "bone-in",
    "(NabiscoSnack\s*Crackers)" : "",
    "(\d+\/\d+\s*Price\s*Sale)" : "",
    "(Excluding\s*While\s*Supplies\s*Last\s*Items)" : "",
    "(Regular\s*Retais\s*\d+\.*\d*\s*to\s*\d+\.*\d*\s*ea\.*)" : "",
    "(Honey\s*Smoked)" : "Honey Smoked",
    "(Sodium\s*or)" : "Sodium or",
    "(Discount\s*will\s*be\s*applied\s*when\s*you\s*buy\s*in\s*increments\s*of\s*\d+\s*only\.*)" : "",
    "(Less\s*or\s*additional\s*items\s*will\s*scan\s*at\s*\d+\.*\d*\s*each\.*)" : "",
    "(orregular)" : "or regular",
    "(SAVE\s*UP\s*TO\s*\d+)" : "",
    "(Dessert\s*Excluding)" : "Dessert Excluding",
    "(Steam\s*In\s*Bag)" : "",
    "(Smart\s*dairy)" : "Smart dairy",
    "(SAVE\s*UP\s*TO\s*\d+\.*\d*)" : "",
    "(or\s*Chock)" : "or Chock",
    "(Limit\s*\d+\s*you\s*save\s*\d+)" : "",
    "(With\s*calcium)" : "With calcium",
    "(BUY\s*\d+\s*\d+\-oz\.*\s*Horizon\s*Organic\s*Yogurt\s*or\s*\d+\-oz\.*\s*cont\.*\s*Oikos\s*or\s*Light\s*\&Fit\s*Drinks\s*\d+\s*to\s*\d+\.*\d+\-oz\.*\s*cont\.*\s*Crunch\s*Greek\s*Any\s*Variety\s*OikosLight\s*\&\s*Fit\s*Greek\s*Mousse\s*Triple\s*Zero\s*Light\s*\&\s*Fit\s*Zero\s*orDannon\s*Greek\s*Yogurt\s*\d+\s*for\s*\d+\s*Limit\s*\d+Per\s*Variety\s*and\.*\s*GET\d+\s*\d+\-oz\.*\s*cont\.*\s*Any\s*Variety\s*Dunkin\s*Donuts\s*Coffee\s*Creamers\s*orInternational\s*Delight\s*Creamer\s*Limit\s*\d+\s*Offers\s*FREE\s*with\s*Price\s*Plus\s*Card\s*YOU\s*SAVE\s*\d+\.*\d+)" : "",
    "(Fit\s*\&\s*Delicious)" : "",
    "(\&Fit)" : "& Fit",
    "(Oikos\s*Light)" : "Oikos Light",
    "(Any\s*Variety\s*LESS\s*THAN\s*\d+\s*per\s*cup)" : "",
    "(Ready\s*to\s*Dip\s*or\s*Cook)" : "",
    "(Bars\s*\&)" : "Bars &",
    "(\d+\s*OFF\s*\d+\s*With\s*digital\s*coupon\s*at\s*shoprite\.com)" : "",
    "(Chocolate\s*cinnamon)" : "Chocolate cinnamon",
    "(ShopRiteSale\s*Price\s*\d+\.*\d*\s*LB\.*\s*\-\s*\d+\.*\d*\s*LB\.*\s*Limit\s*\d+\-lbs\.*)" : "",
    "(Turkey\s*Family)" : "Turkey Family",
    "(Breast\s*Iqf)" : "Breast IQF",
    "(Regular\s*Retail\s*\d+\.*\d*\s*Lb\.*\s*To\s*\d+\.*\d*\s*Ea\.*)" : "",
    "(Regular\s*Retails\s*\d+\.*\d*\s*lb\.*\s*to\s*\d+\.*\d*\s*lb\.*)" : "",
    "(\d+\.*\d*\s*with\s*additional\s*\d*\s*purchase\s*redeemable\s*only\s*at\s*ACME)" : "",
    "(Not\s*valid\s*toward\s*previous\s*purchase\.*)" : "",
    "(Items\s*may\s*not\s*be\s*available\s*in\s*all\s*locations\.*)" : "",
    "(In\s*the\s*event\s*of\s*return\s*coupon\s*savings\s*may\s*be\s*deducted\s*from\s*refund\.*)" : "",
    "(This\s*coupon\s*valid\s*at\s*ACME\s*locations\.*)" : "",
    "(Limit\s*one\s*offer\s*per\s*coupon\.*)" : "",
    "(XTRA\s*coupon\s*savings)" : "",
    "(Void\s*if\s*copied\s*or\s*transferred\.*)" : "",
    "(Boars\s*Head\s*STORE\s*COUPON\s*VALID\s*\d+\/\d+/\d+\-\d+\/\d+\/\d+)" : "",
    "(STORE\s*COUPON\s*VALID\s*\d+\/\d+/\d+\-\d+\/\d+\/\d+)" : "",
    "(Prices\s*on\s*package\s*reflects\s*Sale\s*Retail)" : "",
    "(Sold As Roast Only)" : "",
    "(Roast\s*Sold)" : "Roast Sold",
    "(Coupon\s*cannot\s*be\s*doubled\s*tripled\s*quadrupled\s*or\s*exchanged\s*for\s*cash\s*or\s*combined\s*with\s*any\s*other\s*offer\.*)" : "",
    "(\d+\.*\d*\s*lb\.*\s*with\s*additional\s*\d+\s*purchase\s*redeemable\s*only\s*at\s*ACME)" : "",
    "(Additional\s*Quantities\s*Or\s*Price\s*Without\s*Mymixx)" : "",
    "(Clip\s*And\s*Redeem\s*By\s*\d+\/\d+\/\d+)" : "",
    "(Must\s*Buy\s*Identical\s*Item\.*)" : "",
    "(\d+\s*The\s*Dannon\s*Company\s*Inc\.*\s*2017\s*WhiteWave\s*Services\s*Inc\.*)" : "",
    "(Try\s*one\s*of\s*our\s*fresh\s*salads\.*)" : "",
    "(cut\s*fresh\s*in\s*store\s*daily)" : "",
    "(crockpot\s*DINNER\s*IDEAS)" : "",
    "(Identical\s*item\s*only)" : "",
    "(BUY\s*\d+\s*of\s*these\**\s*Lancaster\s*Brand\s*Sliced\s*Bacon\s*\d+\s*oz\.*\s*pkg\.*\s*and\s*GET\s*\d+\s*of\s*these\s*Habbersett\s*or\s*Rapa\s*Scrapple\s*\d+\s*oz\.*\s*pkg\.*\s*or\s*Smithfield\s*Breakfast\s*Sausage\s*\d+\s*oz\.*\s*pkg\.*\s*links\s*or\s*patties\s*FOR\s*\d+)" : "",
    "(BUY\s*\d+\s*Monster\s*Energy\s*Drink\s*\d+\-pk\.*\s*\d+\s*fl\.*\s*oz\.*\s*cans\s*GET\s*\d+\s*FREE\**\s*Adult\s*Tickets\s*to\s*the\s*Monster\s*Energy\s*NASCAR\s*Cup\s*Series\s*Playoff\s*Race\s*on\s*October\s*\d+st\s*at\s*Dover\s*International\s*Speedway\s*\**)" : "",
    "(Offer\s*valid\s*thru\s*\d+\/\d+\/\d+\.*)" : "",
    "(Coupon\s*prints\s*at\s*register\.*)" : "",
    "(Purchase\s*must\s*be\s*made\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(Does\s*not\s*include\s*\d+\s*per\s*ticket\s*processing\s*fee\.*)" : "",
    "(SCORE\s*GREAT\s*DEALS\s*PARTICIPATING\s*ITEM)" : "",
    "(SAVE\s*\d+\s*INSTANTLY\s*when\s*you\s*buy\s*\d+\s*worth\s*of\s*any\s*of\s*these\s*participating\s*Campbells\s*Pepperidge\s*Farm\s*V\d+\s*or\s*Swanson\s*products\s*in\s*a\s*single\s*transaction\s*\d+\/\d+\/\d+\-\d+\/\d+\/\d+)" : "",
    "(\d+\s*for\s*\d+\.*\d*\s*WHEN\s*YOU\s*BUY\s*\d+\s*with\s*coupon\s*on\s*pg\.*\s*\d+\s*and\s*an\s*additional\s*\d+\s*purchase)" : "",
    "(Individual\s*Price\s*\d+\s*for\s*\d+)" : "",
    "(Surrounded\s*By\s*fillers\s*In\s*Deco\s*Craft\s*Sleeve\s*perfect\s*for\s*Roshhashanah\s*holiday)" : "",
    "(Additionalor\s*Lesser\s*quantities\s*will\s*Scan\s*At\d+\.*\d*\s*Ea)" : "",
    "(Assorted\s*Colors)" : "",
    "(limit\s*\d+)" : "",
    "(Offers\s*you\s*Save\s*\d+\.*\d*)" : "",
    "(Perfect\s*For\s*Cooking)" : "",
    "(Perfect\s*For\s*Your\s*Patio)" : "",
    "(Offers\s*must\s*buy\s*\d+)" : "",
    "(Seasonal\s*Assortment\s*Of)" : "",
    "(Will Rebloom Yearly)" : "",
    "(Great\s*Color\s*for\s*Your\s*Garden)" : "",
    "(Reblooms\s*Yearly\s*Fora\s*Beautiful\s*Garden\s*Of\s*Color)" : "",
    "(A\s*Seasonal\s*Assortment\s*Of)" : "",
    "(Freshclub\s*Size\s*Savings)" : "",
    "(no\s*Membership\s*Fees)" : "",
    "(for\s*Additional\s*Savings\s*Visitshoprite\.Com\/Clubsizesavings)" : "",
    "(Italianclub\s*Size\s*Savings)" : "",
    "(Produce\s*Pick\s*Of\s*The\s*Week)" : "",
    "(Yellow\s*Tomatoes\s*Are\s*Sweeter\s*In\s*Taste\s*Than\s*Traditional\s*Redtomatoes\s*And\s*Still\s*Provide\s*A\s*Good\s*Dose\s*Of\s*Vitamin\s*C\.*)" : "",
    "(Did\s*You\s*Know\s*Tomatoes\s*Taste\s*Best\s*When\s*Not\s*Refrigerated)" : "",
    "(Limit\s*\d+\s*Per\s*Variety)" : "",
    "(Save\s*up\s*To\s*\d+\.*\d*)" : "",
    "(\d+\.*\d*\s*Off\.*)" : "",
    "(Reg\.*\s*\d+\.*\d*\s*To\s*\d+\.*\d*\s*Ea\.*)" : "",
    "(\d+\/\d+\s*Price)" : "",
    "(Refastenable\s*Small\/Medium\s*Large\s*Or\s*extra\s*Large\s*Maximum\s*Absorbency)" : "",
    "(Look\s*For\s*\d+\.*\d*\s*Off)" : "",
    "(Mfr\s*Coupon\s*Inmost\s*Sunday\s*Papers\s*Registered\s*Trademark\s*Or\s*\**\s*Trademark\s*Of\s*Kimberly\-Clark\s*Worldwide\s*Inc\.\s*Kcww\.*)" : "",
    "(U\s*By\s*Kotex\s*Fitness\**\s*U\s*By\s*Kotex\s*Fitness\**)" : "U By Kotex Fitness",
    "(U\s*By\s*Kotex\s*U\s*By\s*Kotex)" : "U By Kotex",
    "(\d+\% Off)" : "",
    "(Assorted\s*varieties)" : "",
    "(Any\s*Variety)" : "",
    "(Buy\s*\d+\s*Schick\s*Quattro\s*Disposable\s*Razor\.*)" : "",
    "(Mens\s*Or\s*Womens\s*Schick\s*Slim\s*Twin\s*Razor\d+\-Ct\.*\s*Regluar\s*Sensitive\s*Womens\s*Or\s*Dry\s*Skin\s*Disposable\s*Schick\s*Xtreme\s*\d+\-Razors\s*\d+\.*\d*\s*And\s*Buy\s*\d+\s*Edge\s*Shave\s*Gel\d+\-Oz\.*)" : "",
    "(Excluding\s*Tropical\s*Splash\s*\d+\.*\d*)" : "",
    "(Save\s*At\s*Checkout\s*\d+\.*\d*)" : "",
    "(Must\s*Buy\s*Both\s*To\s*Receive\s*Discount\s*With\s*Price\s*Plus\s*Card)" : "",
    "(Limit\s*\d+\s*Offers\s*\d+\.*\d*\s*Off\s*With\s*Digital\s*Coupon\s*At\s*Shioprite\.Com\s*Limit\s*\d+)" : "",
    "(Assorted\s*Varieties\s*Excluding\s*Edgeinfused\s*And\s*Edge\s*Energy\s*Skintimate\s*Shave\s*Gel\d+\-Oz\.*)" : "",
    "(Extra\s*Clean)" : "",
    "(Limit \d+ Offers)" : "",
    "(discount\s*Will\s*Be\s*Applied\s*When\s*You\s*Buy\s*In\s*increments\s*Of\s*\d+\s*Only\.*)" : "",
    "(Less\s*Or\s*Additional\s*items\s*Will\s*Scan\s*At\s*\d+\s*Each\.*)" : "",
    "(Look\s*For\s*\d+\s*Off)" : "",
    "(Mfr\s*coupon\s*In\s*Most\s*Sunday\s*Papers)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*Save\s*\d+)" : "",
    "(Extra\s*Strength)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*SAVE\s*\d+\.*\d*)" : "",
    "(Yes\s*To\s*)" : "",
    "(\d+\.*\d*\s*Off)" : "",
    "(limit\s*\d+\s*Per\s*Variety)" : "",
    "(Any\s*Shade)" : "",
    "(Fits\s*All\s*Brita\s*Pitchers)" : "",
    "(Where\s*Available\s*While\s*Supplies Last)" : "",
    "(Breast\s*Cancer\s*Awareness\s*World\s*of)" : "",
    "(Breast\s*Cancer)" : "",
    "(Knock\s*The\s*Socks\s*Off\s*Breast\s*Cancer)" : "",
    "(Assorted\s*Color\s*And\s*Designs)" : "",
    "(Exclusively\s*At\s*Shoprite)" : "",
    "(Wrinkle\s*Free\s*Stain\s*Resistant\s*Deep\s*Pockets\s*Microfiber)" : "",
    "(includes\s*Batteries)" : "",
    "(You\s*Save\s*\d+\.*\d*)" : "",
    "(Less\s*Than\s*\d+\/\d+\s*Price)" : "",
    "(Limit\s*\d+\s*Per\s*Variety)" : "",
    "(Variety Seasonal)" : "",
    "(Cans\/Btls)" : "cans btls",
    "(Super Sampler Event)" : "",
    "(\d+\s*With\s*Digital\s*Coupon\s*At\s*Shoprite\.com)" : "",
    "(Must\s*Buy\s*\d+)" : "",
    "(Any\s*Variety\s*Of\s*Protein\s*Plus\s*Collezione\s*Or\s*Gluten\s*Free\s*Or)" : "",
    "(Oven\s*ready)" : "",
    "(Plus\s*Dep\.*\s*Or\s*fee\s*Where\s*Req\.*)" : "",
    "(Buy\s*More\.*Save\s*More)" : "",
    "(buy\s*\d+\s*For\s*\d+\.*\d*\s*Ea\.*)" : "",
    "(Save\s*\d+\.*\d*\s*Ea\.*\s*And\s*Buy\s*\d+\s*For\s*\d+\.*\d*\s*Ea\.*)" : "",
    "(Save\s*\d+\.*\d*\s*On\s*\d+\s*With\s*Price\s*Plus\s*Card\d*limit\s*\d+\s*Offer)" : "",
    "(Flavored\s*Water)" : "",
    "(\d+\.*\d*\s*Off\s*\d+\s*With\s*Digital\s*Coupon\s*At\s*Shoprite\.Com\s*)" : "",
    "(Buy\s*\d+\s*\d+\.*\d*\s*To\s*\d+\.*\d*\-Oz\.*\s*Box\s*\d+\-Ct\.*\s*Any\s*Variety\s*K\-Cups\s*Or\s*\d+\s*To\s*\d+\-Oz\.*\s*Bag\s*Any\s*Variety\s*Whole\s*Bean\s*Or\s*Groundstarbuckscoffee\s*\d+\.*\d*\s*Limit\s*\d+\s*Per\s*Variety\s*Save\s*Up\s*To\s*\d+\.*\d*\s*And\s*Get\s*\d+\s*\d+\.*\d*\s*To\s*\d+\.*\d*\-Oz\.*\s*Bag\s*Any\s*Variety\s*pepperidge\s*Farmmilano\s*Cookies\s*Free\s*With\s*Price\s*Plus\s*Card)" : "",
    "(Buy \d+ \d+\-Cz\.* Tot\.* Wt\.* Btls\.* \d+\-Oz\.* Bottles Any Variety\s*gatorade Drinks\d+\-Pack \d+ For \d+\.*\d*)" : "",
    "(And Get \d+ \d+\.*\d*\-Oz\.* Tot\.* Wt\.* Btls\.* Plus Dep\.* Or Feewhere Req\.* \d+\.*\d*\-Oz\.* Bottles Any VarietyWater Beveragepropel Zero \d+\-Pack Free With Price Plus Card You Save \d+\.*\d*)" : "",
    "(Limit\s*\d+\s*SAVE\s*\d+)" : "",
    "(\d+\.*\d*\s*OFF\s*WITH\s*DIGITAL\s*COUPON\s*AT\s*SHOPRITE\.COM)" : "",
    "(\s*\-*\s*Assorted\s*Shades)" : "",
    "(Regular\s*Retails\s*\d+\.*\d*\s*to\s*\d+\.*\d*\s*ea\.*)" : "",
    "(Buy \d+ \d+\-Oz\.* Horizon Organic Yogurt Or \d+\-Oz\.* Cont\.* Oikos Or Light \&Fit Drinks \d+ To \d+\.*\d*\-Oz\.* Cont\.* Crunch Greek Any Variety OikosLight \& Fit Greek Mousse Triple Zero Light \& Fit Zero Ordannon Greek Yogurt \d+ For \d+  \d+\-Oz\.* Cont\.* Any Variety Dunkin Donuts Coffee Creamers Orinternational Delight Creamer)" : "",
    "(Limit\s*\d+\s*Offers\.*)" : "",
    "(Free\s*With\s*Price\s*Plus\s*Card\s*You\s*Save\s*\d+\.*\d*)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*And\.*\s*Get\d+)" : "",
    "(Plus\s*Limit\s*\d+\s*Offers\s*Discount\s*Will\s*Be\s*Applied\s*When\s*You\s*Buy\s*In\s*Increments\s*Of\s*\d+\s*Only\.*)" : "",
    "(Less\s*Or\s*Additional\s*Items\s*Will\s*Scan\s*At\s*\d+\.\d+\s*Each\.*)" : "",
    "(Fresh\s*Meaty\s*Breast\s*Bone\s*Removed)" : "",
    "(Any\s*Variety\s*\d+\/\d+\s*Price)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*You\s*Save\s*\d+)" : "",
    "(shopritesale\s*Price\s*\d+\.*\d*\s*Lb\.*\s*\-\s*\d+\.*\d*\s*Lb\.*)" : "",
    "(Fresh\s*Locally\s*Raised\s*Raised\s*Without\s*Antibiotics)" : "",
    "(Limit\s*\d+\-Pkgs\.*)" : "",
    "(Local\s*beef\s*\&\s*Pork\s*Raised\s*On\s*Family\s*Farms)" : "",
    "(Where\s*available)" : "",
    "(Assorted\s*Shades)" : "",
    "(Any\s*Variety)" : "",
    "(Fully\s*Cooked)" : "",
    "(Heat\s*\&\s*Eat)" : "",
    "(Assorted\s*Varieties)" : "",
    "(\d+\s*Off\s*With\s*Digital\s*Coupon\s*At\s*Shoprite\.Com)" : "",
    "(Limit\s*\d+)" : "",
    "(Product\s*Of\s*Australia)" : "",
    "(No\s*Antibiotics\s*Ever)" : "",
    "(u\.S\.\s*Grade\s*A)" : "",
    "(Responsibly\s*Raised)" : "",
    "(Peeled\s*\&\s*Deveined\s*Tail\s*Off)" : "",
    "(Farm\s*Raised\s*In\s*Idaho\s*Dressed\s*Never\s*Frozen)" : "",

    "(catch\s*of\s*The\s*week)" : "",
    "(Line\s*Caught)" : "",
    "(Never\s*Frozen\s*U.S.\s*Grade\s*A)" : "",
    "(Store\s*Baked)" : "",
    "(Pkg\.*\s*Of\s*\d+)" : "",
    "(Hand\s*Mademade\s*With\s*greek\s*Yogurtand\s*Locally\s*grown\s*zucchini)" : "",
    "(Store\s*Made)" : "",
    "(New\s*flavor\s*For\s*fall)" : "",
    "(Fall\s*Favorites)" : "",
    "(Excluding\s*Family\s*Size)" : "",
    "(Any\s*Variety)" : "",
    "(Seedless\s*regular\s*Or\s*Golden)" : "",
    "(Limit\s*\d+\s*YOU\s*SAVE\s*\d+\.*\d*)" : "",
    "(National\s*Breast\s*Cancer\s*Foundation)" : "",
    "(SAVE\s*\d+\.*\d*)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+\.*\d*)" : "",
    "(or\s*AA)" : "or AA",
    "(Xtralife)" : "",
    "(Reg\.*\s*Retails\s*\d+\.*\d*\s*to\s*\d+\.*\d*\s*ea\.*\s*Limit\s*\d+\s*Per\s*Variety)" : "",
    "(Limit\s*\d+\s*YOU\s*SAVE\s*\d+\.*\d*)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+\.*\d*)" : "",
    "(Model\s*No\.*\s*\d+t\d+\-qt\.*\s*with\s*Lid\s*save\s*\d+\.*\d*)" : "",
    "(Reg\.*\s*Retails\s*\d+\.*\d*\s*to\s*\d+\.*\d*\s*ea\.*)" : "",
    "(Where\s*Available\s*While\s*Supplies\s*Last)" : "",
    "(Must\s*Buy\s*\d+\s*Limit\s*\d+\s*Offer)" : "",
    "(Store\s*Sliced)" : "",
    "(Each\s*Equal\s*Parts\s*Roasted\s*Or\s*available)" : "",
    "(limit\s*\d+\s*Per\s*Variety\s*You\s*Save\s*\d+\.*\d+)" : "",
    "(Hot\s*Or\s*Freshly\s*Chilled)" : "",
    "(fried\s*In\s*trans\s*Fat\s*free\s*Oil)" : "",
    "(Select\s*Varieties\s*limit\s*\d+\s*Per\s*Variety\s*You\s*Save\s*\d+\.*\d*)" : "",
    "(Hot\s*Or\s*Sweet)" : "",
    "(Non\-*Gmo)" : "",
    "(Antibiotic\s*Free)" : "",
    "(You\s*Wont\s*Find\s*Higher\s*Quality\s*In\s*Any\s*Other\s*Sandwich\s*Shop\s*Or\s*Deli)" : "",
    "(Natural\s*Casing\s*Meat)" : "",
    "(Greek\s*or\s*Limit\s*\d+\s*Per\s*Variety)" : "",
    "(Excluding\s*sugar)" : "Excluding sugar",
    "(New\s*At\s*Shoprite)" : "",
    "(\d+\s*For\s*\d+\s*With\s*Digital\s*Coupon\s*At\s*Shoprite\.Com\s*Must\s*Buy\s*\d+\s*Limit\s*\d+\s*Offer)" : "",
    "(Low\s*Salt)" : "",
    "(Imported\s*Parmesan)" : "Imported Parmesan",
    "(Excluding\s*Greek)" : "Excluding Greek",
    "(limit\s*\d+\s*Per\s*Variety)" : "",
    "(Buy\s*\d+\s*Get\s*\d+\s*Free)" : "",
    "(Limit\s*\d+\s*Offers\s*You\s*Save\s*\d+\.*\d*)" : "",
    "(Yogurt drink)" : "Yogurt Drink",
    "(\d+\s*For\s*\d+\s*With\s*Digital\s*Coupon\s*At\s*Shoprite\.Com)" : "",
    "(Limit\s*\d+\s*You\s*Save\s*\d+\.*\d*)" : "",
    "(Never\s*Administered\s*Antibiotics)" : "",
    "(you\s*Save\s*\d+\.*\d*\s*Limit\s*\d+\s*Per\s*Variety\s*With\s*Price\s*Plus\s*Card\s*\d+\.*\d*\s*Instant\s*Bonus\s*Bucks\s*\-*\d+\.*\d*)" : "",
    "(save\s*Up\s*To\s*\d+\.*\d*\s*Limit\s*\d+\s*Per\s*Variety\s*With\s*Price\s*Plus\s*Card\s*\d+\.*\d*\s*Instant\s*Bonus\s*Bucks\s*\-*\d+\.*\d*)" : "",
    "(You\s*Save\s*\d+\.*\d*\s*Limit\s*\d+\s*With\s*Price\s*Plus\s*Card\s*\d+\.*\d*\s*Instant\s*Bonus\s*Bucks\s*\-*\d+\.*\d*)" : "",
    "(\d+\.*\d*\s*Instant\s*Bonus\s*Bucks\s*\-*\d+\.*\d*)" : "",
    "(you\s*Save\s*\d+\s*Limit\s*\d+\s*With\s*Price\s*Plus\s*Card\s*\d+\.*\d*\s*Instant\s*Bonus\s*Bucks\s*\-*\d+\.*\d*)" : "",
    "(Look\s*For\s*\d+\.*\d*\s*Off\s*\d+\s*Mfr\s*Coupon\s*in\s*Most\s*sunday\s*Papers\s*better\s*Together)" : "",
    "(better\s*Together)" : "",
    "(limit\s*\d+\s*Offers\.*)" : "",
    "(Discount\s*will\s*Be\s*Applied\s*when\s*You\s*Buy\s*in\s*Increments\s*of\s*\d+\s*Only\.*)" : "",
    "(Less\s*Or\s*Additional\s*Items\s*Will\s*Scan\s*At\s*\d+\.*\d*\s*Each\.*)" : "",
    "(Look\s*For\s*\d+\.*\d*\s*Off\s*\d+\s*Mfr\s*Coupon\s*in\s*Most\s*sunday\s*Papers)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+\s*OFF\s*with\s*Digital\s*Coupon\s*at\s*shoprite\.com\s*Limit\s*\d+)" : "",
    "(Regular\s*rolls)" : "Regular rolls",
    "(Limit\s*\d+\s*Offers\s*MUST\s*BUY\s*\d+\s*Additional\s*or\s*lesser\s*quantities\s*will\s*scan\s*at\s*\d+\s*for\s*\d+\.*\.*\d*\s*OFF\s*\d+\s*with\s*Digital\s*Coupon\s*at\s*shoprite\.com\s*Must\s*Buy\s*\d+\s*Limit\s*\d+\s*Offer)" : "",
    "(Free\s*Plus)" : "Free Plus",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+\.*\d*\s*OFF\s*with\s*Digital\s*Coupon\s*at\s*shoprite\.com\s*Limit\s*\d+)" : "",
    "(Seasonal\s*Organic)" : "Seasonal Organic",
    "(and\s*warm)" : "and Warm",
    "(cans\s*Mtn)" : "cans Mtn",
    "(bottles\s*Dr)" : "bottles Dr",
    "(Seagrams\s*Sprite)" : "Seagrams Sprite",
    "(Little\s*snugglers)" : "Little Snugglers",
    "(Overnites\s*Goodnites)" : "Overnites Goodnites",
    "(Club\s*Soda\s*or\s*Any\s*Variety)" : "Club Soda",
    "(bag\s*Excluding)" : "bag Excluding",
    "(Frost\s*or)" : "Frost or",
    "(Whips\s*or\s*Any\s*Variety)" : "Whips",
    "(Bowls\s*or\s*Any\s*Variety)" : "Bowls",
    "(oz\s*Bowls)" : "oz Bowls",
    "(Box\s*Triple)" : "box Triple",
    "(oz\s*box)" : "oz box",
    "(Spray\s*Childrens)" : "Spray Childrens",
    "(Limit\s*\d+\s*Offers\s*MUST\s*BUY\s*\d+\s*Additional\s*or\s*lesser\s*quantities\s*will\s*scan\s*at\s*\d+\.*\d*\s*for\s*\d+\.*\d*)" : "",
    "(Limit\s*\d+\s*Per\s*Variety\s*YOU\s*SAVE\s*\d+\.*\d*\s*\d+\.*\d*\s*OFF\s*With\s*Digital\s*coupon\s*at\s*Shorite\.com\s*limit\s*\d+)" : "",
    "(Italian\s*Extra\s*Virgin\s*Olive\s*Oil)" : "Italian Olive Oil",
    "(Yogurt\s*Drink)" : "Yogurt Drink",
    "(Simply\s*\d+\s*flips)" : "",
    "(pkg\.*\s*Neufchatel)" : "pkg Neufchatel",
    "(Dozen\s*Cage)" : "Dozen Cage",
    "(Quarters\s*Salted)" : "Quarters Salted",
    "(Sheet\s*Fettucine)" : "Sheet Fettucine",
    "(Rosemary\s*Tomato)" : "Rosemary Tomato",
    "(YOU\s*WON\'*T\s*FIND\s*HIGHER\s*QUALITY\s*IN\s*ANY\s*OTHER\s*SANDWICH\s*SHOP\s*OR\s*DELI)" : "",
    "(Sriracha\s*Zesty)" : "Sriracha Zesty",
    "(Greek\s*or\s*Limit\s*\d+\s*Per\s*Variety\s*you\s*save\s*\d+\.*\d*)" : "Greek",
    "(oz\.*\s*box)" : "oz box",
    "(box\s*Reclosable)" : "box Reclosable",
    "(Grade\s*A\s*Dozen)" : "Grade A Dozen",
    "(Kaiser\s*Regular)" : "Kaiser Regular",
    "(Oil\s*Kneadin)" : "Oil Kneadin",
    "(Corn\s*Blueberry)" : "Corn Blueberry",
    "(oz\.*\s*Round)" : "oz Round",
    "(\&\s*Skinless)" : "& Skinless",
    "(Farm\s*Raised\s*in\s*Idaho\s*Dressed\s*Never\s*Frozen\s*U\.S\.\s*GRADE\s*A\s*ShopRiteSale\s*Price\s*\d+\.*\d*\s*LB\.*\s*\-\s*\d+\s*LB\.*\s*Limit\s*\d+\-lbs\*.)" : "",
    "(Responsibly\s*Raised\s*Peeled\s*\&\s*Deveined\s*Tail\s*Off\s*ShopRiteSale\s*Price\s*\d+\.*\d*\s*lb\.*\s*\-*\s*\d+\.*\d*\s*lb\.*\s*Limit\s*\d+\-*lbs\.*)" : "",
    "(Fed\s*A\s*Vegetarian\s*Diet)" : "",
    "(Local\s*beef\s*\&\s*Pork\s*Raised\s*On\s*Family\s*Farms)" : "",
    "(oz\.*\s*bottles)" : "oz bottles",
    "(Custard\s*Sweet)" : "Custard Sweet",
    "(cans\s*Izze)" : "cans Izze",
    "(bag\s*Excluding)" : "bag Excluding",
    "(oz\.*\s*Bowls)" : "oz Bowls",
    "(oz\s*box)" : "oz box",
    "(liquid\s*scentables)" : "liquid Scentables",
    "(Limit\s*\d+\s*offer)" : "",
    "(\d+\s*DAY\s*SALE\s*FRIDAY\s*SEPTEMBER\s*\d+ND\s*THRU\s*MONDAY\s*SEPTEMBER\s*\d+TH)" : "",
    "(\s*OR\s*FREE\s*Instantly\s*When\s*you\s*buy\s*\d+\s*Knorr\s*Pasta\s*Sides\**\s*\d+\s*value)" : "",
    "(PLUS\s*DON\'*T\s*MISS\s*THESE\s*XTRAsavings\!*\s*ON\s*YOUR\s*HOUSEHOLD\s*FAVORITES\!*)" : "",
    "(stock\s*up\s*and\s*SAVE)" : "",
    "(grocery\s*\&\s*snack\s*SAVINGS)" : "",
    "(\s*Gluten\s*Free\s*savings)" : "",
    "(\s*Pet\s*Savings)" : "",
    "(tasty\s*organic\s*favorites\s*from\s*Annies\s*Homegrown\s*\"*\s*Organic\s*for\s*Everybunny\s*\"*\s*USDA\s*ORGANIC\.*)" : "",
    "(SAVE\s*EVEN\s*MORE\s*WITH\s*THESE\s*EXTENDED\s*GOOD\s*THRU\s*XTRAsavings\!*)" : "",
    "(\s*beverage\s*SAVINGS)" : "",
    "(Knorr\s*Sides\s*Knorr\s*Sides)" : "Knorr Sides",
    "(ACME\s*DON\'*T\s*MISS\s*THESE\s*XTRAsavings\!*)" : "",
    "(\$*\d+\.*\d*\s*ea\.*\-*\$*\d+\.*\d*\s*ea\.*\s*INSTANT\s*SAVINGS\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*SAVE\s*\$\d+\.*\d*\s*INSTANTLY\!*)" : "",
    "(WHEN\s*YOU\s*BUY\s*\d+\s*PARTICIPATING\s*ITEMS\s*IN\s*A\s*SINGLE\s*TRANSACTION\.*)" : "",
    "(Lucerne\s*DAIRY\s*FARMS\s*SINCE\s*\d+\.*\s*DOLLAR\s*DAYS)" : "",
    "(Offer\s*valid\s*\d+\/\d+\-\d+\/\d+\s*\**Participating\s*items\s*must\s*be\s*purchased\s*in\s*a\s*single\s*transaction\s*with\s*Card\.*)" : "",
    "(See\s*store\s*and\s*display\s*for\s*full\s*details\.*)" : "",
    "(Online\s*and\s*in\-store\s*prices\s*offers\s*and\s*discounts\s*may\s*differ\.*)" : "",
    "(Not\s*all\s*varieties\s*available\s*in\s*all\s*stores\.*)" : "",
    "(Customer\s*pays\s*tax\s*and\s*CRV\s*where\s*applicable\.*)" : "",
    "(Discount\s*taken\s*at\s*the\s*register\.*)" : "",
    "(FREE\s*TREAT\s*WITH\s*A\s*SCARY\s*MOVIE\!*\s*Buy\s*select\s*Halloween\s*DVDs\s*for\s*\$*\d+\.*\d*\s*ea\.*\s*DVD\s*AND\s*GET\s*ONE\s*\d+\s*MARS\s*Brand\s*Fun\s*Size\s*Bags\s*\d+\.*\d*\s*oz\.*\s*\-*\s*\d+\.*\d*\s*oz\.*\s*\$*\d+\.*\d*\s*Estimated\s*Value\s*includes\s*M\&MS\s*SNICKERS\s*TWIX\s*\d+MUSKETEERS\s*and\s*MILKYWAY\s*FREE*)" : "",
    "(\s*\/\s*trademarks\s*Mars\s*Incorporated\s*\d+)" : "",
    "(Verlasso\s*is\s*a\s*premium\s*salmon\s*raised\s*to\s*promote\s*balance\s*between\s*our\s*need\s*and\s*the\s*need\s*of\s*the\s*environment\.*)" : "",
    "(Maintaining\s*this\s*equilibrium\s*is\s*at\s*the\s*heart\s*of\s*everything\s*we\s*do\.*)" : "",
    "(Celebrating\s*four\s*years\s*as\s*Monterey\s*Bay\s*Aquariums\s*first\s*to\s*be\s*approved\s*ocean\s*raised\s*Atlantic\s*salmon\.*\s*www\.verlasso\.com)" : "",
    "(Oikos\s*Is\s*A\s*Registered\s*Trademark\s*Of\s*Stonyfield\s*Farm\s*Inc\.*)" : "",
    "(\d+\s*The\s*Dannon\s*Company\s*Inc\.*)" : "",
    "(\d+\%\s*Less\s*Sugar\s*Than\s*Other\s*Traditional\s*Yogurts)" : "",
    "(\d+\s*Chobani\s*Llc)" : "",
    "(A\s*Traditional\s*Yogurt\s*By\s*)" : "",
    "(Other\s*Traditional\s*Yogurts\s*\d+G\s*Sugar\s*\d+G\s*Protein)" : "",
    "(Chobani\s*Chobani)" : "Chobani",
    "(quick\s*meal\s*ideas)" : "",
    "(burger\s*NIGHT)" : "",
    "(CHOOSE\s*YOUR\s*FAVORITES\s*Bagel\s*Weekend\s*Every\s*Saturday\s*\&\s*Sunday\s*mix\s*or\s*match)" : "",
    "(\d+\.*\d*\s*ea\.*\-\d+\s*ea\.*\s*INSTANT\s*SAVINGS\s*WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*SAVE\s*\d+\s*INSTANTLY)" : "",
    "(All\s*varieties\.*)" : "",
    "(Bakery\s*Dept\.*)" : "",
    "(All\s*items\s*must\s*be\s*purchased\s*in\s*the\s*single\s*transaction\.*)" : "",
    "(No\s*cash\s*back\.*)" : "",
    "(Select\s*varieties\.*)" : "",
    "(Plus\s*deposit\s*where\s*applicable\.*)" : "",
    "(\s*for\s*\d+\.*\d*)" : "",
    "(Select\s*Styles\s*\&\s*Varieties)" : "",
    "(First\s*of\s*the\s*Season)" : "",
    "(First\s*of\s*the\s*Season\s*or)" : "",
    "(Honeycrisp\s*Apples)" : "Honeycrisp Apples",
    "(\d+\.*\d*\s*lb\s*with\s*Card)" : "",
    "(Healthy\s*and\s*Delicious)" : "",
    "(Found\s*in\s*the\s*Produce\s*Department)" : "",
    "(Found\s*in\s*Bakery)" : "",
    "(Found\s*in\s*the\s*Meat\s*Department)" : "",
    "(Order\s*Online\s*by\s*Phone\s*or\s*in\s*Person)" : "",
    "(Participating\s*Varieties\s*and\s*Sizes\s*May\s*Vary\s*by\s*Store)" : "",
    "(Limited\s*Time\s*Originals)" : "",
    "(Sliced\s*to\s*Order)" : "",
    "(Sliced\s*to\s*Order\s*or\s*Prepackaged\s*for\s*Your\s*Convenience)" : "",
    "(AND\s*FAMOUS\s*FOR\s*FLAVOR\.*)" : "",
    "(FOUND\s*IN\s*THE\s*SPECIALTYCHEESE\s*DEPARTMENT\.*)" : "",
    "(Sold\s*by\s*the\s*Each\s*or\s*Giant\s*Spareribs\s*Previously\s*Frozen\s*or\s*Chicken\s*Tenderloins\s*Sold\s*by\s*the\s*Pound)" : "",
    "(ADDITIONAL\s*QUANTITIES\s*\&\s*REST\s*OF\s*WEEK\s*\d+\/\d+)" : "",
    "(Up\s*to\s*\d+\%\s*Solution\s*Added)" : "",
    "(oz\.*\s*Excludes)" : "oz Excludes",
    "(\d+\s*DAY\s*SALE\s*FRIDAY\s*SEPTEMBER\s*\d+ND\s*THRU\s*MONDAY\s*SEPTEMBER\s*\d+TH)" : "",
    "(cut\s*fresh\s*in\-store\s*daily)" : "",
    "(Additional\s*quantities\s*\d+\.*\d*\s*lb\.*\s*discount\s*given\s*at\s*register)" : "",
    "(BUY\s*\d+\s*of\s*these\s*Ferrera\s*Cherry\s*Tomato\s*Pasta\s*Sauce\s*\d+\s*oz\.*\s*jar\s*and\s*GET\s*\d+\s*of\s*these\s*Signature\s*Kitchens\s*Pasta\s*\d+\-\d+\s*oz\.*\s*pkg\.*\s*excludes\s*lasagna\s*jumbo\s*shells\s*and\s*manicotti\s*FREE\s*INSTANTLY\s*\d+\s*value\s*\**\s*)" : "",
    "(grocery\s*\&\s*snack\s*SAVINGS)" : "",
    "(Limit\s*\d+\s*offer\.*)" : "",
    "(Purchase\s*must\s*be\s*made\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(All\s*items\s*must\s*be\s*purchased\s*in\s*a\s*single\s*transaction\.*)" : "",
    "(Participating\s*Sizes\s*and\s*Varieties\s*May\s*Vary\s*by\s*Store)" : "",
    "(Great\s*Tasting\s*ADDITIONAL\s*QUANTITIES\s*\&\s*REST\s*OF\s*WEEK\s*\d+\.*\d*\/lb\.*)" : "",
    "(LEMON\s*BLISS\s*CAKE\s*KING\s*ARTHUR\s*FLOUR\s*RECIPE\s*OF\s*THE\s*YEAR)" : "",
    "(SAVE\s*\d+\s*ON\s*BERRIES)" : "",
    "(WHEN\s*YOU\s*BUY\s*ANY\s*\d+\s*PARTICIPATING\s*PRODUCTS\s*CORN\s*FLAKES\s*OR\s*RICE\s*KRISPIES\s*\d+\s*OZ\.*\s*CRISPIX\s*\d+\s*OZ\.*\s*FROSTED\s*BITE\s*SIZE\s*MINI\s*WHEATS\s*\d+\s*OZ\.*\s*FROSTED\s*FLAKES\s*\d+\s*OZ\.*\s*RAISIN\s*BRAN\s*\d+\.*\d*\s*OZ\.*\s*MIX\s*OR\s*MATCH\.*)" : "",
    "(OFFER\s*VALID\s*\d+\/\d+\/\d+\/\d+\/\d+\.*)" : "",
    "(Go\s*Lean)" : "",
    "(Soups\s*on)" : "",
    "(Get\s*into\s*the\s*season\s*with\s*savings\.*)" : "",
    "(Baking\s*Essentials\.*)" : "",
    "(breakfast\s*essentials)" : "",
    "(WE\s*LOVE\s*LOCAL\s*LOCALLY\s*GROWN\s*PRODUCE\.*)" : "",
    "(CHOOSE\s*YOUR\s*FAVORITES\s*Bagel\s*Weekend\s*mix\s*or\s*match\.*)" : "",
    "(antibiotic\s*free\s*meats\s*or\s*rBst\s*free\s*cheeses\.*)" : "",
    "(\d+\s*drumsticks\s*\d+\s*wings\s*\d+\s*breasts\s*and\s*\d+\s*thighs\s*Individual\s*Price\s*\d+\.*\d*\s*ea\.*)" : "",
    "(CHEEP\s*CHICKEN\s*WEEK)" : "",
    "(Escapes\s*Maxwell)" : "Escapes Maxwell",
    "(Sale\s*Price\s*\d+\s*for\s*\d+\s*Limit\s*\d+\s*Rewards\s*Per\s*Transaction\s*MIX\s*\&\s*MATCH)" : "",
    "(\d+\s*FOR\s*\d+\s*DOWNLOAD\s*EXTRA\s*SAVINGS\.*)" : "",

    # Remove apostrophes and ampersands.
    "(\u\d+)" : "",
    # Remove spaces from begining of complete description.
    "^\s*": "",
    # Remove spaces from end of complete description.
    "\s*$": "",
    # Remove multiple spaces before a dot or inbetween two dots.
    "\.*\s*\.": ".",

    # Template
    # "()" : "",
}

DIRTY_SYMBOLS_PATTERNS = {
    # Remove all the special characters.
    # But keep these ones.
    "[^A-Za-z0-9\"\'\.\-\_\s\&\%\/]+": "",
}

DIRTY_ABBREVIATIONS_PATTERNS = {
    # Clean up all the dots on the end for common abbreviations.
    "(\'s)" : "'s",
    "(\'t)" : "'t",
    "(\s+7\s*up)" : " 7up",
    "(\s+7\s*\-\s*up)" : " 7up",
    "(^7\s*up)" : "7up",
    "(\s+aa\.*)" : " AA",
    "(\s+aaa\.*)" : " AAA",
    "(\s+ABV\.*)" : " ABV",
    "( and )" : " and ",
    "(\s+avg\.*)" : " avg",
    "(\s+bag\.*)" : " bag",
    "(\s+bbq\.*)" : " BBQ",
    "(\s+btl\.*)" : " btl",
    "(\s+btls\.*)" : " btls",
    "(\s+bottle\.*)" : " bottle",
    "(\s+bottles\.*)" : " bottles",
    "(\s+bowls\.*)" : " bowls",
    "(\s+box\.*)" : " box",
    "(\s+boxes\.*)" : " boxes",
    "(\s+bunches\.*)" : " bunches",
    "(\s+can\.*)" : " can",
    "(\s+cans\.*)" : " cans",
    "(\s+cartons\.*)" : " cartons",
    "(\s+caught\.*)" : " caught",
    "(\s+Cereal\.*)" : " cereal",
    "(\s+cont\.*)" : " cont",
    "(\s+ct\.*)" : " ct",
    "(\-\s*ct\.*\/lb\.*)" : " ct/lb",
    "(\-\s*ct\.*)" : " ct",
    "(\s+ctn\.*)" : " ctn",
    "(\s+ctns\.*)" : " ctns",
    "(\s+cont\.*)" : " cont",
    "(\s+CRV\.*)" : " CRV",
    "(\s+cz\.*)" : " cz",
    "(\-\s*cz\.*)" : " cz",
    "(\s+dbl\.*)" : " dbl",
    "(\s+dvd\s+)" : " DVD ",
    "(\s+dvds\s+)" : " DVDs ",
    "(\s+dvd\.*)" : " DVD",
    "(\s+fl\.*)" : " fl",
    "(\-\s*fl\.*)" : " fl",
    "(\s+for\s+)" : " for ",
    "(\s+from\s+)" : " from ",
    "(\s+frozen\.*)" : " frozen",
    "(\s+ft\.*)" : " ft",
    "(\s+hdtv\s*)" : " HDTV ",
    "(\s+gal\.*)" : " gal",
    "(\-\s*gal\.*)" : " gal",
    "(\s+in\.*)" : " in",
    "(\s+inch\.*)" : " inch",
    "(\-\s*inch\.*)" : " inch",
    "(\s*ipa\.*)" : " IPA",
    "(\s*ipad\.*)" : " iPAD",
    "(\s*iqf\.*)" : " IQF",
    "(\s+jar\.*)" : " jar",
    "(\s+jr\.*)" : " jr",
    "(\s+jug\.*)" : " jug",
    "(\s+lb\.*)" : " lb",
    "(\-\s*lb\.*)" : " lb",
    "(\s+lbs\.*)" : " lb",
    "(\-\s*liter\.*)" : " liter",
    "(\s+liter\.*)" : " liter",
    "(\s+liquid\.*)" : " liquid",
    "(\s+ltr\.*)" : " ltr",
    "(\s+mg\.*)" : " mg",
    "(\s+ml\.*)" : " ml",
    "(\-\s*ml\.*)" : " ml",
    "(^mta\s+)" : "MTA ",
    "(\s+mta\s+)" : " MTA ",
    "(mw\.*)" : " mw",
    "(^nfl\s+)" : "NFL ",
    "(\s+nfl\s+)" : " NFL ",
    "(\s+of\s+)" : " of ",
    "(\s+on\s+)" : " on ",
    "(\s+or\s+)" : " or ",
    "(\s+oz\.*)" : " oz",
    "(\-\s*oz\.*)" : " oz",
    "(\s+pack\.*)" : " pack",
    "(\-\s*pack\.*)" : " pack",
    "(\s+package\.*)" : " package",
    "(\s+pc\.*)" : " pc",
    "(\-\s*pc\.*)" : " pc",
    "(\s+pk\.*)" : " pk",
    "(\-\s*pk\.*)" : " pk",
    "(\s+pkg\.*)" : " pkg",
    "(\s+pkgs\.*)" : " pkgs",
    "(\s+ply\.*)" : " ply",
    "(\-\s*ply\.*)" : " ply",
    "(\s+pr\.*)" : " pr",
    "(\s+pt\.*)" : " pt",
    "(\s+rv\s+)" : " RV ",
    "(\s+pouches\.*)" : " pouches",
    "(\s+qt\.*)" : " qt",
    "(\-\s*qt\.*)" : " qt",
    "(\s+raised\.*)" : " raised",
    "(\s+rolls\.*)" : " rolls",
    "(\s+sht\.*)" : " sht",
    "(\s+sq\.*)" : " sq",
    "(\s+stem\.*)" : " stem",
    "(\-\s*stem\.*)" : " stem",
    "(\s+the\s+)" : " the ",
    "(\s+to\s+)" : " to ",
    "(\s+tot\.*)" : " tot",
    "(\-\s*tot\.*)" : " tot",
    "(\s+with\s+)" : " with ",
    "(\s+wt\.*)" : " wt",
    "(\s+yd\.*)" : " yd",
}

