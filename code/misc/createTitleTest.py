#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Line 1 
# 

NUMBER_IN_A_PAIR = 2

INPUTFILE = "./inputTitleTest.txt"

# Keep track of input lines.
pairCount = NUMBER_IN_A_PAIR
inputTitle = ""
inputDescription = ""


with open(INPUTFILE, 'r') as fileHandle:
    for currentLine in fileHandle:
        pairCount -= 1
        if pairCount == 1:
            inputTitle = currentLine.rstrip("\r\n")

        elif pairCount == 0:
            inputDescription = currentLine.rstrip("\r\n")

            testName = inputTitle
            testName = testName.replace(".", "_")
            testName = testName.replace(" ", "_")
            testName = re.sub('[^A-Za-z0-9\_]+', '', testName)

            expectedTitle = inputTitle + " " + inputDescription
            expectedTitle = expectedTitle.title()

            testPrice = "9.99"

            print "    def test_" + testName + "(self):"
            print ""
            print "        # Input and expected result."
            print "        test_input_title = \"" + inputTitle + "\""
            print "        test_input_description = \"" + inputDescription + "\""
            print "        test_input_price = \"" + testPrice + "\""
            print "        test_expected_price_cleansed = float(9.99)"
            print "        test_expected_multibuy = \"\""
            print "        test_expected_promotion_type = PRICE_REDUCTION"
            print "        test_expected_title_cleansed = \"" + expectedTitle + "\""
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

            # Reset.
            pairCount = NUMBER_IN_A_PAIR

