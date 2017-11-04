#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from StoreItem import StoreItem

# Get the Promotion Type categories.
from DataCleanse import *


#
# Categorise all tests for the Flipp Retailers.
#
class TestFlippForWalmart(object):

    #
    # Create the Device Under Test (DUT).
    #
    def setup_method(self, method):
        self.dut = StoreItem()

    #
    # Perform any necessary clean-up.
    #
    def teardown_method(self, method):
        pass

    ##############
    # Test-Cases #
    ##############

    def test_99_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description™"
        test_input_price = "99.99"
        test_expected_price_cleansed = float(99.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

#
# Testcases to write.
#


#    def test_(self):
#
#        # Input and expected result.
#        test_input_title = "test title"
#        test_input_description = "test description"
#        test_input_price = ""
#        test_expected_price_cleansed = float(-1.00)
#        test_expected_multibuy = ""
#        test_expected_promotion_type = PRICE_REDUCTION
#        test_expected_title_cleansed = "Test Title Test Description"
#
#        # Perform the test
#        self.dut.mTitle = test_input_title
#        self.dut.mDescription = test_input_description
#        self.dut.mPrice = test_input_price
#        # Perform the cleanse.
#        self.dut.cleanse()
#        # Verify the results.
#        assert self.dut.mTitleCleansed == test_expected_title_cleansed
#        assert self.dut.mPriceCleansed == test_expected_price_cleansed
#        assert self.dut.mMultibuy == test_expected_multibuy
#        assert self.dut.mPromotionType == test_expected_promotion_type
