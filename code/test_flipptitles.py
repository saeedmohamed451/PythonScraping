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
class TestFlippTitles(object):

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

    def test_GE_Relax_Reveal_or_Refresh_LED_Light_Bulbs(self):

        # Input and expected result.
        test_input_title = "GE Relax, Reveal or Refresh LED Light Bulbs*"
        test_input_description = "Reg. 7.99-24.99."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ge Relax Reveal or Refresh Led Light Bulbs"

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

    def test_Spray_Paint(self):

        # Input and expected result.
        test_input_title = "Spray Paint*"
        test_input_description = "DIY Dept. Reg. 99¢-18.99."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Spray Paint"

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

    def test_Select_Meijer_LED_Light_Bulbs(self):

        # Input and expected result.
        test_input_title = "Select Meijer LED Light Bulbs"
        test_input_description = "Reg. 5.99-6.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Meijer Led Light Bulbs"

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

    def test_AutoQuest_Premium_RV_Antifreeze(self):

        # Input and expected result.
        test_input_title = "AutoQuest Premium RV Antifreeze*"
        test_input_description = "GallonReg. 3.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Autoquest premium RV Antifreeze gallon"

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

    def test_RainX_Weatherbeater_Wiper_Blades(self):

        # Input and expected result.
        test_input_title = "Rain-X Weatherbeater Wiper Blades*"
        test_input_description = "Reg. 8.99-10.59 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rain-X Weatherbeater Wiper Blades"

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

    def test_Pennzoil_Full_Synthetic_or_High_Mileage_Full_Synthetic_Oil(self):

        # Input and expected result.
        test_input_title = "Pennzoil Full Synthetic or High Mileage Full Synthetic Oil*"
        test_input_description = "5 qt. jug. Reg. 25.69."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pennzoil Full Synthetic or High Mileage Full Synthetic Oil 5 qt jug"

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

    def test_Prestone_Full_Strength_or_5050_Coolant(self):

        # Input and expected result.
        test_input_title = "Prestone Full Strength or 50/50 Coolant*"
        test_input_description = "Reg. 8.99-10.99."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Prestone Full Strength or 50/50 Coolant"

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

    def test_Pennzoil_Conventional_Oil(self):

        # Input and expected result.
        test_input_title = "Pennzoil Conventional Oil*"
        test_input_description = "5 qt. jug.Reg. 16.79."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pennzoil Conventional Oil 5 qt jug"

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

    def test_Golf_Balls(self):

        # Input and expected result.
        test_input_title = "Golf Balls*"
        test_input_description = "Limit one coupon per offer."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Golf Balls"

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

    def test_Shock_Doctor_Products(self):

        # Input and expected result.
        test_input_title = "Shock Doctor Products*"
        test_input_description = "Reg. 7.99-69.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shock Doctor products"

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

    def test_Water_Bottles_and_Tumblers(self):

        # Input and expected result.
        test_input_title = "Water Bottles and Tumblers*"
        test_input_description = "Sporting Goods Dept. Reg. 4.99-37.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Water bottles and Tumblers"

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

    def test_Wilson_Volleyballs_and_Footballs(self):

        # Input and expected result.
        test_input_title = "Wilson Volleyballs and Footballs*"
        test_input_description = "Reg. 11.99-29.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Wilson Volleyballs and Footballs"

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

    def test_Soccer_Equipment(self):

        # Input and expected result.
        test_input_title = "Soccer Equipment*"
        test_input_description = "Reg. 4.99-49.99,"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Soccer Equipment"

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

    def test_Folding_Furniture_Home_Dept_(self):

        # Input and expected result.
        test_input_title = "Folding Furniture* Home Dept."
        test_input_description = "Reg. 11.99-59.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Folding Furniture"

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

    def test_Yankee_Candle_Tarts_or_Votives(self):

        # Input and expected result.
        test_input_title = "Yankee Candle Tarts or Votives*"
        test_input_description = "Reg. 1.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Yankee candle Tarts or Votives"

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

    def test_Perfect_Touch_Throw(self):

        # Input and expected result.
        test_input_title = "Perfect Touch Throw*"
        test_input_description = "Reg. 19.99,"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Perfect Touch Throw"

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

    def test_Keurig_K50_or_K55_Brewer(self):

        # Input and expected result.
        test_input_title = "Keurig K50 or K55 Brewer"
        test_input_description = "Limit two coupons per offer."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Keurig K50 or K55 Brewer"

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

    def test_My_Temp_Sheet_Sets_and_Evercool_Pillows(self):

        # Input and expected result.
        test_input_title = "My Temp Sheet Sets and Evercool Pillows"
        test_input_description = "Reg. 24.99-59.99,"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "My Temp Sheet Sets and Evercool Pillows"

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

    def test_Martex_Oversized_Bath_Towel(self):

        # Input and expected result.
        test_input_title = "Martex Oversized Bath Towel*"
        test_input_description = "Reg. 9.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Martex Oversized Bath Towel"

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

    def test_Mohawk_Utility_Rugs_and_Mats(self):

        # Input and expected result.
        test_input_title = "Mohawk Utility Rugs and Mats"
        test_input_description = "Reg. 3.99-39.99,"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mohawk Utility Rugs and Mats"

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

    def test_Kitchen_Rugs_and_Comfort_Mats(self):

        # Input and expected result.
        test_input_title = "Kitchen Rugs and Comfort Mats*"
        test_input_description = "Reg. 9.99-24.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kitchen Rugs and Comfort Mats"

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

    def test_FoodSaver_Sealers_and_Accessories(self):

        # Input and expected result.
        test_input_title = "FoodSaver Sealers and Accessories"
        test_input_description = "Reg. 7.49-169.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Foodsaver Sealers and Accessories"

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

    def test_Select_Womens_and_Juniors_Apparel_and_Outerwear(self):

        # Input and expected result.
        test_input_title = "Select Women's and Juniors' Apparel and Outerwear"
        test_input_description = "Sizes S-3X, 0-24W. Excludes activewear, "
        test_input_description += "basics and The Find. Reg. $10-$34 and "
        test_input_description += "Select Young Men's Apparel* "
        test_input_description += "Sizes S-3XL, 28-38. Reg. $12-$40."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Women's and Juniors' Apparel and "
        test_expected_title_cleansed += "Outerwear Sizes S-3X 0-24W. Sizes S-3Xl 28-38."

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

    def test_Select_Falls_Creek_Kids_Apparel(self):

        # Input and expected result.
        test_input_title = "Select Falls Creek Kids' Apparel*"
        test_input_description = "Sizes NB-18. Reg. $5-$24"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Falls Creek Kids' Apparel Sizes Nb-18."

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

    def test_Falls_Creek_and_Massini_Womens_Fashion_Boots(self):

        # Input and expected result.
        test_input_title = "Falls Creek and Massini Women's Fashion Boots*"
        test_input_description = "Reg. $30-$50"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Falls Creek and Massini Women's Fashion Boots"

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

    def test_Fruit_of_the_Loom_Women_3_Pr__Socks(self):

        # Input and expected result.
        test_input_title = "Fruit of the Loom Women 3 Pr. Socks*"
        test_input_description = "Reg. 5.99.Women 6 Pr. Socks*Reg. 6.49....5.49"
        test_input_description += "Women 10 Pr. Socks*Reg.9.99...8.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fruit of the Loom Women 3 pr Socks "
        test_expected_title_cleansed += "Women 6 pr Socks Women 10 pr Socks"

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

    def test_Fruit_of_the_Loom_Mens_3_Pk__Breathable_Boxer_Briefs(self):

        # Input and expected result.
        test_input_title = "Fruit of the Loom Men's 3 Pk. Breathable Boxer Briefs*"
        test_input_description = "Reg. 12.99.Men's 5 Pk. Boxers* Reg.17.49...13.49"
        test_input_description += "Men's 6 Pk. Fashion Briefs* Reg. 15.49..13.49"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fruit of the Loom Men's 3 pk Breathable boxer "
        test_expected_title_cleansed += "Briefs Men's 5 pk boxers Men's 6 pk Fashion Briefs"

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

    def test_iPad_iPad_Mini_or_iPad_Pro_or_Apple_Watch_Series_1_or_Series_2(self):

        # Input and expected result.
        test_input_title = "iPad, iPad Mini or iPad Pro or Apple Watch Series 1 or Series 2"
        test_input_description = "Excludes clearance. Limit two coupons per offer."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = " IPAD IPAD Mini or IPAD pro or Apple Watch"

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

    def test_The_Mummy_Bluray(self):

        # Input and expected result.
        test_input_title = "The Mummy Blu-ray"
        test_input_description = "DVD.....16.99Date subject to change. limit 2."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "The Mummy Blu-Ray DVD"

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

    def test_Captain_Underpants_Bluray(self):

        # Input and expected result.
        test_input_title = "Captain Underpants Blu-ray"
        test_input_description = "DVD.....$14.99Cape included with Blu-ray."
        test_input_description += "Date subject to changed: Limit 2"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Captain Underpants Blu-Ray DVD"

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

    def test_Cat_Chow(self):

        # Input and expected result.
        test_input_title = "Cat Chow"
        test_input_description = "13-16 lbs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Cat Chow 13-16 lb"

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

    def test_Fruit_of_the_Loom_Kids_6_Pr__Socks(self):

        # Input and expected result.
        test_input_title = "Fruit of the Loom Kids' 6 Pr. Socks*"
        test_input_description = "Reg. 5.99.Boys' 5 Pk. Boxer Briefs* Reg. 11.49......9.99Girls' 8 or 9 Pk. Underwear* Reg. 9.49...7.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fruit of the Loom Kids' 6 pr Socks Boys' 5 pk boxer Briefs Girls' 8 or 9 pk Underwear"

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

    def test_Reading_Glasses_or_Accessories(self):

        # Input and expected result.
        test_input_title = "Reading Glasses or Accessories*"
        test_input_description = "Health & Beauty CareDept."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Reading Glasses or Accessories"

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

    def test_Allergy_Products(self):

        # Input and expected result.
        test_input_title = "Allergy Products*"
        test_input_description = "Excludes pseudoephedrine products."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Allergy products"

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

    def test_Dr__Scholls_Insoles(self):

        # Input and expected result.
        test_input_title = "Dr. Scholl's® Insoles*"
        test_input_description = "Excludes custom fit orthotics."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dr. Scholl's insoles"

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

    def test_Airborne_Adult_Gummies_42_ct__ne_or_Digestive_Advantage_ne_Probiotic_Gummies_60_ct_(self):

        # Input and expected result.
        test_input_title = "Airborne Adult Gummies 42 ct. ne, or Digestive Advantage ne Probiotic Gummies 60 ct."
        test_input_description = "Other Airborne and DigestiveAdvantage Products.......... 10% off"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Airborne Adult Gummies 42 ct Ne or Digestive Advantage Ne probiotic Gummies 60 ct"

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

    def test_Ricola_Cough_Drops(self):

        # Input and expected result.
        test_input_title = "Ricola Cough Drops"
        test_input_description = "45-50 ct.Ricola Cough Drops19-24 ct. All varieties....... 10% off"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ricola Cough Drops 45-50 ctRicola Cough Drops19-24 ct"

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

    def test_Sudafed_PE_Tylenol_Cold_and_Tylenol_Sinus(self):

        # Input and expected result.
        test_input_title = "Sudafed PE, Tylenol Cold and Tylenol Sinus"
        test_input_description = "8 oz. and 18-24 ct. Excludespseudoephedrine products."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sudafed Pe Tylenol Cold and Tylenol Sinus 8 oz and 18-24 ct"

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

    def test_Always_Tampax_or_Always_Discreet_Products(self):

        # Input and expected result.
        test_input_title = "Always, Tampax or Always Discreet Products*"
        test_input_description = "Excludes Always Discreet Boutique."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Always Tampax or Always Discreet products"

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

    def test_Card_Party_Everyday(self):

        # Input and expected result.
        test_input_title = "Card Party Everyday"
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Card Party Everyday"

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

    def test_Kleenex_4_Pk__Facial_Tissue_Bundle(self):

        # Input and expected result.
        test_input_title = "Kleenex 4 Pk. Facial Tissue Bundle"
        test_input_description = "Uprights, flats orcanisters."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kleenex 4 pk Facial Tissue Bundle Uprights flats Orcanisters."

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

    def test_Clorox_Disinfecting_Wipes_Triple_Pack(self):

        # Input and expected result.
        test_input_title = "Clorox Disinfecting Wipes Triple Pack"
        test_input_description = "225 ct."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Clorox Disinfecting Wipes Triple pack 225 ct"

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

    def test_PineSol_Pourable_Cleaner_4048_oz__or_Clorox_Cleaner_Trigger_Spray_3032_oz__or_Scrub_Singles_1014_ct(self):

        # Input and expected result.
        test_input_title = "Pine-Sol Pourable Cleaner 40-48 oz. or Clorox Cleaner Trigger Spray 30-32 oz. or Scrub Singles* 10-14 ct"
        test_input_description = "Limit one offer per transaction."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pine-Sol Pourable Cleaner 40-48 oz or Clorox Cleaner Trigger Spray 30-32 oz or Scrub Singles 10-14 ct"

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

    def test_Clorox_Liquid_Bleach_116121_oz__or_Toilet_Bowl_Cleaner_Twin_Pack_224_oz_(self):

        # Input and expected result.
        test_input_title = "Clorox Liquid Bleach 116-121 oz. or Toilet Bowl Cleaner Twin Pack 2/24 oz."
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Clorox liquid Bleach 116-121 oz or Toilet Bowl Cleaner Twin pack 2/24 oz"

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

    def test_Scrubbing_Bubbles_Mega_Shower_or_Color_Power_Foamer_20_oz__or_Toilet_Cleaning_Gel_1_34_oz_(self):

        # Input and expected result.
        test_input_title = "Scrubbing Bubbles Mega Shower or Color Power Foamer 20 oz. or Toilet Cleaning Gel 1.34 oz."
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Scrubbing Bubbles Mega Shower or Color Power Foamer 20 oz or Toilet Cleaning Gel 1.34 oz"

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

    def test_Windex_Glass_or_Multi_Surface_Cleaner_23_oz__or_Scrubbing_Bubbles_Foaming_Bathroom_Cleaner_20_oz_(self):

        # Input and expected result.
        test_input_title = "Windex Glass or Multi Surface Cleaner 23 oz. or Scrubbing Bubbles Foaming Bathroom Cleaner 20 oz."
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Windex Glass or Multi Surface Cleaner 23 oz or Scrubbing Bubbles Foaming Bathroom Cleaner 20 oz"

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

    def test_Vicks_DayQuil_NyQuil_ZzzQuil_and_Sinex_Products_12_oz_24_ct(self):

        # Input and expected result.
        test_input_title = "Vicks DayQuil, NyQuil, ZzzQuil and Sinex Products 12 oz./24 ct"
        test_input_description = "Other Vicks Products.... 10% offExcludes pseudoephedrine products."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Vicks Dayquil Nyquil Zzzquil and Sinex products 12 oz/24 ct"

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

    def test_Mens_and_Womens_Fragrances(self):

        # Input and expected result.
        test_input_title = "Men's and Women's Fragrances"
        test_input_description = "Reg. 21.99 or more."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Men's and Women's Fragrances"

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

    def test_Blistex_or_Carmex_Products(self):

        # Input and expected result.
        test_input_title = "Blistex or Carmex Products*"
        test_input_description = "Select varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Blistex or Carmex products"

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

    def test_Arm__Hammer_or_Arrid_Deodorant_or_Travel_or_Trial_Size_get_one_Products(self):

        # Input and expected result.
        test_input_title = "Arm & Hammer or Arrid Deodorant or Travel or Trial Size get one Products*"
        test_input_description = "2.5-2.8 oz. Reg. 1.99Reg. $1-1.50."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Arm & Hammer or Arrid Deodorant or Travel or Trial Size Get One products 2.5-2.8 oz"

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

    def test_Colgate_4_oz__or_Close_Up_Toothpaste(self):

        # Input and expected result.
        test_input_title = "Colgate 4 oz. or Close Up Toothpaste*"
        test_input_description = "6 oz. Select varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate 4 oz or Close Up Toothpaste 6 oz"

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

    def test_Pantene_Hair_Care_Products(self):

        # Input and expected result.
        test_input_title = "Pantene Hair Care Products"
        test_input_description = "Excludes travel and trial size. Offers cannot mix or match."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pantene Hair Care products"

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

    def test_Hair_Accessories(self):

        # Input and expected result.
        test_input_title = "Hair Accessories*"
        test_input_description = "Excludes Wet Brush."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hair Accessories"

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

    def test_John_Frieda_Hair_Care_or_Color_Products(self):

        # Input and expected result.
        test_input_title = "John Frieda Hair Care or Color Products*"
        test_input_description = "Excludes travel and trial size."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "John Frieda Hair Care or Color products"

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

    def test_Suave_Hair_Care_Products(self):

        # Input and expected result.
        test_input_title = "Suave Hair Care Products*"
        test_input_description = "Excludes travel and trial size."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Suave Hair Care products"

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

    def test_LOreal_Preference_or_Excellence_Hair_Color_Products(self):

        # Input and expected result.
        test_input_title = "L'Oreal Preference or Excellence Hair Color Products*"
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "L'Oreal preference or Excellence Hair Color products"

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

    def test_LOreal_Advanced_Hair_Care_Products_4_212_6_oz__or_Garnier_Whole_Blends_Products_12_5_oz_(self):

        # Input and expected result.
        test_input_title = "L'Oreal Advanced Hair Care Products 4.2-12.6 oz. or Garnier Whole Blends Products 12.5 oz."
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "L'Oreal Advanced Hair Care products 4.2-12.6 oz or Garnier Whole Blends products 12.5 oz"

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

    def test_Meijer_Bath_Products(self):

        # Input and expected result.
        test_input_title = "Meijer Bath Products*"
        test_input_description = "Excludes bath poufs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Meijer Bath products"

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

    def test_Olay_Facial_Skin_Care_Products_Body_Wash_and_Bar_Soap(self):

        # Input and expected result.
        test_input_title = "Olay Facial Skin Care Products, Body Wash and Bar Soap"
        test_input_description = "Excludes travel and trial size."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Olay Facial Skin Care products Body Wash and Bar Soap"

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

    def test_Gillette_Razor_System(self):

        # Input and expected result.
        test_input_title = "Gillette Razor System"
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gillette Razor System"

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

    def test_Almay_or_Mitchum_Deodorant(self):

        # Input and expected result.
        test_input_title = "Almay or Mitchum Deodorant*"
        test_input_description = "1.6-4 oz.Excludes twin packs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Almay or Mitchum Deodorant 1.6-4 oz"

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

    def test_Revlon_Cosmetics(self):

        # Input and expected result.
        test_input_title = "Revlon Cosmetics"
        test_input_description = "Excludes travel and trial size. Offers cannot mix or match."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Revlon Cosmetics"

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

    def test_Armour_Cooked_Deli_Ham(self):

        # Input and expected result.
        test_input_title = "Armour Cooked Deli Ham"
        test_input_description = "Water added."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Armour Cooked Deli Ham"

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

    def test_80_Lean_Ground_Beef(self):

        # Input and expected result.
        test_input_title = "80% Lean Ground Beef"
        test_input_description = "3 lb. pkg. or larger. Ground fresh daily in store. Product of U.S.A.80% Lean Ground Beef Patty Unseasoned. 2.99 lb"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ground Beef 3 lb pkg"

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

    def test_True_Goodness_Organic_Orange_Juice(self):

        # Input and expected result.
        test_input_title = "True Goodness Organic Orange Juice"
        test_input_description = "59 oz. Not from concentrate."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "True Goodness Organic Orange Juice 59 oz"

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

    def test_Certified_Angus_Beef_Boneless_Strip_Steak(self):

        # Input and expected result.
        test_input_title = "Certified Angus Beef Boneless Strip Steak"
        test_input_description = "Beef top loin.Certified Angus Beef Boneless Strip Loin Sold whole in Cryovac. Sliced free ... 8.99 lb"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Certified Angus Beef Boneless Strip Steak Beef Top Loin."

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

    def test_Certified_Angus_Beef_Chuckeye_Roast(self):

        # Input and expected result.
        test_input_title = "Certified Angus Beef Chuckeye Roast"
        test_input_description = "Certified Angus BeefBoneless Chuckeye Steak .. 4.49 lb"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Certified Angus Beef Chuckeye Roast Certified Angus Beefboneless Chuckeye Steak 4.49 lb"

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

    def test_Yoplait_Original_or_Whips_46_oz__or_Dannon_Whole_Milk_or_Light__Fit_Yogurt(self):

        # Input and expected result.
        test_input_title = "Yoplait Original or Whips 4-6 oz. or Dannon Whole Milk or Light & Fit Yogurt"
        test_input_description = "5.3 oz. Excludes Greek."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Yoplait Original or Whips 4-6 oz or Dannon Whole Milk or Light & Fit Yogurt 5.3 oz"

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

    def test_Bud_Light_NFL(self):

        # Input and expected result.
        test_input_title = "Bud Light NFL*"
        test_input_description = "36 pk./12 oz. cans. Limited edition. Plus deposit where applicable."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bud Light NFL 36 pk/12 oz cans"

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

    def test_Meijer_Deli_Sandwich_Assorted_varieties_or_Jimmy_Dean_Breakfast_Sandwich(self):

        # Input and expected result.
        test_input_title = "Meijer Deli Sandwich Assorted varieties or Jimmy Dean Breakfast Sandwich"
        test_input_description = "Served hot from the Deli Case."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Meijer Deli Sandwich or Jimmy Dean Breakfast Sandwich"

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

    def test_Conagra_Brands(self):

        # Input and expected result.
        test_input_title = "Conagra Brands"
        test_input_description = "Save $1 on your next shopping trip via Custom Coupon at checkout when you buy $5Save $3 on your next shopping trip via Custom Coupon at checkout when you buy $10Save $5 on your next shopping trip via Custom Coupon at checkout when you buy $15"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Conagra Brands"

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

    def test_Caramel_Apple(self):

        # Input and expected result.
        test_input_title = "Caramel Apple"
        test_input_description = "Single. Plain or with nuts."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Caramel Apple Single."

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

    def test_Craft_Your_Own_4_Pack_Beer(self):

        # Input and expected result.
        test_input_title = "Craft Your Own 4 Pack Beer*"
        test_input_description = "4 pk./11.2-12 oz. bottles. Choose from one or more select varieties of our 1.99 single bottle beers. Plus deposit where applicable."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Craft Your Own 4 pack Beer 4 pk/11.2-12 oz bottles"

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

    def test_Collegiate_Tableware(self):

        # Input and expected result.
        test_input_title = "Collegiate Tableware*"
        test_input_description = "Teams may vary by store."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Collegiate Tableware"

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

    def test_NFL_Licensed_Team_Apparel_for_the_Family(self):

        # Input and expected result.
        test_input_title = "NFL Licensed Team Apparel for the Family*"
        test_input_description = "Teams may vary by store.Reg. $12-$99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "NFL Licensed Team Apparel"

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

    def test_Hooded_Towels_Washcloths_Bath_Toys_Tubs_or_Bath_Accessories(self):

        # Input and expected result.
        test_input_title = "Hooded Towels, Washcloths, Bath Toys, Tubs or Bath Accessories*"
        test_input_description = "Baby Dept. Reg. 1.99-24.99."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hooded Towels Washcloths Bath Toys Tubs or Bath Accessories"

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

    def test_Sprout_Organic_Pouches(self):

        # Input and expected result.
        test_input_title = "Sprout Organic Pouches*"
        test_input_description = "3.5-4.5 oz.Baby Dept."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sprout Organic pouches 3.5-4.5 oz"

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

    def test_Element_32_LED_HDTV(self):

        # Input and expected result.
        test_input_title = "Element 32 LED HDTV*"
        test_input_description = "Reg. 149.99.Limit two coupons per offer."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Element 32 Led HDTV "

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

    def test_Trico_Wiper_Blades(self):

        # Input and expected result.
        test_input_title = "Trico Wiper Blades*"
        test_input_description = "Reg. 7.49-21.99."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Trico Wiper Blades"

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

    def test_MTA_Sport_Activewear_for_the_Family(self):

        # Input and expected result.
        test_input_title = "MTA Sport Activewear for the Family*"
        test_input_description = "Sizes S-3X. Excludesclearance. Reg. $10-$39."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "MTA Sport Activewear Sizes S-3X."

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

    def test_Athletic_Shoes_for_the_Family(self):

        # Input and expected result.
        test_input_title = "Athletic Shoes for the Family*"
        test_input_description = "Reg. $18-$70Excludes adidas and Skechers."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Athletic Shoes"

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

    def test_Arctic_Zone_Lunch_Bags(self):

        # Input and expected result.
        test_input_title = "Arctic Zone Lunch Bags*"
        test_input_description = "Reg. 7.99-19.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Arctic Zone Lunch bags"

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

    def test_Reynolds_Wrap_Aluminum_Foil(self):

        # Input and expected result.
        test_input_title = "Reynolds Wrap Aluminum Foil"
        test_input_description = "65 sq. ft.55¢ off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Reynolds Wrap Aluminum Foil 65 sq ft"

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

    def test_Sonicare_Series_2_Rechargeable_Toothbrush(self):

        # Input and expected result.
        test_input_title = "Sonicare Series 2 Rechargeable Toothbrush"
        test_input_description = "$10 off coupon online or in most Sunday papersΩ"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sonicare Series 2 Rechargeable Toothbrush"

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

    def test_Olay_Eyes_Luminous_or_Regenerist_Skin_Care(self):

        # Input and expected result.
        test_input_title = "Olay Eyes, Luminous or Regenerist Skin Care"
        test_input_description = "Select varieties.coupon savings online or in most Sunday papersΩ"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Olay Eyes Luminous or Regenerist Skin Care"

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

    def test_Garnier_Fructis_Hair_Care(self):

        # Input and expected result.
        test_input_title = "Garnier Fructis Hair Care"
        test_input_description = "Shampoo or Conditioner,12 or 12.5 oz. Select Stylers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Garnier Fructis Hair Care Shampoo or Conditioner12 or 12.5 oz"

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

    def test_Softsoap_Body_Wash(self):

        # Input and expected result.
        test_input_title = "Softsoap Body Wash"
        test_input_description = "15 or 18 oz. Liquid Hand Soap: Pump, 7.5 to 11.25 oz. Refill, 56 oz.coupon savings in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Softsoap Body Wash 15 or 18 oz liquid Hand Soap Pump 7.5 to 11.25 oz Refill 56 oz"

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

    def test_Mucinex(self):

        # Input and expected result.
        test_input_title = "Mucinex"
        test_input_description = "16 or 20 ct. or 6 oz. Select varieties.$2 off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mucinex 16 or 20 ct or 6 oz"

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

    def test_ICaps_Eye_Vitamins(self):

        # Input and expected result.
        test_input_title = "I-Caps Eye Vitamins"
        test_input_description = "30 to 120 ct.Additional $5 off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "I-Caps Eye Vitamins 30 to 120 ct"

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

    def test_Schiff_Mega_Red_Vitamins_and_Supplements(self):

        # Input and expected result.
        test_input_title = "Schiff Mega Red Vitamins and Supplements"
        test_input_description = "30 to 120 ct.Additional $1 off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Schiff Mega Red Vitamins and Supplements 30 to 120 ct"

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

    def test_Zantac_Acid_Reducer(self):

        # Input and expected result.
        test_input_title = "Zantac Acid Reducer"
        test_input_description = "Duo Fusion 20 ct. 75 mg., 30 ct. or 150 mg., 24 ct.$4 off coupon in most Sunday papers† "
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Zantac Acid Reducer Duo Fusion 20 ct 75 mg 30 ct or 150 mg 24 ct"

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

    def test_Dulcolax_or_Dulcoease(self):

        # Input and expected result.
        test_input_title = "Dulcolax or Dulcoease"
        test_input_description = "Select Tablets, 25 ct. Suppositories, 4 pk.$3 Off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dulcolax or Dulcoease Select Tablets 25 ct Suppositories 4 pk"

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

    def test_Star_Wars_Action_Figure(self):

        # Input and expected result.
        test_input_title = "Star Wars Action Figure"
        test_input_description = "Action Figure Items shown, plus more!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Star Wars Action Figure"

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

    def test_4x6_Digital_Prints(self):

        # Input and expected result.
        test_input_title = "4x6 Digital Prints"
        test_input_description = "Enter promo code: REMEMBER"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "4X6 Digital prints"

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

    def test_Enlargements_and_Posters(self):

        # Input and expected result.
        test_input_title = "Enlargements and Posters"
        test_input_description = "Enter promo code: HALFOFF"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Enlargements and Posters"

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

    def test_Canvas_Prints_and_Wood_Panels(self):

        # Input and expected result.
        test_input_title = "Canvas Prints and Wood Panels"
        test_input_description = "Enter promo code: DECOR"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Canvas prints and Wood Panels"

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

    def test_GE_Light_Bulbs_4_pk(self):

        # Input and expected result.
        test_input_title = "GE Light Bulbs 4 pk."
        test_input_description = "Select varieties.$1 off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ge Light Bulbs 4 pk"

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

    def test_Photo_Books_and_PrintBooks(self):

        # Input and expected result.
        test_input_title = "Photo Books and PrintBooks"
        test_input_description = "Enter promo code: PRINTBOOKFREE Same Day Pickup‡‡"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Photo Books and printbooks"

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

    def test_Theater_Pack_Candy(self):

        # Input and expected result.
        test_input_title = "Theater Pack Candy"
        test_input_description = "Items shown, plus more!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Theater pack candy"

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

    def test_Candy_Gum_Mints_or_Welchs_Fruit_Snacks(self):

        # Input and expected result.
        test_input_title = "Candy, Gum, Mints or Welch's Fruit Snacks"
        test_input_description = "Items shown, plus more!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Candy Gum Mints or Welch's Fruit Snacks"

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

    def test_Halloween_Candy(self):

        # Input and expected result.
        test_input_title = "Halloween Candy"
        test_input_description = "Items shown, plus more!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Halloween candy"

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

    def test_Werthers_or_Riesen(self):

        # Input and expected result.
        test_input_title = "Werther's or Riesen"
        test_input_description = "2.35 to 5.5 oz. Select varieties.$1 off coupon on 2 in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Werther's or Riesen 2.35 to 5.5 oz"

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

    def test_White_Cloud_Bath_Tissue(self):

        # Input and expected result.
        test_input_title = "White Cloud Bath Tissue"
        test_input_description = "6 mega rolls or 12 giant rolls. $1.50 less coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "White Cloud Bath Tissue 6 Mega rolls or 12 Giant rolls"

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

    def test_Schick_Disposable_Razors(self):

        # Input and expected result.
        test_input_title = "Schick Disposable Razors"
        test_input_description = "Select varieties.3 to 12 pk.$3 off coupon in most Sunday paperst"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Schick Disposable Razors 3 to 12 pk"

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

    def test_Walgreens_Pain_Relief(self):

        # Input and expected result.
        test_input_title = "Walgreens Pain Relief"
        test_input_description = "Select Ibuprofen, Acetaminophen, All Day, Heat Wrap or Heating Pads."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Walgreens Pain Relief Ibuprofen Acetaminophen Heat Wrap or Heating Pads."

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

    def test_Vitamins_and_Supplements(self):

        # Input and expected result.
        test_input_title = "Vitamins and Supplements"
        test_input_description = "Select Qunol Co Q10, Move Free or Schiff Glucosamine."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Vitamins and Supplements Qunol Co Q10 or Schiff Glucosamine."

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

    def test_Digestive_Care_Walgreens_walzan(self):

        # Input and expected result.
        test_input_title = "Digestive Care Walgreens."
        test_input_description = "Select Wal-Zan®, Lansoprazole,Omeprazole, Omeprazole Magnesium, Smooth LAX® or Anti-Diarrheal."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Digestive Care Walgreens. Wal-Zan Lansoprazole Omeprazole Magnesium Smooth Lax or Anti-Diarrheal."

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

    def test_Always_Discreet(self):

        # Input and expected result.
        test_input_title = "Always Discreet"
        test_input_description = "Select Pads, 28 to 66 pk. Underwear, 10 to 19 pk."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Always Discreet Pads 28 to 66 pk Underwear 10 to 19 pk"

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

    def test_Certainty_Walgreens_Underwear(self):

        # Input and expected result.
        test_input_title = "Certainty Walgreens."
        test_input_description = "Select Underwear or Briefs, 10 to 22 pk. Guards, 52 pk. Pads, 27 to 66 pk. Underpads, 10, 18 or 36 pk."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Certainty Walgreens. Underwear or Briefs 10 to 22 pk Guards 52 pk Pads 27 to 66 pk Underpads 10 18 or 36 pk"

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

    def test_Home_Health_Care(self):

        # Input and expected result.
        test_input_title = "Home Health Care"
        test_input_description = "Homedics Pulse Oximeter ChoiceMMed Lung Boost Respiratory Trainer Walgreens Deluxe Arm or Wrist Blood Pressure Monitors"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Home Health Care Homedics Pulse Oximeter Choicemmed Lung Boost Respiratory Trainer Walgreens Deluxe Arm or Wrist Blood pressure Monitors"

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

    def test_Dulcolax_or_Dulcoease(self):

        # Input and expected result.
        test_input_title = "Dulcolax or Dulcoease"
        test_input_description = "Select Tablets, 25 ct. Suppositories, 4 pk.$3 Off coupon in most Sunday papers†"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dulcolax or Dulcoease Tablets 25 ct Suppositories 4 pk"

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

    def test_Gillette_Shave_Needs(self):

        # Input and expected result.
        test_input_title = "Gillette Shave Needs"
        test_input_description = "Select Cartridges, Shave Gel, Razors or Razor Systems."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gillette Shave Cartridges Shave Gel Razors or Razor Systems."

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

    def test_General_Mills_Cereal(self):

        # Input and expected result.
        test_input_title = "General Mills Cereal"
        test_input_description = "8.9 to 16.25 oz. Select varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "General Mills cereal 8.9 to 16.25 oz"

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

    def test_Nice_One_Dozen_Large_Grade_A_or_AA_Eggs(self):

        # Input and expected result.
        test_input_title = "Nice!® One Dozen Large Grade A or AA Eggs"
        test_input_description = "Butterball Turkey Bacon- $1.29 with card"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nice One Dozen Large Grade A or AA Eggs Butterball Turkey Bacon"

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

    def test_Maxwell_House_Instant_Coffee(self):

        # Input and expected result.
        test_input_title = "Maxwell House Instant Coffee"
        test_input_description = "8 oz.Decaf - $3.99 with card"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Maxwell House instant Coffee 8 ozDecaf"

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

    def test_Nice_Select_Nuts(self):

        # Input and expected result.
        test_input_title = "Nice!® Select Nuts"
        test_input_description = "Cashews Halves & Pieces, 8 or 9.25 oz. Mixed Nuts, 10.3 oz. Pistachios, 8 oz."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nice Select Nuts Cashews Halves & Pieces 8 or 9.25 oz Mixed Nuts 10.3 oz Pistachios 8 oz"

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

    def test_9_99_While_Supplies_Last(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "9.99 While Supplies Last"
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
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_10_99_Order_Online_by_Phone_or_in_Person(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "10.99 Order Online, by Phone or in Person!"
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

