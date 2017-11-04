#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from StoreItem import StoreItem

# Get the Promotion Type categories.
from DataCleanse import *

#
# Categorise all tests for the Web Grocer Retailers.
#
class TestWebgrocer(object):

    def setup_method(self, method):
        self.dut = StoreItem()


    def teardown_method(self, method):
        pass


    def test_dollar_99_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description™"
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
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_dollar_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $5"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_99_Cross_symbol_Only_available_on_in_store(self):

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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_for_dollar_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10 for $10"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $99"
        test_expected_price_cleansed = float(33.0)
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

    def test_2_for_dollar_7(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $7"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_dollar_6(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $6"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_FOR_dollar_10_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4 FOR $10.00 with Price Plus Card"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR__dollar_22_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR $22.00 with Price Plus Card"
        test_expected_price_cleansed = float(11.00)
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

    def test_2_FOR_dollar_7_Club_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR $7 Club Price"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_1_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.00 with Price Plus Card"
        test_expected_price_cleansed = float(1.0)
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

    def test_dollar_2_49_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$2.49 with Price Plus Card"
        test_expected_price_cleansed = float(2.49)
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

    def test_79_cents_ea_with_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "79¢ ea with card"
        test_expected_price_cleansed = float(0.79)
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

    def test_SPEND_dollar_3_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $3, See description for details"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_9_when_you_BUY_6_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $9 when you BUY 6 or more"
        test_expected_price_cleansed = float(3.0)
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

    def test_dollar_8_10_when_you_BUY_6_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$8.10 when you BUY 6 or more"
        test_expected_price_cleansed = float(8.10)
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

    def test_BUY_1_Kingsford_or_dots__AND_GET_1_Kingsford_BBQ_Sauce_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 Kingsford or.. "
        test_input_price += "AND GET 1 Kingsford BBQ Sauce FREE w/CARD"
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

    def test_PICK_10_PAY_ONLY_77_cent_EA_dot_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "PICK 10 PAY ONLY 77¢ EA. with Price Plus Card"
        test_expected_price_cleansed = float(0.77)
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

    def test_FREE_with_Purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE with Purchase"
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

    def test_3_FOR_dollar_15_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 FOR $15.0 with Price Plus Card"
        test_expected_price_cleansed = float(5.0)
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

    def test_3_FOR__dollar_3_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 FOR $3 with Price Plus Card"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SALE_dollar_3_39to_dollar_6_79_EA_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SALE: $3.39 to $6.79 EA. with Price Plus Card"
        test_expected_price_cleansed = float(3.39)
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

    def test_BUY_3_dots_AND_GET_1_dots_FREE_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 3...AND GET 1...FREE with Price Plus Card"
        test_expected_price_cleansed = float(-1.00)
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

    def test_BUY_2_dots_AND_GET_1_dots_FREE_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 2... AND GET 1... FREE with Price Plus Card"
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

    def test_Your_Choice_bang_dollar_1_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Your Choice! $1.99"
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

    def test_YOUR_CHOICE_dollar_2_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "YOUR CHOICE $2.99"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUY_3_FOR_ONLY_dollar_3_99_EA_dot__with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 3 FOR ONLY $3.99 EA. with Price Plus Card"
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

    def test_97_cent_with_Price_QPlus_Car(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "97¢ with Price QPlus Car"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_99_cent_EA_Club_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "99¢ EA. Club Price"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_89_cent_ea(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "89¢ ea"
        test_expected_price_cleansed = float(0.89)
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

    def test_BUY_1_GET_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1"
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

    def test_FREE_star_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE*, See description for details"
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

    def test_dollar_8_10_when_you_BUY_6_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$8.10 when you BUY 6 or more"
        test_expected_price_cleansed = float(8.10)
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

    def test_dollar_1_99_WHEN_YOU_BUY_3_LIMIT_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.99 WHEN YOU BUY 3 LIMIT 3"
        test_expected_price_cleansed = float(1.99)
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

    def test_99_cent_lb_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "99¢ lb."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_for_dollar_10_WHEN_YOU_BUY_5_Limit_1_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5 for $10 WHEN YOU BUY 5 Limit 1 offer"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_for_dollar_9_98_WHEN_YOU_BUY_4_with_coupon_on(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4 for $10 WHEN YOU BUY 4 with coupon on "
        test_input_price += "pg. 4 Limit 1 offer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_12_WHEN_YOU_BUY_3_LIMIT_3_TOTAL(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $12 WHEN YOU BUY 3 LIMIT 3 TOTAL"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_97_Cent_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "97¢ with Price Plus Card"
        test_expected_price_cleansed = float(0.97)
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

    def test_dollar_5_with_your_club_card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$5 with your club card"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_99_cent_SALE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "99¢ SALE"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FINAL_PRICE_dollar_2_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FINAL PRICE $2.99"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_patties_or_links_for_dollar_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10 patties or links for $10"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Every_Day_dollar_1_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Every Day $1.99"
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

    def test_Every_Day_79_cent(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Every Day 79¢"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_99_cent(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "99¢"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_dollar_1_Instantly_when_you_buy_4_in_a_single_transaction(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $1 Instantly when you buy 4 "
        test_input_price += "in a single transaction"
        test_expected_price_cleansed = float(-1.00)
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

    def test_SAVE_dollar_1_Instantly_when_you_buy_4_in_a_single_transaction(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $1 Instantly when you buy 4 "
        test_input_price += "in a single transaction"
        test_expected_price_cleansed = float(-1.00)
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

    def test_5_FOR_dollar_5_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5 FOR $5 with Price Plus Card"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_9_WHEN_YOU_BUY_3_Limit_1_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $9 WHEN YOU BUY 3 Limit 1 offer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_6_WHEN_YOU_BUY_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $6 WHEN YOU BUY 3"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_12_WHEN_YOU_BUY_3_Limit_1_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $12 WHEN YOU BUY 3 Limit 1 offer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_6_WHEN_YOU_BUY_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $6.00 WHEN YOU BUY 3"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_10_WHEN_YOU_BUY_3_Limit_1_offer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $9 WHEN YOU BUY 3 Limit 1 offer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_3_for_dollar_3_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 for $3 Plus deposit where required"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR_dollar_4_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR $4 with Price Plus Card"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_for_dollar_22_WHEN_YOU_BUY_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $22.00 WHEN YOU BUY 2"
        test_expected_price_cleansed = float(11.0)
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

    def test_2_for_dollar_11_WHEN_YOU_BUY_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $11 WHEN YOU BUY 2"
        test_expected_price_cleansed = float(5.50)
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

    def test_2_for_dollar_10_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 for $10 Plus deposit where required"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_FREE_bang_star_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE!*, See description for details"
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

    def test_FREE_bang_INSTANTLY_comma_See_description_for_detail(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE! INSTANTLY, See description for details"
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

    def test_79_cent_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "79¢, See description for details"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_79_cent_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "79¢ Plus deposit where required"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_88_cent_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "88¢ Plus deposit where required"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_See_Circular_Page_for_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "See Circular Page for Price"
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

    def test_new_line(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description\nmore description"
        test_input_price = "See Circular Page for Price"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description More Description"

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

    def test_remove_slash_new_lines(self):

        # Input and expected result.
        test_input_title = "Coleman Breaded Organic Chicken"
        test_input_description = "	8 oz. pkg.; frozen \nstrips, "
        test_input_description += "tenders \nor nuggets. meat SAVINGS"
        test_input_price = "$4.99 ea."
        test_expected_price_cleansed = float(4.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coleman Breaded Organic Chicken "
        test_expected_title_cleansed += "8 oz pkg"

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

    def test_slash_u0026(self):

        # Input and expected result.
        test_input_title = "test \u0027 title"
        test_input_description = "test \u0026 description \u0029 60 oz. "
        test_input_description += "Health \u0026 Home SAVINGS "
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title Test Description 60 oz Health"

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

    def test_Large_Snow_Crab_Clusters_FRIDAY_SEPTEMBER_1ST_THRU_MONDAY(self):

        # Input and expected result.
        test_input_title = "Large Snow Crab Clusters"
        test_input_description = "FRIDAY SEPTEMBER 1ST THRU MONDAY SEPTEMBER 4TH "
        test_input_description += "wild caught. ACME Celebrate LABOR DAY"
        test_input_price = "3.55"
        test_expected_price_cleansed = float(3.55)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Large Snow Crab Clusters Wild caught"

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

    def test_Lawrys_Marinades_FRIDAY_SEPTEMBER_1ST_THRU_MONDAY(self):

        # Input and expected result.
        test_input_title = "Lawrys Marinades"
        test_input_description = "FRIDAY SEPTEMBER 1ST THRU MONDAY SEPTEMBER 4TH "
        test_input_description += "12 fl. oz. btl. ACME Celebrate LABOR DAY"
        test_input_price = "2.33"
        test_expected_price_cleansed = float(2.33)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lawrys Marinades 12 fl oz btl"

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

    def test_4_packages_for_dollar_19_99_PLUS_comma_many_more_in_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4 packages for $19.99 PLUS, many more in store! "
        test_input_price += "MIX \u0026 MATCH"
        test_expected_price_cleansed = float(5.00)
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

    def test_FREE_star_with_purchase_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "FREE* with purchase, See description for details"
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

    def test_dollar_4_99_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$4.99 Every Day"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_5_Every_Day(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$5 Every Day"
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

    def test_Your_Choice_of_either_1_lb_Potato_Salad(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "Your Choice of either: 1 lb. Potato Salad, "
        test_input_description += "Macaroni Salad or Cole Slaw and 4 King’s "
        test_input_description += "Hawaiian Rolls"
        test_input_price = "0.99"
        test_expected_price_cleansed = float(0.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title"

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

    def test_Dinner_Includes_8_Piece_Fried_or_Baked_Chicken(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "Dinner Includes: (1) 8 Piece Fried "
        test_input_description += "or Baked Chicken or (1) Rotisserie "
        test_input_description += "Chicken"
        test_input_price = "1.99"
        test_expected_price_cleansed = float(1.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title"

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

    def test_fresh_ground_instore_daily(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "fresh ground in-store daily"
        test_input_price = "2.88"
        test_expected_price_cleansed = float(2.88)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Test Title"

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

    def test_dollar_1_comma_See_description_for_details(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1, See description for details"
        test_expected_price_cleansed = float(1.00)
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

    def test_dollar_18_90_Card_Price_when_you_BUY_6_or_more(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$18.90 Card Price when you BUY 6 or more"
        test_expected_price_cleansed = float(18.90)
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

    def test_dollar_1_99_Card_Price_LIMIT_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.99 Card Price LIMIT 3"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_dollar_7_99_Card_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$7.99 Card Price"
        test_expected_price_cleansed = float(7.99)
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

    def test_BUY_2_Gatorade_GET_5_PROPEL_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 2 Gatorade GET 5 PROPEL FREE"
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

    def test_dollar_21_99_Club_Price_Plus_deposit_in_Oregon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$21.99 Club Price Plus deposit in Oregon"
        test_expected_price_cleansed = float(21.99)
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

    def test__dollar_6_99_Club_Price_CRV(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$6.99 Club Price +CRV"
        test_expected_price_cleansed = float(6.99)
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

    def test_dollar_1_99_Club_Price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.99 Club Price"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SAVE_AT_CHECKOUT_3_00_MUST_BUY_both_To_Receive_Discount_WC(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE AT CHECKOUT $3.00 MUST BUY both To Receive Discount W/C"
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

    def test_1_49_MFR_with_Price_Plus_Card(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$1.49 MFR with Price Plus Card"
        test_expected_price_cleansed = float(1.49)
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

    def test_29_99_to_49_99(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$29.99 to $49.99"
        test_expected_price_cleansed = float(29.99)
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

    def test_COMING_SOON(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "COMING SOON!"
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

    def test_4_99_buy_5_save_5_instantly_Mix_or_match_signed_items(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 buy 5 & save $5 instantly* Mix or match "
        test_input_price += "signed items across store. *While supplies last. "
        test_input_price += "No rainchecks or substitutions"
        test_expected_price_cleansed = float(4.99)
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

    def test_3_49_buy_5_save_5_instantly_mix_or_match_signed_items(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.49 buy 5 & save $5 instantly* mix or match "
        test_input_price += "signed items across store *While supplies last. "
        test_input_price += "No rainchecks or substitutions"
        test_expected_price_cleansed = float(3.49)
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

    def test_2_89_buy_5_save_5_instantly_Mix_or_match_signed_items(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.89 buy 5 & save $5 instantly*. "
        test_input_price += "Mix or match signed items across store. "
        test_input_price += "*While supplies last. No rainchecks or substitutions"
        test_expected_price_cleansed = float(2.89)
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

    def test_get_both_for_7_0_buy_one_Meijer_Rotisserie_Chicken(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "get both for 7.0 buy one Meijer Rotisserie "
        test_input_price += "Chicken 30 oz. and one Coca-Cola 2 Liter "
        test_input_price += "Plus deposit where applicable *While supplies "
        test_input_price += "last. No rainchecks or substitutions."
        test_expected_price_cleansed = float(7.00)
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

    def test__save_10_on_your_next_shopping_trip_when_you_buy_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " save $10 on your next shopping trip when you buy 2"
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

    def test_0_88_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.88 EXTRA hot price!"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_99_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 EXTRA hot price!"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_49_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.49 EXTRA hot price!"
        test_expected_price_cleansed = float(2.49)
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

    def test_10_99_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.99 EXTRA hot price!"
        test_expected_price_cleansed = float(10.99)
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

    def test_13_99_EXTRA_hot_price_While_supplies_last__No_rainchecks_or_substitutions_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "13.99 EXTRA hot price! *While supplies last. No rainchecks or substitutions."
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 EXTRA hot price!"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_0_EXTRA_hot_price(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.0 EXTRA hot price!"
        test_expected_price_cleansed = float(1.00)
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

