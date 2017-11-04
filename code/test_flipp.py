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
class TestFlipp(object):

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
        test_input_description = "test description"
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

    def test_dollar_99_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$99.99"
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

    def test_6_99_lb(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 /lb."
        test_expected_price_cleansed = float(6.99)
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

    def test_3_99_ea(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 /ea."
        test_expected_price_cleansed = float(3.99)
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

    def test_0_99_when_you_buy(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 /ea. when you buy 4*"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
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

    def test_7_99_when_you_buy_3_pkgs(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "7.99 /lb. when you buy 3 pkgs. or more*"
        test_expected_price_cleansed = float(7.99)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_buy_2_get_1_free_of_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " buy 2, get 1 free of equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_buy_1_get_1_free_of_equal_or_lesser_value_MIX_OR_MATCH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " buy 1, get 1 free of equal or lesser value "
        test_input_price += "MIX OR MATCH"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_33_percent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "33% OFF"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
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

    def test_1_dollar_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.00 off"
        test_expected_price_cleansed = float(-1.00)
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

    def test_40_cent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "40¢ off"
        test_expected_price_cleansed = float(-1.00)
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

    def test_11_99_when_you_buy_any_3_participating_products_with_your_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 when you buy any 3 participating products with "
        test_input_price += "your card SAVE $15 WHEN YOU BUY ANY 3 PARTICIPATING "
        test_input_price += "PRODUCTS & SAVE $5 OFF EACH"
        test_expected_price_cleansed = float(11.99)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_FINAL_PRICE__9_0_off_when_you_buy_any_3_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE $9.00 off when you buy any 3 participating "
        test_input_price += "products with your card. SAVE $15 WHEN YOU BUY ANY 3 "
        test_input_price += "PARTICIPATING PRODUCTS & SAVE $5 OFF EACH"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_dollar_off_SAVE_3_When_You_Buy_2_Participating_Products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "$1.00 off SAVE $3 When You Buy 2 Participating Products"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_off_comma_SAVE_3_When_You_Buy_2_Participating_Products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  " 1.00 off, SAVE $3 When You Buy 2 Participating Products"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_off_dot_SAVE_3_When_You_Buy_2_Participating_Products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  " 1.00 off. SAVE $3 When You Buy 2 Participating Products"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_3_89_Save_when_you_buy_Tribe_Hummus(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "3.89 /ea. Save $3 when you buy 2 Tribe Hummus*"
        test_expected_price_cleansed = float(3.89)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_3_99_SAVE_when_you_buy_participating_Horizon_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "3.99 SAVE $3 when you buy 3 participating Horizon products*"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_SAVE_when_you_buy(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "SAVE $2 when you buy 2"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_9_99_FREE_and_Seasoning_Steaming(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "9.99 /lb. FREE and Seasoning Steaming"
        test_expected_price_cleansed = float(9.99)
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

    def test_6_0_Save_ON_PRODUCE_when_you_buy_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "6.0 Save $4 ON PRODUCE when you buy 4 "
        test_input_price += "participating products*"
        test_expected_price_cleansed = float(6.00)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
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

    def test_33_percent_off_SAVE_when_you_buy_5_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "33% off, SAVE $5 when you buy 5 participating products"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
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

    def test_SAVE_when_you_buy_participating_Horizon_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "SAVE $3 when you buy 3 participating Horizon products*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_7_0_SAVE_5_when_you_buy_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "7.0 SAVE $5 when you buy 5 participating products*"
        test_expected_price_cleansed = float(7.00)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
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

    def test_5_0_SAVE_5_when_you_spend_15_on_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "5.0 SAVE $5 when you spend $15 on participating products*"
        test_expected_price_cleansed = float(5.00)
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

    def test_Save_5_when_you_buy_Hallmark_cards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "Save $5 when you buy 3 Hallmark cards*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_3_99_SAVE_when_you_buy_any_4_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "3.99 SAVE $4 when you buy any 4 participating products"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
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

    def test_10_99_SAVE_BUY_ANY_PARTICIPATING_PRODUCTS_SAVE_OFF_EACH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price =  "10.99 SAVE $15 BUY ANY 3 PARTICIPATING "
        test_input_price += "PRODUCTS & SAVE $5 OFF EACH"
        test_expected_price_cleansed = float(10.99)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
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

    def test_4_SAVE_MORE_OFF_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 SAVE MORE! $2 OFF with Smart Coupon"
        test_expected_price_cleansed = float(4.00)
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

    def test_SAVE_MORE_dollar_OFF_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE MORE! $2 OFF with Smart Coupon"
        test_expected_price_cleansed = float(-1.00)
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

    def test_SAVE_MORE_OFF_dollar_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 SAVE MORE! OFF $2 with Smart Coupon"
        test_expected_price_cleansed = float(10.00)
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

    def test_dollar_SAVE_MORE_OFF_dollar_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 SAVE MORE! OFF $2 with Smart Coupon"
        test_expected_price_cleansed = float(10.00)
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

    def test_SAVE_MORE_OFF_dollar_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE MORE! OFF $1 with Smart Coupon"
        test_expected_price_cleansed = float(-1.00)
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

    def test_4_to_8(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 - $8"
        test_expected_price_cleansed = float(4.00)
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

    def test_3_75_price_drop(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.75 PRICE DROP!"
        test_expected_price_cleansed = float(3.75)
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

    def test_5_price_drop(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 PRICE DROP"
        test_expected_price_cleansed = float(5.00)
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

    def test_SAVE_MORE_25_cent_OFF_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE MORE! 25¢ OFF with Smart Coupon"
        test_expected_price_cleansed = float(-1.00)
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

    def test_1_95_with_Smart_Coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.95 with $2 Smart Coupon"
        test_expected_price_cleansed = float(1.95)
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

    def test_3_69_PER_LB_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.69 PER LB."
        test_expected_price_cleansed = float(3.69)
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

    def test_0_85_Each(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.85 Each"
        test_expected_price_cleansed = float(0.85)
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

    def test_6_99_Per_Lb_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 Per Lb."
        test_expected_price_cleansed = float(6.99)
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

    def test_3_79_Per_16_oz_dot_Pkg_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.79 Per 16-oz. Pkg."
        test_expected_price_cleansed = float(3.79)
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

    def test_1_69_Per_Pint(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.69 Per Pint"
        test_expected_price_cleansed = float(1.69)
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

    def test_3_69_Per_Dozen(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.69 Per Dozen"
        test_expected_price_cleansed = float(3.69)
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

    def test_3_49_plus_CRV(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.49 +CRV"
        test_expected_price_cleansed = float(3.49)
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

    def test_6_99_LB_HOT_SALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 LB HOT SALE"
        test_expected_price_cleansed = float(6.99)
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

    def test_4_HOTSALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 HOTSALE"
        test_expected_price_cleansed = float(4.0)
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

    def test_5_HOT_SALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 HOT SALE"
        test_expected_price_cleansed = float(5.0)
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

    def test_1_79_EA_HOT_SALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.79 EA HOT SALE"
        test_expected_price_cleansed = float(1.79)
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

    def test_BUY_ONE_GET_ONE_FREE_SINGLE_ITEM_HALF_PRICE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE FREE SINGLE ITEM HALF PRICE"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = HALF_PRICE
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

    def test_1_99_LB_Low_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 LB Low Price Every Day"
        test_expected_price_cleansed = float(1.99)
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

    def test_2_19_EA_WOW_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.19 EA WOW Price Every Day"
        test_expected_price_cleansed = float(2.19)
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

    def test_3_29_EA_Low_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.29 EA Low Price Every Day"
        test_expected_price_cleansed = float(3.29)
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

    def test_22_99_discount_coupon_dollar_2_off_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "22.99 EA w/ Mfr. discount coupon $2.00 off 1"
        test_expected_price_cleansed = float(22.99)
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

    def test_5_BUY_TWO_Smart_Balance_GET_ONE_FREE_Lender_Bagels(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 BUY TWO Smart Balance & GET ONE FREE "
        test_input_price += "of Lender Bagels 17 Oz Select Varieties"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_0_69_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.69 with card"
        test_expected_price_cleansed = float(0.69)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_3_or_dollar_1_79_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.0 or $1.79 with card"
        test_expected_price_cleansed = float(1.79)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_buy_1_get_1_free_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1 get 1 free* with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_buy_1_get_1_percent_off_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1 get 1 0.50% off* with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_buy_1_get_1_percent_percent_off_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 1 get 1 50% % off* with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_5_or_dollar_2_99_with_card_MIX_MATCH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 or $2.99 ea. with card MIX & MATCH"
        test_expected_price_cleansed = float(2.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_6_or_dollar_3_99_with_card_dollar_1_off_coupon_online_or_in_store_on_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.0 or $3.99 ea. with card $1 off "
        test_input_price += "coupon online or in store on 2‡"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_0_15_triangle(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.15 ea.Δ"
        test_expected_price_cleansed = float(0.15)
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

    def test_buy_2_get_3rd_FREE_hair_care_mix_match_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 2 get 3rd FREE§ hair care mix & match with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_BONUS_POINTS_5000_dollar_5_reward_when_you_spend_dollar_10_or_more_on_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS POINTS 5000 = $5 reward when you spend "
        test_input_price += "$10 or more on participating products††"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_BONUS_POINTS_2000_dollar_2_reward_when_you_buy_pariticipating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS POINTS 2000=$2 reward when you "
        test_input_price += "buy pariticipating products††"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_buy_2_get_3rd_FREE_shaving_and_deodorant(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 2 get 3rd FREE§ shaving & deodorant"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_buy_2_get_3rd_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 2 get 3rd FREE§§"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_1_49_Per_Dry_Pint(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.49 Per Dry Pint"
        test_expected_price_cleansed = float(1.49)
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

    def test_1_19_Per_1_lb_Pkg(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.19 Per 1-lb. Pkg."
        test_expected_price_cleansed = float(1.19)
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

    def test_2_39_Per_Lb_SAVE_29_percent(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.39 Per Lb. SAVE 29%"
        test_expected_price_cleansed = float(2.39)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
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

    def test_BUY_1_GET_1_OF_EQUAL_OR_LESSER_VALUE_FREE_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_BUY_1_GET_1_OF_EQUAL_OR_LESSER_VALUE_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 OF EQUAL OR LESSER VALUE FREE"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_9_99_and_up_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 and up with card"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_SAVE_50_percent_SHELF_TAG_REFLECTS_SAVINGS_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE 50% SHELF TAG REFLECTS SAVINGS WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = HALF_PRICE
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

    def test_buy_one_comma_get_one_of_equal_or_lesser_value_free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one, get one of equal or lesser value free"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_1_each_10_for_dollar_10_comma_mix_or_match(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.0 each 10 for $10, mix or match 10,"
        test_input_price += "get the 11th free*"
        test_expected_price_cleansed = float(1.00)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
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

    def test_buy_two_comma_get_one_of_equal_or_lesser_value_free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy two, get one of equal or lesser value free"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_5_Get_dollar_5_off_instantly_when_you_buy_General_Mills(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 Get $5 off instantly when you buy $15 "
        test_input_price += "or more in participating General Mills Box "
        test_input_price += "Tops for Education Products*"
        test_expected_price_cleansed = float(5.00)
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

    def test_12_99_10_percent_off_Wine_Purchase_of_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "12.99 10% off Wine Purchase of 4 or More "
        test_input_price += "Bottles 750 ml and/or 1.5 liter."
        test_expected_price_cleansed = float(12.99)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
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

    def test_3_49_Per_12_oz_Bag(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.49 Per 12-oz. Bag."
        test_expected_price_cleansed = float(3.49)
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

    def test_1_49_Per_6_oz_Pkg(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.49 Per 6-oz. Pkg."
        test_expected_price_cleansed = float(1.49)
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

    def test_1_19_Per_4_Pack(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.19 Per 4-Pack"
        test_expected_price_cleansed = float(1.19)
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

    def test_1_99_Per_3_lb_Bag(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 Per 3-lb. Bag"
        test_expected_price_cleansed = float(1.99)
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

    def test_5_PER_WING_HOT_SALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.5 PER WING HOT SALE"
        test_expected_price_cleansed = float(0.50)
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

    def test_BUY_1_comma_GET_1_FREE_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 FREE WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_BUY_1_comma_GET_1_FREE_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 FREE WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_0_99_when_you_buy_any_5_participating_products_with(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 when you buy any 5 participating "
        test_input_price += "products with your card"
        test_input_price += " -$1.00 off SAVE $5 when you "
        test_input_price += "buy 5 participating products*"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
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

    def test_0_99_participating_products_with(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 when you buy any 5 participating products "
        test_input_price += "with your card -$1.00 off SAVE $5 when you "
        test_input_price += "buy 5 participating products*"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
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


    def test_0_99_participating_products_with_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 when you buy any 5 participating products "
        test_input_price += "with your card. $1.00 OFF SAVE $5 when you "
        test_input_price += "buy 5 participating products*"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
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

    def test_0_99_participating_products_with_no_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 when you buy any 7 participating "
        test_input_price += "products with your card $1.00 Off "
        test_input_price += "SAVE $7 when you buy 7 participating products*"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 7
        test_expected_promotion_type = MULTIBUY
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

    def test_BONUS_POINTS_equals_dollar_5_reward_when(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS POINTS =$5 reward when you $15 or "
        test_input_price += "more on participating products†† $2 off "
        test_input_price += "online coupon on 2◊"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_Buy_2_Get_1_free_or_Equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 2 Get 1 free or Equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_buy_5_get_1_free_buy_of_equal(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " buy 5 get 1 free buy of equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 6
        test_expected_promotion_type = MULTIBUY
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

    def test_0_49_Each(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.49 Each"
        test_expected_price_cleansed = float(0.49)
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

    def test_1_59_Per_Lb_dot_SAVE_15_percent(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.59 Per Lb. SAVE 15%"
        test_expected_price_cleansed = float(1.59)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
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

    def test_Price_Raw(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Price Raw"
        test_expected_price_cleansed = float(-1.00)
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

    def test_BUY_2_GET_1_FREE_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " BUY 2 GET 1 FREE*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_Buy_2_Get_1_free_or_Equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " Buy 2 Get 1 free or Equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_buy_5_get_1_free_buy_of_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 5 get 1 free buy of equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 6
        test_expected_promotion_type = MULTIBUY
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

    def test_1_95_BUY_2_GET_1_FREE_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.95 BUY 2 GET 1 FREE*"
        test_expected_price_cleansed = float(1.95)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_25_BUY_1_GET_1_50_percent_OFF_star_Equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "25.0 BUY 1 GET 1 50% OFF* Equal or lesser value"
        test_expected_price_cleansed = float(25.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_4_W_MFR_dot_DISCOUNT_COUPON_dollar_2_OFF_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 W/ MFR. DISCOUNT COUPON $2.00 OFF 2"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
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

    def test_4_49_50_percent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.49 50% off"
        test_expected_price_cleansed = float(4.49)
        test_expected_multibuy = ""
        test_expected_promotion_type = HALF_PRICE
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

    def test_dollar_4_OFF_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$4 OFF with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_50_percent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "50% off"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = HALF_PRICE
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

    def test_59_99_Save_dollar_10_on_your_next_shopping_trip(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "59.99 * Save $10 on your next shopping "
        test_input_price += "trip via Custom Coupon at checkout when "
        test_input_price += "you buy one Madden NFL 18 Edition"
        test_expected_price_cleansed = float(59.99)
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

    def test_dollar_5_off_Automotive_Dept_dot_Purchase_of(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$5 off Automotive Dept. "
        test_input_price += "Purchase of $30 or More"
        test_expected_price_cleansed = float(-1.00)
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

    def test_dollar_5_OFF_with_card_with_purchase_of_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " $5 OFF with card (with purchase of 2)"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = LOYALTY_CARD
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

    def test_additional_dollar_2_off_coupon_online_or_in_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " additional $2 off coupon online or in store‡"
        test_expected_price_cleansed = float(-1.00)
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

    def test_BUY_1_GET_1_25_percent_OFF_star_Equal_or_lesser(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1 25% OFF* Equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
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

    def test_buy_1_get_1_50_percent_off_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1 get 1 50% off*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_buy_1_get_1_50_percent_off_star_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " buy 1 get 1 50% off* with card"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_buy_1_get_1_50_percent_off_star_with_card_plus(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1 get 1 50% off* with card + "
        test_input_price += "BONUS POINTS 5000 = $5 reward when "
        test_input_price += "you spend $20††"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_BUY_1_GET_1_FREE_Equal_or_lesser_value_Must(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " BUY 1 GET 1 FREE Equal or lesser "
        test_input_price += "value • Must purchase 2 to get "
        test_input_price += "discount price"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_BUY_1_GET_1_FREE_SAVE_UP_TO_dollar_16_99_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " BUY 1 GET 1 FREE SAVE UP TO $16.99 "
        test_input_price += "WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_Buy_2_get_3rd_FREE_star_hair_care_mix_match(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 2 get 3rd FREE* hair care mix & match"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
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

    def test_BUY_ONE_GET_ONE_FREE_SINGLE_ITEM_HALF_PRICE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE FREE SINGLE "
        test_input_price += "ITEM HALF PRICE"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_Buy_one_get_one_Of_Equal_Or_Lesser_value_50_percent(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy one get one Of Equal Or Lesser "
        test_input_price += "value 50% off*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_buy_one_get_one_of_equal_or_lesser_value_for_dollar(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one get one of equal or "
        test_input_price += "lesser value for $1"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
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

    def test_buy_one_get_one_of_equal_or_lessor_value_50(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one get one of equal or lessor "
        test_input_price += "value 50% off*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
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

    def test_get_dollar_3_off_instantly_when_you_buy_dollar_13(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " get $3 off instantly when you buy $13"
        test_expected_price_cleansed = float(-1.00)
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

    def test_1_99_Sizes_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 Sizes Vary by Store"
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_5_Selection_varies_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.5 Selection varies by store"
        test_expected_price_cleansed = float(3.5)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Starting_at_5_Selection_varies_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Starting at 5.0 Selection varies by store"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Starting_at_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Starting at 20.0"
        test_expected_price_cleansed = float(20.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_Excludes_Organic(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 Excludes Organic"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_YOUR_CHOICE_2_88(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "YOUR CHOICE 2.88"
        test_expected_price_cleansed = float(2.88)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_As_Low_As_19_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "As Low As 19.99"
        test_expected_price_cleansed = float(19.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Sale_Price_0_88(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Sale Price 0.88"
        test_expected_price_cleansed = float(0.88)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Reg_1_75(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Reg. 1.75"
        test_expected_price_cleansed = float(1.75)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_5_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 5.5"
        test_expected_price_cleansed = float(5.50)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_NOW_1_39(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "NOW 1.39"
        test_expected_price_cleansed = float(1.39)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_5_0_Must_purchase_2_to_get(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 5.0 Must purchase 2 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined   "
        test_input_price += "†Prices not valid in the City of Philadelphia, "
        test_input_price += "PA Or Cook Country, IL"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_6_for_120_star_Offers_With_Like_Items_Cannot_Be_Combined(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 6 for 120.0 *Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(20.00)
        test_expected_multibuy = 6
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_5_for_10_Must_purchase_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 5 for 10.0 "
        test_input_price += "Must purchase 5 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined   ‡ "
        test_input_price += "Prices not valid in the City of Philadelphia, "
        test_input_price += "PA, or Cook Country, IL"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_4_for_44_Must_purchase_4_to(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 4 for 44.0 Must purchase 4 "
        test_input_price += "to get discount price   "
        test_input_price += "Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(11.0)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_6_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 6.0 Must purchase 3 to get discount price."
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_2_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 2.40"
        test_expected_price_cleansed = float(0.80)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_9_star_Offers_With_Like(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 9.0 "
        test_input_price += "*Offers With Like Items Cannot Be Combined   "
        test_input_price += "Must purchase 2 to get discount price"
        test_expected_price_cleansed = float(4.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_for_110(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10 for 110.0"
        test_expected_price_cleansed = float(11.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for 3.0"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_6_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for 6.0 "
        test_input_price += "Must purchase 2 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_24(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for 24.0"
        test_expected_price_cleansed = float(12.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_12_Must_purchase_3_to_get_discount(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for 12.0 Must purchase 3 to get discount price "
        test_input_price += "*Offers With Like Items Cannot Be Combined. "
        test_input_price += "‡ Prices not valid in the City of Philadelphia, "
        test_input_price += "PA, or Cook Country, IL"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_9_star_While_supplies_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for 9.0 *While supplies last. No rainchecks "
        test_input_price += "or substitutions."
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_20_slash_10_Excludes_Greek(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "20/ 10.0 Excludes Greek"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = 20
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_patties_slash_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10 patties/ 10.0"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_Excludes_Beef(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 Excludes Beef"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_slash_5_Plus_Deposit_Where_Applicable(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5/ 5.0 Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_slash_9_dollar_6_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 9.0 - $6.00 "
        test_input_price += "when you buy 3 with coupon in most sunday papers"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_slash_9_FREE_POLAND_SPRING(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 9.0 FREE POLAND SPRING SPARKLING WATER 6 PACK, "
        test_input_price += "16.9 FL. OZ. BTLS. when you buy 3 Poland Spring "
        test_input_price += "24 Pack* Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_8_Excludes_Gluten_Free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 8.0 Excludes Gluten Free"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_4_Some_Exclusions_Apply(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 4.0 Some Exclusions Apply"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 4.0"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_dollar_1_On_Little_Debbie_Zebra_Cakes(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $1 On Little Debbie Zebra Cakes 7.38–"
        test_input_price += "13.1 oz. pkg. WHEN YOU BUY 2 Little Debbie Family Pack"
        test_expected_price_cleansed = float(7.38)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_now_4_79_20_percent_off_star_While_supplies_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "now 4.79 20% off *While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(4.79)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Reg_1_95_BUY_2_GET_FREE_Offers_With(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Reg. 1.95 BUY 2, GET 1 FREE* "
        test_input_price += "*Offers With Like Items Cannot Be Combined   "
        test_input_price += "Must purchase 3 to get discount price"
        test_expected_price_cleansed = float(3.90)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_3_29_BUY_ONE_GET_ONE_FREE_JIF_OR_JIF_TO(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 3.29 BUY ONE & GET ONE FREE JIF OR JIF TO GO "
        test_input_price += "PEANUT BUTTER Limit 1 reward per shopping visit. "
        test_input_price += "W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(3.29)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_10_slash_7_MVP_Card_86_cents_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 10/ 7.0 W/O MVP Card 86¢ EA"
        test_expected_price_cleansed = float(0.70)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_10_slash_6__MVP_Card_74_cents_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 10/ 6.0 W/O MVP Card 74¢ EA"
        test_expected_price_cleansed = float(0.60)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_3_slash_12_MVP_Card_Regular_Retail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 3/ 12.0 W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_5_MVP_Card_Regular_Retail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 5.0 W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_3_99_1_OFF_1_W_MVP_Card_Regular_Retail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 3.99 -1.00 OFF 1 W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_1_79_W_O_MVP_Card_Regular_Retail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 1.79 W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(1.79)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_prices_not_valid_in_the_City(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.0 prices not valid in the "
        test_input_price += "City of Philadelphia, PA, or Cook County, IL"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_25_Phone_and_Plan_Sold_Separately(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "25.0 Phone and Plan Sold Separately"
        test_expected_price_cleansed = float(25.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_Excludes_Pantene_Gold_Series(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 Excludes Pantene Gold Series"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_12_Available_in_Most_Stores(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "12.0 Available in Most Stores."
        test_expected_price_cleansed = float(12.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_Accessories_not_included(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 Accessories not included."
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_12_91_Backpack_Not_Included(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "12.91 Backpack Not Included"
        test_expected_price_cleansed = float(12.91)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_Sizes_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 Sizes Vary by Store"
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_16_Cover_not_included(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "16.0 Cover not included"
        test_expected_price_cleansed = float(16.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_See_Tag_for_Details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 See Tag for Details"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_49_Limit_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.49 Limit 4"
        test_expected_price_cleansed = float(0.49)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_When_You_Buy_4_FINAL_COST_8_When_you_buy_4_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "When You Buy 4 FINAL COST 8.0 When you buy 4 "
        test_input_price += "or more in the same transaction with Card. "
        test_input_price += "Quantities less than 4 will be priced at $2.50 each."
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_When_You_Buy_2_FINAL_COST_4_99_When_you_buy_in_multiples(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "When You Buy 2 FINAL COST 6.00 When you buy in multiples "
        test_input_price += "of 2 in the same transaction with Card. "
        test_input_price += "All other quantities will be priced at $5.99 each."
        test_expected_price_cleansed = float(3.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_When_You_Buy_2_FINAL_COST_4_99_When_you_buy_multiples_of_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "When You Buy 2 FINAL COST 4.00 When you buy "
        test_input_price += "multiples of 2 in the same transaction with Card. "
        test_input_price += "All other quantities will be priced at $5.99 each."
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_99_FREE_bang_Snuggle_Fabric_Softener(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 FREE! Snuggle Fabric Softener, Liquid, "
        test_input_price += "32-40 Use or Sheets, 70-80 ct. "
        test_input_price += "When you buy 2 all Laundry Detergent, "
        test_input_price += "30-52 fl oz or 18-24 ct Items must be "
        test_input_price += "purchased in the same transaction with Card."
        test_expected_price_cleansed = float(2.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FREE_BANANAS_UP_TO_dollar_3_VALUE_when_you_spend_dollar(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE BANANAS UP TO $3 VALUE when you spend $10 on "
        test_input_price += "participating Danimals products* "
        test_input_price += "(excludes Organic Bananas) Only with your Giant card. "
        test_input_price += "*In a single transaction."
        test_expected_price_cleansed = float(10.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_FREE_NATURE_S_PROMISE_SOUP_16_24_OZ_CONT_when(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 FREE NATURE'S PROMISE SOUP 16–24 OZ. CONT. "
        test_input_price += "when you buy Panera Soup* Only with your Giant card.  "
        test_input_price += "*In a single transaction. Limit 5 offers per household."
        test_expected_price_cleansed = float(10.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_Weekly_sale_price_without_digital_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 Weekly sale price "
        test_input_price += "without digital coupon is $2.79 each with Card."
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_39_99_Valid_week_of(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "39.99 Valid week of August 23"
        test_expected_price_cleansed = float(39.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_Free_When_you_buy_Panera_soup_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 Free When you buy Panera soup* "
        test_input_price += "Nature's Promise Soup 16-24oz. "
        test_input_price += "cont Only with you stop & shop card. "
        test_input_price += "*In a single transaction. "
        test_input_price += "Limit 5 offers per household"
        test_expected_price_cleansed = float(10.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_Plus_Deposit_Where_Applicable(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_3_slash_9_dollar_5_when_you_buy_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 3/ 9.0 $5.00 "
        test_input_price += "when you buy 3 with coupon "
        test_input_price += "in most sunday papers"
        test_expected_price_cleansed = float(3.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_0_99_dollar_1_off_SAVE_dollar_5_when_you_buy(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 0.99 $1.00 off. "
        test_input_price += "SAVE $5 when you buy 5 participating products* "
        test_input_price += "Only with your Stop & Shop Card! "
        test_input_price += "*In a single transaction. "
        test_input_price += "Limit 2 offers per transaction"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_7_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 7.0 Must purchase 2 to get discount "
        test_input_price += "price  *Offers With Like Items Cannot Be Combined."
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_10_Must_Purchase_2_To_Get_Discount_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 10.0 Must Purchase 2 To Get Discount Price. "
        test_input_price += "*Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_18_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 18.0 Must purchase 2 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(9.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_12_Phone_and_Plan_sold_separately(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 12.0 Phone and Plan sold separately. "
        test_input_price += "Service Plan required for activation.  "
        test_input_price += "Models may vary by store."
        test_expected_price_cleansed = float(12.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_0_95_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 0.95 Must purchase 3 to get discount price "
        test_input_price += "‡Prices not valid in the City Philadelphia, PA, "
        test_input_price += "or Cook Country, IL, PA Or Cook Country, IL"
        test_expected_price_cleansed = float(0.95)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_49_Simple_Mobile_handset_Availability_varies_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 49.0 Simple Mobile handset "
        test_input_price += "Availability varies by store."
        test_expected_price_cleansed = float(49.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_Available_in_most_stores(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3.0 Available in most stores"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_for_10__2_DAYS_ONLY_bang_where_available_Must_purchase_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5 for 10.0 2 DAYS ONLY! where available Must purchase 5 "
        test_input_price += "to get discount price ‡Prices not valid in the City of "
        test_input_price += "Philadelphia, PA or Cook Country, IL *Offers with like "
        test_input_price += "items cannot be combined. While Supplies Last"
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_DOLLAR_2_INSTANTLY_when_you_spend_dollar_10_on_Lysol_Disinfecting_Spray(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $2 INSTANTLY when you spend $10 on Lysol Disinfecting "
        test_input_price += "Spray 12.5 oz. or ANY Lysol Wipes, Toilet Bowl Cleaner, "
        test_input_price += "Trigger or Pourable Cleaner"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_3_SAVE_dollar_1_WHEN_YOU_BUY_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 3.0 SAVE $1 WHEN YOU BUY 2, "
        test_input_price += "2 DAYS ONLY! Must purchase 2 to get discount Price  "
        test_input_price += "*offers with like items cannot be combined"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_Save_an_additional_50_cents(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 Save an additional 50¢* with DG DIGITAL COUPONS "
        test_input_price += "*Offers with like items cannot be combined"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_77_star_Other_quantities_2_slash_dollar_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.77 *Other quantities 2/$5"
        test_expected_price_cleansed = float(1.77)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_Low_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 Low Price Every Day"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_10_slash_10_HOT_SALE_W_O_MVP_Card_dolllar_2_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 10/ 10.0 HOT SALE W/O MVP Card $2.19 EA"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_10_slash_10_W_O_MVP_Card_dollar_1_19(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 10/ 10.0 W/O MVP Card $1.19 EA"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_5_slash_5_HOT_SALE_W_O_MVP_Card_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 5/ 5.0 HOT SALE W/O MVP Card 4/$5"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_4_slash_12_HOT_SALE_W_O_MVP_Card_Regular_Retail_Limit_8(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 4/ 12.0 HOT SALE W/O MVP Card Regular Retail Limit 8"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_3_slash_6_HOT_SALE_W_O_MVP_Card__dollar_2_48(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 3/ 6.0 HOT SALE W/O MVP Card $2.48 EA"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_18_BUY_TWO_GET_ONE_FREE_DEL_MONTE_FRUIT(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2.18 BUY TWO & GET ONE FREE DEL MONTE FRUIT "
        test_input_price += "& CHIA W/O MVP Card $2.68 EA Limit 1 reward per "
        test_input_price += "shopping visit. W/O MVP card Regular Retail"
        test_expected_price_cleansed = float(2.18)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_6_HOT_SALE_W_O_MVP_CARD_REGULAR_RETAIL(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 6.0 HOT SALE W/O MVP CARD REGULAR RETAIL"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_4_HOT_SALE_W_O_MVP(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 4.0 HOT SALE W/O MVP Card $2.19 EA"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_FREE_BUY_ONE_GET_ONE_SINGLE_ITEM_HALF_PRICE_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP  FREE BUY ONE GET ONE "
        test_input_price += "SINGLE ITEM HALF PRICE W/O "
        test_input_price += "MVP Card Regular Retail"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_five_comma_get_five_of_equal_or_lesser_value_free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy five, get five of equal or lesser value free"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_cross_Only_available_on_instore_purchases(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 † Only available on in-store purchases."
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_Brands_may_vary_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 Brands may vary by store."
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_sale_20_percent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "sale 20% off "
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_sale_4_for_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "sale 4 for 1.0"
        test_expected_price_cleansed = float(0.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_Xbox_One_1TB_Console_get_one_free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one Xbox One 1TB Console get one free* "
        test_input_price += "*While supplies last. "
        test_input_price += "No rainchecks or substitutions"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_save_dollar_75_on_your_next_shopping_trip_when_you_buy_one_iPad(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $75 on your next shopping trip "
        test_input_price += "when you buy one iPad "
        test_input_price += "*While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_two_comma_get_one_of_equal_or_lesser_free_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy two, get one of equal or lesser free* "
        test_input_price += "*While supplies last. "
        test_input_price += "No rainchecks or substitutions"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_get_one_or_equal_or_lesser_value_star_While(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one get one or equal or lesser value "
        test_input_price += "*While supplies last. "
        test_input_price += "No rainchecks or substitutions"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_comma_get_one_for_dollar_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one, get one for $1 of equal or lesser value "
        test_input_price += "*While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_5_slash_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 5/ 5.0 -$5.00 WHEN YOU BUY 5 DIGITAL COUPON"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_2_slash_4_dollar_1_OFF(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 2/ 4.0 $1.00 OFF 2 DIGITAL COUPON Limit 1"
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_8_SAVE_dollar_4_when_you_buy_4_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 8.0 SAVE $4 "
        test_input_price += "when you buy 4 participating products* "
        test_input_price += "Participating Varieties and Sizes May "
        test_input_price += "Vary by Store Only with your "
        test_input_price += "Giant card *in a single transaction. "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_9_SAVE_dollar_4_when_you_buy_4_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 9.0 SAVE $4 "
        test_input_price += "when you buy 4 participating products* "
        test_input_price += "Participating Varieties and Sizes May Vary "
        test_input_price += "by Store  Only with your Giant card *"
        test_input_price += "in a single transaction. "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(4.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_SAVE_dollar_6_when_you_buy_6_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 SAVE $6 "
        test_input_price += "when you buy 6 participating products* "
        test_input_price += "Only with your Giant Card!. "
        test_input_price += "*In a single transaction. "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(3.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_9_99_star_Lesser_quantities_dollar_10_99_slash_lb(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 *Lesser quantities $10.99/lb."
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_Limit_2_offers_per_transaction_star_Other(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 Limit 2 offers per transaction. "
        test_input_price += "*Other quantities $4.99/ea."
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_12_star_Other_quantities_dollar_5_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 12.0 *Other quantities $5.99/ea. "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_9_99_star_Other_quantities_dollar_11_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 *Other quantities $11.99/ea. "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_star_Other_quantities_2_slash_dollar_6(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 *Other quantities 2/$6"
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_66_star_Other_quantities_2_slash_dollar_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.66 *Other quantities 2/$5"
        test_expected_price_cleansed = float(1.66)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_save_dollar_5_on_your_next_shopping_trip(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 save $5 on your next shopping trip via "
        test_input_price += "Custom Coupon at checkout when you buy $20 "
        test_input_price += "or more of health & beauty brands in one "
        test_input_price += "transaction* *While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(6.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_2_get_3rd_FREE_star_Card_required_for_promotional_pricing(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 2 get 3rd FREE* * Card required for promotional pricing. "
        test_input_price += "Third item free, of equal or lesser price. "
        test_input_price += "Includes No7 and Soap & Glory products. "
        test_input_price += "Excludes Sinful Nail Polish, Essie, e.l.f., "
        test_input_price += "NYC cosmetics, all cotton products, "
        test_input_price += "all nail polish removers, Jordana, Lip Smackers, "
        test_input_price += "Tweezerman, Circa, $ Shop, Colour Prevails, gift sets, "
        test_input_price += "and No7 and Soap & Glory clearance items. "
        test_input_price += "Subject to availability. "
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = BUY_TWO_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Purchase_one_at_a_time_or_all_at_once(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Purchase one at a time or all at once 8/25/2017 "
        test_input_price += "through 11/2/2017.  Excludes Stop & Shop Milk. "
        test_input_price += "Free coupon redeemable through 11/16/2017"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_29_buy_their_get_ours_free_star_When_purchased(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.29 buy their get ours free* "
        test_input_price += "*When purchased in a single transaction "
        test_input_price += "with your Stop & Shop card from 8/25–8/31/17"
        test_expected_price_cleansed = float(3.29)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_20_slash_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "20/ 10.0"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = 20
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_Plus_Deposit_Where_Applicable(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_10_Plus_Deposit_Where_Applicable(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 10.0 Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_Plus_deposit_or_CRV_where_required_dot_MIX_and_MATCH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 / 5.0 "
        test_input_price += "Plus deposit or CRV where required. "
        test_input_price += "MIX & MATCH"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_Plus_deposit_or_CRV_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 / 5.0 Plus deposit or CRV where required."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_now_7_49_sale_25_percent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "now 7.49 sale 25% off"
        test_expected_price_cleansed = float(7.49)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_sale_2_for_5_get_dollar_2_off_instantly_when_you_buy_two(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "sale 2 for 5.0 get $2 off instantly when you buy two "
        test_input_price += "Ziploc Bags Storage 19-24 ct., freezer 14-19 ct. "
        test_input_price += "or snack or sandwich bags 90 ct. or Containers 2-8 ct."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_50_50_save_dollar_5_on_your_next_shopping_trip_via_Custom_Coupon_at_checkout(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for 50.50 save $5 on your next shopping trip via "
        test_input_price += "Custom Coupon at checkout when you buy $20 or more "
        test_input_price += "of health & beauty brands in one transaction* "
        test_input_price += "*While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(25.25)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_10_Must_purchase_2_to_get_discount_price_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 10.0 Must purchase 2 to get discount price "
        test_input_price += "*Offers with like items cannot be combined. "
        test_input_price += "Excludes 37 ct. and Family Packs"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Reg_dot_4_BUY_1_comma_GET_1_50_percent_OFF_star_Equal(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Reg. 4.0 BUY 1, GET 1 50% OFF* Equal or lesser value, "
        test_input_price += "2 Day Only! Must purchase 2 to get discount price "
        test_input_price += "*Offers With Like Items Cannot Be Combined Items "
        test_input_price += "on this page only. While supplies last."
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_8_5_When_you_Buy_1_Kibbles_Bits_symbol__Dog_Food_GET_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 8.5 When you Buy 1 Kibbles 'n Bits® Dog Food "
        test_input_price += "GET 1 FREE* Canine Carry Outs®, 2 DAYS ONLY! "
        test_input_price += "*Offers With Like Items Cannot Be Combined  "
        test_input_price += "While Supplies Last"
        test_expected_price_cleansed = float(8.50)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Buy_1_comma_Get_1_25_percent_Off_star_Equal_or_Lesser_Value_Must_purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 1, Get 1 25% Off* Equal or Lesser Value "
        test_input_price += "Must purchase 2 to get discount price  "
        test_input_price += "*Offers with like items cannot be combined.   "
        test_input_price += "Excludes 3M® Bath Command®"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_7_SAVE_dollar_5_on_your_next_purchase_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 7.0 SAVE $5 on your next purchase when you "
        test_input_price += "spend $15 or more on ANY P&G Brands! "
        test_input_price += "Must purchase 2 to get discount price "
        test_input_price += "*Offers with like items cannot be combined. "
        test_input_price += "*Offer Valid 8/20-9/23. Exclusions Apply. $15 "
        test_input_price += "Net Purchase Price Determined After "
        test_input_price += "All Discounts, Offers And Coupons. "
        test_input_price += "Limit One Offer Per Transaction."
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_6_Save_25_cent_with_DG_DIGITAL_COUPONS(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 6.00 Save 25¢ with DG DIGITAL COUPONS, "
        test_input_price += "Save $5 on your next purchase when you spend $15 or more "
        test_input_price += "on any P&G brands!* *Offers with like items cannot be combined  "
        test_input_price += "Must purchase 3 to get discount price  *Offer valid 8/20-9/23. "
        test_input_price += "Exclusions apply. $15 Net purchase price determined after all "
        test_input_price += "discount, offers and coupons. Limit one offer per transaction."
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_Save_dollar_1_DG_DIGITAL_COUPONS_Excludes_Hardest_Working(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.0 Save -$1 DG DIGITAL COUPONS Excludes Hardest Working "
        test_input_price += "Collection and Invisible Sprays "
        test_input_price += "*Offers with like items cannot be combined."
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_1_OFF_INSTANTLY_AT_REGISTER(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1 OFF INSTANTLY AT REGISTER"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_4_for_1_another(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 4 for 1.0"
        test_expected_price_cleansed = float(0.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Sale_Reg_dot_2_BUY_1_comma_GET_1_FREE_star_Equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Sale Reg. 2.0 BUY 1, GET 1 FREE* Equal or lesser "
        test_input_price += "value Must purchase 2 to get discount price  "
        test_input_price += "*Offers with like items cannot be combined"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_4_MIX_and_MATCH_star_Offers_With_Like_Items(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 4.0 MIX & MATCH *"
        test_input_price += "Offers With Like Items Cannot Be Combined  "
        test_input_price += "Must purchase 2 to get discount price"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_Low_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 Low Price Every Day"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BONUS_POINTS_10_comma_000_equal_dollar_10_reward_when_you(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS POINTS 10,000 = $10 reward when you spend $50 "
        test_input_price += "or more on participating products†† "
        test_input_price += "Selection may vary by store. Excludes Well Beginnings®. "
        test_input_price += "†† Good on next purchase. Purchase requirement must "
        test_input_price += "be met in a single transaction, before taxes and after "
        test_input_price += "discounts, store credit and redemption dollars are applied. "
        test_input_price += "Due to state and federal laws, points cannot be earned or "
        test_input_price += "redeemed on some items. "
        test_input_price += "Complete details at Walgreens.com/Balance."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_49_BONUS_POINTS_1000__1_reward_when_you_buy_2_cross(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.49 BONUS POINTS 1000 = $1 reward when you buy 2†† †† "
        test_input_price += "Good on next purchase. Purchase requirement must be met "
        test_input_price += "in a single transaction, before taxes and after discounts, "
        test_input_price += "store credit and redemption dollars are applied. "
        test_input_price += "Due to state and federal laws, points cannot be earned or "
        test_input_price += "redeemed on some items. Complete details at "
        test_input_price += "Walgreens.com/Balance. "
        test_input_price += "† Only available on in-store purchases.  "
        test_expected_price_cleansed = float(2.49)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_BONUS_POINTS_1000__equal_dollar_1_reward_when_you_buy_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 BONUS POINTS 1000 = $1 reward when you buy 2†† † "
        test_input_price += "Only available on in-store purchases. "
        test_input_price += "†† Good on next purchases. Purchase requirement, "
        test_input_price += "must be met in a single transaction, before taxes and "
        test_input_price += "after discounts, store credit and redemption dollars are applied. "
        test_input_price += "Due to state and federal laws, points cannot be earned or "
        test_input_price += "redeemed on some items. "
        test_input_price += "Complete details at Walgreens.com/Balance."
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_REGISTER_REWARDS_symbol_dollar_3_OFF_with_card_on_next_purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.0 REGISTER REWARDS® $3 OFF with card on next purchase when "
        test_input_price += "you buy 2** ** Only available on in-store purchases. "
        test_input_price += "Limit 1 Savings Reward coupon per customer per offer. "
        test_input_price += "See coupon for terms, restrictions and expiration. "
        test_input_price += "Purchase requirement must be met in a single transaction, "
        test_input_price += "before taxes and after discounts, store credit and "
        test_input_price += "redemption dollars are applied."
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_10_REGISTER_REWARDS_symbol_on_next_purchase_when_you_buy(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$10 REGISTER REWARDS® on next purchase when you buy 2 participating"
        test_input_price += "products** Minimum 1 cartridge purchase required. Ω"
        test_input_price += "Manufacturer coupon available in most Sunday papers or at "
        test_input_price += "Walgreens.com/Coupons. Only available on in-store purchases. "
        test_input_price += "**Only available on in-store purcheses.Limit 1 "
        test_input_price += "Register Reward coupons per customer per offer. "
        test_input_price += "See coupon for terms, restricitons and expiration. "
        test_input_price += "Purchase requirement must be met in a single transaction, "
        test_input_price += "before taxes and after discounts, store credit and "
        test_input_price += "redemption dollars are are applied."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_11_99_horse_Manufacturer_coupon_available_in_most_Sunday_papers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 Ω Manufacturer coupon available in most Sunday papers "
        test_input_price += "or at Walgreens.com/Coupons. "
        test_input_price += "Only available on in-store purchases."
        test_expected_price_cleansed = float(11.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_10_OFF_with_card_Limit_one_coupon_per_customer_per_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$10 OFF with card Limit one coupon per customer per offer. "
        test_input_price += "Vendor-funded offer. Customer pays any sales tax. "
        test_input_price += "Void if copied or where prohibited. Cash value 1/100¢. "
        test_input_price += "Coupon offer valid 8/27/2017 thru 9/30/2017 $5OFF"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_5_OFF_with_card_Limit_one_coupon_per_customer_per_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$5 OFF with card Limit one coupon per customer per offer. "
        test_input_price += "Vendor-funded offer. Customer pays any sales tax. "
        test_input_price += "Void if copied or where prohibited. Cash value 1/100¢. "
        test_input_price += "Coupon offer valid 8/27/2017 thru 9/30/2017 $10OFF"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type


    def test_SALE_2_for_9_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 9.0 Must purchase 2 to get "
        test_input_price += "discount price "
        test_input_price += "*Offers with like items cannot be combined"
        test_expected_price_cleansed = float(4.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_12_75_Save_25_cent__with_DG_DIGITAL_COUPONS(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 12.75 Save 25¢ with DG DIGITAL COUPONS, "
        test_input_price += "Save $5 on your next purchase when you spend $15 or "
        test_input_price += "more on any P&G brands!* *Offers with like items cannot "
        test_input_price += "be combined  Must purchase 3 to get discount price  "
        test_input_price += "*Offer valid 8/20-9/23. Exclusions apply. $15 Net "
        test_input_price += "purchase price determined after all discount, "
        test_input_price += "offers and coupons. Limit one offer per transaction."
        test_expected_price_cleansed = float(4.25)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_9_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 9.0 Must purchase 3 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined   "
        test_input_price += "†Prices not valid in the City of Philadelphia"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_3_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 3.0 Must purchase 3 to get discount price  "
        test_input_price += "‡Prices not valid in the City of Philadelphia, "
        test_input_price += "PA, or Cook County, IL"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_9_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 9.0 Must purchase 3 to get discount price   "
        test_input_price += "*offers with like items cannot be combined  "
        test_input_price += "‡Prices Not Valid In The City Of Philadelphia, PA"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_3_star_Offers_with_like_items_cannot_be_combined(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 3.0 *Offers with like items cannot be combined  "
        test_input_price += "Must purchases 2 to get discount price"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_5_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 5.0 Must purchase 2 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined   "
        test_input_price += "†Prices not valid in the City of Philadelphia,"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_9_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 9.0 Must purchase 2 to get discount "
        test_input_price += "price * Offer With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(4.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_10_Must_Purchase_2_To_Get_Discount_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 10.0 Must Purchase 2 To Get Discount Price.    "
        test_input_price += "*Offers With Like Items Cannot Be Combin"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_18_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 18.0 Must purchase 2 to get discount price  "
        test_input_price += "*Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(9.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_3_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 3.0 Must purchase 2 to get discount price "
        test_input_price += "*Offers with like items cannot be combined."
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_5_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 5.0 Must purchase 2 to get discount price. "
        test_input_price += "*Offers with like items cannot be combined. "
        test_input_price += "Prices Not valid In The City Of Philadelphia, "
        test_input_price += "PA or Cook County, IL."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_1_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 1.0 Must purchase 2 to get discount price  "
        test_input_price += "*Offers with like items cannot be combined"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_5_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 5.0 Must purchase 2 to get discount price *"
        test_input_price += "Offer With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_99_FREE_bang_Snuggle_Fabric_Softener(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 FREE! Snuggle Fabric Softener, Liquid, "
        test_input_price += "31.7-32 oz or Sheets, 70-80 ct. "
        test_input_price += "When you buy 2 all Laundry Detergent, "
        test_input_price += "30-50 fl oz or 18-24 ct Pods Items must be "
        test_input_price += "purchased in the same transaction with Card."
        test_expected_price_cleansed = float(2.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_Weekly_sale_price_without_digital_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 Weekly sale price without digital coupon is "
        test_input_price += "$2.79 each with Card. USE DIGITAL COUPON UP TO 5X "
        test_input_price += "IN A SINGLE TRANSACTION"
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_16_99_Valid_week_of_August_23_Accessories_not_included(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "16.99 Valid week of August 23 Accessories not included."
        test_expected_price_cleansed = float(16.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_99_Plus_Deposit_Where_Applicable_star_Other_quantities(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 Plus Deposit Where Applicable *Other quantities $5.49/ea."
        test_expected_price_cleansed = float(4.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_99_Excludes_Cubes_and_Slices(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 Excludes Cubes and Slices."
        test_expected_price_cleansed = float(4.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_Excludes_Cheddar_Franks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.0 Excludes Cheddar Franks"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_Available_while_quantities_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 Available while quantities last."
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_See_tag_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 See tag for details"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_69_Limit_4_dot__While_supplies_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.69 Limit 4. While supplies last. Reduction taken at the register."
        test_expected_price_cleansed = float(1.69)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_99_RED_HOT_SPECIAL_Valid_week_of_August_30(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 RED HOT SPECIAL Valid week of August 30"
        test_expected_price_cleansed = float(2.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_special_character_of_hyphen(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test–description"
        test_input_price = "9.77"
        test_expected_price_cleansed = float(9.77)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test-Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_75_special_char_cent_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "75¢ off"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_77_4_DAYS_ONLY_bang_Limit_4_Lobsters(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.77 4 DAYS ONLY! Limit 4 Lobsters"
        test_expected_price_cleansed = float(5.77)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_1_comma_get_1_of_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1, get 1 of equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_CUT_FRESH_INSTORE_DAILY(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.99 CUT FRESH IN-STORE DAILY"
        test_expected_price_cleansed = float(3.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_19_99_Participating_Varieties_and_Sizes_May_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "19.99 Participating Varieties and Sizes May Vary by Store"
        test_expected_price_cleansed = float(19.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_slash_1_WOW_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 3.0 WOW Price Every Day"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_WOW_Price_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 WOW Price Every Day"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_7_SAVE_dollar_10_INSTANTLY_when_you_spend_dollar_30(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 SAVE $10 INSTANTLY when you spend $30 "
        test_input_price += "on participating products in a single "
        test_input_price += "transaction* * Limit 1 offer per transaction"
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_SAVE_dollar_10_INSTANTLY_when_you_spend_dollar_30(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 SAVE $10 INSTANTLY when you spend $30 on "
        test_input_price += "participating products in a single transaction* "
        test_input_price += "* Limit 1 offer per transaction"
        test_expected_price_cleansed = float(2.5)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_97_LIMIT_5_LBS_WITHOUT_COUPON_dollar_1_99_lb(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.97 LIMIT 5 LBS. WITHOUT COUPON $1.99/lb."
        test_expected_price_cleansed = float(0.97)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_77_LIMIT_1_WITHOUT_COUPON_dollar_4_99_slash_ea(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.77 LIMIT 1 WITHOUT COUPON $4.99/ea."
        test_expected_price_cleansed = float(3.77)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_3_SAVE_dollar_2_INSTANTLY_WHEN_YOU_BUY_ANY_THREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 3.0 SAVE $2 INSTANTLY WHEN YOU BUY "
        test_input_price += "ANY THREE PARTICIPATING SUAVE ITEMS W/O "
        test_input_price += "MVP Card 2/$4 Limit 1 reward per shopping visit."
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_3_dollar_3_OFF_2_W_O_MVP_Card_Regular_Retail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 3.0 - $3.00 OFF 2 W/O MVP Card Regular Retail"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_6_dollar_1_OFF_2_W_O_MVP_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 6.0 -$1.00 OFF 2 W/O MVP Card $4.28 EA"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_2_slash_6_dollar_1_OFF_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 2/ 6.0 - $1.00 OFF 2"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_7_29_W_O_MVP_Card_dollar_8_99_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 7.29  W/O MVP Card $8.99 EA"
        test_expected_price_cleansed = float(7.29)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_0_89_W_O_MVP_Card_99_cent_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP 0.89  W/O MVP Card 99¢ EA"
        test_expected_price_cleansed = float(0.89)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_Save_An_Additional_dollar_3_star_with_DG_Digital_Coupons_When_You(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 Save An Additional $3* with DG Digital Coupons "
        test_input_price += "When You Buy 2 Save $5 On Your Next Purchase When "
        test_input_price += "You Spend $15 Or More On Any P&G Brands!* *$15 Net "
        test_input_price += "Purchase Price Determined After All Discounts Offers "
        test_input_price += "And Coupons. Limit One Offer Per Transaction."
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_When_You_Buy_3_FINAL_COST_1_77_When_you_buy_in_multiples(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "When You Buy 3 FINAL COST 1.77 When you buy in "
        test_input_price += "multiples of 3 in the same transaction with Card. "
        test_input_price += "Quantities not purchased in multiples of 3 will "
        test_input_price += "be $2.49 each with Card."
        test_expected_price_cleansed = float(1.77)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Reg_1_5_50_cent_OFF_INSTANTLY_AT_REGISTER(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Reg. 1.5 50¢ OFF INSTANTLY AT REGISTER"
        test_expected_price_cleansed = float(1.5)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Sale_Reg_3_6_BUY_2_GET_1_50_percent_OFF_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Sale Reg. 3.6 BUY 2 GET 1 50% OFF* "
        test_input_price += "Must purchase 3 "
        test_input_price += "to get discount price *"
        test_input_price += "Offers with like items cannot be combined."
        test_expected_price_cleansed = float(3.6)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Save_50_cent_Manufacturers_Coupon_Consumer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Save 50¢ Manufacturer's Coupon Consumer: "
        test_input_price += "Limit one coupon per purchase on product specified. "
        test_input_price += "Void if reproduced transferred used to purchase "
        test_input_price += "products for resale or where prohibited/regulated by law. "
        test_input_price += "Redeemable at your favorite "
        test_input_price += "participating Dollar General store. "
        test_input_price += "Consumer pays sales tax. Retailer: You are authorized "
        test_input_price += "to act as our agent and redeem this coupon in accordance "
        test_input_price += "with the E.T. Browne Drug Co. Inc. coupon redemption policy "
        test_input_price += "available upon request. We will reimburse you for the face "
        test_input_price += "value plus 8¢ handling. Void where prohibited. "
        test_input_price += "Cash value 1/100 of 1¢. Send coupons to: E.T. "
        test_input_price += "Browne Drug Co. 1192 NCH Marketing Services "
        test_input_price += "P.O. Box 880001 El Paso TX 88588-0001."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_6_Mix_and_Match_bang_Must_purchase_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 6.0 Mix & Match! Must purchase 3 to "
        test_input_price += "get discount price *Offers with like items "
        test_input_price += "cannot be combined."
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_6_2_DAYS_ONLY(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 6.0 2 DAYS ONLY! "
        test_input_price += "*Offers With Like Items Cannot Be Combined "
        test_input_price += "Must Purchase 2 to get discount price"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_3_for_2_5_Must_purchase_3_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 3 for 3.0 Must purchase 3 to get discount price  "
        test_input_price += "Prices Not valid in The City Of Philadelphia PA Or "
        test_input_price += "Cook Country IL  Offers With Like Items Cannot Be Combined"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_1_0_Must_Purchase_2_to_get_Discount_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 1.0 Must Purchase 2 to get Discount Price  "
        test_input_price += "*Offers with like items cannot be combined"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_0_5_HOT_PRICE_bang(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 0.5 HOT PRICE!"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_2_slash_3_DIGITAL_COUPON_2_OFF_2_Limit_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 2/ 3.0 DIGITAL COUPON $2.00 OFF 2 Limit 1"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_0_75_DIGITAL_COUPON_25_cent_Limit_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 0.75 DIGITAL COUPON -25¢ Limit 1"
        test_expected_price_cleansed = float(0.75)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_Save_dollar_2_with_DG_DIGITAL_COUPONS_dollar_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 Save $2 with DG DIGITAL COUPONS $1 OFF "
        test_input_price += "INSTANTLY AT REGISTER *Offers With Like "
        test_input_price += "Items Cannot Be Combined"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_11_99_SAVE_dollar_10_INSTANTLY_when_you_spend_dollar_30(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 SAVE $10 INSTANTLY when you spend $30 on "
        test_input_price += "participating products in a single transaction* * "
        test_input_price += "Limit 1 offer per transaction"
        test_expected_price_cleansed = float(11.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_5_SAVE_dollar_4_when_you_buy_4(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.5 SAVE $4 when you buy 4"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Price_Raw(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Price Raw"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUY_1_GET_1_50_percent_OFF_star__Equal_or_lesser_value_star_Offers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1 50% OFF* Equal or lesser value "
        test_input_price += "*Offers with like items cannot be combined. "
        test_input_price += "Must purchase 2 to get discount price. "
        test_input_price += "Excludes items with green dot on tag"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_1_get_1_of_free_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 1 get 1 of free equal or lesser value"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_FREE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_slash_11_star_Other_quantities_dollar_2_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5/ 11.0 *Other quantities $2.99/ea. "
        test_input_price += "Limit 2 offers per transaction"
        test_expected_price_cleansed = float(2.20)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_11_Limit_2_offers_per_transaction(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 11.0 Limit 2 offers per transaction."
        test_expected_price_cleansed = float(2.75)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_5_SAVE_dollar_5_when_you_spend_dollar_15_on_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 5.0 SAVE $5 when you spend $15 on "
        test_input_price += "participating products* Only with your Giant "
        test_input_price += "card. *In a single transaction. "
        test_input_price += "Limit 1 offer per transaction."
        test_expected_price_cleansed = float(1.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_slash_5_SAVE_5_when_you_spend_15_on_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 6.0 SAVE $5 when you spend $15 on "
        test_input_price += "participating products* Only with your Giant Card. "
        test_input_price += "* In a single transaction. Limit 1 offer per transaction."
        test_expected_price_cleansed = float(2.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_10_SAVE_dollar_5_When_you_spend_dollar_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 10.0 SAVE $5 When you spend $15 on participating "
        test_input_price += "products* In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(5.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_7_SAVE_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 SAVE $5 when you spend $15 on participating "
        test_input_price += "products* Some Exclusions Apply In a single transaction "
        test_input_price += "from 9/1-9/7/17 Only with your Giant card "
        test_input_price += "or register phone number!"
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_7_SAVE_dollar_5_When_you_spend_dollar_15_on_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 SAVE $5 When you spend $15 on participating "
        test_input_price += "products. In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_Save_dollar_5_when_you_spend_dollar_15_on_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 Save $5 when you spend $15 on participating "
        test_input_price += "products* Only with your Giant card. * "
        test_input_price += "In a single transactions. Limit 1 offer per transaction."
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_Save_dollar_5_when_you_spend__DOLLAR_15_on_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 Save $5 when you spend $15 on participating "
        test_input_price += "products* Only with your Giant card. * "
        test_input_price += "In a single transaction. Limit 1 offer per transaction."
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_SAVE_dollar_5_When_you_spend_dollar_15_on_participating(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 SAVE $5 When you spend $15 on participating products. "
        test_input_price += "In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_SAV_dollar_5_When_you_spend_dollar_15_on(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 SAVE $5 When you spend $15 on participating "
        test_input_price += "products. In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_SAVE_dollar_5_when_you_spend_dollar_15_on_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 SAVE $5 when you spend $15 on participating "
        test_input_price += "products* In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_HOT_SALE_W_O_MVP_Card_dollar_4_09_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 HOT SALE W/O MVP Card $4.09 EA"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FREE_when_you_buy_10_Other_quantities(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FREE when you buy 10* *"
        test_input_price += "Other quantities 10/$10 "
        test_input_price += "Limit 2 offers per transaction"
        test_expected_price_cleansed = float(0.83)
        test_expected_multibuy = 12
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_SAVE_dollar_5_When_you_spend_dollar_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 SAVE $5 When you spend $15 on participating "
        test_input_price += "products. In a single transaction from 9/1-9/7/17. "
        test_input_price += "Only with your Giant card or registered phone number!"
        test_expected_price_cleansed = float(1.00)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_MVP_BUY_ONE_GET_ONE_FREE_SINGLE_ITEM_HALF_PRICE_WO_MVP_Card_7_99_ea(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "MVP BUY ONE GET ONE FREE SINGLE "
        test_input_price += "ITEM HALF PRICE W/O MVP Card $7.99 ea"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_Floral_not_included(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 Floral not included."
        test_expected_price_cleansed = float(10.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUY_1_comma_GET_1_50_percent_OFF_Star_Equal_or_lesser(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 50% OFF* "
        test_input_price += "Equal or lesser value "
        test_input_price += "Must purchase 2 to get discount price"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUY_1_comma_GET_1_50_percent_OFF_star_Equal(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1 50% OFF* "
        test_input_price += "Equal or lesser value Excludes "
        test_input_price += "multi-packs Must purchase 2 to get discount price"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_4_for_4_SAVE_dollar_4_WHEN_YOU_BUY_4_Must_purchase_4_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 4 for 4.0 SAVE $4 WHEN YOU BUY 4 "
        test_input_price += "Must purchase 4 to get discount price"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_2_for_1_SAVE_70_cent_WHEN_YOU_BUY_2_Must_purchase_2_to_get_discount_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE 2 for 1.0 SAVE 70¢ "
        test_input_price += "WHEN YOU BUY 2 Must purchase 2 "
        test_input_price += "to get discount price"
        test_expected_price_cleansed = float(0.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_15_Selection_may_vary_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "15.0 Selection may vary by store."
        test_expected_price_cleansed = float(15.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_20_Airtime_sold_separately(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "20.0 Airtime sold separately."
        test_expected_price_cleansed = float(20.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Reg_Price_5_0(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Reg. Price 5.0"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_AT_and_T_Top_Up_Airtime_Card(self):

        # Input and expected result.
        test_input_title = "AT&T Top Up Airtime Card "
        test_input_description = "test description"
        test_input_price = "NOW 40.5 10% OFF"
        test_expected_price_cleansed = float(40.51)
        test_expected_multibuy = ""
        test_expected_promotion_type = PERCENT_OFF
        test_expected_title_cleansed = "AT&T Top Up Airtime Card test description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_7_Save_dollar_5_when_you_buy_any_5_participating_Kraft(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 Save $5 when you buy any 5 participating "
        test_input_price += "Kraft or Heinz products Items must be purchased "
        test_input_price += "in a single transaction between 9/8-9/14/17"
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_4_Save_dollar_5_when_you_buy_any_5_participating_Kraft(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 4.0 Save $5 when you buy any 5 participating "
        test_input_price += "Kraft or Heinz products Items must be purchased "
        test_input_price += "in a single transaction between 9/8-9/14/17"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_50_cent_off_dot_Save_dollar_5_when_you_buy_any_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "50¢ off. Save $5 when you buy any 5 "
        test_input_price += "participating Kraft or Heinz products "
        test_input_price += "Items must be purchased in a single "
        test_input_price += "transaction between 9/8-9/14/17"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_retailer_We_will_reimburse_you_the_face_value_of(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "retailer: We will reimburse you the face "
        test_input_price += "value of this coupon plus 8 cent handling "
        test_input_price += "provided you and the consumer have complied "
        test_input_price += "with the terms of this offer. Invoices "
        test_input_price += "proving purchases of sufficient stock to "
        test_input_price += "cover presented coupons must be shown on "
        test_input_price += "request. Any other application may constitute "
        test_input_price += "fraud. Coupon void where prohibited, taxed "
        test_input_price += "or restricted. Consumer must pay any sales tax."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_6_SAVE_dollar_3_when_you_buy_any_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 SAVE $3 when you buy any 10 participating "
        test_input_price += "products In a single transaction from "
        test_input_price += "9/8-9/14/17.  Only with your Giant card "
        test_input_price += "or registered phone number!"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_5_SAVE_dollar_3_when_you_buy_any(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 5.0 SAVE $3 when you buy any 10 participating "
        test_input_price += "products In a single transaction from "
        test_input_price += "9/8-9/14/17.  Only with your Giant card "
        test_input_price += "or registered phone number!"
        test_expected_price_cleansed = float(1.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_slash_10_SAVE_dollar_3_when_you_buy_any(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10/ 10.0 SAVE $3 when you buy any 10 "
        test_input_price += "participating products In a single "
        test_input_price += "transaction from 9/8-9/14/17.  "
        test_input_price += "Only with your Giant card or "
        test_input_price += "registered phone number!"
        test_expected_price_cleansed = float(1.0)
        test_expected_multibuy = 10
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_Only_with_your_Giant_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.0 Only with your Giant card. "
        test_input_price += "*In a single transaction."
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_slash_10_Other_quantities_3_slash_dollar_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 10.0 *Other quantities 3/$10 "
        test_input_price += "Limit 2 offers per transaction."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_99_Moneysaving_WEEKLY_DEALS_in_every_aisle(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 Money-saving WEEKLY DEALS in every aisle."
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Buy_Any_Osem_Cake(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy Any 2 Osem Cake 8.8 oz. get Bamba 1 oz. free "
        test_input_price += "RETAILER: We will reimburse you the face value "
        test_input_price += "of this coupon plus & handling provides you "
        test_input_price += "and the consumer have compiled with the terms "
        test_input_price += "of this offer. Invoices providing purchased of "
        test_input_price += "sufficient stock to cover presented coupons must "
        test_input_price += "be shown on request. Any other application may "
        test_input_price += "fraud. Coupon void where prohibited taxed or "
        test_input_price += "restricted. Consumer must pay any sales tax. "
        test_input_price += "Cash value reproduction of this coupon is "
        test_input_price += "expressly prohibited."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_3_Slash_9_dollar_2_off_of_3_WITH_COUPON_IN_MOST_SUNDAY_PAPERS_Limit(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 3/ 9.0 -$2.00 off "
        test_input_price += "of 3 WITH COUPON IN MOST SUNDAY "
        test_input_price += "PAPERS Limit 1"
        test_expected_price_cleansed = float(3.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_3_day_sale(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.0 3 day sale!"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_99_excludes_Organic(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 (excludes Organic)"
        test_expected_price_cleansed = float(2.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_three_comma_get_one_free_star_While_supplies_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy three, get one free *While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_save_Dollar_50_on_your_next_shopping_trip_via_Custom(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $50 on your next shopping trip via Custom "
        test_input_price += "at checkout when you buy one of the Element TVs "
        test_input_price += "featured above* *While supplies last. "
        test_input_price += "No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Buy_two_comma_get_two_free(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy two, get two free"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_0_Select_stores_only(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.0 Select stores only."
        test_expected_price_cleansed = float(10.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_5_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE 5.5"
        test_expected_price_cleansed = float(5.50)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_18_99_BONUS_3000_equals_dollar_3_reward_when_you_buy_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "18.99 BONUS 3000=$3 reward when you buy 2†† †† Good on next purchase requirement must be met in a single transaction, before taxes and after discounts, store credit and redemption dollars are applied.Due to state and federal laws, points cannot be earned or redeemed on some items. Complete details at walgreens.com/Balance"
        test_expected_price_cleansed = float(18.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3000_BONUS_points__equals_dollar_3_reward(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3000 BONUS points = $3 reward†† when you spend $15 or more on participating Feminine Care products †† Good on next purchases. If offer has purchase requirement, it must "
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BONUS_3000_points_when_you_spend_dollar_15_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS 3000 points when you spend $15 or more on participating Feminine Care products = $3 reward†† †† Good on next purchase. Purchase requirememt must be met in a single transaction, before taxes and after discounts, store credit and redemption dollars are applied. Due to state and federal laws, points cannot be earned or redeemed on some items. Complete details at Walgreens.com/Balance"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BONUS_POINTS_2000_dollar_2_reward_when_you_buy_participating_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BONUS POINTS 2000= $2 reward when you buy participating products†† ‡‡Valid in select stores. See associate for details."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_8_REGISTER_REWARDS_on_next_purchase_when_you_spend_dollar_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$8 REGISTER REWARDS® on next purchase when you spend $15 or more on participating products** **Only available on in-store purchases. Limit 1 coupon per customer per printed offer. See coupon for exclusions, limitations and expiration. Card required for sale price but not to redeem Register Rewards. If offer has purchase requirement, it must be met in a single transaction, before taxes, after discounts, store credit and redemption dollars are applied."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_Bonus_point_2000(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 Bonus point 2000 = $2 reward When you buy 2†† †† Good on next purchase. Purchase requirement must be met in a single transaction, before taxes and after discounts, store credit and redemption dollars are applied. Due to state and federal laws, points cannot be earned or redeemed on some items. Complete details at Walgreens. com/Balance"
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_19_99_Dollar_5_less_coupon_online_or_in_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "19.99 $5 less coupon online or in store‡ ‡ Clip paperless coupons to card at Walgreens.com/Coupons. † Only available on in-store purchases."
        test_expected_price_cleansed = float(19.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_dollar_1_less_coupon_online_or_in_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99  $1 less coupon online or in store‡ †Only available on in-store purchases. ‡Clip paperless coupon to card at Walgreens.com/coupon."
        test_expected_price_cleansed = float(6.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_11_99_dollar_4_mail_in_rebate_horseshoe_Prices_may_vary_by_state(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 $4 mail-in rebateΩ Prices may vary by state. Alcoholic beverages available at select Walgreens locations. Plus deposit or CRV where required. Ω Rebate form prints at register. see form for terms, exclusions and expiration. rebate offered by manufacturer.  "
        test_expected_price_cleansed = float(11.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_8_99_dollar_5_mail_in_rebate_on_2_horeshoe_Prices_may_vary_by_state(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "8.99 $5 mail-in rebate on 2Ω Prices may vary by state. Alcoholic beverages available at select Walgreens locations. Plus deposit or CRV where required. Ω Rebate form prints at register. See form for terms, exclusions and expiration. Rebate offered by manufacturer."
        test_expected_price_cleansed = float(8.99)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_13_99_dollar_4_mail_in_rebate_horseshoe_Prices_may_vary_by_state(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "13.99 $4 mail-in rebateΩ Prices may vary by state. Alcoholic beverages available at select Walgreens locations. Plus deposit or CRV where required. Ω Rebate form prints at register. See form for terms, exclusions and expiration. Rebate offered by manufacturer."
        test_expected_price_cleansed = float(13.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_16_99_dollar_3_mail_in_rebate_horseshoe(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "16.99 $3 mail-in rebateΩ"
        test_expected_price_cleansed = float(16.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_HOT_DEAL(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 HOT DEAL"
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_cross_Only_available_on_dash_in_store_purchases(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "† Only available on-in store purchases."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_coupon_savings_19_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "coupon savings 19.99"
        test_expected_price_cleansed = float(19.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_9_99_plus_Only_available_on_instore_purchases(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 +Only available on in-store purchases."
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_See_gift_card_for_terms_conditions_and_applicable_fees(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "See gift card for terms, conditions and applicable fees.** ** Selection may vary by store. Cards have no value until activated at register. See gift card for tems and conditions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_BONUS_POINTS_3000_equal_dollar_3_reward_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 BONUS POINTS 3000=$3 reward when you spend $10†† † Only available on in-store purchases. †† Good on next purchase. Purchase requirement must be met in a single "
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "See description for details"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_99_USE_DIGITAL_COUPON_UP_TO_5X_IN_THE_SAME_TRANSACTION(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 USE DIGITAL COUPON UP TO 5X IN THE SAME TRANSACTION "
        test_input_price += "Weekly sale price without digital coupon is $1.99 each with Card. While supplies last."
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FREE_KRAFT_SHREDDED_CHEESE_6_67_8_OZ_PKG(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE KRAFT SHREDDED CHEESE 6.67-8 OZ. PKG., "
        test_input_price += "WHEN YOU SPEND $7 ON PARTICIPATING OLD EL PASO PRODUCTS* "
        test_input_price += "*In a single transaction"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FREE_KRAFT_SHREDDED_CHEESE_6_67_8_OZ_dot_PKG_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE KRAFT SHREDDED CHEESE 6.67-8 OZ. PKG., WHEN YOU SPEND $7 ON PARTICIPATING OLD EL PASO PRODUCTS* Sizes May Vary by Store. *In a single transaction"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_79_Not_all_items_available_in_all_stores_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.79 Not all items available in all stores."
        test_expected_price_cleansed = float(0.79)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Exclusions_apply_dot_See_store_for_details_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Exclusions apply. See store for details."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_Some_Exclusions_Apply(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 Some Exclusions Apply"
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_Where_Available(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 Where Available"
        test_expected_price_cleansed = float(6.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_Dollar_5_WHEN_YOU_SPEND_dollar_20_ON_ALL_HEALTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $5 WHEN YOU SPEND $20 ON ALL HEALTH & BEAUTY PRODUCTS *EXCLUDES HAIR CARD Only with you stop & shop card  *In a single transaction."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_Dollar_6_when_you_spend_dollar_20_on_participating_product(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $6 when you spend $20 on participating product* * Some exclusion apply.In a single transaction with your Stop & Shop card"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_88_May_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.88 May Vary by Store"
        test_expected_price_cleansed = float(0.88)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_2_00_INSTANTLY_on_any_32_oz(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $2.00 INSTANTLY on any 32 oz. or larger ZING ZANG BLOODY MARY MIX with the purchase of ONE (1) 1.75-liter bottle This coupon is good on any 32 oz. or larger bottle of ZING ZANG Bloody Mary Mix with the purchase of ONE (1)1.75-Liter bottle of TITO'S Handmade Vodka. A ZING ZANG BLOODY MARY MIX PURCHASE GREATER THAN $2.00 IS REQUIRED TO QUALIFY FOR THIS OFFER. This offer is limited to one coupon per purchase. You must be 21 years of age or older to redeem this coupon."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Mix__match_any_participating_items_and_save_on(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Mix & match any participating items and save on your next shopping trip. Select varieties. No rainchecks or substitutions. Limited one coupon per transaction. Conagra Brands, Inc. All Rights Reserved."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_1_Instantly_on_the_purchase_of_one_1_750ml_of_Evan_Williams_Bourbon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $1 Instantly on the purchase of one (1) 750ml of Evan Williams Bourbon"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_2_00_Instantly_on_the_purchase_of_one_1_750ml_of_Larceny_Bourbon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $2.00 Instantly on the purchase of one (1) 750ml of Larceny Bourbon"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_3_00_INSTANTLY_ON_THE_PURCHASE_OF_ONE_1_750ML_BOTTLE_OF_Elijah_Craig_SMALL_Batch(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $3.00 INSTANTLY ON THE PURCHASE OF ONE (1) 750ML BOTTLE OF Elijah Craig SMALL Batch"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_get_one_50_off_of_equal_or_lesser_value_While_supplies_last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one, get one 50%* off of equal or lesser value *While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_get_one_50_off_of_equal_or_lesser_value_Excludes(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one, get one 50%* off of equal or lesser value Excludes travel and trial size. Offers cannot mix or match."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = BUY_ONE_GET_ONE_HALF_PRICE
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_five_get_one_of_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy five, get one of equal or lesser value free *While supplies last. No rainchecks or substitutions"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_24_99_buy_one_Wonder_Woman_DVD_Orville(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "24.99 buy one Wonder Woman DVD or Blu-ray Combo Pack, get one Orville Redenbacher's Popcorn 3 ct./8.07-9.87 oz. All varieties free* A 2.99 value. *While supplies last. No rainchecks or substitutions"
        test_expected_price_cleansed = float(24.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_two_Libbys_100_Pure_Pumpkin_15_oz(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy two Libby's 100% Pure Pumpkin 15 oz., get one Carnation Evaporated Milk 12 oz. Excludes organic. free* *While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_save_10_via_Custom_Coupon_at_checkout_when_you_buy_40_or_more_of_Luvs_Diapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $10 via Custom Coupon at checkout when you buy $40 or more of Luvs Diapers*"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_three_get_one_of_equal_or_lesser_value(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy three, get one of equal or lesser value free *While supplies last. No rainchecks or substitutions"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_buy_one_Softsoap_Body_Wash_get_one_Softsoap(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy one Softsoap Body Wash get one Softsoap Liquid Hand Soap Pump 7.5 oz. free* *While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_24_99_buy_one_Wonder_Woman_DVD_Orvillie(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "24.99 buy one Wonder Woman DVD or Blu-ray Combo Pack, get one Orvillie Redennacher's popcorn 3 ct./8.07-9.87 oz. All varieties free* 2.99 value. *While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(24.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_59_99_Date_Subject_to_change(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "59.99 Date Subject to change. *While supplies last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(59.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_Must_bring_coupon_to_get_advertised_discount__Good(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 Must bring coupon to get advertised discount. Good only at RITE AID Pharmacies. Limit one per customer. Coupon redemption paid by manufacturer. Not valid if duplicated."
        test_expected_price_cleansed = float(5.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_95_Fees_and_limits_apply(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.95 Fees and limits apply"
        test_expected_price_cleansed = float(5.95)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test__SAVE_1_When_you_buy_any_TWO_Must_buy_two_qualifying_items_to_receive_discount_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " SAVE $1 When you buy any TWO Must buy two qualifying items to receive discount."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR_4_0_PRICE_DROP(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 4.0 PRICE DROP!"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_3_when_you_spend_10_on_participating_Dove_products(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $3 when you spend $10 on participating Dove products* Only with your Stop & Shop card. *In a single transaction. Participating Varieties and Sizes May Vary by Store"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FREE_when_you_buy_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FREE when you buy 1"
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Final_price_2_4_0_DIGITAL_COUPON_1_00_OFF_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Final price 2/ 4.0 DIGITAL COUPON $1.00 OFF 2"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Final_price_3_7_0_5_00_OFF_3_DIGITAL_COUPON(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Final price 3/ 7.0 $5.00 OFF 3 DIGITAL COUPON"
        test_expected_price_cleansed = float(2.33)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_10_0_Other_quantities_26_Where_Available_While_Supplies_Last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5/ 10.0 *Other quantities 2/$6 Where Available While Supplies Last"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_6_0_Other_quantities_25(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 6.0 *Other quantities 2/$5"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_6_0_Plus_Deposit_Where_Applicable(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 6.0 Plus Deposit Where Applicable"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_5_0_SAVE_2_when_you_buy_4_participating_products_Only_with_your_Stop__Shop_card_In_a_single_transaction_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 5.0 SAVE $2 when you buy 4 participating products* Only with your Stop & Shop card.*In a single transaction."
        test_expected_price_cleansed = float(1.67)
        test_expected_multibuy = 3
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_7_0_buy_theirs_get_ours_free_When_purchase_in_a_single_transaction_with_your_stop__shop_card_from_106101217(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 buy theirs get ours free* *When purchase in a single transaction with your stop & shop card from 10/6-10/12/17"
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_8_0_Where_Available_While_Supplies_Last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 8.0 Where Available While Supplies Last"
        test_expected_price_cleansed = float(4.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_10_0_Where_Available_While_Supplies_Last_In_a_single_transaction(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5/ 10.0 Where Available While Supplies Last *In a single transaction"
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_5_0_Participating_Varieties_and_Sizes_May_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 5.0 Participating Varieties and Sizes May Vary by Store"
        test_expected_price_cleansed = float(1.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_3_0_Participating_Varieties_and_Sizes_May_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 3.0 Participating Varieties and Sizes May Vary by Store"
        test_expected_price_cleansed = float(1.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_10_0_Participating_Varieties_and_Sizes_May_Vary_by_Store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 10.0 Participating Varieties and Sizes May Vary by Store"
        test_expected_price_cleansed = float(5.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test__FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products*. SAVE UP TO $3.79/EA. Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/610/12/17."
        test_expected_price_cleansed = float(-1.0)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_10_0_FREE_NATUREs_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5/ 10.0 FREE NATURE's PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/610/12/17."
        test_expected_price_cleansed = float(2.0)
        test_expected_multibuy = 5
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_10_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 10.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number *In a single transaction from, 10/6-10/12/17"
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_7_0_FREE_NATUREs_PROMISE_ORGANIC_SALAD_MIX_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 7.0 FREE NATURE's PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/610/12/17."
        test_expected_price_cleansed = float(3.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_10_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 10.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/6-12/17."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_6_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 6.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number *In a single transaction from, 10/6-10/12/17"
        test_expected_price_cleansed = float(3.0)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_49_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.49 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products*. Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/610/12/17."
        test_expected_price_cleansed = float(4.49)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_99_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop and Shop card or registered phone number! *Ina single transaction from 10/6-10/12/17"
        test_expected_price_cleansed = float(4.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = LOYALTY_CARD
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_5_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15_on(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your stop & Shop card to registered phone number! *In a single transaction from 10/6-10/12/17."
        test_expected_price_cleansed = float(1.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_5_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/6-12/17."
        test_expected_price_cleansed = float(1.25)
        test_expected_multibuy = 4
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_5_0_FREE_NATURES_PROMISE_ORGANIC_SALAD_MIX_when_you_spend_15(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 FREE NATURE'S PROMISE ORGANIC SALAD MIX when you spend $15 on participating products* Only with your Stop & Shop card or registered phone number! *In a single transaction from 10/610/12/17."
        test_expected_price_cleansed = float(2.50)
        test_expected_multibuy = 2
        test_expected_promotion_type = MULTIBUY
        test_expected_title_cleansed = "Test Title Test Description"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

