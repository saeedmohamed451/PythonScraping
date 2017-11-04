#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Line 1 
# 


INPUTFILE = "./inputPriceTest.txt"

with open(INPUTFILE, 'r') as fileHandle:
    for currentLine in fileHandle:

        
        testName = currentLine.rstrip("\r\n")
        testName = testName.replace(".", "_")
        testName = testName.replace(" ", "_")
        testName = re.sub('[^A-Za-z0-9\_]+', '', testName)
        testPrice = currentLine.rstrip("\r\n")

        print "    def test_" + testName + "(self):"
        print ""
        print "        # Input and expected result."
        print "        test_input_title = \"test title\""
        print "        test_input_description = \"test description\""
        print "        test_input_price = \"" + testPrice + "\""
        print "        test_expected_price_cleansed = float(-1.00)"
        print "        test_expected_multibuy = \"\""
        print "        test_expected_promotion_type = PRICE_REDUCTION"
        print "        test_expected_title_cleansed = \"Test Title Test Description\""
        print ""
        print "        # Perform the test"
        print "        self.dut.mTitle = test_input_title"
        print "        self.dut.mDescription = test_input_description"
        print "        self.dut.mPrice = test_input_price"
        print "        # Perform the cleanse."
        print "        self.dut.cleanse()"
        print "        # Verify the result."
        print "        assert self.dut.mTitleCleansed == test_expected_title_cleansed"
        print "        assert self.dut.mPriceCleansed == test_expected_price_cleansed"
        print "        assert self.dut.mMultibuy == test_expected_multibuy"
        print "        assert self.dut.mPromotionType == test_expected_promotion_type"
        print ""





