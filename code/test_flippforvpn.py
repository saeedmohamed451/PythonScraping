#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from StoreItem import StoreItem

# Get the Promotion Type categories.
from DataCleanse import *


#
# Categorise all tests for the Flipp For VPN Retailers.
#
class TestFlippForVpn(object):

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


    def test_Earn_100_Plenti_points_Worth_dollar_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Earn 100 Plenti points* "
        test_input_price += "Worth $1.00 When you buy 2 of these items."
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

    def test_Earn_800_Plenti_points_start_Worth_dollar_8(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Earn 800 Plenti points* "
        test_input_price += "Worth $8.00 When you buy $50 of these items."
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

    def test_Earn_200_Plenti_points_star_When_you_buy_2(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Earn 200 Plenti points* "
        test_input_price += "When you buy 2 of these items."
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

    def test_BUY_TWO_GET_THIRD_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY TWO GET THIRD FREE!"
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

    def test_Buy_1_Get_1_50_off_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 1 Get 1* 50% off WITH CARD"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD_PLUS_5_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD "
        test_input_price += "PLUS $5 ExtraBucks® Rewards when you "
        test_input_price += "spend $15 on ANY of the products "
        test_input_price += "listed here"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD_PLUS_8_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% "
        test_input_price += "OFF WITH CARD PLUS $8 ExtraBucks® Rewards "
        test_input_price += "when you spend $25 on ANY of these products"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD_PLUS_BUY_4_GET_5_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD PLUS "
        test_input_price += "BUY 4 GET $5 ExtraBucks® Rewards"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD_SPEND_12_GET_3_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD. "
        test_input_price += "SPEND $12 GET $3 ExtraBucks® Rewards"
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

    def test_BUY_1_GET_1_50_OFF_WITH_CARD_SPEND_20_GET_5_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD. "
        test_input_price += "SPEND $20 GET $5 ExtraBucks® Rewards"
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

    def test_Buy_1_Get_1_star_50_percent_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Buy 1 Get 1* 50% WITH CARD"
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

    def test_BUY_1_GET_1_star_50_percent_OFF_plus_SPEND_dollar_25(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1* 50% OFF + "
        test_input_price += "SPEND $25, GET $8 ExtraBucks® Rewards"
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

    def test_BUY_1_comma_GET_1_star_50_OFF_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1* 50% OFF WITH CARD"
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

    def test_BUY_1_comma_GET_1_50_OFF_WITH_CARD_SPEND_dollar_25(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1, GET 1* 50% OFF WITH CARD. SPEND $25, "
        test_input_price += "ON SELECT ALEVE & ALEVE DIRECT THERAPY DEVICE, "
        test_input_price += "GET $8 ExtraBucks® Rewards"
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

    def test_BUY_2_GET_dollar_4_ExtraBucks_Rewards_PLUS_dollar_3_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 2 GET $4 ExtraBucks® Rewards PLUS $3 ExtraBucks® "
        test_input_price += "Rewards when you ANY 2 of the products listed here"
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

    def test_BUY_2_GET_dollar_8_ExtraBucks_Rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 2 GET $8 ExtraBucks® Rewards"
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

    def test_BUY_2_GET_3rd_FREE_star_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 2 GET 3rd FREE* WITH CARD"
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

    def test_save_dollar_1_WITH_CARD_PLUS_BUY_2_GET_dollar_5_ExtraBucks_Rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $1 WITH CARD PLUS BUY 2 "
        test_input_price += "GET $5 ExtraBucks® Rewards"
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

    def test_save_dollar_3_50_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $3.50 WITH CARD"
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
  
    def test_save_dollar_4_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "save $4 WITH CARD"
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

    def test_SPEND_dollar_25_GET_dollar_5_ExtraBucks_Rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $25 GET $5 ExtraBucks® Rewards"
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

    def test_dollar_5_OFF_YOUR_OF_dollar_25_OF_RITE_AID_BRAND(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$5 OFF YOUR OF $25 OF RITE AID BRAND"
        test_expected_price_cleansed = float(25.00)
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

    def test_SAVE_dollar_1_50_WITH_COUPON(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SAVE $1.50 WITH COUPON"
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

    def test_2_99_Earn_100_Plenti_points_start_Worth_dollar_1_2_PRICE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 Earn 100 Plenti points* Worth "
        test_input_price += "$1.00/ 1/2 PRICE WITH CARD  "
        test_input_price += "*Limit 2 offers per customer."
        test_expected_price_cleansed = float(2.99)
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

    def test_1_99_1_2_PRICE_WITH_CARD_Selection_may_vary_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 1/2 PRICE WITH CARD  "
        test_input_price += "Selection may vary by store"
        test_expected_price_cleansed = float(1.99)
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

    def test_3_FOR_9_99_Must_bring_coupon_to_get(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3 FOR 9.99 Must bring coupon to get advertised discount. "
        test_input_price += "Good only at RITE AID Pharmacies. Limit one per customer. "
        test_input_price += "Coupon redemption paid by manufacturer. "
        test_input_price += "Not valid if duplicated."
        test_expected_price_cleansed = float(3.33)
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

    def test_7_99_Earn_300_Plenti_points_star_Worth_dollar_3_when_you(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "7.99 Earn 300 Plenti points* Worth $3.00 when you "
        test_input_price += "buy 2 of these items. WITH CARD  "
        test_input_price += "*Limit 2 offers per customer."
        test_expected_price_cleansed = float(7.99)
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

    def test_16_99_Earn_200_Plenti_points_star_Worth_dollar_2_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "16.99 Earn 200 Plenti points* Worth $2.00 WITH CARD"
        test_input_price += "*Limit 2 offers per customer."
        test_expected_price_cleansed = float(16.99)
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

    def test_2_FOR_10_Earn_500_Plenti_points_star_Worth_dollar_5_When(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 10.0 Earn 500 Plenti points* "
        test_input_price += "Worth $5.00 When you buy $25 of these items. "
        test_input_price += "*Limit 4 offers per customer."
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

    def test_buy_4_of_these_items_OR_99_cents_EA(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4 FOR 2.0 Earn 100 Plenti points* Worth $1.00 "
        test_input_price += "when you buy 4 of these items. OR 99¢ EA. WITH "
        test_input_price += "CARD  *Limit 2 offers per customer."
        test_expected_price_cleansed = float(0.50)
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

    def test_2_99_1_2_PRICE_bang_WITH_CARD_Selection_may_vary_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 1/2 PRICE! WITH CARD  Selection may vary by store"
        test_expected_price_cleansed = float(2.99)
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

    def test_2_FOR_3_OR_1_99_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 3.0 OR 1.99 EA. WITH CARD"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4_FOR_6_OR_1_79_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4 FOR 6.0 OR 1.79 EA. WITH CARD  "
        test_input_price += "or 4 FOR $5 WITH $1.00 OFF ON 4 "
        test_input_price += "MANUFACTURER'S COUPON WITH CARD  "
        test_input_price += "Find this coupon in most Sunday papers"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR_8_excludes_PM__OR_4_29_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 8.0 (excludes PM)  OR 4.29 EA. WITH CARD"
        test_expected_price_cleansed = float(4.00)
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

    def test_title_description(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.0"
        test_expected_price_cleansed = float(0.00)
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

    def test_special_symbol(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description®"
        test_input_price = "0.0"
        test_expected_price_cleansed = float(0.00)
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

    def test_special_symbol_bullet_point(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description•"
        test_input_price = "0.0"
        test_expected_price_cleansed = float(0.00)
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

    def test_special_symbol_trademark(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description™"
        test_input_price = "0.0"
        test_expected_price_cleansed = float(0.00)
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

    def test_0_99_diamond_Plus_deposit_where_required_Limit_3_items(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 ◊Plus deposit where required. Limit 3 items."
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

    def test_4_99_dollar_5_ExtraBucks_Rewards_when_you_spend_dollar_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 $5 ExtraBucks® Rewards "
        test_input_price += "when you spend $20 on ANY of the "
        test_input_price += "products listed here ExtraBucks® Rewards "
        test_input_price += "offer limit of 1 per household with card. "
        test_input_price += "(20003617151)"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_dollar_5_ExtraBucks_Rewards_when_you_spend_dollar_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 $5 ExtraBucks® Rewards "
        test_input_price += "when you spend $20 on ANY of the product "
        test_input_price += "listed here ExtraBucks® "
        test_input_price += "Rewards offer limit of 1 per household "
        test_input_price += "with card. (20003617151)"
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

    def test_2_99_dollar_5_ExtraBucks_Rewards_when_you_spend_dollar_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 $5 ExtraBucks® Rewards "
        test_input_price += "when you spend $20 on ANY of the products "
        test_input_price += "listed here ExtraBucks Rewards offer limit of 1 "
        test_input_price += "per household with card (20003617151)"
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

    def test_SPEND_dollar_15_GET_dollar_5_ExtraBucks_Rewards_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $15 GET $5 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 per "
        test_input_price += "household with card. (20003685847)"
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

    def test_2_99_Brand_may_vary_by_store_excludes_flavored_milk(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 Brand may vary by store "
        test_input_price += "(excludes flavored milk). Limit 2 items."
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

    def test_9_99_dollar_9_99_ExtraBucks_Rewards_for_next_purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 $9.99 ExtraBucks® Rewards for "
        test_input_price += "next purchase ExtraBucks® Rewards offer "
        test_input_price += "limit of 1 per household with card. "
        test_input_price += "(20003675116)"
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

    def test_regular_retail_of_14_99_HP_comma_Canon_or_Epson_ink_cartridges(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "regular retail of 14.99 HP, Canon or Epson ink "
        test_input_price += "cartridges with a regular retail of 14.99-49.99. "
        test_input_price += "BUY 1 GET $3 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 per "
        test_input_price += "household with card. (20003664764)"
        test_expected_price_cleansed = float(14.99)
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

    def test_14_99_BUY_2_GET_dollar_5_ExtraBucks_Rewards_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "14.99 BUY 2 GET $5 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 "
        test_input_price += "per household with card. (20003684151)"
        test_expected_price_cleansed = float(14.99)
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

    def test_1_79_dollar_2_Instant_Coupon_at_coupon_center_Must_be_an_ExtraCare(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.79 $2.00 Instant Coupon at coupon center "
        test_input_price += "Must be an ExtraCare® cardholder as of 8/27/17 "
        test_input_price += "to get this coupon. "
        test_input_price += "Limit of 1 offer per household with card. "
        test_input_price += "Offer valid 9/3/17-9/9/17."
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

    def test_BUY_1_GET_1_star_50_percent_OFF_WITH_CARD_SPEND_30(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY 1 GET 1* 50% OFF WITH CARD. "
        test_input_price += "SPEND $30 GET $10 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 per household "
        test_input_price += "with card. (20003682277) *Discount "
        test_input_price += "applies to item(s) of equal or lesser "
        test_input_price += "value & excludes clearance items."
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

    def test_11_99_BUY_2_GET_dollar_5_ExtraBucks_Rewards_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 BUY 2 GET $5 ExtraBucks® "
        test_input_price += "Rewards ExtraBucks® Rewards offer "
        test_input_price += "limit of 1 per household with card. "
        test_input_price += "(20003685355)"
        test_expected_price_cleansed = float(11.99)
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

    def test_8_99_dollar_2_ExtraBucks_Rewards_for_next_purchase_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "8.99 $2 ExtraBucks® Rewards for next "
        test_input_price += "purchase ExtraBucks® Rewards offer limit "
        test_input_price += "of 1 per household with card. (20003685354)"
        test_expected_price_cleansed = float(8.99)
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

    def test_2_94_dollar_1_coupon_savings_in_our_app(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.94 $1.00 coupon savings in our app** "
        test_input_price += "**Coupons from Sunday newspaper must be "
        test_input_price += "presented at time of purchase."
        test_expected_price_cleansed = float(2.94)
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

    def test_13_99_dollar_5_mfr_s_mail_in_rebate(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "13.99 $5 mfr's mail-in rebate"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_99_dollar_1_instant_coupon_at_coupon_center(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " 0.99 $1.00 instant coupon at coupon center "
        test_input_price += "^Must be an ExtraCare® cardholder as of 8/27/17 "
        test_input_price += "to get this coupon. "
        test_input_price += "Limit of 1 offer per household with card."
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

    def test_9_99_dollar_1_coupon_savings_in_our_app(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 $1.00 coupon savings in our app** "
        test_input_price += "**Coupons from Sunday newspaper must be "
        test_input_price += "presented at time of purchase."
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

    def test_2_99_excludes_Baked(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 (excludes Baked)."
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

    def test_3_44_Brand_may_vary_by_store_dot_diamond_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3.44 Brand may vary by store. "
        test_input_price += "◊Plus deposit where required."
        test_expected_price_cleansed = float(3.44)
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

    def test_2_FOR_5_Earn_100_Plenti_points_star_Worth(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 5.0 Earn 100 Plenti points* "
        test_input_price += "Worth $1.00 When you buy 2 of these items. "
        test_input_price += "OR 2.99 EA. WITH CARD  * "
        test_input_price += "Limit 2 offers per customer."
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

    def test_2_FOR_7_Earn_400_Plenti_points_star_When_you_buy(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 7.0 Earn 400 Plenti points* "
        test_input_price += "When you buy $12 of these items "
        test_input_price += "Worth $4.00 OR $3.99 EA. WITH CARD  "
        test_input_price += "*Plenti points Earned at rite aid "
        test_input_price += "generally credit to account 6AM day "
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

    def test_2_FOR_6_excludes_Lay_Kettle(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 6.0 (excludes Lay's Kettle) OR $3.29 EA. "
        test_input_price += "WITH CARD *Limit 2 offers per customer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR_6_Earn_100_Plenti_Worth_dollar_1_points_star(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 6.0 Earn 100 Plenti Worth $1.00 points* "
        test_input_price += "When you buy 2 of these items OR $3.49 EA. "
        test_input_price += "WITH CARD  * Limit 2 offers per customer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_Was_9_99_Save_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 Was $9.99. Save $3."
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

    def test_10_79_Was_dollar_14_99_dot_Save_dollar_4_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.79 Was $14.99. Save $4.20."
        test_expected_price_cleansed = float(10.79)
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

    def test_9_79_Was_dollar_13_99_dot_Save_4_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.79 Was $13.99. Save $4.20."
        test_expected_price_cleansed = float(9.79)
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

    def test_16_99_Was_dollar_24_49_dot_Save_dollar_7_50_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "16.99 Was $24.49. Save $7.50."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_38_19_Was_dollar_49_99_dot_Save_dollar_11_80_dot(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "38.19 Was $49.99. Save $11.80."
        test_expected_price_cleansed = float(38.19)
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

    def test_28_89_Was_dollar_41_29_dot_Save_dollar_12_40(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "28.89 Was $41.29. Save $12.40"
        test_expected_price_cleansed = float(28.89)
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

    def test_dollar_2_off(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$2 off"
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

    def test_0_1_Same_day_pickup_FREE(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.1 Same day pickup FREE"
        test_expected_price_cleansed = float(0.10)
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

    def test_21_99_Excludes_Mucinex_D(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "21.99 (*Excludes Mucinex D)"
        test_expected_price_cleansed = float(21.99)
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

    def test_7_99_Children_Cough_and_Cold_Category_comma_ProVoice_2017_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "7.99 (*Children Cough and Cold Category, ProVoice 2017)"
        test_expected_price_cleansed = float(7.99)
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

    def test_SPEND_dollar_30_GET_dollar_10_ExtraBucks_Rewards_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $30 GET $10 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 "
        test_input_price += "per household with card. "
        test_input_price += "(20003619051) (excludes trial/travel sizes)."
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

    def test_2_99_dollar_1_coupon_savings_in_our_app(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.99 $1.00 coupon savings in our app** "
        test_input_price += "**Coupons from Sunday newspaper must "
        test_input_price += "be presented at time of purchase."
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

    def test_4_99_dollar_2_ExtraBucks_Rewards_for_next_purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.99 $2 ExtraBucks® Rewards for next "
        test_input_price += "purchase (excludes trial/ travel sizes). "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 per "
        test_input_price += "household with card. (20003674956)"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SPEND_dollar_20_GET_dollar_10_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $20 GET $10 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 per "
        test_input_price += "household with card. (20003616666) "
        test_input_price += "(excludes trial/travel sizes)"
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

    def test_SPEND_dollar_15_GET_dollar_5_ExtraBucks_Rewards_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $15 GET $5 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 "
        test_input_price += "per household with card. (20003685202)"
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

    def test_2016_by_CVS_pharmacy_Not_all_advertised_items_available(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "© 2016 by CVS/pharmacy®. "
        test_input_price += "Not all advertised items available in all stores. "
        test_input_price += "We reserve the right to limit quantities on all items. "
        test_input_price += "Regular retail prices quoted may vary in some stores. "
        test_input_price += "Weekly sale offers valid at participating stores only "
        test_input_price += "and are not valid at CVS/Pharmacy® Target locations. "
        test_input_price += "Sorry, rainchecks are not available on items that "
        test_input_price += "are not regularly carried. No rainchecks on items "
        test_input_price += "valued $15.00 or more in NJ. Beverage items "
        test_input_price += "are \"plus deposit\" or \"+CRV\" where required by law. "
        test_input_price += "All mfr.'s rebate offers limited to one per "
        test_input_price += "household unless otherwise stated. "
        test_input_price += "Not responsible for typographical or printing errors. "
        test_input_price += "‡Some camera products may contain parts that "
        test_input_price += "have been used or recycled. "
        test_input_price += "*Discount applies to item(s) of equal or lesser "
        test_input_price += "value & excludes clearance items. "
        test_input_price += "All ExtraBucks® offers exclude clearance items. "
        test_input_price += "Your ExtraBucks® rewards will print as a coupon "
        test_input_price += "on your receipt immediately following "
        test_input_price += "qualifying purchase(s).  **"
        test_input_price += "Coupons from Sunday newspaper must be "
        test_input_price += "presented at time of purchase."
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

    def test_9_99_Earn_100_Plenti_points_star_When_you_buy_2_of_these_items_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 Earn 100 Plenti points* "
        test_input_price += "When you buy 2 of these items WITH CARD  "
        test_input_price += "*Limit 2 offers per customer"
        test_expected_price_cleansed = float(9.99)
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

    def test_2_FOR_7_PLUS_bang_Earn_200_Plenti_points(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 7.0 PLUS! "
        test_input_price += "Earn 200 Plenti points* Worth $2.00 "
        test_input_price += "When you buy 2 of these items OR $3.99 EA. "
        test_input_price += "WITH CARD *Limit 2 offers per customer."
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

    def test_2_FOR_7_Earn_200_Plenti_points_star_Worth(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 7.0 Earn 200 Plenti points* "
        test_input_price += "Worth $2.00 when you buy 2 of these items. "
        test_input_price += "OR $3.99 EA. WITH CARD * "
        test_input_price += "Limit 2 offers per customer."
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

    def test_2_FOR_4_Earn_100_Plenti_points_star_Worth(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 4.0 Earn 100 Plenti points* "
        test_input_price += "Worth $1.00 When you buy 2 of these items. "
        test_input_price += "OR $2.99 EA. WITH CARD  "
        test_input_price += "*Limit 2 offers per customer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_FOR_3_OR_1_79_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 3.0 OR 1.79 EA. WITH CARD"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_10_dollar_5_ExtraBucks_Rewards_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 10.0 $5 ExtraBucks® Rewards "
        test_input_price += "when you spend $20 on ANY of the "
        test_input_price += "products listed here ExtraBucks® "
        test_input_price += "Rewards offer limit of 1 per "
        test_input_price += "household with card. (20003617151)"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_Slash_5_dollar_5_ExtraBucks_Rewards_when_you_spend_20(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 $5 ExtraBucks® Rewards "
        test_input_price += "when you spend $20 on ANY of the "
        test_input_price += "products listed here ExtraBucks® Rewards "
        test_input_price += "offer limit of 1 per household with card. "
        test_input_price += "(20003617151)"
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

    def test_6_99_Earn_400_Plenti_points_Star__when_you_buy_12(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 Earn 400 Plenti points* "
        test_input_price += "when you buy $12 of these items. "
        test_input_price += "Worth $4.00 WITH CARD  * "
        test_input_price += "Limit 4 offers per customer. "
        test_input_price += "Purchase dates 9/3 - 9/30/17."
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

    def test_4_49_Earn_500_Plenti_points_star_Worth_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.49 Earn 500 Plenti points* "
        test_input_price += "Worth $5.00 when you buy $20 of these items. "
        test_input_price += "WITH CARD  (excludes PM)  * "
        test_input_price += "Limit 2 offers per customer."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_49_Earn_500_Plenti_points_star_Worth_5(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.49 Earn 500 Plenti points* "
        test_input_price += "Worth $5.00 When you buy $20 of these items "
        test_input_price += "WITH CARD  (excludes PM)  * "
        test_input_price += "Limit 2 offers per customer. "
        test_expected_price_cleansed = float(10.49)
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

    def test_4_PLUS_bang_Earn_300_Plenti_points_Worth_3(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.0 PLUS! Earn 300 "
        test_input_price += "Plenti points Worth $3.00 WITH CARD "
        test_input_price += "OR $3.00 WITH $1.00 OFF MFR. "
        test_input_price += "LOAD2CARD OFFER WITH CARD * "
        test_input_price += "Limit 2 offers per customer."
        test_expected_price_cleansed = float(4.00)
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

    def test_6_99_SPEND_Dollar_20_GET_dollar_5_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 SPEND $20 GET $5 ExtraBucks® Rewards "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 "
        test_input_price += "per household with card. (20003615331)"
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

    def test_1_99_SPEND_dollar_9_GET_dollar_3_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 SPEND $9 GET $3 ExtraBucks® "
        test_input_price += "Rewards ExtraBucks® Rewards offer "
        test_input_price += "limit of 1 per household with card. "
        test_input_price += "(20003653748)"
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

    def test_25_percent_OFF_PLUS_bang_Earn_2_000_Plenti_points(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "25% OFF  PLUS! Earn 2,000 "
        test_input_price += "Plenti points* Worth $20.00 "
        test_input_price += "When you buy $100 of these items. "
        test_input_price += "REGULAR RETAIL WITH CARD  * "
        test_input_price += "Limit 2 offers per customer."
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

    def test_SPEND_dollar_10_GET_dollar_5_ExtraBucks_Rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $10 GET $5 ExtraBucks® Rewards "
        test_input_price += "(excludes multipacks). "
        test_input_price += "ExtraBucks® Rewards offer limit of 2 "
        test_input_price += "per household with card. (20003676337)"
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

    def test_SPEND_dollar_12_GET_dollar_4_ExtraBucks_Rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $12 GET $4 ExtraBucks® Rewards "
        test_input_price += "(excludes trial/travel sizes). "
        test_input_price += "ExtraBucks® Rewards offer limit "
        test_input_price += "of 1 per household with card. "
        test_input_price += "(200036832)"
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

    def test_Earn_500_Plenti_points_star_Worth_Dollar_5_customer(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Earn 500 Plenti points* "
        test_input_price += "Worth $5.00 WITH CARD  "
        test_input_price += "*Limit 2 offers per customer."
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

    def test_2_FOR_8_OR_dollar_4_49_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 8.0 OR $4.49 EA. WITH CARD  "
        test_input_price += "(excludes PM)"
        test_expected_price_cleansed = float(4.00)
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

    def test_2_FOR_3_OR_dollar_1_99_EA_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 3.0 OR $1.99 EA. WITH CARD"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUY_ONE_GET_ONE_FREE_star_bang_Earn_1_000_Plenti_points_Star_Worth_dollar_10(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE FREE*  "
        test_input_price += "!Earn 1,000 Plenti points* "
        test_input_price += "Worth $10.00 When you buy $25 of these items. "
        test_input_price += "EQUAL OR LESSER VALUE WITH CARD  "
        test_input_price += "*Limit 4 offers per customer.  "
        test_input_price += "*PLENTI POINTS EARNED AT RITE AID GENERALLY CREDIT "
        test_input_price += "TO ACCOUNT 6AM DAY AFTER ISSUANCE. "
        test_input_price += "EXPIRES AFTER 2 YEARS. "
        test_input_price += "MUST FULLY ENROLL AND HAVE AT LEAST 200 "
        test_input_price += "POINTS TO USE PLENTI POINTS. "
        test_input_price += "SEE PLENTI.COM/TERMS FOR DETAILS. "
        test_input_price += "PLENTI POINTS ARE WORTH AT LEAST $1 "
        test_input_price += "IN SAVINGS FOR EVERY 100 POINTS EARNED. "
        test_input_price += "BUY ONE GET ONE FREE GOOD ON ITEMS EQUAL "
        test_input_price += "OR LESSER VALUE OF THE SAME BRAND, "
        test_input_price += "NO MIX & MATCH. BUY ONE GET ONE FREE "
        test_input_price += "ITEMS OFFERED AT REGULAR PRICE, "
        test_input_price += "APPLICABLE SALES TAX APPLIES."
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

    def test_BUY_ONE_GET_ONE_50_PERCent_OFF__PLUS_bang_Earn_1_000_Plenti_points(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE 50% OFF  "
        test_input_price += "PLUS! Earn 1,000 Plenti points* "
        test_input_price += "Worth $10.00 When you buy $30 of "
        test_input_price += "these items. Excludes Value Packs  * "
        test_input_price += "Limit 2 offers per customer."
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

    def test_BUY_ONE_GET_ONE_50_percent_OFF_Earn_1_000_Plenti_points(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE 50% OFF  "
        test_input_price += "Earn 1,000 Plenti points* "
        test_input_price += "Worth $10.00 When you buy $30 "
        test_input_price += "of these items. Excludes pseudoephedrine "
        test_input_price += "products located at the pharmacy "
        test_input_price += "counter.  * Limit 2 offers per customer."
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

    def test_3_slash_10_diamond_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 10.0 ◊Plus deposit where required"
        test_expected_price_cleansed = float(3.33)
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

    def test_2_slash_3_diamond_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 3.0 ◊Plus deposit where required."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_slash_5_SPEND_dollar_20_GET_dollar_5_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 5.0 SPEND $20 GET $5 ExtraBucks® "
        test_input_price += "Rewards ◊Plus deposit where required.  "
        test_input_price += "ExtraBucks® Rewards offer limit of 1 "
        test_input_price += "per household with card. "
        test_input_price += "(20003615331)"
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

    def test_5_99_REGULAR_RETAIL(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 REGULAR RETAIL"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_BUT_TWO_GET_THIRD_ONE_FREE_bang_Selection_may_vary_by_store(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUT TWO GET THIRD ONE FREE!  "
        test_input_price += "Selection may vary by store  "
        test_input_price += "EQUAL OR LESSER VALUE  WITH CARD"
        test_expected_price_cleansed = float(-1.00)
        test_expected_multibuy = ""
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

    def test_6_99_buy_2_get_4_OR_buy_3_get_dollar_8_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 buy 2, get $4 OR buy 3, get $8 ExtraBucks® Rewards (excludes trial/travel sizes). ExtraBucks® Rewards offer limit of $8 per household with card. (20003726220)"
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

    def test_0_99_75_cent_ExtraBucks_Rewards_for_next_purchase(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 75¢ ExtraBucks® Rewards for next purchase ExtraBucks® Rewards offer limit of 1 per household with card. (200037295)"
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

    def test_3_Slash_6_dollar_3_ExtraBucks_Rewards_when_you_spend(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 6.0 $3 ExtraBucks® Rewards when you spend $12 on ANY of the products listed here ExtraBucks® Rewards offer limit of 1 per household with card. (20003760129)*Discount applies to item(s) of equal or lesser value & excludes clearance items."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_19_99_dollar_4_mfrs_coupon_in_most_Sunday(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "19.99 $4 mfr's coupon in most Sunday newspapers** **Coupons from Sunday newspaper must be presented at time of purchase."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_6_99_dollar_1_mfrs_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 $1 mfr's coupon in most Sunday newspapers**"
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

    def test_dollar_3_ExtraBucks_Rewards_when_you_spend_dollar_10_on(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$3 ExtraBucks® Rewards when you spend $10 "
        test_input_price += "on ANY of the products listed here ExtraBucks® "
        test_input_price += "Rewards offer limit of 1 per household with "
        test_input_price += "card. (20003769850)"
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

    def test_4_94_dollar_2_mfrs_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.94 $2 mfr's coupon in most Sunday newspapers** PLUS $5 ExtraBucks® Reward when you spend $20 on ANY of the product listed here. **Coupons from Sunday newspaper must be presented at time of purchase. ExtraBucks® Reward offer limit of 1 per household with card (2000371674)"
        test_expected_price_cleansed = float(4.94)
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

    def test_0_99_25_cent_MFR_coupon_in_our_app(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.99 25¢ MFR coupon in our app** **Coupons from Sunday newspaper must be presented at time of purchase."
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

    def test_2_slash_2_dollar_2_instant_coupon_on_2_at_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2/ 2.0 $2.00 instant coupon on 2 at coupon center PLUS $3.00 mfr's coupon on 2 in most Sunday newspaper** Must be an ExtraCare® cardholder as of 9/3/17 to get this coupon. Limit of 1 offer per household with card. Offer valid 9/10/17-9/16/17 **Coupons from Sunday newspaper must be presented at time of purchase."
        test_expected_price_cleansed = float(1.00)
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

    def test_3_slash_6_dollar_3_instant_coupon_on_3_Manufacturers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "3/ 6.0 $3.00 instant coupon on 3 Manufacturers coupon in most Sunday newspapers Must be an ExtraCare® cardholder as of 9/3/17 to get this coupon. Limit of 1 offer per household with card. Offer valid 9/10/17-9/16/17"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_9_99_dollar_1_mfrs_coupon_in_most_Sunday(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 $1 mfr's coupon in most Sunday newspapers**PLUS 5 ExtraBucks® Reward when you spend $20 on ANY of the products listed here. **Coupons from Sunday newspaper must be presented at time of purchase. ExtraBucks® Reward offer limit of 1 per household with card (2000371674)"
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

    def test_2_44_diamond_Plus_deposit_where_required(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.44 ✧Plus deposit where required."
        test_expected_price_cleansed = float(2.44)
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

    def test_Support_right_from_the_start_comma_made_for_your_pregnancy_journey(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "Support right from the start, made for your pregnancy journey."
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

    def test_41_99_PLUS_dollar_5_ExtraBucks_Rewards_Manufacturers_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "41.99 PLUS $5 ExtraBucks Rewards Manufacturers "
        test_input_price += "coupon in most Sunday newspapers ExtraBucks "
        test_input_price += "Rewards offer limit of 1 per household with card."
        test_expected_price_cleansed = float(41.99)
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

    def test_34_99_PLUS_dollar_5_ExtraBucks_Rewards_Manufacturers_coupon(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "34.99 PLUS $5 ExtraBucks Rewards Manufacturers "
        test_input_price += "coupon in most Sunday newspapers ExtraBucks "
        test_input_price += "Rewards offer limit of 1 per household with card."
        test_expected_price_cleansed = float(34.99)
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

    def test_19_99_dollar_4_mfrs_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "19.99 $4 mfr\'s coupon in most Sunday newspapers** "
        test_input_price += "(excludes chewables 30 ct.). **Coupons from Sunday "
        test_input_price += "newspaper must be presented at time of purchase."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_19_99_dollar_4_mfrs_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "19.99 $4 mfr\'s coupon in most Sunday newspapers"
        test_input_price += "** **Coupons from Sunday newspaper must be "
        test_input_price += "presented at time of purchase."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_SPEND_dollar_20_GET_dollar_4_ExtraBucks_Rewards_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $20 GET $4 ExtraBucks Rewards WITH CARD "
        test_input_price += "select Dr. Scholl's  Extrabucks Rewards offer "
        test_input_price += "limit 1 per household with card."
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

    def test_SPEND_dollar_10_dollar_5_GET_extrabucks_rewards(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "SPEND $10 $5 GET extrabucks® rewards "
        test_input_price += "(excludes douches). extrabucks® rewards "
        test_input_price += "extrabucks® rewards offer limit of 1 "
        test_input_price += "per household with card. (20003757576)"
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

    def test_dollar_3_ExtraBucks_Rewards_for_next_purchase_PLUS(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "$3 ExtraBucks® Rewards for next purchase "
        test_input_price += "PLUS $1 MFR coupon in our app** **Coupons "
        test_input_price += "from Sunday newspaper must be presented "
        test_input_price += "at time of purchase.  extrabucks® "
        test_input_price += "rewards offer limit of 2 per household "
        test_input_price += "with card. (20003784340)"
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

    def test_buy_2_comma_get_dollar_6_OR_buy_3_comma_get_dollar_12_ExtraBucks(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "buy 2, get $6 OR buy 3, get $12 ExtraBucks® "
        test_input_price += "Rewards (excludes disposables and trial/travel "
        test_input_price += "sizes).  extrabucks® rewards offer limit of "
        test_input_price += "$12 per household with card. (20003719051)"
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

    def test_5_99_excludes_Rite_Aid_Aspirin_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 (excludes Rite Aid Aspirin)  WITH CARD"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_WITH_CARD(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "WITH CARD"
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

    def test_2_FOR_5_0_EARN_2_000_IN_PLENTI_POINTS_WORTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 FOR 5.0 EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS. OR 2.99 EA. WITH CARD  (excludes Protein & Nut)  *Limit 2 offers per customer."
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

    def test_6_99_EARN_2000_IN_PLENTY_POINTS_WORTH_again(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 EARN 2,000 IN PLENTY POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS WITH CARD  *Limit 2 offers per customer."
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

    def test_0_69_EARN_2000_IN_PLENTI_POINTS_WORTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.69 EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS WITH CARD  *Limit 2 offers per customer"
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

    def test_4_94_EARN_2000_IN_PLENTI_POINTS_WORTH_another(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.94 EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS WITH CARD  OR 2.94 WITH $2.00 OFF MFR. LOAD2CARD OFFER WITH CARD  CLICK. LOAD. SAVE. riteaid.com/load2card  *Limit 2 offers per customer."
        test_expected_price_cleansed = float(4.94)
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

    def test_4_94_EARN_2000_IN_PLENTI_POINTS_WORTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.94 EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS. WITH CARD  (excludes Pur Clean 37 oz.)  *Limit 2 offers per customer."
        test_expected_price_cleansed = float(4.94)
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

    def test_BUY_ONE_GET_ONE_50_OFF_EARN_2000_IN_PLENTI_POINTS_WORTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE 50% OFF  EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS (excludes Trial Sizes)  EQUAL OR LESSER VALUE WITH CARD  *Limit 2 offers per customer."
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

    def test_6_99_EARN_2000_IN_PLENTI_POINTS_WORTH(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "6.99 EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS. WITH CARD  OR 5.99 WITH 1.00 OFF MANUFACTURER'S COUPON WITH CARD  * Limit 2 offers per customer."
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

    def test_BUY_ONE_GET_ONE_50_OFF__EARN_2000_IN_PLENTI_POINTS(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE 50% OFF  EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS EQUAL OR LESSER VALUE WITH CARD  *Limit 2 offers per customer."
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

    def test_BUY_ONE_GET_ONE_50_OFF_EARN_2000_IN_PLENTI(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE 50% OFF  EARN 2,000 IN PLENTI POINTS* WORTH $20.00 WHEN YOU BUY $50 OF SELECT ITEMS. (excludes clearance items)  EQUAL OR LESSER VALUE WITH "
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

    def test_BUY_ONE_GET_ONE_FREE__EARN_2000_IN_PLENTI(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "BUY ONE GET ONE FREE*  EARN 2,000 IN PLENTI POINTS WORTH $20 WHEN YOU BUY $50 OF SELECT ITEMS. EQUAL OR LESSER VALUE WITH CARD  *Limit 2 offers per customers.  "
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

    def test_21_99_dollar_2_00_mfrs_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "21.99 $2.00 mfr's coupon in most Sunday newspapers** **Coupons from Sunday newspaper must be presented at time of purchase."
        test_expected_price_cleansed = float(21.99)
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

    def test_2017_by_CVS_pharmacyPrices_promotions_styles_and_availability(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " © 2017 by CVS/pharmacy®. Prices, promotions, styles and availability may vary by store. Advertised prices good only for dates indicated. Sale prices generally require ExtraCare® card. Prices subject to state and local taxes and fees. We reserve the right to limit quantities on all items or the availability of rainchecks for items where permitted by law. Weekly sale offers are not valid at CVS/Pharmacy® at Target locations. All coupon offers are subject to CVS/pharmacy coupon policy which is available online or in stores. If using multiple coupons, we reserve the right to determine the order in which the coupons are applied. All manufacturer rebate offers limited to one per household unless otherwise stated. Not responsible for typographical or printing errors. *Discount applies to item(s) of equal or lesser value & excludes clearance items. All ExtraBucks® offers exclude clearance items. Your ExtraBucks® rewards will print as a coupon on your receipt immediately following qualifying purchase(s)"
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

    def test_11_99_Dollar_2_MFR_coupon_in_our_app(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "11.99 $2 MFR coupon in our app** **Coupons from Sunday newspaper must be presented at time of purchase."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_5_99_excludes_trial_travel_sizes(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.99 (excludes trial/travel sizes)."
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Available_in_select_stores(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " Available in select stores."
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

    def test_13_99_dollar_5_00_mfrs_mailin_rebate(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "13.99 $5.00 mfr's mail-in rebate"
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
        # Verify the results.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type


    def test_2_98_saveahorre_3_01(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.98 save/ahorre $3.01"
        test_expected_price_cleansed = float(2.98)
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

    def test_1_28_saveahorre_72(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.28 save/ahorre 72¢"
        test_expected_price_cleansed = float(1.28)
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

    def test_4_98_saveahorre_1_21(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.98 save/ahorre $1.21"
        test_expected_price_cleansed = float(4.98)
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

    def test_2_98_saveahorre_1(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.98 save/ahorre $1"
        test_expected_price_cleansed = float(2.98)
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

    def test_4_98_saveahorre_2_01_lb_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.98 save/ahorre $2.01 lb."
        test_expected_price_cleansed = float(4.98)
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

    def test_0_48_save_from_ahorre_entre_2151(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.48 save from /ahorre entre 21-51¢"
        test_expected_price_cleansed = float(0.48)
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

    def test_4_98_save_fromahorre_entre_1_012_01(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "4.98 save from/ahorre entre $1.01-2.01"
        test_expected_price_cleansed = float(4.98)
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

    def test_2_48_save_fromahorre_entre_1_712_01(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.48 save from/ahorre entre $1.71-2.01"
        test_expected_price_cleansed = float(2.48)
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

    def test_5_48_saveahorre_3_51(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "5.48 save/ahorre $3.51"
        test_expected_price_cleansed = float(5.48)
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

    def test_7_48_saveahorre_2_51(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "7.48 save/ahorre $2.51"
        test_expected_price_cleansed = float(7.48)
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

    def test_0_88_saveahorre_51(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.88 save/ahorre 51¢"
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

    def test_2_48_saveahorre_1_51(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.48 save/ahorre $1.51"
        test_expected_price_cleansed = float(2.48)
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

    def test_NOWAHORA_0_75(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "NOW/AHORA 0.75"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_NOWAHORA_1_0(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "NOW/AHORA 1.0"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_NOWAHORA_1_75(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "NOW/AHORA 1.75"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_2_bags_for_0_98(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2 bags for 0.98"
        test_expected_price_cleansed = float(0.49)
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

