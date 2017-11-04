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
class TestWebgrocerTitles(object):

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

    def test_Fresh_Premium_Apples(self):

        # Input and expected result.
        test_input_title = "Fresh Premium Apples"
        test_input_description = "All Sizes All Varieties WASHINGTON®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh premium Apples"

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

    def test_Lucerne_Full_Line_Sale(self):

        # Input and expected result.
        test_input_title = "Lucerne® Full Line Sale"
        test_input_description = "Fresh Dairy & Frozen Grocery Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lucerne Full Line"

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

    def test_Signature_SELECT_or_O_Organics_Coffee(self):

        # Input and expected result.
        test_input_title = "Signature SELECT™ or O Organics® Coffee"
        test_input_description = "Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Select or O Organics Coffee"

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

    def test_Save_10_Off_Your_Grocery_Purchase_Of_100_Or_More(self):

        # Input and expected result.
        test_input_title = "Save 10% Off Your Grocery Purchase Of $100 Or More"
        test_input_description = "LIMIT 1 PER CUSTOMER. This coupon cannot be used unless the purchase is $100 or more after deducting all manufacturer coupons and store coupons, and without including money orders, lottery tickets, gift cards, alcohol, tobacco, prescriptions, stamps and other products prohibited by law. Cannot be doubled, tripled, quadrupled or exchanged for cash. Not valid toward previous purchase. Void if copied or transferred in the event of return, coupon savings may be deducted from refund. May not be used in combination with any other offer. One coupon per customer, per transaction. *See Store For Exclusions Albertsons® Coupon Effective 9/13/17 - 9/19/17"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = ""

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

    def test_Progresso_Traditional_Rich_u0026_Hearty_18_519_oz__Campbells_Cream_of_Chicken_Mushroom_Chicken_Noodle_or_Tomato_Soup_10_75_oz_(self):

        # Input and expected result.
        test_input_title = "Progresso Traditional, Rich \u0026 Hearty 18.5-19 oz., Campbell’s Cream of Chicken, Mushroom, Chicken Noodle or Tomato Soup 10.75 oz."
        test_input_description = "Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Progresso Traditional Rich Hearty 18.5-19 oz Campbells Cream of Chicken Mushroom Chicken Noodle or Tomato Soup 10.75 oz"

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

    def test_Stouffers_Red_Box_or_Lean_Cuisine_Entrees(self):

        # Input and expected result.
        test_input_title = "Stouffer’s Red Box or Lean Cuisine Entrees"
        test_input_description = "5.25-12.75 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stouffers Red box or Lean Cuisine Entrees 5.25 oz"

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

    def test_Tombstone_Pizza(self):

        # Input and expected result.
        test_input_title = "Tombstone Pizza"
        test_input_description = "18.1-22 oz., Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tombstone Pizza 18.1-22 oz"

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

    def test_Thomas_Bagels(self):

        # Input and expected result.
        test_input_title = "Thomas’ Bagels"
        test_input_description = "6 ct. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Thomas bagels 6 ct"

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

    def test_Classico_Pasta_Sauce(self):

        # Input and expected result.
        test_input_title = "Classico Pasta Sauce"
        test_input_description = "15-24 oz., Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Classico Pasta Sauce 15-24 oz"

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

    def test_Kraft_Salad_Dressing(self):

        # Input and expected result.
        test_input_title = "Kraft Salad Dressing"
        test_input_description = "14-16 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kraft Salad Dressing 14-16 oz"

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

    def test_Barilla_Pasta(self):

        # Input and expected result.
        test_input_title = "Barilla Pasta"
        test_input_description = "12-16 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Barilla Pasta 12-16 oz"

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

    def test_Lays_Stax(self):

        # Input and expected result.
        test_input_title = "Lay’s Stax"
        test_input_description = "5.5-5.75 oz., Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lays Stax 5.5 oz"

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

    def test_Taco_Bell_Sauce(self):

        # Input and expected result.
        test_input_title = "Taco Bell Sauce"
        test_input_description = "7.5 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Taco Bell Sauce 7.5 oz"

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

    def test_Taco_Bell_Taco_Shells(self):

        # Input and expected result.
        test_input_title = "Taco Bell Taco Shells"
        test_input_description = "12 ct. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Taco Bell Taco Shells 12 ct"

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

    def test_Taco_Bell_Refried_Beans(self):

        # Input and expected result.
        test_input_title = "Taco Bell Refried Beans"
        test_input_description = "16 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Taco Bell Refried Beans 16 oz"

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

    def test_Angel_Soft_Bath_Tissue(self):

        # Input and expected result.
        test_input_title = "Angel Soft Bath Tissue"
        test_input_description = "6-12 rolls., Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Angel Soft Bath Tissue 6-12 rolls"

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

    def test_Sparkle_Paper_Towels(self):

        # Input and expected result.
        test_input_title = "Sparkle Paper Towels"
        test_input_description = "6-8 rolls Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sparkle Paper Towels 6-8 rolls"

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

    def test_Gain_Laundry_Detergent(self):

        # Input and expected result.
        test_input_title = "Gain Laundry Detergent"
        test_input_description = "50 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gain Laundry Detergent 50 oz"

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

    def test_Dasani_Water(self):

        # Input and expected result.
        test_input_title = "Dasani Water"
        test_input_description = "24 pk., 16.9 oz., Select Varieties Sale Price $4.99 ea. MIX & MATCH SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dasani Water 24 pk 16.9 oz"

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

    def test_Powerade_Sports_Drinks(self):

        # Input and expected result.
        test_input_title = "Powerade Sports Drinks"
        test_input_description = "8 pk., 20 oz. Select Varieties Sale Price $4.99 ea. MIX & MATCH SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Powerade Sports Drinks 8 pk 20 oz"

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

    def test_Glacau_Vitaminwater(self):

        # Input and expected result.
        test_input_title = "Glacéau Vitaminwater"
        test_input_description = "6 pk., 16.9 oz. Select Varieties Sale Price $4.99 ea. MIX & MATCH SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Glaceau Vitaminwater 6 pk 16.9 oz"

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

    def test_Natures_Own_Butter_Bread(self):

        # Input and expected result.
        test_input_title = "Nature’s Own Butter Bread"
        test_input_description = "20 oz. SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Natures Own Butter Bread 20 oz"

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

    def test_Coke_(self):

        # Input and expected result.
        test_input_title = "Coke."
        test_input_description = "12 pk., 12 oz. cans or 8 pk., 12 oz. bottles Select Varieties Sale  Price $5.99 ea. MIX & MATCH SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke. 12 pk 12 oz cans or 8 pk 12 oz bottles"

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

    def test_Late_July_Chips_5_56_oz__Snyders_Pretzel_Pieces_812_oz_(self):

        # Input and expected result.
        test_input_title = "Late July Chips 5.5-6 oz., Snyder’s Pretzel Pieces 8-12 oz."
        test_input_description = "Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Chips 5.5-6 oz Snyders pretzel Pieces 8-12 oz"

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

    def test_Pop_Secret_Popcorn(self):

        # Input and expected result.
        test_input_title = "Pop Secret Popcorn"
        test_input_description = "3 ct. Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pop Secret Popcorn 3 ct"

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

    def test_Coke__(self):

        # Input and expected result.
        test_input_title = "Coke.."
        test_input_description = "2 Liter Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke. 2 liter"

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

    def test_Campbells_Chunky_Soup(self):

        # Input and expected result.
        test_input_title = "Campbell’s Chunky Soup"
        test_input_description = "18.6-18.8 oz. Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Campbells Chunky Soup 18.6-18.8 oz"

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

    def test_Dietz_u0026_Watson_Pre_Sliced_Meat_or_Cheese(self):

        # Input and expected result.
        test_input_title = "Dietz \u0026 Watson Pre Sliced Meat or Cheese"
        test_input_description = "7-8 oz. Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dietz Watson pre Sliced Meat or Cheese 7-8 oz"

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

    def test_Stella_Artois__Four_Peaks(self):

        # Input and expected result.
        test_input_title = "Stella Artois  Four Peaks"
        test_input_description = "12 pack bottles Select Varieties SCORE GREAT DEALS PARTICIPATING ITEM"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stella Artois Four Peaks 12 pack bottles"

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

    def test_CrockPot_7_Qt__Manual_Slow_Cooker(self):

        # Input and expected result.
        test_input_title = "Crock-Pot 7 Qt. Manual Slow Cooker*"
        test_input_description = "Reg. 29.99.Other Select Crock-Pot Slow Cookers*Reg. 10.99-39.99, now 9.89-35.99.....10% off"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Crock-Pot 7 qt Manual Slow Cooker"

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

    def test_Primo_Taglio_Ham_Turkey_or_Cheese(self):

        # Input and expected result.
        test_input_title = "Primo Taglio® Ham, Turkey or Cheese"
        test_input_description = "Select Varieties Sliced Fresh in the Deli PRIMO TAGLIO®  FIRST CUT QUALITY  SAY: PREE-MO  TAHL-YO"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Primo Taglio Ham Turkey or Cheese primo Taglio"

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

    def test_Fresh_All_Natural_Pork_Shoulder_Blade_Roast(self):

        # Input and expected result.
        test_input_title = "Fresh All Natural* Pork Shoulder Blade Roast"
        test_input_description = "In The Bag *The product is a natural food because it contains no artificial ingredients and is only minimally processed."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Pork Shoulder Blade Roast in the bag"

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

    def test_Fiber_One_Nature_Valley_Granola_Bars_Breakfast_Biscuits_or_Soft_Baked_Squares(self):

        # Input and expected result.
        test_input_title = "Fiber One, Nature Valley Granola Bars, Breakfast Biscuits or Soft Baked Squares"
        test_input_description = "5-6 ct., Select Varieties Sale Price: 2 for $5 Limit 2 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fiber One Nature Valley Granola Bars Breakfast Biscuits or Soft Baked squares 5-6 ct"

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
        test_input_description = "9.6-13 oz., Select Varieties Sale Price: 2 for $5 Limit 2 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "General Mills cereal 9.6-13 oz"

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

    def test_Dreyers_Ice_Cream_48_fl_oz_Nestl(self):

        # Input and expected result.
        test_input_title = "Dreyer\u0027s Ice Cream 48 fl. oz., Nestlé, Hostess Novelties 4-12 ct., Häagen-Dazs Ice Cream or Bars 14 fl. oz. or 3 pk."
        test_input_description = "Select Varieties Additional: $2.99 ea. Limit 2 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dreyers Ice Cream 48 fl oz Nestle Hostess Novelties 4-12 ct Haagen-Dazs Ice Cream or Bars 14 fl oz or 3 pk"

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

    def test_Lays_Family_Size_9_510_oz(self):

        # Input and expected result.
        test_input_title = "Lay\u0027s Family Size 9.5-10 oz., Fritos, Cheetos 8.75-10.25 oz. or Kettle Cooked Chips 6.5-8.5 oz."
        test_input_description = "Select Varieties Sale Price: $2.99 ea. Limit 1 Reward Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lays 9.5-10 oz Fritos Cheetos 8.75 oz or Kettle Cooked Chips 6.5-8.5 oz"

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

    def test_Nabisco_Chips_Ahoy_Cookies(self):

        # Input and expected result.
        test_input_title = "Nabisco Chips Ahoy! Cookies"
        test_input_description = "7-13 oz., Select Varieties Sale Price: $2.99 ea. Limit 1 Reward Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nabisco Chips Ahoy Cookies 7-13 oz"

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

    def test_Nabisco_Snack_Crackers_3_59_1_oz_Toasted_Chips_8_1_oz__or_Cheese_Nips(self):

        # Input and expected result.
        test_input_title = "Nabisco Snack Crackers 3.5-9.1 oz., Toasted Chips 8.1 oz. or Cheese Nips 10-11 oz."
        test_input_description = "Select Varieties Sale Price: $2.99 ea. Limit 1 Reward Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nabisco Snack Crackers 3.5-9.1 oz Toasted Chips 8.1 oz or Cheese Nips 10-11 oz"

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

    def test_Gatorade_Sports_Drink(self):

        # Input and expected result.
        test_input_title = "Gatorade Sports Drink"
        test_input_description = "32 oz. Select Varieties Sale Price: 10 for $10 Limit 3 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gatorade Sports Drink 32 oz"

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

    def test_Kelloggs_Poptarts(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Poptarts"
        test_input_description = "8 ct. Select Varieties Sale Price: 2 for $5 Limit 2 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Poptarts 8 ct"

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

    def test_Betty_Crocker_Fruit_Snacks(self):

        # Input and expected result.
        test_input_title = "Betty Crocker Fruit Snacks"
        test_input_description = "6-10 ct. Select Varieties Sale Price: 2 for $5 Limit 2 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Betty Crocker Fruit Snacks 6-10 ct"

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

    def test_Signature_8_Piece_Fried_or_Baked_Chicken(self):

        # Input and expected result.
        test_input_title = "Signature 8 Piece Fried or Baked Chicken"
        test_input_description = "2 Breasts, 2 Wings, 2 Thighs, 2 Legs Hot & Fresh"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature 8 Piece Fried or Baked Chicken 2 Breasts 2 Wings 2 Thighs 2 Legs"

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

    def test_Boneless_Skinless_Chicken_Breast_or_Thighs(self):

        # Input and expected result.
        test_input_title = "Boneless Skinless Chicken Breast or Thighs"
        test_input_description = "Sold Out of Our Fresh Butcher Block Fresh Never Frozen"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boneless Skinless Chicken Breast or Thighs"

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

    def test_USDA_Choice_Beef_Chuck_Tender_Fillet_or_Petite_Sirloin_Steaks(self):

        # Input and expected result.
        test_input_title = "USDA Choice Beef Chuck Tender Fillet or Petite Sirloin Steaks"
        test_input_description = "Boneless, Reg. Retail: up to $12.99 lb. Equal or Lesser Value USDA CHOICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Beef Chuck Tender Fillet or Petite Sirloin Steaks Boneless"

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

    def test_85_Lean_Ground_Beef(self):

        # Input and expected result.
        test_input_title = "85% Lean Ground Beef"
        test_input_description = "Sold in Packages of 3 lb. or More in the Meat Case GROUND FRESH in Store Daily"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ground Beef"

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

    def test_Propel_Fitness_Water(self):

        # Input and expected result.
        test_input_title = "Propel Fitness Water"
        test_input_description = "24 oz. Select Varieties Sale Price: 10 for $10 Limit 3 Rewards Per Transaction MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Propel Fitness Water 24 oz"

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

    def test_Oscar_Mayer_Beef_Hot_Dogs(self):

        # Input and expected result.
        test_input_title = "Oscar Mayer Beef Hot Dogs"
        test_input_description = "14-15 oz. QUICK & EASY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Oscar Mayer Beef Hot Dogs 14-15 oz"

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

    def test_Oscar_Mayer_Fun_Pack_Lunchables(self):

        # Input and expected result.
        test_input_title = "Oscar Mayer Fun Pack Lunchables"
        test_input_description = "8-10.7 oz. QUICK & EASY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Oscar Mayer Fun pack Lunchables 8-10.7 oz"

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

    def test_Margherita_Genoa_Hard_Salami_Pepperoni_or_President_Swiss_Cheese(self):

        # Input and expected result.
        test_input_title = "Margherita Genoa, Hard Salami, Pepperoni or President Swiss Cheese"
        test_input_description = "Sliced Fresh in the Deli"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Margherita Genoa Hard Salami Pepperoni or president Swiss Cheese"

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

    def test_Resers_Sensational_Side_Dishes(self):

        # Input and expected result.
        test_input_title = "Reser’s Sensational Side Dishes"
        test_input_description = "12-14 oz. Select Varieties RESER'S FINE FOODS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Resers Sensational 12-14 oz"

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

    def test_Signature_Chicken_Tenders_Nuggets_or_Hot_Wings(self):

        # Input and expected result.
        test_input_title = "Signature Chicken Tenders, Nuggets or Hot Wings"
        test_input_description = "Makes a Great Lunch! Hot & Fresh"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Chicken Tenders Nuggets or Hot Wings"

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

    def test_Cucumber_Dill_Tomato_Hawaiian_Fruit_or_Greek_Veggie_Pasta_Salad(self):

        # Input and expected result.
        test_input_title = "Cucumber Dill \u0026 Tomato, Hawaiian Fruit or Greek Veggie Pasta Salad"
        test_input_description = "Made Fresh Daily"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Cucumber Dill Tomato Hawaiian Fruit or Greek Veggie Pasta Salad"

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

    def test_Signature_Cafe_Green_Entre_Salad(self):

        # Input and expected result.
        test_input_title = "Signature Cafe® Green Entrée Salad"
        test_input_description = "8.5-10.75 oz. Select Varieties Signature CAFE®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Cafe Green Entree Salad 8.5 oz"

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

    def test_Signature_Farms_Lunchmeat_Tubs(self):

        # Input and expected result.
        test_input_title = "Signature Farms Lunchmeat Tubs"
        test_input_description = "7-8 oz. QUICK & EASY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Farms Lunchmeat Tubs 7-8 oz"

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

    def test_Land_O_Frost_Premium_Sliced_Lunchmeats(self):

        # Input and expected result.
        test_input_title = "Land O’ Frost Premium Sliced Lunchmeats"
        test_input_description = "16 oz. QUICK & EASY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Land O Frost premium Sliced Lunchmeats 16 oz"

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

    def test_Open_Nature_St_Louis_Style_Pork_Spareribs_Bone_In_or_Boneless_Pork_Shoulder_Roast(self):

        # Input and expected result.
        test_input_title = "Open Nature™ St. Louis Style Pork Spareribs Bone In or Boneless Pork Shoulder Roast"
        test_input_description = "No Antibiotics or Added Hormones, Vegertarian Fed OPEN NATURE®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Open Nature St. Louis Style Pork Spareribs Bone in or Boneless Pork Shoulder Roast"

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

    def test_USDA_Choice_Beef_Chuck_Cross_Rib_Eye_of_Round_or_Tip_Roast(self):

        # Input and expected result.
        test_input_title = "USDA Choice Beef Chuck, Cross Rib, Eye of Round or Tip Roast"
        test_input_description = "Boneless or Family Pack Steaks USDA CHOICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Beef Chuck Cross Rib Eye of Round or Tip Roast Boneless or Family pack Steaks"

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

    def test_Fresh_All_Natural_Pork_Shoulder_Country_Style_Ribs_or_Pork_Steak(self):

        # Input and expected result.
        test_input_title = "Fresh All Natural* Pork Shoulder Country Style Ribs or Pork Steak"
        test_input_description = "Family Pack, Bone In *The product is a natural food because it contains no artificial ingredients and is only minimally processed."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Pork Shoulder Country Style Ribs or Pork Steak Family pack Bone in"

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

    def test_Fresh_All_Natural_Pork_Sirloin_Chops(self):

        # Input and expected result.
        test_input_title = "Fresh All Natural* Pork Sirloin Chops"
        test_input_description = "Boneless, Family Pack *The product is a natural food because it contains no artificial ingredients and is only minimally processed."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Pork Sirloin Chops Boneless Family pack"

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

    def test_Fresh_Wild_Caught_King_Salmon_Fillets(self):

        # Input and expected result.
        test_input_title = "Fresh Wild Caught King Salmon Fillets"
        test_input_description = "Subject to Availability wild"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Wild caught King Salmon Fillets"

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

    def test_Signature_Farms_73_Lean_Ground_Beef_Patties(self):

        # Input and expected result.
        test_input_title = "Signature Farms™ 73% Lean Ground Beef Patties"
        test_input_description = "40 oz., Frozen Signature Farms® Quality Guaranteed"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Farms Ground Beef Patties 40 oz frozen"

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

    def test_Open_Nature_Boneless_Skinless_Chicken_Breast(self):

        # Input and expected result.
        test_input_title = "Open Nature™ Boneless Skinless Chicken Breast"
        test_input_description = "2.25 lb., Frozen, Package, No Antibiotics or Addezd Hormones, Vegetarian Fed OPEN NATURE®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Open Nature Boneless Skinless Chicken Breast 2.25 lb frozen package"

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

    def test_Open_Nature_93_Lean_Ground_Turkey(self):

        # Input and expected result.
        test_input_title = "Open Nature™ 93% Lean Ground Turkey"
        test_input_description = "16 oz., Frozen No Antibiotics or Added Hormones, Vegetarian Fed OPEN NATURE®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Open Nature Ground Turkey 16 oz frozen"

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

    def test_Sanderson_Farms_Drumsticks_Thighs_or_Leg_Quarters(self):

        # Input and expected result.
        test_input_title = "Sanderson Farms Drumsticks, Thighs or Leg Quarters"
        test_input_description = "Bone In, Jumbo Pack Sanderson Farms®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sanderson Farms Drumsticks Thighs or Leg Quarters Bone in Jumbo pack Sanderson Farms"

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

    def test_Oscar_Mayer_Meat_Turkey_Hot_Dogs_Meat_Bologna_or_Cotto_Salami(self):

        # Input and expected result.
        test_input_title = "Oscar Mayer Meat, Turkey Hot Dogs, Meat Bologna or Cotto Salami"
        test_input_description = "16 oz. QUICK & EASY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Oscar Mayer Meat Turkey Hot Dogs Meat Bologna or Cotto Salami 16 oz"

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

    def test_Coke(self):

        # Input and expected result.
        test_input_title = "Coke"
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY 20 pk., 12 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke 20 pk 12 oz"

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

    def test_Fruit_u0026_Seed_or_Berry_Crunch_Granola(self):

        # Input and expected result.
        test_input_title = "Fruit \u0026 Seed or Berry Crunch Granola"
        test_input_description = "9.2-10.5 oz. Delicious"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fruit Seed or Berry Crunch Granola 9.2-10.5 oz"

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

    def test_Philadelphia_Cream_Cheese_Brick(self):

        # Input and expected result.
        test_input_title = "Philadelphia Cream Cheese Brick"
        test_input_description = "8 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Philadelphia Cream Cheese Brick 8 oz"

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

    def test_Signature_SELECT_Ice_Cream(self):

        # Input and expected result.
        test_input_title = "Signature SELECT™ Ice Cream 48 fl. oz., Open Nature™ Sorbet, Gelato, Ice Cream 16 fl. oz. or Lucerne® Ice Cream Sandwiches 12 ct."
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Select Ice Cream 48 fl oz Open Nature Sorbet Gelato Ice Cream 16 fl oz or Lucerne Ice Cream Sandwiches 12 ct"

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

    def test_Hersheys_All_Time_Greats_100_00_ct__or_Childs_Play_Candy_3_50_lb(self):

        # Input and expected result.
        test_input_title = "Hershey’s All Time Greats 100.00 ct. or Child’s Play Candy 3.50 lb."
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hersheys All Time Greats 100.00 ct or Childs Play candy"

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

    def test_Tropical_Pineapple(self):

        # Input and expected result.
        test_input_title = "Tropical Pineapple"
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tropical Pineapple"

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

    def test_Signature_Hot_Wings(self):

        # Input and expected result.
        test_input_title = "Signature Hot Wings"
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY Makes a Great Lunch Hot & Fresh"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Hot Wings"

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

    def test_USDA_Choice_Beef_Bone_In_Ribeye_Steak(self):

        # Input and expected result.
        test_input_title = "USDA Choice Beef Bone In Ribeye Steak"
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY Family Pack USDA CHOICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Beef Bone in Ribeye Steak Family pack"

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

    def test_Green_Giant_Steamers_Frozen_Vegetables(self):

        # Input and expected result.
        test_input_title = "Green Giant Steamers Frozen Vegetables"
        test_input_description = "11-12 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Green Giant Steamers frozen Vegetables 11-12 oz"

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

    def test_O_Organics_Mini_Peeled_Carrots_16_oz__or_Rainbow_Mini_Peeled_Carrots_12_oz(self):

        # Input and expected result.
        test_input_title = "O Organics® Mini Peeled Carrots 16 oz. or Rainbow Mini Peeled Carrots 12 oz."
        test_input_description = "USDA ORGANIC WE PROUDLY OFFER OVER 150 VARIETIES OF ORGANIC PRODUCTS. "
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "O Organics Mini Peeled Carrots 16 oz or Rainbow Mini Peeled Carrots 12 oz"

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

    def test_THIS_WEEKS_FEATURED_ORGANIC_ITEMSOrganic_Red_or_Green_Seedless_Grapes(self):

        # Input and expected result.
        test_input_title = "THIS WEEKS FEATURED ORGANIC ITEMS:Organic Red or Green Seedless Grapes"
        test_input_description = "USDA ORGANIC WE PROUDLY OFFER OVER 150 VARIETIES OF ORGANIC PRODUCTS. THIS WEEKS FEATURED ORGANIC ITEMS:"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Organic Red or Green Seedless Grapes"

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

    def test_Rose_Bouquet(self):

        # Input and expected result.
        test_input_title = "Rose Bouquet"
        test_input_description = "9 Stem"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rose Bouquet 9 stem"

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

    def test_Valid_Friday_only_09152017_Assorted_Donuts(self):

        # Input and expected result.
        test_input_title = "Valid Friday only 09-15-2017 Assorted Donuts"
        test_input_description = "12 ct. donut friday"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Donuts 12 ct"

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

    def test_Assorted_Donut_Holes(self):

        # Input and expected result.
        test_input_title = "Assorted Donut Holes"
        test_input_description = "23 oz."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Donut Holes 23 oz"

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

    def test_Speed_Stick_Deodorant(self):

        # Input and expected result.
        test_input_title = "Speed Stick Deodorant"
        test_input_description = "2.7-3 oz. Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Speed Stick Deodorant 2.7-3 oz"

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

    def test_Signature_SELECT_80_ct__or_Green_Mountain_Pods_36_ct(self):

        # Input and expected result.
        test_input_title = "Signature SELECT™ 80 ct. or Green Mountain Pods 36 ct."
        test_input_description = "Select Varieties. GREAT SAVINGS DOWN EVERY AISLE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Select 80 ct or Green Mountain Pods 36 ct"

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

    def test_Signature_Kitchens_Apple_Cranberry_Juice_or_Lemonade(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens™ Apple, Cranberry Juice or Lemonade"
        test_input_description = "64 oz. Select Varieties. GREAT SAVINGS DOWN EVERY AISLE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Apple Cranberry Juice or Lemonade 64 oz"

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

    def test_Nestea(self):

        # Input and expected result.
        test_input_title = "Nestea"
        test_input_description = "6 pk., 16.9 oz. Select Varieties. GREAT SAVINGS DOWN EVERY AISLE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nestea 6 pk 16.9 oz"

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

    def test_Stella_Rosa_Select_Varieties_Jose_Cuervo_Tequila_Gold_or_Silver(self):

        # Input and expected result.
        test_input_title = "Stella Rosa Select Varieties  Jose Cuervo Tequila Gold or Silver"
        test_input_description = "750 ml Sale Price $11.99 ea Discount When You Buy 2 -$2.00 $11.99 ea-$2.00 MIX & MATCH"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stella Rosa Jose Cuervo Tequila Gold or Silver 750 ml"

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

    def test_Jack_Daniels_Tennessee_Whiskey_Select_Varieties_Titos_Handmade_Vodka(self):

        # Input and expected result.
        test_input_title = "Jack Daniel’s Tennessee Whiskey Select Varieties  Tito’s Handmade Vodka"
        test_input_description = "750 ml Sale Price $19.99 ea Discount When You Buy 6 -10% $19.99 ea-10%"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Jack Daniels Tennessee Whiskey Titos Vodka 750 ml"

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

    def test_Firestone_Walker_805__Sierra_Nevada__Blue_Moon(self):

        # Input and expected result.
        test_input_title = "Firestone Walker 805  Sierra Nevada  Blue Moon"
        test_input_description = "12 Pack Bottles Select Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Firestone Walker 805 Sierra Nevada Blue Moon 12 pack bottles"

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

    def test_14_Hands(self):

        # Input and expected result.
        test_input_title = "14 Hands"
        test_input_description = "Cabernet, Chardonnay, or Merlot 750 ml Sale Price $9.49 ea Discount When You Buy 2 -$1.50 $9.49 ea-$1.50"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "14 Hands Cabernet Chardonnay or Merlot 750 ml"

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

    def test_Kendall_Jackson_Vintners_Reserve_Chardonnay_or_Select_Varieties(self):

        # Input and expected result.
        test_input_title = "Kendall Jackson Vintner’s Reserve Chardonnay or Select Varieties  Curious Beasts Red Blend or Select Varieties"
        test_input_description = "750 ml Sale Price $10.99 ea Discount When You Buy 6 -10% $10.99 ea-10%"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kendall Jackson Vintners Reserve Chardonnay or Curious Beasts Red Blend or 750 ml"

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

    def test_Jam_Cellars(self):

        # Input and expected result.
        test_input_title = "Jam Cellars"
        test_input_description = "Butter Chardonnay or Cabernet Sauvignon 750 ml Sale Price $14.99 ea Discount When You Buy 6 -10% $14.99 ea-10%"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Jam Cellars Butter Chardonnay or Cabernet Sauvignon 750 ml"

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

    def test_Dozen_Donuts(self):

        # Input and expected result.
        test_input_title = "Dozen Donuts"
        test_input_description = "$5 FRIDAY SEPTEMBER 15TH ONE DAY ONLY Assorted Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dozen Donuts"

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

    def test_Arrowhead_Sparkling_Water(self):

        # Input and expected result.
        test_input_title = "Arrowhead Sparkling Water"
        test_input_description = "12 pk., 23.7 oz. Select Varieties. GREAT SAVINGS DOWN EVERY AISLE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Arrowhead Sparkling Water 12 pk 23.7 oz"

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

    def test_Crystal_Geyser_Alpine_Spring_Water(self):

        # Input and expected result.
        test_input_title = "Crystal Geyser Alpine Spring Water"
        test_input_description = "24 pk., 16.9 oz. GREAT SAVINGS DOWN EVERY AISLE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Crystal Geyser Alpine Spring Water 24 pk 16.9 oz"

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

    def test_Red_or_Green_Seedless_Grapes(self):

        # Input and expected result.
        test_input_title = "Red or Green Seedless Grapes"
        test_input_description = "2 lb. package LOCAL GROWN IN TULARE COUNTY"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Red or Green Seedless Grapes 2 lb package Local"

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

    def test_U_S_D_A_CHOICE_BEEF_Filet_Mignon_Roast(self):

        # Input and expected result.
        test_input_title = "U.S.D.A. CHOICE BEEF Filet Mignon Roast"
        test_input_description = "Boneless Sold in the bag U.S.D.A. CHOICE BEEF"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Beef Filet Mignon Roast Boneless"

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

    def test_Annies_Mountain_High_or_Cascadian_Farm_products(self):

        # Input and expected result.
        test_input_title = "Annie’s, Mountain High or Cascadian Farm products"
        test_input_description = "Buy any 3 select Annie’s, Mountain High or Cascadian Farm products and get 1 of equal or lesser value, FREE. Items must be purchased in a single transaction. $1 ea $2 ea $3 ea BUY 3, GET 1 FREE MOUNTAIN HIGH® The Natural Choice in Yoghurt Cascadian Farm™ ORGANIC FOUNDED IN SKAGIT VALLEY, WA SINCE 1972 Annie's® HOMEGROWN RABBIT OF APPROVAL®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Annies Mountain High or Cascadian Farm products"

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

    def test_Crest_ProHealth_Toothpaste_OralB_Crossaction_ProHealth_Toothbrush(self):

        # Input and expected result.
        test_input_title = "Crest Pro-Health Toothpaste 4.6 oz. Oral-B Crossaction Pro-Health Toothbrush 1 ct. or Crest Glide Floss Twin pack 43.7 yd."
        test_input_description = "Selected varieties. health & home savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Crest pro-Health Toothpaste 4.6 oz Oral-B Crossaction pro-Health Toothbrush 1 ct or Crest Glide floss Twin pack 43.7 yd"

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

    def test_Aleve_Naproxen_Tablets_Bayer_Genuine_Aspirin(self):

        # Input and expected result.
        test_input_title = "Aleve Naproxen Tablets or Caplets 50 ct. Bayer Genuine Aspirin 100-120 ct. or Children’s Tylenol Suspension Liquid 4 oz."
        test_input_description = "Selected varieties. health & home savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Aleve Naproxen Tablets or Caplets 50 ct Bayer Genuine Aspirin 100-120 ct or Childrens Tylenol Suspension liquid 4 oz"

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

    def test_Tropicana_Pure_Premium_Orange_Juice(self):

        # Input and expected result.
        test_input_title = "Tropicana Pure Premium Orange Juice"
        test_input_description = "Valid Only Friday September 15, 201789-oz. Selected varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tropicana Pure premium Orange Juice 89 oz"

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

    def test_Skippy_Peanut_Butter(self):

        # Input and expected result.
        test_input_title = "Skippy Peanut Butter"
        test_input_description = "Valid Only Friday September 15, 201740-oz.Selected varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Skippy Peanut Butter 40 oz"

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

    def test_La_Victoria_Salsa(self):

        # Input and expected result.
        test_input_title = "La Victoria Salsa"
        test_input_description = "Valid Only Friday September 15, 201767-oz.Selected varieties.Plus deposit in Oregon."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "La Victoria Salsa 67 oz"

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

    def test_Coors_Budweiser_Miller_or_Tecate(self):

        # Input and expected result.
        test_input_title = "Coors, Budweiser, Miller or Tecate"
        test_input_description = "30-pack, 12-oz. cans.Selected varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coors Budweiser Miller or Tecate 30 pack 12 oz cans"

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

    def test_Signature_Home_Facial_Tissue(self):

        # Input and expected result.
        test_input_title = "Signature Home Facial Tissue"
        test_input_description = "Valid Only Friday September 15, 201760 to 85-ct.Selected varieties.Club Price: $1.25 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Home Facial Tissue 60 to 85 ct"

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

    def test_Signature_Home_Napkins(self):

        # Input and expected result.
        test_input_title = "Signature Home Napkins"
        test_input_description = "Valid Only Friday September 15, 2017500-ct.Selected varieties. Club Price: $2.50 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Home Napkins 500 ct"

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

    def test_Signature_Kitchens_Apple_Juice(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Apple Juice"
        test_input_description = "64-oz. Selected varieties. Plus deposit in Oregon.WHEN YOU BUY 3"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Apple Juice 64 oz"

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

    def test_Langers_Tropical_Juice(self):

        # Input and expected result.
        test_input_title = "Langers Tropical Juice"
        test_input_description = "Valid Only Friday September 15, 201764-oz. Selected varieties. Club Price: $1.67 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Langers Tropical Juice 64 oz"

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

    def test_refreshe_Soda_Seltzer(self):

        # Input and expected result.
        test_input_title = "refreshe Soda, Seltzer"
        test_input_description = "12-pack, 12-oz. cansSelected varieties. Plus deposit in Oregon.WHEN YOU BUY 3"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Refreshe Soda Seltzer 12 pack 12 oz cans"

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

    def test_Pepsi(self):

        # Input and expected result.
        test_input_title = "Pepsi"
        test_input_description = "Valid Only Friday September 15, 20172-liter bottles.Selected varieties.Club Price: $1.00 ea.Plus depositin Oregon."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepsi 2 liter bottles"

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

    def test_7_UP(self):

        # Input and expected result.
        test_input_title = "7 UP"
        test_input_description = "Valid Only Friday September 15, 201724-pack, 12-oz. Selected varieties.Plus deposit in Oregon."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "7up 24 pack 12 oz"

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

    def test_Snapple(self):

        # Input and expected result.
        test_input_title = "Snapple"
        test_input_description = "Valid Only Friday September 15, 201764-oz. bottles.Selected varieties.Club Price: $1.67 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Snapple 64 oz bottles"

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

    def test_Kelloggs_Eggo_Waffles(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Eggo Waffles"
        test_input_description = "Valid Only Friday September 15, 201724-ct.Selected varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Eggo Waffles 24 ct"

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

    def test_Tillamook_Chunk_Shredded(self):

        # Input and expected result.
        test_input_title = "Tillamook Chunk, Shredded"
        test_input_description = "16-oz.Selected varieties.Club Price: $3.00 ea.LOCAL NORTHWEST"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tillamook Chunk Shredded 16 oz Local Northwest"

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

    def test_Tillamook_Sliced_Cheese(self):

        # Input and expected result.
        test_input_title = "Tillamook Sliced Cheese"
        test_input_description = "12-oz. Selected varieties.Club Price: $3.00 ea.LOCAL NORTHWEST"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tillamook Sliced Cheese 12 oz Local Northwest"

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

    def test_Lucerne_Cottage_Cheese_or_Sour_Cream(self):

        # Input and expected result.
        test_input_title = "Lucerne Cottage Cheese or Sour Cream"
        test_input_description = "16-oz. Selected varieties.Club Price: $1.50 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lucerne Cottage Cheese or Sour Cream 16 oz"

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

    def test_Lucerne_Cream_Cheese(self):

        # Input and expected result.
        test_input_title = "Lucerne Cream Cheese"
        test_input_description = "8-oz. Selected varieties.Club Price: $1.25 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lucerne Cream Cheese 8 oz"

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

    def test_Lucerne_Low_Fat_Yogurt(self):

        # Input and expected result.
        test_input_title = "Lucerne Low Fat Yogurt"
        test_input_description = "6-oz. Selected varieties.Club Price: 25¢ ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lucerne Low Fat Yogurt 6 oz"

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

    def test_Foster_Farms_Pancake_on_a_Stick(self):

        # Input and expected result.
        test_input_title = "Foster Farms Pancake on a Stick"
        test_input_description = "Valid Only Friday September 15, 201732.04-oz.Selected varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Foster Farms Pancake on A Stick 32.04 oz"

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

    def test_Ice_Cream_Sale(self):

        # Input and expected result.
        test_input_title = "Ice Cream Sale"
        test_input_description = "Selected sizes and varieties."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ice Cream"

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

    def test_Signature_Kitchens_Calrose_Rice(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Calrose Rice"
        test_input_description = "Valid Only Friday September 15, 20175-lb.Selected varieties.Plus deposit in Oregon."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Calrose Rice 5 lb"

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

    def test_O_Organics_Grass_Fed_Ground_Beef_or_Patties(self):

        # Input and expected result.
        test_input_title = "O Organics Grass Fed Ground Beef or Patties"
        test_input_description = "16-oz. 85% Lean.No hormones added."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "O Organics Grass Fed Ground Beef or Patties 16 oz"

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

    def test_Oscar_Mayer_Carving_Board_Deli_Fresh_or_Selects_Lunchmeat(self):

        # Input and expected result.
        test_input_title = "Oscar Mayer Carving Board, Deli Fresh or Selects Lunchmeat"
        test_input_description = "7 to 9-oz.Selected varieties.Club Price: $3.00 ea.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Oscar Mayer Carving Board Deli Fresh or Selects Lunchmeat 7 to 9 oz"

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

    def test_Kelloggs_Cereal_Signature_Kitchens_Instant_Oatmeal(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Cereal, Signature Kitchens Instant Oatmeal..."
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17Kellogg’s Cereal 8.7 to 13.7-oz.,Signature Kitchens InstantOatmeal 11.85 to 13.76-oz., CanisterOats 18-oz., Granola, Chewy,Crunchy Bars 6 to 12-ct. or ToasterPastries 11-oz. Selected varieties.$1.79 EA. Club Price Limit 3This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs cereal Signature Kitchens instant Oatmeal. Kelloggs cereal 8.7 to 13.7 ozSignature Kitchens instantoatmeal 11.85 to 13.76 oz canisteroats 18 oz Granola Chewycrunchy Bars 6 to 12 ct or Toasterpastries 11 oz"

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

    def test_Value_Corner_Milk_or_Tropicana_Orange_Juice(self):

        # Input and expected result.
        test_input_title = "Value Corner Milk or Tropicana Orange Juice"
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17Value Corner Milk Gallonor Tropicana Orange Juice59-oz. Selected varieties.$1.99 EA. Club Price Limit 2This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Value Corner Milk or Tropicana Orange Juice Value Corner Milk gallonor Tropicana Orange Juice59 oz"

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

    def test_Nabisco_Snack_Crackers(self):

        # Input and expected result.
        test_input_title = "Nabisco Snack Crackers"
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17NabiscoSnack Crackers3.5 to 9.1-oz.Selected varieties.$1.79 EA. Club Price Limit 4This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nabisco Snack Crackers 3.5 to 9.1 oz"

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

    def test_USDA_Choice_Beef_Loin_New_York_Strip_Steak(self):

        # Input and expected result.
        test_input_title = "USDA Choice Beef Loin New York Strip Steak"
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17USDA Choice Beef LoinNew York Strip SteakBone-in. Value Pack.$4.97 LB. Club Price Limit 2 Pkgs.This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Beef Loin New York Strip Steak Bone-In."

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

    def test_Fresh_Ground_Beef(self):

        # Input and expected result.
        test_input_title = "Fresh Ground Beef"
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17Fresh Ground Beef93% Lean.$2.99 LB. Club Price Limit 2 Pks.This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17.VALUE PACK"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Ground Beef"

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

    def test_Signature_Farms_Bacon(self):

        # Input and expected result.
        test_input_title = "Signature Farms Bacon"
        test_input_description = "clip or CLICK! Just for u. Valid Thru 9/19/17Signature Farms BaconSold in a 3-lb. package.Only $11.97 ea.$3.99 LB. Club Price Limit 3 Pks.This coupon must be presented at time of purchase. Offer valid with Card and Coupon.COUPON CANNOT BE DOUBLED or combined with digital coupon. Coupon valid thru 9/19/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Farms Bacon 3 lb package"

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

    def test_Kelloggs_Fruit_Snacks_Rice_Krispies_Treats(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Fruit Snacks, Rice Krispies Treats"
        test_input_description = "8 to 10-ct.Selected varieties.BUY 4& SAVE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Fruit Snacks Rice Krispies Treats 8 to 10 ct"

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

    def test_Kelloggs_Special_K_Cereal(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Special K Cereal"
        test_input_description = "10.8 to 13.1-oz.Selected varieties.BUY 4& SAVE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Special K cereal 10.8 to 13.1 oz"

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

    def test_Gatorade(self):

        # Input and expected result.
        test_input_title = "Gatorade"
        test_input_description = "32-oz. bottlesSelected varieties.Plus deposit in Oregon.BUY 4& SAVE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gatorade 32 oz bottles"

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

    def test_Lays_Potato_Chips(self):

        # Input and expected result.
        test_input_title = "Lay’s Potato Chips"
        test_input_description = "9.5 to 10.25-oz.Selected varieties.Club Price: $3.00 ea.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lays Potato Chips 9.5 to 10.25 oz"

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

    def test_Smartfood_Popcorn(self):

        # Input and expected result.
        test_input_title = "Smartfood Popcorn"
        test_input_description = "4.5 to 10.5-oz.Selected varieties.Club Price: $3.00 ea.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Smartfood Popcorn 4.5 to 10.5 oz"

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

    def test_Snapple(self):

        # Input and expected result.
        test_input_title = "Snapple"
        test_input_description = "6-pack, 16-oz. bottles.Selected varieties.Club Price: $3.50 ea.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Snapple 6 pack 16 oz bottles"

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

    def test_Nabisco_Variety_Snack_Packs(self):

        # Input and expected result.
        test_input_title = "Nabisco Variety Snack Packs"
        test_input_description = "12 to 18-pack.Selected varieties.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nabisco Variety Snack packs 12 to 18 pack"

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

    def test_Gatorade(self):

        # Input and expected result.
        test_input_title = "Gatorade"
        test_input_description = "BUY 2 Gatorade 8-pack, 20-oz. bottles. Selected varieties. GET 5 FREE Propel 24-oz. bottles. Selected varieties.Plus deposit in Oregon.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gatorade 8 pack 20 oz bottles"

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

    def test_Open_Nature_Grass_Fed_Ground_Beef_or_Patties(self):

        # Input and expected result.
        test_input_title = "Open Nature Grass Fed Ground Beef or Patties"
        test_input_description = "16-oz. 85% Lean.Antibiotic free."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Open Nature Grass Fed Ground Beef or Patties 16 oz"

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

    def test_Open_Nature_Boneless_Skinless_Chicken_Breasts(self):

        # Input and expected result.
        test_input_title = "Open Nature Boneless Skinless Chicken Breasts"
        test_input_description = "No hormones.VALUE PACK"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Open Nature Boneless Skinless Chicken Breasts"

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

    def test_CAPTAIN_UNDERPANTS_THE_FIRST_EPIC_MOVIE(self):

        # Input and expected result.
        test_input_title = "CAPTAIN UNDERPANTS THE FIRST EPIC MOVIE"
        test_input_description = "CAPTAIN UNDERPANTS THE FIRST EPIC MOVIE $20.99 EA. BLU-RAY OR $17.99 EA. DVD AND GET FREE OFFER VALID 9/12/17-9/26/17 ONE (1) Trolli SourBrite Crawlers Originalor Bites Assorted,7.25 - 9oz. Standup Bag 2017 Ferrara Candy Company *Participating items must be purchased in a single transaction with Club Card . Limit one Blu-ray Combo Pack or DVD per transaction. Discount taken at the register. Not all varietiesavailable in all stores. Customer pays tax and CRV where applicable. Online and in-store prices, offers and discounts may differ. 2017 DreamWorks Animation LLC. All Rights Reserved.TWENTIETH CENTURY FOX, FOX and associated logos are trademarks of Twentieth Century Fox Film Corporation and its related entities."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Captain Underpants the First Epic Movie Blu-Ray or DVD"

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

    def test_THE_MUMMY_2017(self):

        # Input and expected result.
        test_input_title = "THE MUMMY [2017]"
        test_input_description = "THE MUMMY $19.99 EA. BLU-RAY OR $16.99 EA. DVD OWN IT ON SEPTEMBER 12 2017 UNIVERSAL PICTURES HOME ENTERTAINMENT."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "The Mummy 2017 the Mummy Blu-Ray or DVD Universal Pictures Home Entertainment."

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

    def test_Gala_Apples(self):

        # Input and expected result.
        test_input_title = "Gala Apples"
        test_input_description = "LOCAL NORTHWEST GROWN"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gala Apples Local Northwest"

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

    def test_Large_Yellow_Peaches(self):

        # Input and expected result.
        test_input_title = "Large Yellow Peaches"
        test_input_description = "LOCAL NORTHWEST GROWN"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Large Yellow Peaches Local Northwest"

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

    def test_Large_Navels_Minneola_Tangelos_or_Cara_Cara_Oranges(self):

        # Input and expected result.
        test_input_title = "Large Navels, Minneola Tangelos or Cara Cara Oranges"
        test_input_description = "Large Navels,MinneolaTangelos or CaraCara Oranges"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Large Navels Minneola Tangelos or Cara Cara Oranges"

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

    def test_Tomatoes_on_the_Vine(self):

        # Input and expected result.
        test_input_title = "Tomatoes on the Vine"
        test_input_description = "Tomatoeson the Vine"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tomatoes on the Vine"

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

    def test_Fall_Poms(self):

        # Input and expected result.
        test_input_title = "Fall Poms"
        test_input_description = "9-stem bunches inbeautiful Fall colors."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fall Poms 9 stem bunches"

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

    def test_Classic_Cake_Fest(self):

        # Input and expected result.
        test_input_title = "Classic Cake Fest"
        test_input_description = "8-inch. Single layer.Selected varieties.SCORE BIG"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Classic Cake Fest 8 inch Single Layer."

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

    def test_Oven_Baked_Jumbo_Cookies(self):

        # Input and expected result.
        test_input_title = "Oven Baked Jumbo Cookies"
        test_input_description = "12-ct."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Oven Baked Jumbo Cookies 12 ct"

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

    def test_Glazed_Cinnamon_Twirl(self):

        # Input and expected result.
        test_input_title = "Glazed Cinnamon Twirl"
        test_input_description = "8-ct. Delicious servedwarm."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Glazed Cinnamon Twirl 8 ct"

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

    def test_Signature_SELECT_Oven_Baked_French_Bread(self):

        # Input and expected result.
        test_input_title = "Signature SELECT Oven Baked French Bread"
        test_input_description = "16-oz. Hot at 4 p.m.Selected varieties.Club Price: $2.00 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Select Oven Baked French Bread 16 oz"

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

    def test_Signature_Kitchens_Breakfast_Breads(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Breakfast Breads"
        test_input_description = "16 to 22-oz.Selected varieties.Club Price: $1.50 ea.LOCAL NORTHWEST"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Breakfast Breads 16 to 22 oz Local Northwest"

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

    def test_Signature_Cafe_Green_Salads(self):

        # Input and expected result.
        test_input_title = "Signature Cafe Green Salads"
        test_input_description = "9.5 to 10.75-oz.Selected varieties.Single Price: $4.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Cafe Green Salads 9.5 to 10.75 oz"

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

    def test_Shanghai_Meal(self):

        # Input and expected result.
        test_input_title = "Shanghai Meal"
        test_input_description = "Your choice of2 Entrées, Rice orLo Mein and 3 PotStickers or 2 Egg Rolls.Introducing Salt and Pepper Calamari"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shanghai Meal Your Choice Of2 Entrees Rice Orlo Mein and 3 Potstickers or 2 Egg rollsIntroducing Salt and Pepper Calamari"

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

    def test_Taylor_Farms_Meals(self):

        # Input and expected result.
        test_input_title = "Taylor Farms Meals"
        test_input_description = "12 to 16-oz.Selected vareities.Single Price: $6.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Taylor Farms Meals 12 to 16 oz"

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

    def test_Ozarka_Spring_Water_33_8_oz__Sparkling_Water_or_refreshe_Mixers_1_Liter(self):

        # Input and expected result.
        test_input_title = "Ozarka Spring Water 33.8 oz., Sparkling Water or refreshe™ Mixers 1 Liter"
        test_input_description = "Select Varieties. cash in your quarters"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ozarka Spring Water 33.8 oz Sparkling Water or Refreshe Mixers 1 liter"

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

    def test_Refreshe_Sodas(self):

        # Input and expected result.
        test_input_title = "Refreshe Sodas"
        test_input_description = "2 Liters, Select Varieties. cash in your quarters"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Refreshe Sodas 2 liters"

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

    def test_Fresh_Whole_Atlantic_Salmon_Fillets(self):

        # Input and expected result.
        test_input_title = "Fresh Whole Atlantic Salmon Fillets"
        test_input_description = "Half or Seasoned Fillets $7.99 lb. Savour The Sea!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Whole Atlantic Salmon Fillets Half or Seasoned Fillets"

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

    def test_Fresh_Atlantic_Salmon_Portions_5_oz__or_Alaskan_Sockeye_Salmon_Fillets(self):

        # Input and expected result.
        test_input_title = "Fresh Atlantic Salmon Portions 5 oz. or Alaskan Sockeye Salmon Fillets"
        test_input_description = "Frozen $9.99 lb. Wild Caught. Savour The Sea!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Atlantic Salmon Portions 5 oz or Alaskan Sockeye Salmon Fillets frozen"

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

    def test_Franzia_5_ltr__or_Meiomi_Chardonnay_750_ml_(self):

        # Input and expected result.
        test_input_title = "Franzia 5 ltr. or Meiomi Chardonnay 750 ml."
        test_input_description = "Select Varietals $16.99-10% OFF"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Franzia 5 ltr or Meiomi Chardonnay 750 ml"

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

    def test_La_Crema_or_Rodney_Strong(self):

        # Input and expected result.
        test_input_title = "La Crema or Rodney Strong"
        test_input_description = "750 ml., Select Varietals $14.99-10% OFF"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "La Crema or Rodney Strong 750 ml"

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

    def test_Large_Size_Cauliflowerr(self):

        # Input and expected result.
        test_input_title = "Large Size Cauliflowerr"
        test_input_description = "Fresh Picked BUY 4 OR MORE & SAVE FAB!4 SALE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Large Size Cauliflowerr Fresh"

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

    def test_General_Mills_Cereals(self):

        # Input and expected result.
        test_input_title = "General Mills Cereals"
        test_input_description = "8.9-14 oz., Select Varieties BUY 4 OR MORE & SAVE FAB!4 SALE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "General Mills cereals 8.9-14 oz"

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

    def test_Kraft_Velveeta_Skillets(self):

        # Input and expected result.
        test_input_title = "Kraft Velveeta Skillets"
        test_input_description = "11.3-15.66 oz., Select Varieties. SAVINGS DOWN EVERY AISLE!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kraft Velveeta Skillets 11.3 oz"

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

    def test_Kelloggs_Cereals(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Cereals"
        test_input_description = "9.3-15 oz., Select Varieties. SAVINGS DOWN EVERY AISLE!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs cereals 9.3-15 oz"

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

    def test_Signature_Kitchens_Apple_Juice(self):

        # Input and expected result.
        test_input_title = "Signature™ Kitchens Apple Juice"
        test_input_description = "$5 Blue Friday PRICES IN THIS SECTION VALID FRIDAY SEPTEMBER 22ND ONLY! 64 oz  Selected Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Apple Juice 64 oz"

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

    def test_Snapple_Tea(self):

        # Input and expected result.
        test_input_title = "Snapple Tea"
        test_input_description = "$5 Blue Friday PRICES IN THIS SECTION VALID FRIDAY SEPTEMBER 22ND ONLY! 64 oz  Selected Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Snapple Tea 64 oz"

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

    def test_Signature_Kitchens_Apple_Sauce_Cups(self):

        # Input and expected result.
        test_input_title = "Signature™ Kitchens Apple Sauce Cups"
        test_input_description = "$5 Blue Friday PRICES IN THIS SECTION VALID FRIDAY SEPTEMBER 22ND ONLY! 6-pk  4 oz  Selected Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Apple Sauce Cups 6 pk 4 oz"

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

    def test_Lancaster_Brand_or_Perdue_Boneless_Chicken_Breasts_or_Thighs(self):

        # Input and expected result.
        test_input_title = "Lancaster Brand or Perdue Boneless Chicken Breasts or Thighs"
        test_input_description = "does not include bulk boneless breasts Lancaster® BRAND PERDUE®"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lancaster Brand or Perdue Boneless Chicken Breasts or Thighs Does Not include Bulk Boneless Breasts Lancaster Brand Perdue"

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

    def test_Kelloggs__Frosted_Flakes_10_5_oz_pkg_Rice_or_Cocoa_Krispies(self):

        # Input and expected result.
        test_input_title = "Kellogg’s  Frosted Flakes 10.5 oz. pkg.  Rice or Cocoa Krispies 9-11 oz. pkg.  Corn Pops, Froot Loops or Apple Jacks 8.7-9.2 oz. pkg.  Frosted or Bite Size Mini Wheats 15.2-18 oz. pkg."
        test_input_description = "Individual Price 2 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Frosted flakes 10.5 oz pkg Rice or Cocoa Krispies 9-11 oz pkg Corn Pops Froot Loops or Apple Jacks 8.7-9.2 oz pkg Frosted or Bite Size Mini Wheats 15.2-18 oz pkg"

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

    def test_Kelloggs_Corn_Flakes_12_oz__pkg__Raisin_Bran_Strawberry(self):

        # Input and expected result.
        test_input_title = "Kellogg’s  Corn Flakes 12 oz. pkg.  Raisin Bran Strawberry, Raspberry, Cranberry or Omega 3 13.5-15 oz. pkg.  Raisin Bran or Raisin Bran Crunch 18.2-18.7 oz. pkg."
        test_input_description = "Individual Price 2 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Corn flakes 12 oz pkg Raisin Bran Strawberry Raspberry Cranberry or Omega 3 13.5-15 oz pkg Raisin Bran or Raisin Bran Crunch 18.2-18.7 oz pkg"

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

    def test_Kelloggs_PopTarts(self):

        # Input and expected result.
        test_input_title = "Kellogg’s PopTarts"
        test_input_description = "14-14.7 oz. pkg. Individual Price 2 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Poptarts 14-14.7 oz pkg"

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

    def test_Keebler_Fudge_Shoppe_813_6_oz_pkg_Chips_Deluxe(self):

        # Input and expected result.
        test_input_title = "Keebler  Fudge Shoppe 8-13.6 oz. pkg.  Chips Deluxe 10-14.8 oz. pkg.  Sandies 11.2-11.3 oz. pkg."
        test_input_description = "Individual Price 2 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Keebler Fudge Shoppe 8-13.6 oz pkg Chips Deluxe 10-14.8 oz pkg Sandies 11.2-11.3 oz pkg"

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

    def test_Keebler_Famous_Amos(self):

        # Input and expected result.
        test_input_title = "Keebler Famous Amos"
        test_input_description = "12.4 oz. pkg. Individual Price 2 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Keebler Famous Amos 12.4 oz pkg"

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

    def test_Coke_Diet_Coke_or_Sprite(self):

        # Input and expected result.
        test_input_title = "Coke, Diet Coke or Sprite"
        test_input_description = "12-pk., 12 fl. oz. cans Limit 1 offer Plus deposit where required Individual Price $6.49 ea. 4 for $9.98 WHEN YOU BUY 4 with coupon on pg. 4 and an additional $25 purchase"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke Diet Coke or Sprite 12 pk 12 fl oz cans"

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

    def test_San_Giorgio_Pasta(self):

        # Input and expected result.
        test_input_title = "San Giorgio Pasta"
        test_input_description = "12-16 oz. pkg. excludes lasagna, tri-color, oven ready, jumbo shells, pot pie squares, whole grain, super greens, organic & gluten free"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "San Giorgio Pasta 12-16 oz pkg Excludes Lasagna Tri-Color Jumbo Shells Pot Pie squares Whole Grain Super Greens Organic & Gluten Free"

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

    def test_Pepperidge_Farm_Gold_Fish(self):

        # Input and expected result.
        test_input_title = "Pepperidge Farm Gold Fish"
        test_input_description = "SAVE $5 INSTANTLY when you buy $20 worth of any of these participating Campbell’s, Pepperidge Farm, V8 or Swanson products in a single transaction 9/15/17-9/21/17 6.6-8 oz. pkg. xtreme value!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepperidge Farm Gold Fish 6.6-8 oz pkg"

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

    def test_Campbells_Chunky_Soup(self):

        # Input and expected result.
        test_input_title = "Campbell’s Chunky Soup"
        test_input_description = "SAVE $5 INSTANTLY when you buy $20 worth of any of these participating Campbell’s, Pepperidge Farm, V8 or Swanson products in a single transaction 9/15/17-9/21/17 15.25-18.8 oz. cans or bowls"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Campbells Chunky Soup 15.25-18.8 oz cans or bowls"

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

    def test_Adult_Tickets(self):

        # Input and expected result.
        test_input_title = "Adult Tickets"
        test_input_description = "BUY 1 Monster Energy Drink 4-pk., 16 fl. oz. cans GET 2 FREE* Adult Tickets to the Monster Energy NASCAR Cup Series Playoff Race on October 1st at Dover International Speedway *Does not include $8 per ticket processing fee. Purchase must be made in a single transaction. Coupon prints at register. Offer valid thru 9/21/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Adult Tickets"

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

    def test_Habbersett_or_Rapa_Scrapple_or_Smithfield_Breakfast_Sausage(self):

        # Input and expected result.
        test_input_title = "Habbersett or Rapa Scrapple or Smithfield Breakfast Sausage"
        test_input_description = "BUY 1 of these* Lancaster Brand Sliced Bacon 16 oz. pkg. and GET 1 of these Habbersett or Rapa Scrapple 16 oz. pkg. or Smithfield Breakfast Sausage 12 oz. pkg., links or patties FOR $1 (Save up to $1.99) *Limit 1 offer. Purchase must be made in a single transaction"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Habbersett or Rapa Scrapple or Smithfield Breakfast Sausage"

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

    def test_Perdue_Chicken__Fully_Cooked_Nuggets_or_Cutlets_1012_oz__pkg___Short_Cuts_89_oz__pkg_(self):

        # Input and expected result.
        test_input_title = "Perdue Chicken  Fully Cooked Nuggets or Cutlets 10-12 oz. pkg.  Short Cuts 8-9 oz. pkg."
        test_input_description = "Identical item only"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Perdue Chicken Nuggets or Cutlets 10-12 oz pkg Short Cuts 8-9 oz pkg"

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

    def test_Lancaster_Brand_U_S_D_A__CHOICE_Beef_Boneless_Shoulder_or_Chuck_Roast(self):

        # Input and expected result.
        test_input_title = "Lancaster Brand U.S.D.A. CHOICE Beef Boneless Shoulder or Chuck Roast"
        test_input_description = "cut fresh in store daily! crockpot DINNER IDEAS Lancaster® BRAND PREMIUM BEEF U.S.D.A. CHOICE. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lancaster Brand Beef Boneless Shoulder or Chuck Roast"

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

    def test_Broccoli_Crunch_Salad(self):

        # Input and expected result.
        test_input_title = "Broccoli Crunch Salad"
        test_input_description = "Try one of our fresh salads!. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Broccoli Crunch Salad"

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

    def test_Fresh_Summer_Salad(self):

        # Input and expected result.
        test_input_title = "Fresh Summer Salad"
        test_input_description = "Try one of our fresh salads!. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Summer Salad"

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

    def test_Dannon__Oikos_Triple_Zero_Crunch_or_Drinks__Light_u0026_Fit_Regular_or_Light_u0026_Fit_Greek_with_Zero_Artificial_Sweeteners_single_serve_cups(self):

        # Input and expected result.
        test_input_title = "Dannon  Oikos Triple Zero, Crunch or Drinks  Light \u0026 Fit Regular or Light \u0026 Fit Greek with Zero Artificial Sweeteners single serve cups"
        test_input_description = "55.3 oz. cups, 7 fl. oz. drinks ©2017 The Dannon Company, Inc. ©2017 WhiteWave Services, Inc. All rights reserved. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dannon Oikos Triple Zero Crunch or Drinks Light Fit Fit Greek with Zero Artificial Sweeteners Single Serve Cups 55.3 oz Cups 7 fl oz Drinks"

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

    def test_Dannon__Light_u0026_Fit_with_Zero_Artificial_Sweeteners__Activia_or_YoCrunch_4packs__Danimals_6packs_21_2_oz__pk__18_6_fl__oz__pk_(self):

        # Input and expected result.
        test_input_title = "Dannon  Light \u0026 Fit with Zero Artificial Sweeteners  Activia or YoCrunch 4-packs  Danimals 6-packs 21.2 oz. pk., 18.6 fl. oz. pk."
        test_input_description = "©2017 The Dannon Company, Inc. ©2017 WhiteWave Services, Inc. All rights reserved. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dannon Light Fit with Zero Artificial Sweeteners Activia or Yocrunch 4 packs Danimals 6 packs 21.2 oz pk 18.6 fl oz pk"

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

    def test_SToK_ColdBrew_Coffee_or_International_Delight_Coffee_Creamers(self):

        # Input and expected result.
        test_input_title = "SToK Cold-Brew Coffee or International Delight Coffee Creamers"
        test_input_description = "48 fl. oz ©2017 The Dannon Company, Inc. ©2017 WhiteWave Services, Inc. All rights reserved. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stok Cold-Brew Coffee or international Delight Coffee Creamers 48 fl oz"

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

    def test_utz_Pretzels_16_oz__bag__Tortilla_Chips_9_512_oz_(self):

        # Input and expected result.
        test_input_title = "utz  Pretzels 16 oz. bag  Tortilla Chips 9.5-12 oz."
        test_input_description = "excluding multi grain or dipping tortilla. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Utz pretzels 16 oz bag Tortilla Chips 9.5-12 oz Excluding Multi Grain or Dipping Tortilla."

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

    def test_Nature_Made_Vitamins(self):

        # Input and expected result.
        test_input_title = "Nature Made Vitamins"
        test_input_description = "30-300 ct. pkg. Must Buy Identical Item. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature Made Vitamins 30-300 ct pkg"

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

    def test_Kleenex_Facial_Tissues(self):

        # Input and expected result.
        test_input_title = "Kleenex Facial Tissues"
        test_input_description = "68-160 ct. pkg. PRICE AFTER MyMixx DIGITAL COUPON SAVINGS. CLIP AND REDEEM BY 9/21/17 ADDITIONAL QUANTITIES OR PRICE WITHOUT MyMixx DIGITAL COUPON SAVINGS: 4 FOR $5 DOWNLOAD EXTRA SAVINGS. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kleenex Facial Tissues 68-160 ct pkg"

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

    def test_Country_Charm_Bouquet(self):

        # Input and expected result.
        test_input_title = "Country Charm Bouquet"
        test_input_description = "making beautiful flowers part of your life. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Country Charm Bouquet Making Beautiful flowers Part of Your Life."

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

    def test_Boars_Head_OvenGold_Turkey_Breast(self):

        # Input and expected result.
        test_input_title = "Boar’s Head OvenGold Turkey Breast"
        test_input_description = "$7.99 lb. with additional $25 purchase redeemable only at: ACME® Coupon cannot be doubled, tripled, quadrupled or exchanged for cash or combined with any other offer. Void if copied or transferred. In the event of return, coupon savings may be deducted from refund. Not valid toward previous purchase. Items may not be available in all locations. This coupon valid at ACME locations. Limit one offer per coupon. XTRA coupon savings! Boar’s Head® STORE COUPON VALID 9/15/17-9/21/17"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boars Head Ovengold Turkey Breast"

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

    def test_Del_Monte_Gold_Pineapple(self):

        # Input and expected result.
        test_input_title = "Del Monte Gold Pineapple"
        test_input_description = "$1.48 with additional $25 purchase redeemable only at: ACME® Coupon cannot be doubled, tripled, quadrupled or exchanged for cash or combined with any other offer. Void if copied or transferred. In the event of return, coupon savings may be deducted from refund. Not valid toward previous purchase. Items may not be available in all locations. This coupon valid at ACME locations. Limit one offer per coupon. XTRA coupon savings! STORE COUPON VALID 9/15/17-9/21/17"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Del Monte Gold Pineapple"

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

    def test_30_Off_Boneless_Beef_Roast_Sale(self):

        # Input and expected result.
        test_input_title = "30% Off Boneless Beef Roast Sale!"
        test_input_description = "Bottom Round, Top Round, Shoulder, Chuck or Sirloin Tip Roast(Sold As Roast Only) (Excluding Ribeye Roast) USDACHOICEBEEF Prices on package reflects Sale Retail Certified Angus beef Regular Retails: $4.99 lb. to $7.19 lb."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boneless Beef Roast Bottom Round Top Round Shoulder Chuck or Sirloin Tip Roast Excluding Ribeye Roast Beef Certified Angus Beef"

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

    def test_40_Off_Perdue_Poultry(self):

        # Input and expected result.
        test_input_title = "40% Off Perdue Poultry"
        test_input_description = "(Excluding Rotisserie, Family Pack Ground Turkey,Family Pack Short Cuts, IQF Wings, IQF Boneless Breast,IQF Tenders, Frozen Cornish Hens, Fresh Air ChilledPoultry, Simply Smart Ground Chicken) Prices on package reflects Sale Retail U.S.D.A GRADE A Regular Retail: $1.49 lb. to $10.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Perdue Poultry Excluding Rotisserie Family pack Ground Turkey Family pack Short Cuts IQF Wings IQF Boneless Breast IQF Tenders frozen Cornish Hens Fresh Air Chilledpoultry Simply Smart Ground Chicken U.S.D.A Grade A"

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

    def test_Hotel_Style_Turkey_Breast(self):

        # Input and expected result.
        test_input_title = "Hotel Style Turkey Breast"
        test_input_description = "Frozen, with Wings U.S.D.A GRADE A"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hotel Style Turkey Breast frozen with Wings U.S.D.A Grade A"

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

    def test_Boneless_Center_Cut_Pork_Chops(self):

        # Input and expected result.
        test_input_title = "Boneless Center Cut Pork Chops"
        test_input_description = "Family Pack, Pork Loin, Regular or Tender Choice"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boneless Center Cut Pork Chops Family pack Pork Loin Regular or Tender Choice"

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

    def test_Cooks_BoneIn_Ham_Steak(self):

        # Input and expected result.
        test_input_title = "Cook’s Bone-In Ham Steak"
        test_input_description = "Smoked (Excluding Thick Cut & Flavored Steaks)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Cooks Bone-In Ham Steak Smoked Excluding Thick Cut & flavored Steaks"

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

    def test_Shoprite_Ground_Turkey(self):

        # Input and expected result.
        test_input_title = "Shoprite Ground Turkey"
        test_input_description = "Fresh, 93% Lean"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Ground Turkey Fresh"

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

    def test_Red_Green_or_Black_Seedless_Grapes(self):

        # Input and expected result.
        test_input_title = "Red, Green or Black Seedless Grapes"
        test_input_description = "Fresh ShopRiteSale Price: $1.79 LB. -30¢ LB. Limit 5-lbs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Red Green or Black Seedless Grapes Fresh"

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

    def test_Bartlett_Pears(self):

        # Input and expected result.
        test_input_title = "Bartlett Pears"
        test_input_description = "Sweet, Bosc"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bartlett Pears Sweet Bosc"

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

    def test_Broccoli_Crowns(self):

        # Input and expected result.
        test_input_title = "Broccoli Crowns"
        test_input_description = "Ready to Dip or Cook"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Broccoli Crowns"

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

    def test_Tree_Ripe_Peaches(self):

        # Input and expected result.
        test_input_title = "Tree Ripe Peaches"
        test_input_description = "Sweet & Juicy"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tree Ripe Peaches Sweet & Juicy"

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
        test_input_description = "11.1 to 12.2-oz. box (Excluding Chocolate)Cinnamon or Apple Cinnamon Toast Crunch,8.9-oz. Original Cheerios, 11.8-oz. Original Cocoa Puffs,10.7-oz. Trix or 12-oz. Golden Grahams Limit 4Per Variety SAVE UP TO $1.71, 50¢ OFF 2 With digital coupon at shoprite.com Must Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "General Mills cereal 11.1 to 12.2 oz box Excluding Chocolate Cinnamon or Apple Cinnamon Toast Crunch8.9 oz Original Cheerios 11.8 oz Original Cocoa Puffs10.7 oz Trix or 12 oz Golden Grahams"

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

    def test_Nature_Valley_Granola_Bars(self):

        # Input and expected result.
        test_input_title = "Nature Valley Granola Bars"
        test_input_description = "6.7 to 8..98-oz. box (Excluding Protein Bars& Seasonal) Any Variety Limit 4Per Variety save up to $1.71, 50¢ OFF 2 With digital coupon at shoprite.com Must Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature Valley Granola Bars 6.7 to 8.98 oz box Excluding protein Bars & Seasonal"

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

    def test_ShopRite_Coffee_K_Cups(self):

        # Input and expected result.
        test_input_title = "ShopRite Coffee K Cups"
        test_input_description = "5.63-oz. box, 18-ct.,Any Variety LESS THAN 27¢ per cup Limit 4 Per Variety you save $1.22"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Coffee K Cups 5.63 oz box 18 ct"

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

    def test_Dannon_Greek_Yogurt(self):

        # Input and expected result.
        test_input_title = "Dannon Greek Yogurt"
        test_input_description = "6-oz., Horizon Organic Yogurt or 7-oz. cont., Oikos or Light &Fit Drinks, 5 to 5.3-oz. cont., Crunch Greek, Any Variety, Oikos,Light & Fit Greek, Mousse, Triple Zero, Light & Fit Zero Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dannon Greek Yogurt 6 oz Horizon Organic Yogurt or 7 oz cont Oikos or Light & Fit Drinks 5 to 5.3 oz cont Crunch Greek Oikos Light & Fit Greek Mousse Triple Zero Light & Fit Zero"

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

    def test_International_Delight_Creamer(self):

        # Input and expected result.
        test_input_title = "International Delight Creamer"
        test_input_description = "BUY 10, 6-oz., Horizon Organic Yogurt or 7-oz. cont., Oikos or Light &Fit Drinks, 5 to 5.3-oz. cont., Crunch Greek, Any Variety, Oikos,Light & Fit Greek, Mousse, Triple Zero, Light & Fit Zero orDannon Greek Yogurt 10 for $10 Limit 4Per Variety and... GET1, 32-oz. cont., Any Variety, Dunkin Donuts Coffee Creamers orInternational Delight Creamer Limit 4 Offers FREE with Price Plus Card YOU SAVE $3.89"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "International Delight Creamer"

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

    def test_Floridas_Natural_Premium_Juice(self):

        # Input and expected result.
        test_input_title = "Florida’s Natural Premium Juice"
        test_input_description = "59-fl. oz. cont., No Pulp or withCalcium Fit & Delicious Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Floridas Natural premium Juice 59 fl oz cont No Pulp or with Calcium"

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

    def test_Land_O_Lakes_Large_Brown_Eggs(self):

        # Input and expected result.
        test_input_title = "Land O Lakes Large Brown Eggs"
        test_input_description = "Grade A, Dozen Limit 4 YOU SAVE 70¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Land O Lakes Large Brown Eggs Grade A Dozen"

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

    def test_Wholesome_Pantry_Organic_Eggs(self):

        # Input and expected result.
        test_input_title = "Wholesome Pantry Organic Eggs"
        test_input_description = "Dozen Carton, Large, Grade A Limit 4 you save 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Wholesome Pantry Organic Eggs Dozen Carton Large Grade A"

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

    def test_Chock_Full_o_Nuts_Ground_Coffee(self):

        # Input and expected result.
        test_input_title = "Chock Full o’ Nuts Ground Coffee"
        test_input_description = "3.8 to 8.4-oz. box, 12-ct, Any Variety, Hills Brothers, Kauai orChock Full o’ Nuts K-Cups or 23 to 26-oz. can, Any Variety SAVE UP TO $1.91 Limit 4 Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Chock Full O Nuts Ground Coffee 3.8 to 8.4 oz box 12 ct Hills Brothers Kauai or Chock Full O Nuts K-Cups or 23 to 26 oz can"

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

    def test_New_England_Single_Serve_Coffee(self):

        # Input and expected result.
        test_input_title = "New England Single Serve Coffee"
        test_input_description = "4.8-oz. box, 12-ct. (Excluding Seasonal)Any Variety Limit 4 Per Variety SAVE UP TO $1.91"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "New England Single Serve Coffee 4.8 oz box 12 ct Excluding Seasonal"

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

    def test_Eight_O_Clock_Coffee_K_Cups(self):

        # Input and expected result.
        test_input_title = "Eight O’ Clock Coffee K Cups"
        test_input_description = "3.7 to 4.1-oz. box, 12-ct., Any Variety Limit 4 Per Variety SAVE UP TO $1.91"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Eight O Clock Coffee K Cups 3.7 to 4.1 oz box 12 ct"

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

    def test_Post_Honey_Bunches_of_Oats_Cereal(self):

        # Input and expected result.
        test_input_title = "Post Honey Bunches of Oats Cereal"
        test_input_description = "Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $2.99 each. 16.5 to 18-oz. box (Excluding Whole Grain) Family Size,Honey Roasted, Almond or Strawberry Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Post Honey bunches of Oats cereal 16.5 to 18 oz box Excluding Whole Grain Honey Roasted Almond or Strawberry"

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

    def test_Breyers_Ice_Cream(self):

        # Input and expected result.
        test_input_title = "Breyers Ice Cream"
        test_input_description = "48-oz. cont., Any Variety, Carb Smart,Dairy Dessert (Excluding Non Dairy) Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Breyers Ice Cream 48 oz cont Carb Smart Dairy Dessert Excluding Non Dairy"

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

    def test_Friendlys_Ice_Cream(self):

        # Input and expected result.
        test_input_title = "Friendly’s Ice Cream"
        test_input_description = "48-oz. cont., Any Variety, Dairy Dessert(Excluding Naturally) Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Friendlys Ice Cream 48 oz cont Dairy Dessert Excluding Naturally"

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

    def test_Ragu_Pasta_Sauce(self):

        # Input and expected result.
        test_input_title = "Ragu Pasta Sauce"
        test_input_description = "21.5-oz. jar, Any Variety, Cheese or 45-oz. Red Limit 4 Per Variety you save $1.70"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ragu Pasta Sauce 21.5 oz jar Cheese or 45 oz Red"

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

    def test_Ellios_9_Slice_Pizza(self):

        # Input and expected result.
        test_input_title = "Ellio’s 9 Slice Pizza"
        test_input_description = "15.3 to 19.64-oz. pkg., Any Variety Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ellios 9 Slice Pizza 15.3 to 19.64 oz pkg"

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

    def test_ShopRite_Vegetables(self):

        # Input and expected result.
        test_input_title = "ShopRite Vegetables"
        test_input_description = "10 to 12-oz. pkg.,Any Variety, Steam In Bag Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Vegetables 10 to 12 oz pkg"

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

    def test_StarKist_Solid_White_Tuna(self):

        # Input and expected result.
        test_input_title = "StarKist Solid White Tuna"
        test_input_description = "2.6 to 3.28-oz. pouch, Any Variety,Creations, Chunk Light Tuna Salad orRegular or Low Sodium, Chunk LightTuna In Water or 5-oz. can, In Water or Oil Limit 4Per Variety SAVE UP TO 26¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Starkist Solid White Tuna 2.6 to 3.28 oz Pouch Creations Chunk Light Tuna Salad or Regular or Low Sodium Chunk Lighttuna in Water or 5 oz can in Water or Oil"

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

    def test_Angel_Soft_Double_Roll_12_pack(self):

        # Input and expected result.
        test_input_title = "Angel Soft Double Roll 12 pack"
        test_input_description = "Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $4.88 each. 2,904 to 3.168-tot. sht. ct. pkg., Mega Roll6-Pack or Lavender or Pretty Prints Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Angel Soft Double Roll 12 pack 2904 to 3.168 tot sht ct pkg Mega Roll6 pack or Lavender or pretty prints"

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

    def test_Sparkle_Towels_8_pack(self):

        # Input and expected result.
        test_input_title = "Sparkle Towels 8 pack"
        test_input_description = "352 to 546-tot. sht. ct. pkg., Big Roll 6-Pack Limit 4 Offers Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $4.88 each."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Sparkle Towels 8 pack 352 to 546 tot sht ct pkg Big Roll 6 pack"

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

    def test_Black_Bear_American_Cheese(self):

        # Input and expected result.
        test_input_title = "Black Bear American Cheese"
        test_input_description = "Store Sliced, Yellow or White, Premium"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear American Cheese Yellow or White premium"

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

    def test_ShopRite_Turkey_Breast(self):

        # Input and expected result.
        test_input_title = "ShopRite Turkey Breast"
        test_input_description = "Store Sliced, Executive, Honey,Smoked, Buffalo, Lower Sodiumor New York Deli Style"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Turkey Breast Executive Honey Smoked Buffalo Lower Sodium or New York Deli Style"

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

    def test_Purex_Ultra_Laundry_Detergent(self):

        # Input and expected result.
        test_input_title = "Purex Ultra Laundry Detergent"
        test_input_description = "30 to 50-oz. btl.,Any Variety, Liquid Limit 4 Per Variety YOU SAVE $1.30"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Purex Ultra Laundry Detergent 30 to 50 oz btl liquid"

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

    def test_12_Price_Sale_Natures_Bounty_Vitamins(self):

        # Input and expected result.
        test_input_title = "1/2 Price Sale! Nature’s Bounty Vitamins"
        test_input_description = "25 to 350-ct., Assorted Varieties (Excluding While Supplies Last Items) Limit 4 Per Variety Regular Retais: $4.69 to $40.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Natures Bounty Vitamins 25 to 350 ct"

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

    def test_International_Delight_Creamer(self):

        # Input and expected result.
        test_input_title = "International Delight Creamer"
        test_input_description = "BUY 10, 6-oz., Horizon Organic Yogurt or 7-oz. cont., Oikos or Light &Fit Drinks, 5 to 5.3-oz. cont., Crunch Greek, Any Variety, Oikos,Light & Fit Greek, Mousse, Triple Zero, Light & Fit Zero orDannon Greek Yogurt 10 for $10 Limit 4Per Variety and... GET1, 32-oz. cont., Any Variety, Dunkin Donuts Coffee Creamers orInternational Delight Creamer Limit 4 Offers FREE with Price Plus Card YOU SAVE $3.89"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "International Delight Creamer"

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

    def test_Motts_Apple_Juice(self):

        # Input and expected result.
        test_input_title = "Mott’s Apple Juice"
        test_input_description = "1/2-gal. btl., Any Variety, Tots, Plus Limit 4 Offers Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $2.49 each."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Motts Apple Juice 1/2 gal btl tots"

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

    def test_Motts_Clamato_Juice(self):

        # Input and expected result.
        test_input_title = "Mott’s Clamato Juice"
        test_input_description = "1-qt. btl. Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $2.49 each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Motts Clamato Juice 1 qt btl"

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

    def test_Hawaiian_Punch_Fruit_Drink(self):

        # Input and expected result.
        test_input_title = "Hawaiian Punch Fruit Drink"
        test_input_description = "1-gal. btl., Any Variety Discount will be applied when you buy in increments of 3 only.Less or additional items will scan at $2.49 each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hawaiian Punch Fruit Drink 1 gal btl"

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

    def test_Pork_Spare_Ribs(self):

        # Input and expected result.
        test_input_title = "Pork Spare Ribs"
        test_input_description = "4 to 6-lb. Avg., Fresh, Meaty,Breast Bone Removed"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pork Spare Ribs 4 to 6 lb avg"

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

    def test_Lays_Family_Size_Potato_Chips(self):

        # Input and expected result.
        test_input_title = "Lay’s Family Size Potato Chips"
        test_input_description = "9.5 to 10-oz. bag(Excluding Baked) Any Variety1/2 PRICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lays Potato Chips 9.5 to 10 oz bag Excluding Baked"

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

    def test_Canada_Dry_Ginger_Ale_2_Liter(self):

        # Input and expected result.
        test_input_title = "Canada Dry Ginger Ale 2 Liter"
        test_input_description = "btl. (Plus Dep. or Fee Where Req.)A&W, Sunkist, 7-Up, Canada Dry Seltzer Limit 4 Per Variety YOU SAVE 53¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Canada Dry Ginger Ale 2 liter btl A&W Sunkist 7up canada Dry Seltzer"

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

    def test_Pepsi_Bottles_8_pack(self):

        # Input and expected result.
        test_input_title = "Pepsi Bottles 8 pack"
        test_input_description = "96-oz. tot. wt. cans (Plus Dep. or Fee Where Req.) 12-oz. Cans,IZZE or Lemon Lemon 8-Pack, 96-oz. tot. wt. btls., 12-oz. Bottles(Where Available) Mist Twst, Mtn Dew Limit 4Offers MUSTBUY 3Additionalor lesserquantitieswill scan at$5.56 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepsi bottles 8 pack 96 oz tot wt cans 12 oz cans Izze or Lemon Lemon 8 pack 96 oz tot wt btls 12 oz bottles Mist Twst Mtn Dew"

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

    def test_Kingsford_Charcoal(self):

        # Input and expected result.
        test_input_title = "Kingsford Charcoal"
        test_input_description = "11.6-lb. bag, Match Light or15.4-lb. bag, Original Limit 4Per Variety YOU SAVE $4.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kingsford Charcoal 11.6 lb bag Match Light Or15.4 lb bag Original"

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

    def test_Pepsi_Cans_12Pack(self):

        # Input and expected result.
        test_input_title = "Pepsi Cans 12-Pack"
        test_input_description = "144-oz. tot. wt. cans (Plus Dep. or Fee Where Req.)12-oz. Cans, Mist Twst, Mtn Dew Limit 4Offers MUSTBUY 3Additionalor lesserquantitieswill scan at$5.56 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepsi cans 12 pack 144 oz tot wt cans 12 oz cans Mist Twst Mtn Dew"

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

    def test_Store_Baked_Pumpkin_Pie(self):

        # Input and expected result.
        test_input_title = "Store Baked Pumpkin Pie"
        test_input_description = "22-oz., Coconut Custard,Sweet Potato Pie Limit 4Per Variety YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pumpkin Pie 22 oz Coconut Custard Sweet Potato Pie"

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

    def test_Nestle_Pure_Life_Water_28_pack(self):

        # Input and expected result.
        test_input_title = "Nestle Pure Life Water 28 pack"
        test_input_description = "192-oz. tot. wt. btls. (Plus Dep. or Fee Where Req.) 8-oz.Bottles, 24-Pack or 473.2-tot. wt. btls., 16.9-oz. BottlesLimit 4Offers MUSTBUY 2Additionalor lesserquantitieswill scan at$5.19 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nestle Pure Life Water 28 pack 192 oz tot wt btls 8 oz bottles 24 pack or 473.2 tot wt btls 16.9 oz bottles"

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

    def test_Farm_Promise_Boneless_Pork_Roast(self):

        # Input and expected result.
        test_input_title = "Farm Promise Boneless Pork Roast"
        test_input_description = "Fresh, Locally Raised, Raised Without AntibioticsShopRiteSale Price $4.99 LB. - $1.00 LB. Limit 4-pkgs. LocalBeef& Pork raised on family farms WhereAvailable"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Farm promise Boneless Pork Roast"

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

    def test_Farm_Promise_Beef_Top_Round_London_Broil(self):

        # Input and expected result.
        test_input_title = "Farm Promise Beef Top Round London Broil"
        test_input_description = "Fresh, Locally Raised on Family Farms,No Antibiotics Ever, Fed a Vegetarian Diet USDACHOICEBEEF LocalBeef& Pork raised on family farms"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Farm promise Beef Top Round London Broil Fresh Locally raised on Family Farms Beef"

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

    def test_Bob_Evans_Mashed_Potatoes(self):

        # Input and expected result.
        test_input_title = "Bob Evans Mashed Potatoes"
        test_input_description = "20 to 24-oz. pkg., Fully Cooked, Heat & Eat, Assorted Varieties50¢ OFF with digital coupon at shoprite.com limit 1"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bob Evans Mashed Potatoes 20 to 24 oz pkg"

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

    def test_Natures_Reserve_Lamb_Loin_Chops(self):

        # Input and expected result.
        test_input_title = "Nature's Reserve Lamb Loin Chops"
        test_input_description = "Fresh, Bone-In, Tailless, Product of Australia"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's Reserve Lamb Loin Chops Fresh Bone-In Tailless"

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

    def test_Fresh_Norwegian_Salmon_Portions(self):

        # Input and expected result.
        test_input_title = "Fresh Norwegian Salmon Portions"
        test_input_description = "5-oz., Boneless & Skinless,No Antibiotics EverU.S. GRADE A"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Norwegian Salmon Portions 5 oz Boneless & Skinless"

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

    def test_Completely_Cleaned_Fresh_2630_count_Lb_Shrimp(self):

        # Input and expected result.
        test_input_title = "Completely Cleaned Fresh 26/30 count Lb Shrimp"
        test_input_description = "Responsibly Raised,Peeled & Deveined, Tail OffShopRiteSale Price $14.99 lb. - $1.00 lb. Limit 4-lbs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Completely Cleaned Fresh 26/30 Count lb Shrimp"

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

    def test_Fresh_Large_Ecuadorian_Shrimp(self):

        # Input and expected result.
        test_input_title = "Fresh Large Ecuadorian Shrimp"
        test_input_description = "36 to 40-ct./lb., Responsibly Raised,Raw, Shell-OnShopRiteSale Price $8.99 LB. - $1.00 LB. Limit 4-lbs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Large Ecuadorian Shrimp 36 to 40 ct/lb Raw Shell-On"

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

    def test_Fresh_Rainbow_Trout(self):

        # Input and expected result.
        test_input_title = "Fresh Rainbow Trout"
        test_input_description = "Farm Raised in Idaho,Dressed, Never Frozen U.S. GRADE A ShopRiteSale Price $5.49 LB. - 50¢ LB. Limit 4-lbs."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Rainbow Trout"

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

    def test_Fresh_Wild_Caught_Icelandic_Cod_Fillet(self):

        # Input and expected result.
        test_input_title = "Fresh Wild Caught Icelandic Cod Fillet"
        test_input_description = "Line Caught, Boneless &Skinless, Never FrozenCATCHOF THEWEEK! U.S. GRADE A"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fresh Wild caught Icelandic Cod Fillet Boneless & Skinless"

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

    def test_Mini_Apple_Spice_Strudels(self):

        # Input and expected result.
        test_input_title = "Mini Apple Spice Strudels"
        test_input_description = "11-oz., pkg. of 4, Store Baked, Peaches 'n Cream SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mini Apple Spice Strudels 11 oz Peaches 'N Cream"

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

    def test_Apple_Cider_Donuts(self):

        # Input and expected result.
        test_input_title = "Apple Cider Donuts"
        test_input_description = "12-oz. pkg. of 6, Pumpkin Spice SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Apple Cider Donuts 12 oz Pumpkin Spice"

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

    def test_Mini_Peanut_Free_Cupcakes(self):

        # Input and expected result.
        test_input_title = "Mini Peanut Free Cupcakes"
        test_input_description = "10-oz., pkg. of 12 SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mini Peanut Free Cupcakes 10 oz"

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

    def test_Jumbo_Glazed_Donuts(self):

        # Input and expected result.
        test_input_title = "Jumbo Glazed Donuts"
        test_input_description = "24-oz., pkg. of 12 SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Jumbo Glazed Donuts 24 oz"

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

    def test_Zucchini_Crumb_Loaf(self):

        # Input and expected result.
        test_input_title = "Zucchini Crumb Loaf"
        test_input_description = "15-oz., Hand MadeMade withGreek Yogurtand LocallyGrownZucchini SAVE50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Zucchini Crumb Loaf 15 oz"

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

    def test_Lillys_Challah_Bread(self):

        # Input and expected result.
        test_input_title = "Lilly's Challah Bread"
        test_input_description = "15 to 16-oz.,Round, Plain or RaisinLimit 4Per Variety YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lilly's Challah Bread 15 to 16 oz Round Plain or Raisin"

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

    def test_Store_Made_Pumpkin_Muffins(self):

        # Input and expected result.
        test_input_title = "Store Made Pumpkin Muffins"
        test_input_description = "15-oz., pkg. of 6, Corn,Blueberry, Chocolate Chip SAVE $1.50"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pumpkin Muffins 15 oz Corn Blueberry Chocolate Chip"

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

    def test_Roasted_Garlic_Ciabatta_Bread(self):

        # Input and expected result.
        test_input_title = "Roasted Garlic Ciabatta Bread"
        test_input_description = "15 to 16-oz., Store Baked,Artisan Plain, Wheat, Olive Oil,Kneadin' Grains SAVE$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Roasted Garlic Ciabatta Bread 15 to 16 oz Artisan Plain Wheat Olive Oil Kneadin' Grains"

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

    def test_Authentic_Portuguese_Rolls(self):

        # Input and expected result.
        test_input_title = "Authentic Portuguese Rolls"
        test_input_description = "12 to 18-oz., pkg. of 12, Store Baked Medium Kaiser,Regular, Wheat SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Authentic Portuguese rolls 12 to 18 oz Medium Kaiser Regular Wheat"

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

    def test_Gourmet_Pumpkin_White_Chocolate_Chunk_Cookies(self):

        # Input and expected result.
        test_input_title = "Gourmet Pumpkin White Chocolate Chunk Cookies"
        test_input_description = "15-oz., pkg. of 12, Store BakedLimit 4 YOU SAVE $1.00 NewFlavor forFall! Fall Favorites"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gourmet Pumpkin White Chocolate Chunk Cookies 15 oz"

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

    def test_Nabisco_Oreo_Cookies(self):

        # Input and expected result.
        test_input_title = "Nabisco Oreo Cookies"
        test_input_description = "8.5 to 15.25-oz. pkg. (Excluding Family Size)Any Variety, Thins, Cremes Limit 4Offers MUSTBUY 2Additionalor lesserquantitieswill scan at$3.49 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nabisco Oreo Cookies 8.5 to 15.25 oz pkg Thins Cremes"

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

    def test_Bubba_Q_Boneless_Pork_Ribs(self):

        # Input and expected result.
        test_input_title = "Bubba Q Boneless Pork Ribs"
        test_input_description = "18-oz. pkg., Pork,Heat & Eat"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bubba Q Boneless Pork Ribs 18 oz pkg Pork"

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

    def test_ShopRite_Cage_Free_Eggs(self):

        # Input and expected result.
        test_input_title = "ShopRite Cage Free Eggs"
        test_input_description = "(Dairy) Grade A,Dozen Carton, Large"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Cage Free Eggs Dairy Grade A Dozen Carton Large"

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

    def test_ShopRite_Apple_Sauce_6_Pack(self):

        # Input and expected result.
        test_input_title = "ShopRite Apple Sauce 6 Pack"
        test_input_description = "1-lb. 8-oz. tot. wt. pkg.,Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Apple Sauce 6 pack 1 lb 8 oz tot wt pkg"

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

    def test_Larabar_Bars(self):

        # Input and expected result.
        test_input_title = "Larabar Bars"
        test_input_description = "1.6 to 1.8-oz. pkg. (ExcludingUber & Seasonal) Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Larabar Bars 1.6 to 1.8 oz pkg Excludinguber & Seasonal"

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

    def test_Organic_Bartlett_Pears(self):

        # Input and expected result.
        test_input_title = "Organic Bartlett Pears"
        test_input_description = "(Produce)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Organic Bartlett Pears produce"

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

    def test_Mango_Spears(self):

        # Input and expected result.
        test_input_title = "Mango Spears"
        test_input_description = "8-oz., Fresh Cut"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mango Spears 8 oz Fresh Cut"

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

    def test_ShopRite_Raisins(self):

        # Input and expected result.
        test_input_title = "ShopRite Raisins"
        test_input_description = "15-oz. pkg. SeedlessRegular or Golden"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Raisins 15 oz pkg"

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

    def test_Muuna_2_Cottage_Cheese(self):

        # Input and expected result.
        test_input_title = "Muuna 2% Cottage Cheese"
        test_input_description = "(Dairy) 5.3-oz. cont.,Any Variety Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Muuna 2% Cottage Cheese Dairy 5.3 oz cont"

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

    def test_Dole_Acai_Bowls(self):

        # Input and expected result.
        test_input_title = "Dole Acai Bowls"
        test_input_description = "(Frozen) 6-oz. pkg.,Any VarietyLimit 4 Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dole Acai bowls frozen 6 oz pkg"

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

    def test_Presto_Portion_Pack_Snack_Bags(self):

        # Input and expected result.
        test_input_title = "Presto Portion Pack Snack Bags"
        test_input_description = "80-ct. box,ReclosableLimit 4 Per Variety, YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Presto Portion pack Snack bags 80 ct box Reclosable"

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

    def test_Manns_Sugar_Snap_Peas(self):

        # Input and expected result.
        test_input_title = "Mann’s Sugar Snap Peas"
        test_input_description = "(Produce) 8-oz. Bag"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Manns Sugar Snap Peas produce 8 oz bag"

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

    def test_General_Mills_Cheerios_Cereal(self):

        # Input and expected result.
        test_input_title = "General Mills Cheerios Cereal"
        test_input_description = "18-oz.box, Original"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "General Mills Cheerios cereal 18 oz box Original"

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

    def test_Planters_Nutrition_Nuts(self):

        # Input and expected result.
        test_input_title = "Planters Nutrition Nuts"
        test_input_description = "9.5 to 10.25-oz. can,Any VarietyLimit 4 Per Variety, YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Planters Nutrition Nuts 9.5 to 10.25 oz can"

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

    def test_1915_Cold_Pressed_Juice(self):

        # Input and expected result.
        test_input_title = "1915 Cold Pressed Juice"
        test_input_description = "(Produce) 12-oz. btl.,Assorted Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "1915 Cold pressed Juice produce 12 oz btl"

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

    def test_Kevita_Komucha(self):

        # Input and expected result.
        test_input_title = "Kevita Komucha"
        test_input_description = "(Dairy) 15.2-fl. oz.,Any VarietyLimit 4 Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kevita Komucha Dairy 15.2 fl oz"

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

    def test_Vitalicious_VitaTops(self):

        # Input and expected result.
        test_input_title = "Vitalicious VitaTops"
        test_input_description = "8-oz. pkg., Any Variety (ExcludingSugar Free and VitaCakesLimit 4 Per Variety, YOU SAVE $1.50"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Vitalicious Vitatops 8 oz pkg Excluding Sugar Free and Vitacakes"

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

    def test_Kind_Strong_Bar(self):

        # Input and expected result.
        test_input_title = "Kind Strong Bar"
        test_input_description = "1.6-oz. pkg.,Any VarietyLimit 4 Per Variety, YOU SAVE 29¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kind Strong Bar 1.6 oz pkg"

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

    def test_Wholesome_Pantry_Organic_Red_Grape_Tomatoes(self):

        # Input and expected result.
        test_input_title = "Wholesome Pantry Organic Red Grape Tomatoes"
        test_input_description = "(Produce) Dry Pint"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Wholesome Pantry Organic Red Grape Tomatoes produce Dry Pint"

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

    def test_LaLa_4_pack_Smoothies(self):

        # Input and expected result.
        test_input_title = "LaLa 4 pack Smoothies"
        test_input_description = "(Dairy) 26.8 to 28-fl. oz. pkg.,Any Variety, Greek orLimit 4 Per Variety, you save $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lala 4 pack Smoothies Dairy 26.8 to 28 fl oz pkg Greek"

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

    def test_Wholesome_Pantry_Omega3_Whole_Milk(self):

        # Input and expected result.
        test_input_title = "Wholesome Pantry Omega-3 Whole Milk"
        test_input_description = "(Dairy) 64-fl. oz. cont.,Omega-3, 2% Limit 4 Per Variety, you save 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Wholesome Pantry Omega-3 Whole Milk Dairy 64 fl oz contOmega-3 2%"

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

    def test_Justins_Chocolate_Peanut_Butter_Cups(self):

        # Input and expected result.
        test_input_title = "Justin’s Chocolate Peanut Butter Cups"
        test_input_description = "4.7-oz. pkg., Any Variety,OrganicLimit 4 Per Variety, you save 20¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Justins Chocolate Peanut Butter Cups 4.7 oz pkg Organic"

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

    def test_Black_Bear_Natural_Casing_1_Lb_Franks(self):

        # Input and expected result.
        test_input_title = "Black Bear Natural Casing 1 Lb Franks"
        test_input_description = "1-lb. pkg.,Natural Casing MeatLimit 4 Per Variety, you save $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear Natural Casing 1 lb Franks 1 lb pkg"

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

    def test_Black_Bear_Buffalo_Chicken_Breast(self):

        # Input and expected result.
        test_input_title = "Black Bear Buffalo Chicken Breast"
        test_input_description = "Store Sliced, BBQ, Sriracha,Zesty Honey, Gourmet YOU WON'T FIND HIGHER QUALITY IN ANY OTHER SANDWICH SHOP OR DELI"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear Buffalo Chicken Breast BBQ Sriracha Zesty Honey Gourmet"

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

    def test_Black_Bear_Virginia_Ham(self):

        # Input and expected result.
        test_input_title = "Black Bear Virginia Ham"
        test_input_description = "Store Sliced, Rosemary,Tomato Basil, Deep Smoked"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear Virginia Ham Rosemary Tomato Basil Deep Smoked"

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

    def test_Black_Bear_Top_Round_Roast_Beef(self):

        # Input and expected result.
        test_input_title = "Black Bear Top Round Roast Beef"
        test_input_description = "Store Sliced, USDA Choice, Seasoned"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear Top Round Roast Beef Seasoned"

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

    def test_Forest_Fresh_Herbed_Turkey(self):

        # Input and expected result.
        test_input_title = "Forest Fresh Herbed Turkey"
        test_input_description = "7-oz. pkg., Antibiotic Free,Chicken, Uncured Ham"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Forest Fresh Herbed Turkey 7 oz pkg Chicken Uncured Ham"

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

    def test_Black_Bear_Imported_Swiss(self):

        # Input and expected result.
        test_input_title = "Black Bear Imported Swiss"
        test_input_description = "Store Sliced,Reduced Fat Lacey"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Black Bear Imported Swiss Reduced Fat Lacey"

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

    def test_Fountain_of_Health_Hummus(self):

        # Input and expected result.
        test_input_title = "Fountain of Health Hummus"
        test_input_description = "9-oz. cont.,Assorted Varieties, Non-GMO"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fountain of Health Hummus 9 oz cont"

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

    def test_ShopRite_Pita_Chips(self):

        # Input and expected result.
        test_input_title = "ShopRite Pita Chips"
        test_input_description = "7.33-oz. Assorted Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Pita Chips 7.33 oz"

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

    def test_ShopRite_Muenster(self):

        # Input and expected result.
        test_input_title = "ShopRite Muenster"
        test_input_description = "Store Sliced"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Muenster"

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

    def test_Carando_Genoa_Salami(self):

        # Input and expected result.
        test_input_title = "Carando Genoa Salami"
        test_input_description = "Store Sliced, Hard"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Carando Genoa Salami Hard"

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

    def test_Kings_Hawaiian_Mini_Sub_Rolls(self):

        # Input and expected result.
        test_input_title = "King’s Hawaiian Mini Sub Rolls"
        test_input_description = "Original SweetLimit 4 YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kings Hawaiian Mini Sub rolls Original Sweet"

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

    def test_Glen_Rock_Virginia_Ham(self):

        # Input and expected result.
        test_input_title = "Glen Rock Virginia Ham"
        test_input_description = "Store Sliced, 97% Fat Free, Honey"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Glen Rock Virginia Ham 97% Fat Free Honey"

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

    def test_Hormel_Pepperoni_Stick(self):

        # Input and expected result.
        test_input_title = "Hormel Pepperoni Stick"
        test_input_description = "Rosa or Rosa Grande"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hormel Pepperoni Stick Rosa or Rosa Grande"

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

    def test_ShopRite_Provolone(self):

        # Input and expected result.
        test_input_title = "ShopRite Provolone"
        test_input_description = "Store Sliced, Mozzarella"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite provolone Mozzarella"

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

    def test_Carando_Capicola(self):

        # Input and expected result.
        test_input_title = "Carando Capicola"
        test_input_description = "Store Sliced,Hot or Sweet"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Carando Capicola"

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

    def test_Smithfield_Domestic_Ham(self):

        # Input and expected result.
        test_input_title = "Smithfield Domestic Ham"
        test_input_description = "Store Sliced,98% Fat Free"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Smithfield Domestic Ham 98% Fat Free"

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

    def test_Norwegian_Jarlsberg(self):

        # Input and expected result.
        test_input_title = "Norwegian Jarlsberg"
        test_input_description = "Imported, Sweet & Nutty"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Norwegian jarlsberg Imported Sweet & Nutty"

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

    def test_ShopRite_Kitchen_Linguine(self):

        # Input and expected result.
        test_input_title = "ShopRite Kitchen Linguine"
        test_input_description = "8.8-oz. pkg., Lasagna Sheet,Fettucine Limit 4 Per Variety, YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Kitchen Linguine 8.8 oz pkg Lasagna Sheet Fettucine"

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

    def test_ShopRite_Filled_Pasta(self):

        # Input and expected result.
        test_input_title = "ShopRite Filled Pasta"
        test_input_description = "9-oz. pkg.Limit 4 Per Variety, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Filled Pasta 9 oz pkg"

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

    def test_ShopRite_Kitchen_Family_Size_Pasta(self):

        # Input and expected result.
        test_input_title = "ShopRite Kitchen Family Size Pasta"
        test_input_description = "20-oz. pkg., Select VarietiesLimit 4 Per Variety, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Kitchen Pasta 20 oz pkg"

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

    def test_Chicken_Tenders(self):

        # Input and expected result.
        test_input_title = "Chicken Tenders"
        test_input_description = "Store Made"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Chicken Tenders"

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

    def test_8_Piece_Drums__Thighs(self):

        # Input and expected result.
        test_input_title = "8 Piece Drums & Thighs"
        test_input_description = "26-oz. each, Equal Parts, Roasted orAvailable Hot or Freshly ChilledFRIED INTRANS FATFREE OILLimit 4 Per Variety, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "8 Piece Drums & Thighs 26 oz"

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

    def test_Boars_Head_OvenGold_Turkey_Breast(self):

        # Input and expected result.
        test_input_title = "Boar’s Head OvenGold Turkey Breast"
        test_input_description = "Store Sliced"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boars Head Ovengold Turkey Breast"

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

    def test_Boars_Head_American_Cheese(self):

        # Input and expected result.
        test_input_title = "Boar’s Head American Cheese"
        test_input_description = "Store Sliced, Yellow or White"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boars Head American Cheese Yellow or White"

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

    def test_ShopRite_Butter(self):

        # Input and expected result.
        test_input_title = "ShopRite Butter"
        test_input_description = "1-lb. pkg., Quarters,Salted or Unsalted (Excluding Organic)Limit 4Per Variety, YOU SAVE 20¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Butter 1 lb pkg Quarters Salted or Unsalted Excluding Organic"

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

    def test_Noahs_Pride_Brown_Eggs(self):

        # Input and expected result.
        test_input_title = "Noah’s Pride Brown Eggs"
        test_input_description = "Grade A, dozen,Cage Free"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Noahs pride Brown Eggs Grade A Dozen Cage Free"

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

    def test_Tree_Ripe_Orange_Juice(self):

        # Input and expected result.
        test_input_title = "Tree Ripe Orange Juice"
        test_input_description = "59-oz. cont.,Any Variety (Excluding Organic)Limit 4Per Variety, YOU SAVE 30¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tree Ripe Orange Juice 59 oz cont Excluding Organic"

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

    def test_Philadelphia_Brick_Cream_Cheese(self):

        # Input and expected result.
        test_input_title = "Philadelphia Brick Cream Cheese"
        test_input_description = "8-oz. pkg.,Neufchatel"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Philadelphia Brick Cream Cheese 8 oz pkg Neufchatel"

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

    def test_Tropicana_Twister(self):

        # Input and expected result.
        test_input_title = "Tropicana Twister"
        test_input_description = "59-oz. cont.,Any Variety, Ades or PunchesLimit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tropicana Twister 59 oz cont Ades or Punches"

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

    def test_Starbucks_Iced_Coffee(self):

        # Input and expected result.
        test_input_title = "Starbucks Iced Coffee"
        test_input_description = "40 to 48 oz. cont., Any VarietyLimit 4Per Variety, YOU SAVE 57¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Starbucks Iced Coffee 40 to 48 oz cont"

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

    def test_Tropicana_Pure_Premium_Juice(self):

        # Input and expected result.
        test_input_title = "Tropicana Pure Premium Juice"
        test_input_description = "89-oz. cont., Any Variety, Trop 50 or OrangeLimit 4Per Variety, YOU SAVE 57¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tropicana Pure premium Juice 89 oz cont Trop 50 or Orange"

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

    def test_Land_O_Lakes_Spreadable_Butter(self):

        # Input and expected result.
        test_input_title = "Land O Lakes Spreadable Butter"
        test_input_description = "15-oz. pkg.,Any VarietyLimit 4Per Variety, YOU SAVE 30¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Land O Lakes Spreadable Butter 15 oz pkg"

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

    def test_Lactaid_Milk(self):

        # Input and expected result.
        test_input_title = "Lactaid Milk"
        test_input_description = "96-oz. cont.,Any VarietyLimit 4Per Variety, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lactaid Milk 96 oz cont"

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

    def test_Turkey_Hill_Iced_Tea(self):

        # Input and expected result.
        test_input_title = "Turkey Hill Iced Tea"
        test_input_description = "64-oz. cont.,Any Variety, Lemonade"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Turkey Hill Iced Tea 64 oz cont Lemonade"

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

    def test_I_Cant_Believe_Its_Not_Butter(self):

        # Input and expected result.
        test_input_title = "I Can’t Believe It’s Not Butter"
        test_input_description = "8 to 16-oz. cont., Any Variety(Excluding Organic)Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "I cant Believe Its Not Butter 8 to 16 oz cont Excluding Organic"

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

    def test_ShopRite_Organic_Milk(self):

        # Input and expected result.
        test_input_title = "ShopRite Organic Milk"
        test_input_description = "Gallon cont., Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Organic Milk gallon cont"

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

    def test_Brew_Doctor_Kombucha(self):

        # Input and expected result.
        test_input_title = "Brew Doctor Kombucha"
        test_input_description = "14-fl. oz. btl., Any Variety(Where Available)new at shoprite"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Brew Doctor Kombucha 14 fl oz btl"

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

    def test_Friendship_Sour_Cream(self):

        # Input and expected result.
        test_input_title = "Friendship Sour Cream"
        test_input_description = "16-oz. cont.,Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Friendship Sour Cream 16 oz cont"

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

    def test_Coffeemate_Flavored_Creamers(self):

        # Input and expected result.
        test_input_title = "Coffee-mate Flavored Creamers"
        test_input_description = "16-oz. cont., Any Variety(Excluding Natural Bliss)Limit 4Per Variety, you save 53¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coffee-Mate flavored Creamers 16 oz cont Excluding Natural Bliss"

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

    def test_Pillsbury_Grands_Biscuits(self):

        # Input and expected result.
        test_input_title = "Pillsbury Grands Biscuits"
        test_input_description = "12 to 16.3-oz. pkg., Any Variety(Excluding 10-ct. Jr.)3 for $5 with digital coupon at shoprite.com Must Buy 3Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pillsbury Grands Biscuits 12 to 16.3 oz pkg Excluding 10 ct jr"

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

    def test_Butterball_Turkey_Bacon(self):

        # Input and expected result.
        test_input_title = "Butterball Turkey Bacon"
        test_input_description = "6-oz. pkg.,Low Salt"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Butterball Turkey Bacon 6 oz pkg"

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

    def test_Kozy_Shack_Puddings_6_pack(self):

        # Input and expected result.
        test_input_title = "Kozy Shack Puddings 6 pack"
        test_input_description = "24-oz. tot. wt. pkg., Any Variety,(Excluding Lactose Free)Limit 4Per Variety, you save 85¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kozy Shack Puddings 6 pack 24 oz tot wt pkg Excluding Lactose Free"

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

    def test_Pillsbury_Cinnamon_Rolls(self):

        # Input and expected result.
        test_input_title = "Pillsbury Cinnamon Rolls"
        test_input_description = "12.4 to 13.9-oz. pkg., Any VarietyLimit 4Per Variety, 2 for $3 with digital coupon at shoprite.com Must Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pillsbury Cinnamon rolls 12.4 to 13.9 oz pkg"

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

    def test_Pillsbury_Crescent_Rolls(self):

        # Input and expected result.
        test_input_title = "Pillsbury Crescent Rolls"
        test_input_description = "8-oz. pkg., Any Variety (Excluding Big Crescents)Limit 4Per Variety, 2 for $3 with digital coupon at shoprite.com Must Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pillsbury Crescent rolls 8 oz pkg Excluding Big Crescents"

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

    def test_Hillshire_Farm_Deli_Selects(self):

        # Input and expected result.
        test_input_title = "Hillshire Farm Deli Selects"
        test_input_description = "7 to 9-oz. pkg.,Any Variety, Deli FreshLimit 4Per Variety, you save 30¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hillshire Farm Deli Selects 7 to 9 oz pkg Deli Fresh"

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

    def test_ShopRite_Whipped_Cream(self):

        # Input and expected result.
        test_input_title = "ShopRite Whipped Cream"
        test_input_description = "13-oz. cont., Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Whipped Cream 13 oz cont"

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

    def test_Colonna_Grated_Cheese(self):

        # Input and expected result.
        test_input_title = "Colonna Grated Cheese"
        test_input_description = "8-oz. plastic cont., Fat Free, ImportedParmesan and Parmesan/Romano"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colonna Grated Cheese 8 oz Plastic cont Fat Free Imported Parmesan and Parmesan/Romano"

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

    def test_Chobani_Greek_Yogurt(self):

        # Input and expected result.
        test_input_title = "Chobani Greek Yogurt"
        test_input_description = "4.2 to 5.3-oz. cont., Any Variety,Simply 100, Flips"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Chobani Greek Yogurt 4.2 to 5.3 oz cont"

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

    def test_Yoplait_Original_Yogurt(self):

        # Input and expected result.
        test_input_title = "Yoplait Original Yogurt"
        test_input_description = "4 to 6-oz. cont., Any Variety,Light, Whips or (ExcludingGreek and Lactose Free)10 FOR $4 with digital coupon at shoprite.com Must Buy 10Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Yoplait Original Yogurt 4 to 6 oz cont Light Whips or Excluding Greek and Lactose Free"

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

    def test_Stonyfield_Organic_Greek_Yogurt(self):

        # Input and expected result.
        test_input_title = "Stonyfield Organic Greek Yogurt"
        test_input_description = "5.3 to 6-oz. cont., Any Variety, GrassfedLimit 4Per Variety, BUY 4 GET 1 FREE, Limit 4Offers, you save $1.25"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stonyfield Organic Greek Yogurt 5.3 to 6 oz cont Grassfed"

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

    def test_Stonyfield_Organic_Yogurt_Pouches(self):

        # Input and expected result.
        test_input_title = "Stonyfield Organic Yogurt Pouches"
        test_input_description = "10-oz. cont., Any Variety, YogurtDrink or 3.5 to 3.7-oz., Any VarietyLimit 4Per Variety, BUY 4 GET 1 FREE Limit 4Offers, you save $1.25"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stonyfield Organic Yogurt pouches 10 oz cont Yogurt Drink or 3.5 to 3.7 oz"

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

    def test_Virtuoso_Pizza(self):

        # Input and expected result.
        test_input_title = "Virtuoso Pizza"
        test_input_description = "11.5 to 16.2-oz. pkg.,Any Variety2 FOR $5 with Digital Coupon at shoprite.com Must Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Virtuoso Pizza 11.5 to 16.2 oz pkg"

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

    def test_Lundberg_Grainspirations_Arancini(self):

        # Input and expected result.
        test_input_title = "Lundberg Grainspirations Arancini"
        test_input_description = "7.5-oz. pkg. (Where Available)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lundberg Grainspirations Arancini 7.5 oz pkg"

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

    def test_ShopRite_Italian_Extra_Virgin_Olive_Oil(self):

        # Input and expected result.
        test_input_title = "ShopRite Italian Extra Virgin Olive Oil"
        test_input_description = "33.8-oz. btl., Imported from ItalyLimit 4, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Italian Olive Oil 33.8 oz btl Imported from Italy"

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

    def test_Barilla_Pasta(self):

        # Input and expected result.
        test_input_title = "Barilla Pasta"
        test_input_description = "12-oz. to 1-lb. box (Excluding Gluten Free,Plus, Collezione, Jumbo Shells & Lasagne)Any Variety, Regular, Whole Grain or Veggie, Limit 4Offers MUSTBUY 3 Additionalor lesserquantitieswill scan at$1.59 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Barilla Pasta 12 oz to 1 lb box Excluding Gluten Free Plus Collezione Jumbo Shells & Lasagne Regular Whole Grain or Veggie"

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

    def test_ShopRite_Imported_Organic_Tomatoes(self):

        # Input and expected result.
        test_input_title = "ShopRite Imported Organic Tomatoes"
        test_input_description = "28-oz. can, Imported from Italy, Whole Peeled or Crushed, Limit 4Per Variety, YOU SAVE 70¢, 25¢ OFF With Digital coupon at Shorite.com limit 1"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Imported Organic Tomatoes 28 oz can Imported from Italy Whole Peeled or Crushed"

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

    def test_Knorr_Pasta_or_Rice_Sides(self):

        # Input and expected result.
        test_input_title = "Knorr Pasta or Rice Sides"
        test_input_description = "3.8 to 5.7-oz. pkg.(Excluding Veggie & Selects) Any Variety, Limit 4Offers, MUSTBUY 5 Additionalor lesserquantitieswill scan at4 for $5"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Knorr Pasta or Rice Sides 3.8 to 5.7 oz pkgExcluding Veggie & Selects"

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

    def test_Pompeian_Classic_Olive_Oil(self):

        # Input and expected result.
        test_input_title = "Pompeian Classic Olive Oil"
        test_input_description = "24-oz. btl., Mediterranean, Limit 4, YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pompeian Classic Olive Oil 24 oz btl Mediterranean"

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

    def test_Lindt_Lindor_Truffles(self):

        # Input and expected result.
        test_input_title = "Lindt Lindor Truffles"
        test_input_description = "5.1-oz. bag, Any Variety, Limit 4Offers, MUSTBUY 3 Additionalor lesserquantitieswill scan at$3.99 ea.$1.00 OFF 3 WITH DIGITAL COUPON AT SHOPRITE.COM Must Buy 3Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lindt Lindor Truffles 5.1 oz bag"

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

    def test_Ghirardelli_Chocolate_Squares(self):

        # Input and expected result.
        test_input_title = "Ghirardelli Chocolate Squares"
        test_input_description = "4.87 to 5.32-oz. bag (Excluding IntenseChocolate & Holiday) Any VarietyLimit 4Offers, MUSTBUY 3 Additionalor lesserquantitieswill scan at$3.99 ea.$1.00 OFF 3 WITH DIGITAL COUPON AT SHOPRITE.COM Must Buy 3Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ghirardelli Chocolate squares 4.87 to 5.32 oz bag"

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

    def test_Empire_Boneless_Chicken_Breast(self):

        # Input and expected result.
        test_input_title = "Empire Boneless Chicken Breast"
        test_input_description = "Fresh, Skinless, Glatt Kosher,Never Administered Antibiotics"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Empire Boneless Chicken Breast Fresh Skinless Glatt Kosher"

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

    def test_Empire_Chicken_Leg_Quarters(self):

        # Input and expected result.
        test_input_title = "Empire Chicken Leg Quarters"
        test_input_description = "Fresh, With Back Attached, Glatt Kosher,Never Administered Antibiotics"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Empire Chicken Leg Quarters Fresh with Back Attached Glatt Kosher"

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

    def test_Empire_CutUp_Frying_Chicken(self):

        # Input and expected result.
        test_input_title = "Empire Cut-Up Frying Chicken"
        test_input_description = "Fresh, Glatt Kosher,Never Administered Antibiotics"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Empire Cut-Up Frying Chicken Fresh Glatt Kosher"

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

    def test_All_2X_Ultra_Laundry_Detergent(self):

        # Input and expected result.
        test_input_title = "All 2X Ultra Laundry Detergent"
        test_input_description = "94.5 to 100-oz. btl.,Any Variety, LiquidYOU SAVE $2.60 Limit 16 Per Variety with Price Plus Card $6.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "All 2X Ultra Laundry Detergent 94.5 to 100 oz btl liquid"

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

    def test_Snuggle_Fabric_Softener(self):

        # Input and expected result.
        test_input_title = "Snuggle Fabric Softener"
        test_input_description = "10.4-oz. btl., Any Variety, LiquidScentables Freshness Booster, 70 to80-ct. box, Fabric Softener Sheets or31.7 to 32-oz. btl., Concentrated LiquidSAVE UP TO $1.10 Limit 16 Per Variety with Price Plus Card $3.49 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Snuggle Fabric Softener 10.4 oz btl liquid Scentables Freshness Booster 70 To80 ct box Fabric Softener Sheets Or31.7 to 32 oz btl Concentrated liquid"

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

    def test_Clorox_Disinfecting_Wipes_3_pack(self):

        # Input and expected result.
        test_input_title = "Clorox Disinfecting Wipes 3 pack"
        test_input_description = "105-tot. sht. ct. pkg.YOU SAVE $1.50 Limit 16 with Price Plus Card $4.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Clorox Disinfecting Wipes 3 pack 105 tot sht ct pkg"

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

    def test_Allegra_Allergy(self):

        # Input and expected result.
        test_input_title = "Allegra Allergy"
        test_input_description = "8-fl. oz., Children’s 12-Hour or30-ct. 24-Hour, Non Drowsey$17.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Allegra Allergy 8 fl oz Childrens 12-Hour Or30 ct 24-Hour Non Drowsey"

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

    def test_Nasacort_Allergy_24_HR(self):

        # Input and expected result.
        test_input_title = "Nasacort Allergy 24 HR"
        test_input_description = ".37-fl. oz., 60-Sprays, Nasal Spray,Children’s or Adult$12.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nasacort Allergy 24 Hr.37 fl oz 60-Sprays Nasal Spray Childrens or Adult"

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

    def test_Clorox_Toilet_Wand(self):

        # Input and expected result.
        test_input_title = "Clorox Toilet Wand"
        test_input_description = "Toilet Wand Starter Kit with 6 Discs or 3.47-oz.box, 20-ct., Value Size Toilet Wand RefillsYOU SAVE $4.00 Limit 16 Per Variety with Price Plus Card $5.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Clorox Toilet Wand Toilet Wand Starter Kit with 6 Discs or 3.47 oz box 20 ct Value Size Toilet Wand Refills"

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

    def test_Clorox_Dust_Wipes(self):

        # Input and expected result.
        test_input_title = "Clorox Dust Wipes"
        test_input_description = "20-ct. box,Triple ActionYOU SAVE 80¢ Limit 16 with Price Plus Card $1.99 INSTANT BONUS BUCKS -$1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Clorox Dust Wipes 20 ct box Triple Action"

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

    def test_Gain_Flings_Laundry_Detergent_Pacs(self):

        # Input and expected result.
        test_input_title = "Gain Flings Laundry Detergent Pacs"
        test_input_description = "12 to 14-oz. pkg., 12 to 16-ct.,Any Variety Limit 4 Offers. Discountwill be appliedwhen you buyin incrementsof 3 only.Less or additional items will scan at $5.79 each.Look for$5.00 off 3MFR couponin mostSunday papersBETTER TOGETHER"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gain flings Laundry Detergent Pacs 12 to 14 oz pkg 12 to 16 ct"

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

    def test_Gain_Liquid_Laundry_Detergent(self):

        # Input and expected result.
        test_input_title = "Gain Liquid Laundry Detergent"
        test_input_description = "50-oz. btl., Any Variety, High EfficiencyLimit 4 Offers. Discountwill be appliedwhen you buyin incrementsof 3 only.Less or additional items will scan at $5.79 each.Look for$5.00 off 3MFR couponin mostSunday papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gain liquid Laundry Detergent 50 oz btl High Efficiency"

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

    def test_Gain_Fireworks(self):

        # Input and expected result.
        test_input_title = "Gain Fireworks"
        test_input_description = "13.2-oz. canister, In-Wash Scent BoosterLimit 4 Offers. Discountwill be appliedwhen you buyin incrementsof 3 only.Less or additional items will scan at $5.79 each.Look for$5.00 off 3MFR couponin mostSunday papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gain Fireworks 13.2 oz canister in-Wash Scent Booster"

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

    def test_Gain_Liquid_Fabric_Softener(self):

        # Input and expected result.
        test_input_title = "Gain Liquid Fabric Softener"
        test_input_description = "120-ct. box, Softener Sheets or 51-oz. btl.,Any VarietyLimit 4 Offers. Discountwill be appliedwhen you buyin incrementsof 3 only. Less or additional items will scan at $5.79 each.Look for$5.00 off 3MFR couponin mostSunday papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gain liquid Fabric Softener 120 ct box Softener Sheets or 51 oz btl"

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

    def test_Bounty_Mega_Roll_Towels_12_pack(self):

        # Input and expected result.
        test_input_title = "Bounty Mega Roll Towels 12 pack"
        test_input_description = "1,260 to 1,264-tot. sht. ct. pkg., Equals 20 RegularRolls, Select-A-Size, Huge Roll 8-Pack Limit 4Per Variety YOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bounty Mega Roll Towels 12 pack 1260 to 1264 tot sht ct pkg Equals 20 Regular rolls Select-A-Size Huge Roll 8 pack"

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

    def test_Bounty_Big_Roll_Towels_2_pack(self):

        # Input and expected result.
        test_input_title = "Bounty Big Roll Towels 2 pack"
        test_input_description = "96 to 168-tot. sht. ct. pkg., Prints or Select-A-SizeLimit 4Per Variety YOU SAVE 70¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bounty Big Roll Towels 2 pack 96 to 168 tot sht ct pkg prints or Select-A-Size"

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

    def test_ShopRite_Bath_Tissue_12_pack(self):

        # Input and expected result.
        test_input_title = "ShopRite Bath Tissue 12 pack"
        test_input_description = "12,000-tot. sht. ct. pkg., 1-PlyLimit 4 YOU SAVE $2.11"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Bath Tissue 12 pack 12000 tot sht ct pkg 1 ply"

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

    def test_ShopRite_Very_Soft_Double_Roll_24_pack(self):

        # Input and expected result.
        test_input_title = "ShopRite Very Soft Double Roll 24 pack"
        test_input_description = "7,200-tot. sht. ct. pkg., Bath Tissue, 2-PlyLimit 4 YOU SAVE $4.11"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Very Soft Double Roll 24 pack 7200 tot sht ct pkg Bath Tissue 2 ply"

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

    def test_Palmolive_Dish_Detergent(self):

        # Input and expected result.
        test_input_title = "Palmolive Dish Detergent"
        test_input_description = "120-oz. btl., Any Variety, LiquidLimit 4 Per Variety YOU SAVE 50¢ 50¢ OFF 2 with Digital Coupon at shoprite.com Must Buy 2 Limit 1 offerLook for 25¢ OFFMFR Coupon in MostSunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Palmolive Dish Detergent 120 oz btl liquid"

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

    def test_Hefty_Foam_Plates(self):

        # Input and expected result.
        test_input_title = "Hefty Foam Plates"
        test_input_description = "16 to 60-ct. pkg., 12-oz.Bowls or Any VarietyLimit 4 Per Variety YOU SAVE 70¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hefty Foam Plates 16 to 60 ct pkg 12 oz bowls"

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

    def test_Smuckers_Grape_Jelly(self):

        # Input and expected result.
        test_input_title = "Smucker’s Grape Jelly"
        test_input_description = "17.4 to 20-oz. squeeze btl.,"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Smuckers Grape Jelly 17.4 to 20 oz squeeze btl"

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

    def test_Reduced_Sugar_Strawberry_Limit_4_Offers__Discount_will_be_applied_when_you_buy_in_increments_of_3_only_(self):

        # Input and expected result.
        test_input_title = "Reduced Sugar Strawberry Limit 4 Offers. Discount will be applied when you buy in increments of 3 only."
        test_input_description = "Less or additional items will scan at $2.48 each."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Reduced Sugar Strawberry"

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

    def test_Jif_Peanut_Butter(self):

        # Input and expected result.
        test_input_title = "Jif Peanut Butter"
        test_input_description = "15 to 16-oz. jar (Excluding Chocolate)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Jif Peanut Butter 15 to 16 oz jar Excluding Chocolate"

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

    def test_Whips_or_Any_Variety_Limit_4_Offers__Discount_will_be_applied_when_you_buy_in_increments_of_3_only_(self):

        # Input and expected result.
        test_input_title = "Whips or Any Variety Limit 4 Offers. Discount will be applied when you buy in increments of 3 only."
        test_input_description = "Less or additional items will scan at $2.48 each."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Whips"

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

    def test_Gatorade_Drinks_8_pack(self):

        # Input and expected result.
        test_input_title = "Gatorade Drinks 8 pack"
        test_input_description = "160-cz. tot. wt. btls., 20-oz. Bottles, Any Variety, Limit 4Offers MUSTBUY 3 Additionalor lesserquantitieswill scan at$5.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gatorade Drinks 8 pack 160 cz tot wt btls 20 oz bottles"

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

    def test_Propel_Zero_12_pack(self):

        # Input and expected result.
        test_input_title = "Propel Zero 12 pack"
        test_input_description = "BUY 3, 160-cz. tot. wt. btls., 20-oz. Bottles, Any VarietyGatorade Drinks8-Pack 3 FOR $15.99 Limit 4Offers MUSTBUY 3 Additionalor lesserquantitieswill scan at$5.99 ea. AND GET 1, 202.8-oz. tot. wt. btls. (Plus Dep. or FeeWhere Req.) 16.9-oz. Bottles, Any Variety,Water BeveragePropel Zero 12-Pack FREE with Price Plus Card YOU SAVE $5.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Propel Zero 12 pack"

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

    def test_Starbucks_Coffee(self):

        # Input and expected result.
        test_input_title = "Starbucks Coffee"
        test_input_description = "3.3 to 10.3-oz. box 10-ct., Any Variety K-Cups or 11to 12-oz. bag, Any Variety, Whole Bean or Ground, Limit 4Per Variety SAVE UP TO $1.60"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Starbucks Coffee 3.3 to 10.3 oz box 10 ct K-Cups or 11To 12 oz bag Whole Bean or Ground"

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

    def test_Pepperidge_Farm_Milano_Cookies(self):

        # Input and expected result.
        test_input_title = "Pepperidge Farm Milano Cookies"
        test_input_description = "BUY 2, 3.3 to 10.3-oz. box 10-ct., Any Variety K-Cups or 11to 12-oz. bag, Any Variety, Whole Bean or GroundStarbucksCoffee $6.99 Limit 4Per Variety SAVE UP TO $1.60 AND GET 1, 4.75 to 7.5-oz. bag, Any VarietyPepperidge FarmMilano Cookies FREE with Price Plus Card Limit 4Offers YOU SAVE $2.99"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepperidge Farm Milano Cookies"

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

    def test_Gatorade_Drinks(self):

        # Input and expected result.
        test_input_title = "Gatorade Drinks"
        test_input_description = "24-oz. btl. (Plus Dep. or Fee Where Req.)Any Variety, Propel Zero or 1-qt. $2.00 OFF 10 With Digital Coupon at shoprite.com Must Buy 10Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gatorade Drinks 24 oz btl propel Zero or 1 qt"

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

    def test_ShopRite_Seltzer_1_Liter(self):

        # Input and expected result.
        test_input_title = "ShopRite Seltzer 1 Liter"
        test_input_description = "btl. (Plus Dep. or Fee WhereReq.) Club Soda or Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Seltzer 1 liter btl Club Soda"

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

    def test_Polar_Club_Soda_1Liter(self):

        # Input and expected result.
        test_input_title = "Polar Club Soda 1-Liter"
        test_input_description = "17-oz. btl. (Plus Dep. or Fee Where Req.) (WhereAvailable, While Supplies Last) Any Variety, Frostor 1-Liter, Half & Half, Tonic"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Polar Club Soda 1 liter 17 oz btl Frost or 1 liter Half & Half Tonic"

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

    def test_New_England_Ground_Coffee(self):

        # Input and expected result.
        test_input_title = "New England Ground Coffee"
        test_input_description = "10 to 12-oz. bag(Excluding Seasonal) Any Variety, Limit 4Per Variety YOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "New England Ground Coffee 10 to 12 oz bag Excluding Seasonal"

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

    def test_Pure_Leaf_Iced_Tea(self):

        # Input and expected result.
        test_input_title = "Pure Leaf Iced Tea"
        test_input_description = "64-oz. btl., Any Variety, Limit 4Offers MUSTBUY 2 Additionalor lesserquantitieswill scan at$2.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pure Leaf Iced Tea 64 oz btl"

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

    def test_Nestea_Iced_Tea_6_pack(self):

        # Input and expected result.
        test_input_title = "Nestea Iced Tea 6 pack"
        test_input_description = "101.4-oz. tot. wt. btls. (Plus Dep. or FeeWhere Req.) 16.9-oz. Bottles, Any Variety, Limit 4Offers MUST BUY 2 Additionalor lesserquantitieswill scan at$2.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nestea Iced Tea 6 pack 101.4 oz tot wt btls 16.9 oz bottles"

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

    def test_Polar_Seltzer_1_Liter(self):

        # Input and expected result.
        test_input_title = "Polar Seltzer 1 Liter"
        test_input_description = "btl. (Plus Dep. or Fee Where Req.) (Where Available,While Supplies Last) Any Variety, Limit 4Offers MUSTBUY 5 Additionalor lesserquantitieswill scan at99¢ ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Polar Seltzer 1 liter btl"

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

    def test_Vintage_Seltzer(self):

        # Input and expected result.
        test_input_title = "Vintage Seltzer"
        test_input_description = "33.8-oz. btl. (Plus Dep. or Fee WhereReq.) Tonic, Club Soda or Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Vintage Seltzer 33.8 oz btl Tonic Club Soda"

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

    def test_Nestl_Pure_Life_Splash_6_pack(self):

        # Input and expected result.
        test_input_title = "Nestlé Pure Life Splash 6 pack"
        test_input_description = "101.4-oz. tot. wt. btls. (Plus Dep. orFee Where Req.) 16.9-oz. Bottles,Any Variety, Flavored Water"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nestle Pure Life Splash 6 pack 101.4 oz tot wt btls 16.9 oz bottles"

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

    def test_ShopRite_Cran_Drinks(self):

        # Input and expected result.
        test_input_title = "ShopRite Cran Drinks"
        test_input_description = "64-oz. btl. (Excluding 100% Juice)Any VarietyLimit 4Offers MUSTBUY 2 Additionalor lesserquantitieswill scan at$1.69 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Cran Drinks 64 oz btl Excluding 100% Juice"

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

    def test_KoolAid_Jammers_Drinks_10_pack(self):

        # Input and expected result.
        test_input_title = "Kool-Aid Jammers Drinks 10 pack"
        test_input_description = "60-oz. tot. wt. pkg., Any VarietyLimit 4Per Variety you save 11¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kool-Aid Jammers Drinks 10 pack 60 oz tot wt pkg"

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

    def test_San_Pellegrino_Sparkling_Mineral_Water_6_pack(self):

        # Input and expected result.
        test_input_title = "San Pellegrino Sparkling Mineral Water 6 pack"
        test_input_description = "202.8-oz. tot. wt. btls.(Plus Dep. or Fee WhereReq.) 1-Liter BottlesLimit 4Per Variety you save $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "San Pellegrino Sparkling Mineral Water 6 pack 202.8 oz tot wt btls 1 liter bottles"

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

    def test_San_Pellegrino_Water_6_pack(self):

        # Input and expected result.
        test_input_title = "San Pellegrino Water 6 pack"
        test_input_description = "66.9-oz. tot. wt. cans (Plus Dep. orFee Where Req.) 11.15-oz. Cans, AnyVariety, Sparkling, Limit 4Offers MUSTBUY 2 Additionalor lesserquantitieswill scan at$4.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "San Pellegrino Water 6 pack 66.9 oz tot wt cans 11.15 oz cans Sparkling"

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

    def test_Duncan_Hines_Seasonal_Baking_Mixes(self):

        # Input and expected result.
        test_input_title = "Duncan Hines Seasonal Baking Mixes"
        test_input_description = "18.2 to 19.4-oz. box, Limit 4Per Variety you save 24¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Duncan Hines Seasonal Baking Mixes 18.2 to 19.4 oz box"

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

    def test_Quaker_Pumpkin_Spice_Instant_Oatmeal(self):

        # Input and expected result.
        test_input_title = "Quaker Pumpkin Spice Instant Oatmeal"
        test_input_description = "12.1-oz. box, Gingerbread"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Quaker Pumpkin Spice instant Oatmeal 12.1 oz box Gingerbread"

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

    def test_Betty_Crocker_Pumpkin_Cookie_or_Bar_Mix(self):

        # Input and expected result.
        test_input_title = "Betty Crocker Pumpkin Cookie or Bar Mix"
        test_input_description = "17.5-oz. pouch/box, Limit 4Per Variety you save 20¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Betty Crocker Pumpkin Cookie or Bar Mix 17.5 oz Pouch/Box"

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

    def test_Quaker_Life_Pumpkin_Spice_Cereal(self):

        # Input and expected result.
        test_input_title = "Quaker Life Pumpkin Spice Cereal"
        test_input_description = "13-oz. box, Quaker, Gingerbread"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Quaker Life Pumpkin Spice cereal 13 oz box Quaker Gingerbread"

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

    def test_New_England_Seasonal_Ground_Coffee(self):

        # Input and expected result.
        test_input_title = "New England Seasonal Ground Coffee"
        test_input_description = "11-oz. bag, Any VarietyLimit 4Per Variety you save $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "New England Seasonal Ground Coffee 11 oz bag"

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

    def test_Simply_Organic_Pumpkin_Spice(self):

        # Input and expected result.
        test_input_title = "Simply Organic Pumpkin Spice"
        test_input_description = "1.94-oz. btl.Limit 4 YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Simply Organic Pumpkin Spice 1.94 oz btl"

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

    def test_Huggies_Diapers_Big_Pak(self):

        # Input and expected result.
        test_input_title = "Huggies Diapers Big Pak"
        test_input_description = "BUY MORE...SAVE MORE!24 to 100-ct. box, Snug & Dry, LittleSnugglers, Little Movers, OverNites,GoodNites or Pull-UpsHuggies DiapersBig PakBUY 1 FOR $18.99 EA. Save $5.00 ea. and BUY 2 FOR $15.00 EA. Save $17.98 on 2 with Price Plus CardLimit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Huggies Diapers Big Pak 24 to 100 ct box Snug & Dry Little Snugglers Little Movers Overnites Goodnites or Pull-Upshuggies Diapersbig Pak"

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

    def test_Coke_Mini_Cans_6Pack(self):

        # Input and expected result.
        test_input_title = "Coke Mini Cans 6-Pack"
        test_input_description = "45-oz. tot. wt. cans (PlusDep. or Fee Where Req.)7.5-oz. Cans, Seagram’s,Sprite, Fanta"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke Mini cans 6 pack 45 oz tot wt cans 7.5 oz cans Seagrams Sprite Fanta"

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

    def test_Coke_Bottles_6Pack(self):

        # Input and expected result.
        test_input_title = "Coke Bottles 6-Pack"
        test_input_description = "101.4-oz. tot. wt. btls. (Plus Dep. or FeeWhere Req.) 16.9-oz. Bottles,Dr Pepper, Seagram’s, Sprite"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke bottles 6 pack 101.4 oz tot wt btls 16.9 oz bottles Dr Pepper Seagrams Sprite"

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

    def test_Pepsi_Mini_Cans_15_pack(self):

        # Input and expected result.
        test_input_title = "Pepsi Mini Cans 15 pack"
        test_input_description = "112.5-oz. tot. wt. cans (Plus Dep. orFee Where Req.) 7.5-oz. Cans,Mtn Dew, Schweppes Ginger AleLimit 4 Per VarietyYOU SAVE 71¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepsi Mini cans 15 pack 112.5 oz tot wt cans 7.5 oz cans Mtn Dew Schweppes Ginger Ale"

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

    def test_Kelloggs_Rice_Krispies_Treats(self):

        # Input and expected result.
        test_input_title = "Kellogg’s Rice Krispies Treats"
        test_input_description = "5.6 to 6.2-oz. box, Any VarietyLimit 4 Per VarietyYOU SAVE 99¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kelloggs Rice Krispies Treats 5.6 to 6.2 oz box"

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

    def test_Quaker_Instant_Oatmeal(self):

        # Input and expected result.
        test_input_title = "Quaker Instant Oatmeal"
        test_input_description = "9.8 to 15.1-oz. box (Excluding Seasonal,Organic, Select Starts, Steel Cut andWarm & Crunchy) Any Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Quaker instant Oatmeal 9.8 to 15.1 oz box Excluding Seasonal Organic Select Starts Steel Cut and Warm & Crunchy"

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

    def test_Hanover_Beans(self):

        # Input and expected result.
        test_input_title = "Hanover Beans"
        test_input_description = "15.5-oz. can (Where Available)Chick Peas, Black or DarkLimit 4 Per VarietyYOU SAVE 20¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hanover Beans 15.5 oz can Chick Peas Black or Dark"

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

    def test_Progresso_Organic_Soup(self):

        # Input and expected result.
        test_input_title = "Progresso Organic Soup"
        test_input_description = "14 to 14.3-oz. can, Any VarietyLimit 4 Per VarietyYOU SAVE 40¢$1.00 OFF with Digital Coupon at shoprite.comLimit 1"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Progresso Organic Soup 14 to 14.3 oz can"

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

    def test_Barilla_Lasagne(self):

        # Input and expected result.
        test_input_title = "Barilla Lasagne"
        test_input_description = "12-oz. to 1-lb. box, Any Variety of Protein Plus,Collezione or Gluten Free or 8-oz. to 1-lb., OvenReady Lasagne, Manicotti, Jumbo ShellsLimit 4 Per VarietySAVE UP TO 39¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Barilla Lasagne 12 oz to 1 lb box 8 oz to 1 lb Lasagne Manicotti Jumbo Shells"

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

    def test_Delverde_Pasta(self):

        # Input and expected result.
        test_input_title = "Delverde Pasta"
        test_input_description = "8.8-oz. to 16-oz. bag, Any Variety,Angel Hair Pasta NestsLimit 4 OffersMUST BUY 3Additionalor lesserquantitieswill scan at3 for $5.97,$1.00 OFF 3 with Digital Coupon at shoprite.comMust Buy 3Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Delverde Pasta 8.8 oz to 16 oz bag Angel Hair Pasta Nests."

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

    def test_Bertolli_Pasta_Sauce(self):

        # Input and expected result.
        test_input_title = "Bertolli Pasta Sauce"
        test_input_description = "15-oz. jar, Any Variety, Alfredo or 24-oz. (ExcludingOrganic, Riserva & Rustic Cut) RedLimit 4 Per VarietyYOU SAVE 20¢30¢ OFF with Digital Coupon at shoprite.comLimit 1"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bertolli Pasta Sauce 15 oz jar Alfredo or 24 oz Excludingorganic Riserva & Rustic Cut Red"

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

    def test_Carolina_Jasmine_Rice(self):

        # Input and expected result.
        test_input_title = "Carolina Jasmine Rice"
        test_input_description = "5-lb. bagLimit 4YOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Carolina Jasmine Rice 5 lb bag"

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

    def test_Carolina_Rice(self):

        # Input and expected result.
        test_input_title = "Carolina Rice"
        test_input_description = "20-lb. bag, Original or GoldLimit 4 Per VarietyYOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Carolina Rice 20 lb bag Original or Gold"

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

    def test_Utz_Snacks(self):

        # Input and expected result.
        test_input_title = "Utz Snacks"
        test_input_description = "9 to 10-oz. bag (Where Available) AnyVariety, Potato Chips, 14 to 16-oz.Pretzels or 9.5 to 12.5-oz. (ExcludingMulti Grain) Tortilla Chips"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Utz Snacks 9 to 10 oz bag Potato Chips 14 to 16 ozPretzels or 9.5 to 12.5 oz Excludingmulti Grain Tortilla Chips"

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

    def test_Rold_Gold_Pretzels(self):

        # Input and expected result.
        test_input_title = "Rold Gold Pretzels"
        test_input_description = "10 to 16-oz. bag, Any Variety$1.00 OFF 2 with Digital Coupon at shoprite.comMust Buy 2Limit 1 Offer"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rold Gold pretzels 10 to 16 oz bag"

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

    def test_Deep_River_Snacks(self):

        # Input and expected result.
        test_input_title = "Deep River Snacks"
        test_input_description = "8-oz. Bag, Any VarietyWhereAvailable,WhileSuppliesLast"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Deep River Snacks 8 oz bag"

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

    def test_Samuel_Adams_Boston_Lager_6_pack(self):

        # Input and expected result.
        test_input_title = "Samuel Adams Boston Lager 6 pack"
        test_input_description = "12-oz. Btls., Seasonal, Rebel IPA, Rebel Grapefruit IPA, Rebel Juiced IPA, Cherry WalnutLimit 4 Offers.Discount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Samuel Adams Boston Lager 6 pack 12 oz btls Seasonal Rebel IPA Rebel Grapefruit IPA Rebel Juiced IPA Cherry Walnut"

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

    def test_Brooklyn_Lager_6_pack(self):

        # Input and expected result.
        test_input_title = "Brooklyn Lager 6 pack"
        test_input_description = "12-oz. Btls., Seasonal, East India Pale Ale, Brown Ale, Green Market Wheat Discount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Brooklyn Lager 6 pack 12 oz btls Seasonal East india Pale Ale Brown Ale Green Market Wheat"

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

    def test_Peroni_6_pack(self):

        # Input and expected result.
        test_input_title = "Peroni 6 pack"
        test_input_description = "11.2-oz. Btls.Discount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Peroni 6 pack 11.2 oz btls"

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

    def test_Captain_Lawrence_Pale_Ale_6_pack(self):

        # Input and expected result.
        test_input_title = "Captain Lawrence Pale Ale 6 pack"
        test_input_description = "12-oz. Btls., Liquid Gold, Kolsch, Pumpkin AleDiscount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Captain Lawrence Pale Ale 6 pack 12 oz btls liquid Gold Kolsch Pumpkin Ale"

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

    def test_Fat_Tire_6_pack(self):

        # Input and expected result.
        test_input_title = "Fat Tire 6 pack"
        test_input_description = "12-oz. Btls.Discount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Fat Tire 6 pack 12 oz btls"

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

    def test_Goose_Island_Seasonal_6_pack(self):

        # Input and expected result.
        test_input_title = "Goose Island Seasonal 6 pack"
        test_input_description = "12-oz. Btls., IPA, Oktoberfest, Four Star PilsnerDiscount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Goose Island Seasonal 6 pack 12 oz btls IPA Oktoberfest Four Star Pilsner"

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

    def test_Blue_Point_Toasted_Lager_6_pack(self):

        # Input and expected result.
        test_input_title = "Blue Point Toasted Lager 6 pack"
        test_input_description = "12-oz. Btls.Discount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Blue Point Toasted Lager 6 pack 12 oz btls"

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

    def test_Blue_Moon_Belgian_White_6_pack(self):

        # Input and expected result.
        test_input_title = "Blue Moon Belgian White 6 pack"
        test_input_description = "12-oz. Btls., Seasonal, White IPADiscount will be appliedwhen you buy inincrements of 2 only.Less or additionalitems will scan at$9.99 each.Limit 4 Offers.Super Sampler Event!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Blue Moon Belgian White 6 pack 12 oz btls Seasonal White IPA"

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

    def test_Blue_Moon_Belgian_White_12_pack(self):

        # Input and expected result.
        test_input_title = "Blue Moon Belgian White 12 pack"
        test_input_description = "12-oz. Cans/Btls., Variety, Seasonal"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Blue Moon Belgian White 12 pack 12 oz cans btls"

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

    def test_12_Price_Good_Cook_Red_Ceramic(self):

        # Input and expected result.
        test_input_title = "1/2 Price Good Cook Red Ceramic"
        test_input_description = "Any Variety White Reg. Retails: $4.99 to $19.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Good Cook Red Ceramic White"

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

    def test_12_PRICE_Good_Cook_Everyday_Saute_Pans(self):

        # Input and expected result.
        test_input_title = "1/2 PRICE Good Cook Everyday Saute Pans"
        test_input_description = "7 3/4”,10” or 11 3/4”Reg. Retails: $11.99 to $17.98 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Good Cook Everyday Saute Pans 7 3/4\"10\" or 11 3/4\""

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

    def test_12_PRICE_Handi_Foil(self):

        # Input and expected result.
        test_input_title = "1/2 PRICE Handi Foil"
        test_input_description = "Assorted Varieties(Excluding Aluminum Foil)Reg. Retails: $1.99 to $8.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Handi Foil Excluding Aluminum Foil"

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

    def test_25_OFF_Good_Cook_Sauce_Pans(self):

        # Input and expected result.
        test_input_title = "25% OFF Good Cook Sauce Pans"
        test_input_description = "2-qt. 3-qt. or 5-qt., Classics SaucePans or 1.5-qt. or 2-qt. Kitchen BasicsReg. Retails: $11.99 to $29.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Good Cook Sauce Pans 2 qt 3 qt or 5 qt Classics Saucepans or 1.5 qt or 2 qt Kitchen Basics"

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

    def test_Good_Cook_Stainless_Steel_Dutch_Oven(self):

        # Input and expected result.
        test_input_title = "Good Cook Stainless Steel Dutch Oven"
        test_input_description = "Model No. 06009,t5-qt. with Lid save $5.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Good Cook Stainless Steel Dutch Oven"

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

    def test_Melitta_Coffee_Filters(self):

        # Input and expected result.
        test_input_title = "Melitta Coffee Filters"
        test_input_description = "200-ct., White and Jr. White (Excluding Brown) Basket CoffeeFilter or 40-ct., #1, 2, 4 or White or Brown Cone Filters"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Melitta Coffee Filters 200 ct White and jr White Excluding Brown Basket Coffeefilter or 40 ct 1 2 4 or White or Brown Cone Filters"

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

    def test_Rubbermaid_Oval_Party_Platter(self):

        # Input and expected result.
        test_input_title = "Rubbermaid Oval Party Platter"
        test_input_description = "Party Platter SAVE $3.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rubbermaid Oval Party Platter Party Platter"

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

    def test_Rubbermaid_Party_Serving_Kit(self):

        # Input and expected result.
        test_input_title = "Rubbermaid Party Serving Kit"
        test_input_description = "Multi Use Container SAVE $8.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rubbermaid Party Serving Kit Multi Use container"

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

    def test_Stainless_Steel_Water_Bottles(self):

        # Input and expected result.
        test_input_title = "Stainless Steel Water Bottles"
        test_input_description = "15 to 18-oz., Manna of Core Bamboo Limit 4Per Variety YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stainless Steel Water bottles 15 to 18 oz Manna of Core Bamboo"

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

    def test_Quickie_Auto_Sponge_Mop(self):

        # Input and expected result.
        test_input_title = "Quickie Auto Sponge Mop"
        test_input_description = "Original, #045Limit 4Per Variety YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Quickie Auto Sponge Mop Original 045"

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

    def test_Quickie_Large_Angle_Broom(self):

        # Input and expected result.
        test_input_title = "Quickie Large Angle Broom"
        test_input_description = "OriginalLimit 4Per Variety YOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Quickie Large Angle Broom Original"

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

    def test_Kodak_Xtralife_Batteries_(self):

        # Input and expected result.
        test_input_title = "Kodak Xtralife Batteries."
        test_input_description = "24-ct., AA or AAA, Alkaline(Excluding 24-ct. Kodak Max)Limit 4 Per Variety YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kodak Batteries. 24 ct AA or AAA Alkalineexcluding 24 ct Kodak Max"

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

    def test_Lysol_Twist_Mop(self):

        # Input and expected result.
        test_input_title = "Lysol Twist Mop"
        test_input_description = "Limit 4 YOU SAVE $3.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lysol Twist Mop"

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

    def test_Lysol_Scrubber_Sponge(self):

        # Input and expected result.
        test_input_title = "Lysol Scrubber Sponge"
        test_input_description = "4-ct., Heavy Duty or Multi-PurposeLimit 4Per Variety YOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lysol Scrubber Sponge 4 ct Heavy Duty or Multi-Purpose"

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

    def test_ShopRite_Latex_Gloves(self):

        # Input and expected result.
        test_input_title = "ShopRite Latex Gloves"
        test_input_description = "1 pair bag, Small, Medium, Large(Excluding Long Cuff)1/2 PRICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Latex Gloves 1 Pair bag Small Medium Largeexcluding Long Cuff"

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

    def test_25_OFF_Comet_Sponges(self):

        # Input and expected result.
        test_input_title = "25% OFF Comet Sponges"
        test_input_description = "Non-Scratch or Heavy Duty, Comet Cellulose Scrub Sponges, 2 to 6-ct.,Assorted Wipes, Pads or Comet Scrubbing Sponges (Excluding Cleanser)Reg. Retails: $1.29 to $1.99 ea.Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Comet Sponges Non-Scratch or Heavy Duty Comet Cellulose Scrub Sponges 2 to 6 ct Wipes Pads or Comet Scrubbing Sponges Excluding Cleanser"

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

    def test_One_Subject_Notebook(self):

        # Input and expected result.
        test_input_title = "One Subject Notebook"
        test_input_description = "70 sht. ct., College or Wide Rule, Assorted Colors(Excluding Mead iScholar Poly and Fashion)LESS THAN 1/2 PRICE Limit 10 Per Variety YOU SAVE 47¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "One Subject Notebook 70 sht ct College or Wide Rule Excluding Mead Ischolar Poly and Fashion"

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

    def test_iScholar_1_View_Binder(self):

        # Input and expected result.
        test_input_title = "iScholar 1” View Binder"
        test_input_description = "Assorted ColorsLimit 4 Per Variety YOU SAVE 25¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ischolar 1\" View Binder"

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

    def test_Ticonderoga_Pencils(self):

        # Input and expected result.
        test_input_title = "Ticonderoga Pencils"
        test_input_description = "12-ct. pkg., #2SAVE $1.30"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ticonderoga Pencils 12 ct pkg 2"

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

    def test_Elmers_School_Glue_Stick(self):

        # Input and expected result.
        test_input_title = "Elmers School Glue Stick"
        test_input_description = "1.26-oz. tot. wt. pkg. 6-Pack WashableLimit 4 Per Variety YOU SAVE $1.20"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Elmers School Glue Stick 1.26 oz tot wt pkg 6 pack Washable"

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

    def test_Kodak_Xtralife_Batteries(self):

        # Input and expected result.
        test_input_title = "Kodak Xtralife Batteries"
        test_input_description = "1-ct. 9-Volt, 2-ct. C or D, 4-ct. AAA orAA, Alkaline"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kodak Batteries 1 ct 9-Volt 2 ct C or D 4 ct AAA or AA Alkaline"

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

    def test_Kodak_Flashlight(self):

        # Input and expected result.
        test_input_title = "Kodak Flashlight"
        test_input_description = "Ultra Bright LED 1000mwIncludes Batteries YOU SAVE $1.00 Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kodak flashlight Ultra Bright Led 1000 mw"

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

    def test_Madison_Luxury_Home_Microfiber_Sheets_Sets(self):

        # Input and expected result.
        test_input_title = "Madison Luxury Home Microfiber Sheets Sets"
        test_input_description = "Full, Queen or King, Wrinkle Free, Stain Resistant, Deep Pockets,Microfiber, Assorted Colors (Where Available, While Supplies Last) LESS THAN 1/2 PRICE“EXCLUSIVELY at ShopRite”Where available, while supplies last"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Madison Luxury Home Microfiber Sheets Sets Full Queen or King \""

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

    def test_Madison_Luxury_Home_BedInBag(self):

        # Input and expected result.
        test_input_title = "Madison Luxury Home Bed-In-Bag"
        test_input_description = "Queen or King, Assorted Color and Designs,Contains: 2-Decorative Pillows, 2-ct. Pillow Shams and 4-Pc. Sheet SetLimit 4 Per Variety YOU SAVE $20.00 “EXCLUSIVELY at ShopRite”Where available, while supplies last"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Madison Luxury Home Bed-In-Bag Queen or King contains 2-Decorative Pillows 2 ct Pillow Shams and 4 pc Sheet Set \""

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

    def test_Breast_Cancer_Socks(self):

        # Input and expected result.
        test_input_title = "Breast Cancer Socks"
        test_input_description = "(Where Available, While Supplies Last)1/2 price"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Socks"

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

    def test_Breast_Cancer_Socks_(self):

        # Input and expected result.
        test_input_title = "Breast Cancer Socks."
        test_input_description = "Knock The Socks Off Breast Cancer,By Sock Bureau, Lounge and Fluffy(Where Available, While Supplies Last)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Socks. By Sock Bureau Lounge and fluffy"

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

    def test_Breast_Cancer_Gripper_Socks(self):

        # Input and expected result.
        test_input_title = "Breast Cancer Gripper Socks"
        test_input_description = "2-Pk.(Where Available,While Supplies Last) SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gripper Socks 2 pk"

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

    def test_Breast_Cancer_Awareness_World_of_Active_Yoga_Leggings(self):

        # Input and expected result.
        test_input_title = "Breast Cancer Awareness World of Active Yoga Leggings"
        test_input_description = "Small - XLarge, Black or Pink (Where Available, While Supplies Last)SAVE $5.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Active Yoga Leggings Small - Xlarge Black or Pink"

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

    def test_National_Breast_Cancer_Foundation_Minky_Pants(self):

        # Input and expected result.
        test_input_title = "National Breast Cancer Foundation Minky Pants"
        test_input_description = "Medium to XXLargeSAVE $5.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Minky Pants Medium to Xxlarge"

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

    def test_Brita_3_Pack_Water_Filters(self):

        # Input and expected result.
        test_input_title = "Brita 3 Pack Water Filters"
        test_input_description = "3-ct., Fits All Brita Pitchers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Brita 3 pack Water Filters 3 ct"

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

    def test_1_00_OFF_Garnier_Olia_Hair_Color(self):

        # Input and expected result.
        test_input_title = "$1.00 OFF Garnier Olia Hair Color"
        test_input_description = "Any Variety,$1.00 OFF With Digital Coupon At shoprite.com Limit 1,Limit 4 Per Variety, Reg.: $7.99 to $8.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Garnier Olia Hair Color"

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

    def test_1_00_OFF_Garnier_Nutrisse_Hair_Color(self):

        # Input and expected result.
        test_input_title = "$1.00 OFF Garnier Nutrisse Hair Color"
        test_input_description = "Any Variety$1.00 OFF With Digital Coupon At shoprite.com Limit 1,Limit 4 Per Variety, Reg.: $7.99 to $8.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Garnier Nutrisse Hair Color"

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

    def test_OGX_Body_Wash(self):

        # Input and expected result.
        test_input_title = "OGX Body Wash"
        test_input_description = "19.5-fl. oz., Any Variety, Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ogx Body Wash 19.5 fl oz"

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

    def test_OGX_Hair_Care(self):

        # Input and expected result.
        test_input_title = "OGX Hair Care"
        test_input_description = "3.3 to 13-oz., Stylers, Conditioner and Shampoo(Excluding Moroccan Oil and 3.3-oz. Keratin Treatment)Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ogx Hair Care 3.3 to 13 oz Stylers Conditioner and Shampooexcluding Moroccan Oil and 3.3 oz Keratin Treatment"

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

    def test_TRESemm_Perfectly_Undone_Shampoo(self):

        # Input and expected result.
        test_input_title = "TRESemmé Perfectly Undone Shampoo"
        test_input_description = "4.3-oz., Volume Dry Shampoo or 25-fl. oz. btl., Naturals, Keratin Smooth or Conditioner, Limit 4Per Variety, SAVE 40¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tresemme Perfectly Undone Shampoo 4.3 oz Volume Dry Shampoo or 25 fl oz btl Naturals Keratin Smooth or Conditioner"

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

    def test_TREsemm_Aerosol_Hair_Spray(self):

        # Input and expected result.
        test_input_title = "TREsemmé Aerosol Hair Spray"
        test_input_description = "11-oz., Assorted Varieties (Excluding 14.6-oz.)Limit 4Per Variety, SAVE 40¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tresemme Aerosol Hair Spray 11 oz Excluding 14.6 oz"

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

    def test_VO5_Shampoo_or_Conditioner(self):

        # Input and expected result.
        test_input_title = "VO5 Shampoo or Conditioner"
        test_input_description = "12.5 to 15-fl. oz., Assorted Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Vo5 Shampoo or Conditioner 12.5 to 15 fl oz"

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

    def test_1_00_OFF_LOreal_Root_Cover_Up(self):

        # Input and expected result.
        test_input_title = "$1.00 OFF L’Oreal Root Cover Up"
        test_input_description = "2-oz., Any ShadeLimit 4Per Variety, Regular Retails: $5.99 to $9.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Loreal Root Cover Up 2 oz"

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

    def test_1_00_OFF_LOreal_Root(self):

        # Input and expected result.
        test_input_title = "$1.00 OFF L’Oreal Root"
        test_input_description = "Assorted Shades, Limit 4Per Variety, Regular Retails: $5.99 to $9.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Loreal Root"

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

    def test_25_OFF_J_R__Watkins_Skin_Care(self):

        # Input and expected result.
        test_input_title = "25% OFF J.R. Watkins Skin Care"
        test_input_description = "3.3 to 18-oz., Body Wash, Cream,Foam or Liquid Hand Soap or Lotion(Excluding Baby) Limit 4Per Variety, $1.00 OFF WITH DIGITAL COUPON AT SHOPRITE.COM LIMIT 1, Reg.: $4.99 to $9.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "J.R. Watkins Skin Care 3.3 to 18 oz Body Wash Creamfoam or liquid Hand Soap or Lotionexcluding Baby"

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

    def test_Yes_To_Facial_Wipes(self):

        # Input and expected result.
        test_input_title = "Yes To Facial Wipes"
        test_input_description = "30-ct., Cucumber or Charcoal, Limit 4Offers, MUSTBUY 2 Additionalor lesserquantitieswill scan at$5.00 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Facial Wipes 30 ct Cucumber or Charcoal"

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

    def test_QTips(self):

        # Input and expected result.
        test_input_title = "Q-Tips"
        test_input_description = "500-ct.. Cotton Swabs, Limit 4, SAVE 30¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Q-Tips 500 ct Cotton Swabs"

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

    def test_Hask_Shampoos__Conditioners(self):

        # Input and expected result.
        test_input_title = "Hask Shampoos & Conditioners"
        test_input_description = "(12oz)Limit 4 Per Variety, SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hask Shampoos & Conditioners 12Oz"

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

    def test_Hask_Shine_oils__Deep_Conditioners(self):

        # Input and expected result.
        test_input_title = "Hask Shine oils & Deep Conditioners"
        test_input_description = "(5/8oz - 1.75oz)Limit 4 Per Variety, save 30¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hask Shine Oils & Deep Conditioners 5/8Oz - 1.75Oz"

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

    def test_Colgate_Enamel_Health_Toothpaste(self):

        # Input and expected result.
        test_input_title = "Colgate Enamel Health Toothpaste"
        test_input_description = "4-oz.Discount will be applied when youbuy in increments of 3 only. Less oradditional items willscan at $2.99 each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate Enamel Health Toothpaste 4 oz"

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

    def test_Colgate_360_Enamel_Health_Toothbrush(self):

        # Input and expected result.
        test_input_title = "Colgate 360º Enamel Health Toothbrush"
        test_input_description = "1-ct.Discount will be applied when youbuy in increments of 3 only. Less oradditional items willscan at $2.99 each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate 360 Enamel Health Toothbrush 1 ct"

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

    def test_Colgate_Enamel_Health_Mouthwash(self):

        # Input and expected result.
        test_input_title = "Colgate Enamel Health Mouthwash"
        test_input_description = "8.4-oz.Discount will be applied when youbuy in increments of 3 only. Less oradditional items willscan at $2.99 each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate Enamel Health Mouthwash 8.4 oz"

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

    def test_Softsoap_Hand_Soap_Refill(self):

        # Input and expected result.
        test_input_title = "Softsoap Hand Soap Refill"
        test_input_description = "56-oz. btl., Any Variety, LiquidDiscount will be applied when youbuy in increments of 3 only.Less or additional items willscan at $3.99 each. Limit 4 Offers, Look for 50¢ OFF MFRCoupon in Most Sunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Softsoap Hand Soap Refill 56 oz btl liquid"

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
        test_input_description = "15 to 18-oz. btl., Any VarietyDiscount will be applied when youbuy in increments of 3 only.Less or additional items willscan at $3.99 each. Limit 4 Offers, Look for 50¢ OFF MFRCoupon in Most Sunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Softsoap Body Wash 15 to 18 oz btl"

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

    def test_Irish_Spring_Bath_Soap_8_pack(self):

        # Input and expected result.
        test_input_title = "Irish Spring Bath Soap 8 pack"
        test_input_description = "30-oz. tot. wt. pkg., Any VarietyDiscount will be applied when youbuy in increments of 3 only.Less or additional items willscan at $3.99 each. Limit 4 Offers, Look for 50¢ OFF MFRCoupon in Most Sunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Irish Spring Bath Soap 8 pack 30 oz tot wt pkg"

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

    def test_Irish_Spring_Body_Wash(self):

        # Input and expected result.
        test_input_title = "Irish Spring Body Wash"
        test_input_description = "18-oz. btl., Assorted Varieties (Excluding Signature)Discount will be applied when youbuy in increments of 3 only.Less or additional items willscan at $3.99 each. Limit 4 Offers, Look for 50¢ OFF MFRCoupon in Most Sunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Irish Spring Body Wash 18 oz btl Excluding Signature"

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

    def test_Mennen_or_Lady_Speed_Stick_Twin_Pack(self):

        # Input and expected result.
        test_input_title = "Mennen or Lady Speed Stick Twin Pack"
        test_input_description = "4.6 to 6-oz. Gel, Solid or Invisible Solid, Ladie’s or Men’s Light, Sport, Alpine, Orchard Blossom, Shower Fresh or Powder, DeodorantDiscount will be applied when youbuy in increments of 3 only.Less or additional items willscan at $3.99 each. Limit 4 Offers, Look for 50¢ OFF MFRCoupon in Most Sunday Papers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mennen or Lady Speed Stick Twin pack 4.6 to 6 oz Gel Solid or invisible Solid Ladies or Mens Light Sport Alpine Orchard Blossom Shower Fresh or Powder Deodorant"

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

    def test_Colgate_Toothpaste(self):

        # Input and expected result.
        test_input_title = "Colgate Toothpaste"
        test_input_description = "2.5 to 2.8-oz., White Mint Zing, Baking Soda andPeroxide Whitening, Tartar Protection and Regular(Excluding 2.8-oz. Max Fresh)Discount will be applied when you buy inincrements of 3 only. Less or additionalitems will scan at 88¢ each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate Toothpaste 2.5 to 2.8 oz White Mint Zing Baking Soda Andperoxide Whitening Tartar protection and Regularexcluding 2.8 oz Max Fresh"

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

    def test_Colgate_Toothbrush(self):

        # Input and expected result.
        test_input_title = "Colgate Toothbrush"
        test_input_description = "1-ct., Firm, Soft or Medum,Extra CleanDiscount will be applied when you buy inincrements of 3 only. Less or additionalitems will scan at 88¢ each. Limit 4 Offers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Colgate Toothbrush 1 ct Firm Soft or Medum"

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

    def test_Schick_Quattro_Disposable_Razor___(self):

        # Input and expected result.
        test_input_title = "Schick Quattro Disposable Razor..."
        test_input_description = "Buy 1 Schick Quattro Disposable Razor3-ct., Men’s or Women’s, Schick Slim Twin Razor12-ct., Regluar, Sensitive, Women’s or Dry Skin, Disposable, Schick Xtreme 3-Razors $5.99 And Buy 1 Edge Shave Gel7-oz. Assorted Varieties (Excluding EdgeInfused and Edge Energy) Skintimate Shave Gel7-oz. Assorted Varieties (Excluding Tropical Splash) $2.99SAVE AT CHECKOUT $3.00 MUST BUY both To Receive Discount with Price Plus Card Limit 4 Offers, $1.00 OFF WITH DIGITAL COUPON AT SHIOPRITE.COM LIMIT 1"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Schick Quattro Disposable Razor. 3 ct"

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

    def test_Carefree_Shields(self):

        # Input and expected result.
        test_input_title = "Carefree Shields"
        test_input_description = "42 to 60-ct., Any Variety, Limit 4Per Variety, SAVEUP TO 49¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Carefree Shields 42 to 60 ct"

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

    def test_Stayfree_Maxi_Pads(self):

        # Input and expected result.
        test_input_title = "Stayfree Maxi Pads"
        test_input_description = "16 to 24-ct. pkg., AssortedVarieties (Excluding 22-ct.Stayfree Ultra Thin)Limit 4Per Variety, SAVEUP TO 49¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Stayfree Maxi Pads 16 to 24 ct pkg Excluding 22 ctStayfree Ultra Thin"

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

    def test_25_OFF_Johnsons_Baby_Toiletries(self):

        # Input and expected result.
        test_input_title = "25% OFF Johnson’s Baby Toiletries"
        test_input_description = "16-oz. Desitin Original Jar, 6.5 to 22-oz. AssortedVarieties, Bath, Oil, Powder, Lotion or Shampoo(Excluding 7-fl. oz. Shampoo, 9-fl. oz., Head-To-Toe,25-ct. Face Wipe and 55-ct., Safety Swabs) Limit 4Per Variety, Reg.: $3.99 to $13.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Johnsons Baby Toiletries 16 oz Desitin Original jar 6.5 to 22 oz Bath Oil Powder Lotion or Shampooexcluding 7 fl oz Shampoo 9 fl oz Head-To-Toe25 ct Face Wipe and 55 ct Safety Swabs"

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

    def test_U_by_Kotex_Security(self):

        # Input and expected result.
        test_input_title = "U by Kotex Security"
        test_input_description = "U by Kotex Pads 1424 ct.,U by Kotex Liners 4064 ct. orU by Kotex Tampons 18 ct.Limit 4 Per Variety, LOOK FOR $1.00 OFF, MFR coupon inmost Sunday papers Registered Trademark or * Trademark of Kimberly-Clark Worldwide, Inc. KCWW."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "U By Kotex Security U By Kotex Pads 1424 ctU By Kotex Liners 4064 ct Oru By Kotex Tampons 18 ct"

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

    def test_U_by_Kotex(self):

        # Input and expected result.
        test_input_title = "U by Kotex"
        test_input_description = "U by Kotex Pads 1618 ct., orU by Kotex Tampons 18 ct.Limit 4 Per Variety, LOOK FOR $1.00 OFF, MFR coupon inmost Sunday papers Registered Trademark or * Trademark of Kimberly-Clark Worldwide, Inc. KCWW."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "U By Kotex Pads 1618 ct Oru By Kotex Tampons 18 ct"

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

    def test_U_by_Kotex_FITNESS(self):

        # Input and expected result.
        test_input_title = "U by Kotex FITNESS*"
        test_input_description = "U by Kotex FITNESS* Pads 2634 ct.,Liners 80 ct. or Tampons 3134 ct.,U by Kotex Security Pads 4056 ct.or U by Kotex Liners 112 ct.Limit 4 Per Variety, LOOK FOR $1.00 OFF, MFR coupon inmost Sunday papers Registered Trademark or * Trademark of Kimberly-Clark Worldwide, Inc. KCWW."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "U By Kotex Fitness Pads 2634 ctLiners 80 ct or Tampons 3134 ctU By Kotex Security Pads 4056 ctOr U By Kotex Liners 112 ct"

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

    def test_Depends_Pant(self):

        # Input and expected result.
        test_input_title = "Depends Pant"
        test_input_description = "10 to 21-ct., Refastenable, Small/Medium, Large orExtra Large, Maximum Absorbency, Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Depends Pant 10 to 21 ct"

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

    def test_Poise_Pads(self):

        # Input and expected result.
        test_input_title = "Poise Pads"
        test_input_description = "27 to 64-ct., Assorted Varieties (Excluding 64-ct.Long and 45-ct. Ultimate)Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Poise Pads 27 to 64 ct Excluding 64 ctLong and 45 ct Ultimate"

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

    def test_Poise_Impression(self):

        # Input and expected result.
        test_input_title = "Poise Impression"
        test_input_description = "10-ct.Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Poise Impression 10 ct"

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

    def test_Rolaids_Chewable_Tablets(self):

        # Input and expected result.
        test_input_title = "Rolaids Chewable Tablets"
        test_input_description = "72-ct. Ultra Strength or 96-ct. Extra Strength,Mint or Fruit Flavors or 150-ct. Tablets, Limit 4Per Variety, SAVE $1.95, 1/2 PRICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Rolaids Chewable Tablets 72 ct Ultra Strength or 96 ct Mint or Fruit flavors or 150 ct Tablets"

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

    def test_1_00_OFF_Mucinex(self):

        # Input and expected result.
        test_input_title = "$1.00 OFF Mucinex"
        test_input_description = "0.75-oz. Nasal Spray, 6-oz. or 9-oz. Adult Liquids, 14 to 40-ct.Assorted Varieties (Excluding Pediatrics, Mucinex D, 14-ct. DMMaximum Strength, 20-ct. DM Expectant & Cough Suppressant,20-ct. 12-HR Expectorant and 68-ct. Expectorant)Limit 4Per Variety, Reg.: $9.69 to $22.99 ea."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mucinex 0.75 oz Nasal Spray 6 oz or 9 oz Adult liquids 14 to 40 ct Excluding Pediatrics Mucinex D 14 ct Dmmaximum Strength 20 ct Dm Expectant & Cough Suppressant20 ct 12-Hr Expectorant and 68 ct Expectorant"

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

    def test_ShopRite_First_Aid_Liquids(self):

        # Input and expected result.
        test_input_title = "ShopRite First Aid Liquids"
        test_input_description = "2-fl. oz. Itch Relief Spray, 6-fl. oz. CalamineLotion, 16-fl. oz. Peroxide, Alcohol or WitchHazel, 32-fl. oz. Alcohol or Peroxide, Limit 4Per Variety"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite First Aid liquids 2 fl oz Itch Relief Spray 6 fl oz Calaminelotion 16 fl oz Peroxide Alcohol or Witchhazel 32 fl oz Alcohol or Peroxide"

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

    def test_5Hour_Energy_Drink(self):

        # Input and expected result.
        test_input_title = "5-Hour Energy Drink"
        test_input_description = "11.58-oz. tot. wt. pkg., 6-pk, Sour Apple orBerry (Excluding Pink Lemon)Limit 4 Per Variety, SAVEUP TO$3.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "5-Hour Energy Drink 11.58 oz tot wt pkg 6 pk Sour Apple Orberry Excluding Pink Lemon"

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

    def test_5Hour_Energy_Extra_Strength(self):

        # Input and expected result.
        test_input_title = "5-Hour Energy Extra Strength"
        test_input_description = "11.58-fl. oz. tot. wt. pkg., 6-pk, Limit 4Per Variety, SAVEUP TO$3.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "5-Hour Energy 11.58 fl oz tot wt pkg 6 pk"

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

    def test_Yellow_Cherry_Tomatoes(self):

        # Input and expected result.
        test_input_title = "Yellow Cherry Tomatoes"
        test_input_description = "Produce Pick of the Week10.5-oz. pkg.Yellow tomatoes are sweeter in taste than traditional redtomatoes and still provide a good dose of vitamin C.Did you know tomatoes taste best when not refrigerated?"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Yellow Cherry Tomatoes 10.5 oz pkg"

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

    def test_Kiwi_Fruit_4_Lb_package(self):

        # Input and expected result.
        test_input_title = "Kiwi Fruit 4 Lb package"
        test_input_description = "ItalianClub Size SavingsNO Membership Feesfor additional savings, visitshoprite.com/clubsizesavings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kiwi Fruit 4 lb package"

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

    def test_ShopRite_Sliced_Baby_Bella_Mushrooms(self):

        # Input and expected result.
        test_input_title = "ShopRite Sliced Baby Bella Mushrooms"
        test_input_description = "16-oz. pkg. FreshClub Size SavingsNO Membership Feesfor additional savings, visitshoprite.com/clubsizesavings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Shoprite Sliced Baby Bella Mushrooms 16 oz pkg"

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

    def test_Mini_Sweet_Mixed_Peppers(self):

        # Input and expected result.
        test_input_title = "Mini Sweet Mixed Peppers"
        test_input_description = "2-lb. bag FreshClub Size SavingsNO Membership Feesfor additional savings, visitshoprite.com/clubsizesavings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mini Sweet Mixed Peppers 2 lb bag"

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

    def test_Autumn_Magic_Bouquet(self):

        # Input and expected result.
        test_input_title = "Autumn Magic Bouquet"
        test_input_description = "A Seasonal Assortment ofFresh Cut FlowersLimit 4 OffersYOU SAVE $1.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Autumn Magic Bouquet Fresh Cut flowers"

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

    def test_Hardy_Mum_or_Aster_Plant(self):

        # Input and expected result.
        test_input_title = "Hardy Mum or Aster Plant"
        test_input_description = "8 Pot, Reblooms Yearly fora Beautiful Garden of ColorLimit 4OffersMUSTBUY 3Additionalor lesserquantitieswill scan at$4.69 ea"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hardy Mum or Aster Plant 8 Pot"

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

    def test_Mum_Buddy_Celosia_Plant(self):

        # Input and expected result.
        test_input_title = "Mum Buddy Celosia Plant"
        test_input_description = "8- inch pot, Great Colorfor Your GardenLimit 4OffersMUSTBUY 3Additionalor lesserquantitieswill scan at$4.69 ea"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mum Buddy Celosia Plant 8 inch Pot"

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

    def test_Mini_Rose_Plant(self):

        # Input and expected result.
        test_input_title = "Mini Rose Plant"
        test_input_description = "4” Pot (459-mL)Will Rebloom YearlyLimit 4OffersYOU SAVE 50¢"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mini Rose Plant 4\" Pot 459 ml"

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

    def test_Autumn_Fresh_Bouquet(self):

        # Input and expected result.
        test_input_title = "Autumn Fresh Bouquet"
        test_input_description = "Seasonal Assortment ofFresh Cut Flowers"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Autumn Fresh Bouquet Fresh Cut flowers"

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

    def test_Hardy_Mum_Plant_in_Deco_Pot(self):

        # Input and expected result.
        test_input_title = "Hardy Mum Plant in Deco Pot"
        test_input_description = "12 Pot, Assorted Colors,Perfect for Your PatioLimit 4OffersYOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hardy Mum Plant in Deco Pot 12 Pot"

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

    def test_Edible_Herb_Plant(self):

        # Input and expected result.
        test_input_title = "Edible Herb Plant"
        test_input_description = "4-Inch Pot, Jersey FreshHerbs, Perfect for Cooking!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Edible Herb Plant 4 inch Pot Jersey Freshherbs"

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

    def test_Hardy_Mum_Hanging_Basket(self):

        # Input and expected result.
        test_input_title = "Hardy Mum Hanging Basket"
        test_input_description = "12 Pot,Assorted ColorsLimit 4OffersYOU SAVE $2.00"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Hardy Mum Hanging Basket 12 Pot"

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

    def test_Mega_Market_Bunches(self):

        # Input and expected result.
        test_input_title = "Mega Market Bunches"
        test_input_description = "Premium Focal Flower Surrounded byFillers In Deco Craft SleevePERFECTFOR ROSHHASHANAHHOLIDAY!Limit 4OffersMUSTBUY 2Additionalor lesserquantitieswill scan at$11.99 ea"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mega Market bunches premium Focal flower"

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

    def test_Signature_Kitchens_Grape_Jelly(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Grape Jelly"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH 18 oz. jar"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Grape Jelly 18 oz jar"

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

    def test_Skippy_Peanut_Butter(self):

        # Input and expected result.
        test_input_title = "Skippy Peanut Butter"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH 15-16.3 oz. jar"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Skippy Peanut Butter 15-16.3 oz jar"

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

    def test_Knorr_Sides(self):

        # Input and expected result.
        test_input_title = "Knorr Sides"
        test_input_description = "Knorr Sides 3.8-5.8 oz. pkg. OR FREE Instantly When you buy 8 Knorr Pasta Sides* $5 value"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Knorr Sides 3.8-5.8 oz pkg"

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

    def test_Tide_Laundry_Detergent(self):

        # Input and expected result.
        test_input_title = "Tide Laundry Detergent"
        test_input_description = " Liquid 46-50 fl. oz.  Pods 20 ct. PLUS DON’T MISS THESE XTRAsavings! ON YOUR HOUSEHOLD FAVORITES!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tide Laundry Detergent liquid 46-50 fl oz Pods 20 ct"

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

    def test_Bounty_Big_Roll(self):

        # Input and expected result.
        test_input_title = "Bounty Big Roll"
        test_input_description = "6 ct. PLUS DON’T MISS THESE XTRAsavings! ON YOUR HOUSEHOLD FAVORITES!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Bounty Big Roll 6 ct"

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

    def test_Turkey_Hill_Ice_Cream_or_Lucerne_Ice_Cream_Bars(self):

        # Input and expected result.
        test_input_title = "Turkey Hill Ice Cream or Lucerne Ice Cream Bars"
        test_input_description = "30-48 fl. oz. pkg. ACME® DON'T MISS THESE XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Turkey Hill Ice Cream or Lucerne Ice Cream Bars 30-48 fl oz pkg"

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

    def test_Signature_Kitchens_Cake_Cup_Ice_Cream_Cones(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Cake Cup Ice Cream Cones"
        test_input_description = "12 ct. pkg. ACME® DON'T MISS THESE XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Cake Cup Ice Cream Cones 12 ct pkg"

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

    def test_Smithfield_Bacon(self):

        # Input and expected result.
        test_input_title = "Smithfield Bacon"
        test_input_description = "12-16 oz. pkg. $5.99 ea.-$1 ea. INSTANT SAVINGS WHEN YOU BUY ANY 4 SAVE $4 INSTANTLY! WHEN YOU BUY 4 PARTICIPATING ITEMS IN A SINGLE TRANSACTION. ACME® DON'T MISS THESE XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Smithfield Bacon 12-16 oz pkg"

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

    def test_Crystal_Farms_Chunk_or_Shredded_Cheese(self):

        # Input and expected result.
        test_input_title = "Crystal Farms Chunk or Shredded Cheese"
        test_input_description = "7-8 oz. pkg. Individual Price $1.99 ea. ACME® DON'T MISS THESE XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Crystal Farms Chunk or Shredded Cheese 7-8 oz pkg"

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

    def test_Lucerne_Half_u0026_Half(self):

        # Input and expected result.
        test_input_title = "Lucerne Half \u0026 Half"
        test_input_description = "16 oz. ctn. Lucerne® DAIRY FARMS SINCE 1904. DOLLAR DAYS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lucerne Half Half 16 oz ctn"

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

    def test_Halloween_DVDs(self):

        # Input and expected result.
        test_input_title = "Halloween DVDs"
        test_input_description = "Offer valid 9/19-9/27 *Participating items must be purchased in a single transaction with Card. Discount taken at the register. Not all varieties available in all stores. Customer pays tax and CRV where applicable. Online and in-store prices, offers and discounts may differ. See store and display for full details."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Halloween DVDs"

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

    def test_MARS_Brand_Fun_Size_Bags(self):

        # Input and expected result.
        test_input_title = "MARS® Brand Fun Size® Bags"
        test_input_description = "FREE TREAT WITH A SCARY MOVIE! Buy select Halloween DVDs for $5.99 ea. DVD AND GET ONE (1) MARS® Brand Fun Size® Bags 9.08 oz. - 11.5 oz., $2.60 Estimated Value (includes: M&MS®, SNICKERS®, TWIX®, 3MUSKETEERS®, and MILKYWAY®) FREE* Offer valid 9/19-9/27 *Participating items must be purchased in a single transaction with Card. Discount taken at the register. Not all varieties available in all stores. Customer pays tax and CRV where applicable. Online and in-store prices, offers and discounts may differ. See store and display for full details. ®/™ trademarks ©Mars, Incorporated 2017"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mars Brand Fun Size bags"

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

    def test_DOZEN_BAGELS(self):

        # Input and expected result.
        test_input_title = "DOZEN BAGELS"
        test_input_description = "CHOOSE YOUR FAVORITES! Bagel Weekend Every Saturday & Sunday! mix or match"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dozen bagels"

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

    def test_Great_American_Burgers(self):

        # Input and expected result.
        test_input_title = "Great American Burgers"
        test_input_description = "32 oz. pkg., beef, angus or turkey, frozen. burger NIGHT!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Great American Burgers 32 oz pkg Beef Angus or Turkey frozen"

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

    def test_Great_American_Beef_Burgers(self):

        # Input and expected result.
        test_input_title = "Great American Beef Burgers"
        test_input_description = "4 lb. box, frozen. burger NIGHT!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Great American Beef Burgers 4 lb box frozen"

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

    def test_Gardein_Meatless_Foods(self):

        # Input and expected result.
        test_input_title = "Gardein Meatless Foods"
        test_input_description = "8.8-12.7 oz. pkg. quick meal ideas"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gardein Meatless Foods 8.8-12.7 oz pkg"

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

    def test_A_traditional_yogurt_by_Chobani(self):

        # Input and expected result.
        test_input_title = "A traditional yogurt by Chobani®"
        test_input_description = "25% less sugar than other traditional yogurts* *Chobani® Smooth: 14g sugar, 11g protein; other traditional yogurts: 19g sugar, 5g protein per 5.3oz serving ©2017 Chobani, LLC"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Chobani Smooth 14G Sugar 11G protein Per 5.3Oz Serving"

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

    def test_DANNON_GREEK_4_PACKS_Oikos_Light_u0026_Fit_Greek_4_Packs(self):

        # Input and expected result.
        test_input_title = "DANNON® GREEK 4 PACKS Oikos, Light \u0026 Fit Greek 4 Packs"
        test_input_description = "21.2 oz. tot. pkg., All varieties Oikos® is a registered trademark of Stonyfield Farm, Inc. ©2017 The Dannon Company, Inc."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dannon Greek 4 packs Oikos Light Fit Greek 4 packs 21.2 oz tot pkg"

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

    def test_VERLASSO_HARMONIOUSLY_RAISED_FISH(self):

        # Input and expected result.
        test_input_title = "VERLASSO™ HARMONIOUSLY RAISED FISH"
        test_input_description = "Verlasso is a premium salmon raised to promote balance between our need and the need of the environment. Maintaining this equilibrium is at the heart of everything we do. Celebrating four years as Monterey Bay Aquarium’s first to be approved ocean raised Atlantic salmon. www.verlasso.com"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Verlasso Harmoniously raised Fish"

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

    def test_Coke_Diet_Coke_or_Sprite(self):

        # Input and expected result.
        test_input_title = "Coke, Diet Coke or Sprite"
        test_input_description = "6-pk., 7.5 fl. oz. cans. beverage SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coke Diet Coke or Sprite 6 pk 7.5 fl oz cans"

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

    def test_Pepsi_Diet_Pepsi_or_Mtn_Dew(self):

        # Input and expected result.
        test_input_title = "Pepsi, Diet Pepsi or Mtn Dew"
        test_input_description = "6-pk., 7.5 fl. oz. cans. beverage SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pepsi Diet Pepsi or Mtn Dew 6 pk 7.5 fl oz cans"

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

    def test_Rag_Old_World_Pasta_Sauce(self):

        # Input and expected result.
        test_input_title = "Ragú Old World Pasta Sauce"
        test_input_description = "24 oz. jar. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ragu Old World Pasta Sauce 24 oz jar"

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

    def test_Rag_Old_World_Pasta_Sauce_(self):

        # Input and expected result.
        test_input_title = "Ragú Old World Pasta Sauce."
        test_input_description = "45 oz. jar. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ragu Old World Pasta Sauce. 45 oz jar"

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

    def test_Capri_Sun_Juice_Pouches(self):

        # Input and expected result.
        test_input_title = "Capri Sun Juice Pouches"
        test_input_description = "10-pk., 6 fl. oz. pkg. excludes organic, 100%, fruit & veggie and super-v. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Capri Sun Juice pouches 10 pk 6 fl oz pkg Excludes Organic 100% Fruit & Veggie and Super-V."

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

    def test_Absolutely_Flatbread(self):

        # Input and expected result.
        test_input_title = "Absolutely Flatbread"
        test_input_description = "4.4-5.29 oz. pkg. GLUTEN FREE. Gluten Free savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Absolutely flatbread 4.4 oz pkg Gluten Free."

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

    def test_Dr__Praegers_Veggie_Burgers(self):

        # Input and expected result.
        test_input_title = "Dr. Praeger’s Veggie Burgers"
        test_input_description = "10 oz. pkg. GLUTEN FREE. Gluten Free savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dr. praegers Veggie Burgers 10 oz pkg Gluten Free."

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

    def test_College_Inn_Broth(self):

        # Input and expected result.
        test_input_title = "College Inn Broth"
        test_input_description = "3.4 fl. oz. pkg. grocery & snack SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "College inn Broth 3.4 fl oz pkg"

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

    def test_Voortman_Wafers(self):

        # Input and expected result.
        test_input_title = "Voortman Wafers"
        test_input_description = "10.6-14.1 oz. pkg. grocery & snack SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Voortman Wafers 10.6-14.1 oz pkg"

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

    def test_Annies_Homegrown_Soup(self):

        # Input and expected result.
        test_input_title = "Annie’s Homegrown Soup"
        test_input_description = "17 oz. pkg. tasty, organic favorites from Annie’s Homegrown “Organic for Everybunny! ” USDA ORGANIC. grocery & snack SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Annies Homegrown Soup 17 oz pkg"

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

    def test_Annies_Deluxe_Macaroni_u0026_Cheese(self):

        # Input and expected result.
        test_input_title = "Annie’s Deluxe Macaroni \u0026 Cheese"
        test_input_description = "10-12 oz. pkg. tasty, organic favorites from Annie’s Homegrown “Organic for Everybunny! ” USDA ORGANIC. grocery & snack SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Annies Deluxe Macaroni Cheese 10-12 oz pkg"

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

    def test_Priority_Bag_Dog_Food(self):

        # Input and expected result.
        test_input_title = "Priority Bag Dog Food"
        test_input_description = "3.5 lb. pkg. NEW LOWER PRICE. Pet Savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Priority bag Dog Food 3.5 lb pkg"

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

    def test_Priority_Bag_Cat_Food(self):

        # Input and expected result.
        test_input_title = "Priority Bag Cat Food"
        test_input_description = "3.15 lb. pkg. NEW LOWER PRICE. Pet Savings"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Priority bag Cat Food 3.15 lb pkg"

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

    def test_Signature_Care_Cotton_Balls_Rounds_or_Swabs(self):

        # Input and expected result.
        test_input_title = "Signature Care Cotton Balls, Rounds or Swabs"
        test_input_description = "80-500 ct. pkg. stock up and SAVE!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Care Cotton Balls Rounds or Swabs 80-500 ct pkg"

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

    def test_Signature_Care_24Hr__Allergy_Tablets(self):

        # Input and expected result.
        test_input_title = "Signature Care 24-Hr. Allergy Tablets"
        test_input_description = "120 ct. pkg. stock up and SAVE!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Care 24-Hr. Allergy Tablets 120 ct pkg"

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

    def test_Freshly_Ground_InStore_Daily_80_Lean_Ground_Beef(self):

        # Input and expected result.
        test_input_title = "Freshly Ground In-Store Daily 80% Lean Ground Beef"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH 3 lbs. or more. Additional quantities $2.88 lb. discount given at register"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Freshly Ground In-Store Daily 80% Lean Ground Beef 3 Lbs or More"

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

    def test_Lancaster_Brand_U_S_D_A__CHOICE_Beef_Tenderloin_Steaks(self):

        # Input and expected result.
        test_input_title = "Lancaster Brand U.S.D.A. CHOICE Beef Tenderloin Steaks"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH cut fresh in-store daily! Lancaster® BRAND PREMIUM BEEF U.S.D.A. CHOICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lancaster Brand U.S.D.A. Tenderloin Steaks Lancaster Brand Premium Beef U.S.D.A. Choice"

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

    def test_Lancaster_Brand_8pc__Fried_or_Grilled_Chicken(self):

        # Input and expected result.
        test_input_title = "Lancaster Brand 8-pc. Fried or Grilled Chicken"
        test_input_description = "2 drumsticks, 2 wings, 2 breasts and 2 thighs Individual Price $5.99 ea. CHEEP CHICKEN WEEK! Lancaster® BRAND. ACME® DON'T MISS THESE XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lancaster Brand 8 pc Fried or Grilled Chicken"

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

    def test_Dietz_u0026_Watson_Originals_Lunchmeats_or_Cheeses(self):

        # Input and expected result.
        test_input_title = "Dietz \u0026 Watson Originals Lunchmeats or Cheeses"
        test_input_description = "4-8 oz., antibiotic free meats or rBst free cheeses. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dietz Watson Originals Lunchmeats or Cheeses 4-8 oz"

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

    def test_DOZEN_BAGELS(self):

        # Input and expected result.
        test_input_title = "DOZEN BAGELS"
        test_input_description = "CHOOSE YOUR FAVORITES! Bagel Weekend mix or match. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Dozen bagels"

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

    def test_Locally_Grown_Honeycrisp_Apples(self):

        # Input and expected result.
        test_input_title = "Locally Grown Honeycrisp Apples"
        test_input_description = "3 lb. bag WE LOVE LOCAL LOCALLY GROWN PRODUCE. XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Locally Grown Honeycrisp Apples 3 lb bag"

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

    def test_Jimmy_Dean_Sliced_Bacon(self):

        # Input and expected result.
        test_input_title = "Jimmy Dean Sliced Bacon"
        test_input_description = "16 oz. pkg. breakfast essentials"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Jimmy Dean Sliced Bacon 16 oz pkg"

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

    def test_Signature_Kitchens_Evaporated_Milk(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Evaporated Milk"
        test_input_description = "12 fl. oz. can Baking Essentials. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Evaporated Milk 12 fl oz can"

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

    def test_Signature_Caf_Soup_24_fl_oz_excludes_clam_chowder_roasted_red_pepper(self):

        # Input and expected result.
        test_input_title = "Signature Café Soup 24 fl. oz. excludes clam chowder, roasted red pepper crab, stompin’ steakhouse chili and beef stroganoff  O Organics Soup 15 fl. oz."
        test_input_description = "Individual Price $4.49 ea. Soups on! Get into the season with savings. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Cafe Soup 24 fl oz Excludes Clam Chowder Roasted Red Pepper Crab Stompin Steakhouse Chili and Beef Stroganoff O Organics Soup 15 fl oz"

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

    def test_Signature_Caf_Clam_Chowder_Roasted_Red_Pepper_Crab_Stompin_Steakhouse_Chili_or_Beef_Stroganoff(self):

        # Input and expected result.
        test_input_title = "Signature Café Clam Chowder, Roasted Red Pepper Crab, Stompin’ Steakhouse Chili or Beef Stroganoff"
        test_input_description = "24 fl. oz. Individual Price $5.49 ea. Soups on! Get into the season with savings. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Cafe Clam Chowder Roasted Red Pepper Crab Stompin Steakhouse Chili or Beef Stroganoff 24 fl oz"

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

    def test_Signature_Caf_Soup(self):

        # Input and expected result.
        test_input_title = "Signature Café Soup"
        test_input_description = "15 fl. oz. Individual Price $3.49 ea. Soups on! Get into the season with savings. SAVE EVEN MORE WITH THESE EXTENDED GOOD THRU XTRAsavings!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Cafe Soup 15 fl oz"

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

    def test_Kashi__Organic_Promise_Cereal_9_516_3_oz__pkg___Heart_to_Heart_12_oz__pkg___Go_Lean_10_812_2_oz__pkg_(self):

        # Input and expected result.
        test_input_title = "Kashi  Organic Promise Cereal 9.5-16.3 oz. pkg.  Heart to Heart 12 oz. pkg.  Go Lean 10.8-12.2 oz. pkg."
        test_input_description = ""
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kashi Organic promise cereal 9.5-16.3 oz pkg Heart to Heart 12 oz pkg 10.8-12.2 oz pkg"

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

    def test_BERRIES(self):

        # Input and expected result.
        test_input_title = "BERRIES"
        test_input_description = "SAVE $3 ON BERRIES (STRAWBERRIES 1 LB. OR BLUEBERRIES 6 OZ.1 PINT) WHEN YOU BUY ANY 3 PARTICIPATING PRODUCTS  CORN FLAKES OR RICE KRISPIES 18 OZ.  CRISPIX 12 OZ.  FROSTED BITE SIZE MINI WHEATS 24 OZ.  FROSTED FLAKES 19 OZ.  RAISIN BRAN 23.5 OZ. MIX OR MATCH). OFFER VALID 9/22/1710/26/17."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Berries Strawberries 1 lb or Blueberries 6 oz1 Pint"

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

    def test_King_Arthurs_Measure_for_Measure_Flour(self):

        # Input and expected result.
        test_input_title = "King Arthur’s Measure for Measure Flour"
        test_input_description = "3 lb. pkg. LEMON BLISS CAKE KING ARTHUR FLOUR RECIPE OF THE YEAR"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "King Arthurs Measure for Measure flour 3 lb pkg"

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

    def test_Signature_Kitchens_Pasta(self):

        # Input and expected result.
        test_input_title = "Signature Kitchens Pasta"
        test_input_description = "BUY 1 of these Ferrera Cherry Tomato Pasta Sauce 24 oz. jar and GET 1 of these Signature Kitchens Pasta 12-16 oz. pkg. excludes lasagna, jumbo shells and manicotti FREE! INSTANTLY ($1 value) *Purchase must be made in a single transaction. Limit 1 offer. grocery & snack SAVINGS"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Signature Kitchens Pasta"

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

    def test_Freshly_Ground_InStore_Daily_80_Lean_Ground_Beef(self):

        # Input and expected result.
        test_input_title = "Freshly Ground In-Store Daily 80% Lean Ground Beef"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH 3 lbs. or more. Additional quantities $2.88 lb. discount given at register"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ground Beef 3 lb"

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

    def test_Lancaster_Brand_U_S_D_A__CHOICE_Beef_Tenderloin_Steaks(self):

        # Input and expected result.
        test_input_title = "Lancaster Brand U.S.D.A. CHOICE Beef Tenderloin Steaks"
        test_input_description = "4 DAY SALE FRIDAY, SEPTEMBER 22ND THRU MONDAY, SEPTEMBER 25TH cut fresh in-store daily! Lancaster® BRAND PREMIUM BEEF U.S.D.A. CHOICE"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lancaster Brand Beef Tenderloin Steaks"

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

    def test_Premium_Tomatoes_on_the_Vine(self):

        # Input and expected result.
        test_input_title = "Premium Tomatoes on the Vine"
        test_input_description = "Great Tasting ADDITIONAL QUANTITIES& REST OF WEEK$1.49/lb."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Premium Tomatoes on the Vine"

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

    def test_Tostitos_Tortilla_Chips(self):

        # Input and expected result.
        test_input_title = "Tostitos Tortilla Chips"
        test_input_description = "Selected Varieties, 914 oz. pkg.ADDITIONAL QUANTITIES& REST OF WEEK2/$6"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Tostitos Tortilla Chips 914 oz pkg"

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

    def test_Boneless_Skinless_Chicken_Breasts_or_Thighs(self):

        # Input and expected result.
        test_input_title = "Boneless, Skinless Chicken Breasts or Thighs"
        test_input_description = "Giant , Grade A, Up to 15% Solution Added,Value Pack, 45 lb. pkg."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boneless Skinless Chicken Breasts or Thighs Giant Grade A Value pack 45 lb pkg"

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

    def test_Red_Baron_Pizza(self):

        # Input and expected result.
        test_input_title = "Red Baron Pizza"
        test_input_description = "Selected Varieties, 14.7623.45 oz. pkg.ADDITIONAL QUANTITIES & REST OF WEEK3/$10"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Red Baron Pizza 14 oz pkg"

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

    def test_Green_Mountain_Dunkin_Donuts_Folgers_Gevalia_or_Maxwell_House_Coffee(self):

        # Input and expected result.
        test_input_title = "Green Mountain, Dunkin' Donuts, Folgers, Gevalia or Maxwell House Coffee"
        test_input_description = "Selected Varieties, Green Mountain, Newman's Own, Donut Shop, Gloria Jean's,Eight O'Clock, Folgers, Café Bustelo, Chock Full O'Nuts, Swiss Miss, Café Escapes,Maxwell House, Gevalia, MAX Boost, McCafé or Donut House, K-Cup, 612 ct. pkg.or Green Mountain, Dunkin' Donuts or Newman's Own, 1012 oz."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Green Mountain Dunkin' Donuts Folgers Gevalia or Maxwell House Coffee Green Mountain Newman's Own Donut Shop Gloria Jean'seight O'Clock Folgers Cafe Bustelo Chock Full O'Nuts Swiss Miss Cafe Escapes Maxwell House Gevalia Max Boost Mccafe or Donut House K-Cup 612 ct pkgOr Green Mountain Dunkin' Donuts or Newman's Own 1012 oz"

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

    def test_Natures_Bounty_Sundown_Kids_or_EsterC_Vitamians_or_Osteo_BiFlex(self):

        # Input and expected result.
        test_input_title = "Nature's Bounty, Sundown Kids or Ester-C Vitamians or Osteo Bi-Flex"
        test_input_description = "Participating Sizes and Varieties MayVary by Store"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's Bounty Sundown Kids or Ester-C Vitamians or Osteo Bi flex"

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

    def test_Johnsonville_Cooked_Brats_Premio_Italian_Sausage_St__Louis_Style_Pork_Spareribs_or_Chicken_Breast_Tenderloins(self):

        # Input and expected result.
        test_input_title = "Johnsonville Cooked Brats, Premio Italian Sausage, St. Louis Style Pork Spareribs or Chicken Breast Tenderloins"
        test_input_description = "Selected Varieties, Johnsonville, 14 oz. or Premio, 1416 oz. pkg., Sold by the Each or Giant,Spareribs, Previously Frozen or Chicken Tenderloins, Sold by the Pound"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Johnsonville Cooked Brats premio Italian Sausage St. Louis Style Pork Spareribs or Chicken Breast Tenderloins Johnsonville 14 oz or premio 1416 oz pkg"

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

    def test_VAN_KAAS_GOUDA(self):

        # Input and expected result.
        test_input_title = "VAN KAAS GOUDA"
        test_input_description = "IMPORTED FROM HOLLAND AND FAMOUS FOR FLAVOR. FOUND IN THE SPECIALTYCHEESE DEPARTMENT."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Van Kaas Gouda Imported from Holland"

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

    def test_Boars_Head_Bold_Ichiban_Teriyaki_Style_Chicken_Breast(self):

        # Input and expected result.
        test_input_title = "Boar's Head Bold Ichiban Teriyaki Style Chicken Breast"
        test_input_description = "Sliced to Order"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boar's Head Bold Ichiban Teriyaki Style Chicken Breast"

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

    def test_Giant_Premium_Roast_Beef(self):

        # Input and expected result.
        test_input_title = "Giant Premium Roast Beef"
        test_input_description = "Sliced to Order or Prepackaged forYour Convenience"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Giant premium Roast Beef"

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

    def test_Boars_Head_Maple_Honey_Ham(self):

        # Input and expected result.
        test_input_title = "Boar's Head Maple Honey Ham"
        test_input_description = "Sliced to Order"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Boar's Head Maple Honey Ham"

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

    def test_Pumpkin_Blooming_Plant_in_Gift_Bag(self):

        # Input and expected result.
        test_input_title = "Pumpkin Blooming Plant in Gift Bag"
        test_input_description = "In a 4 inch pot, Limited Time Originals"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Pumpkin Blooming Plant in Gift bag in A 4 inch Pot"

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

    def test_Centrum_or_Vitafusion_Multivitamins_or_Olly_Gummy_Vitamins(self):

        # Input and expected result.
        test_input_title = "Centrum or Vitafusion Multivitamins or Olly Gummy Vitamins"
        test_input_description = "Participating Varieties and Sizes May Vary by Store"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Centrum or Vitafusion Multivitamins or Olly Gummy Vitamins"

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

    def test_Custom_Made_Corsages_and_Boutonnieres_for_Homecoming(self):

        # Input and expected result.
        test_input_title = "Custom Made Corsages and Boutonnieres for Homecoming"
        test_input_description = "Order Online, by Phone or in Person!"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Custom Made Corsages and Boutonnieres for Homecoming"

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

    def test_Natures_Promise_Free_From_Meatballs(self):

        # Input and expected result.
        test_input_title = "Nature's Promise Free From Meatballs"
        test_input_description = "16 oz. pkg., Found in the MeatDepartment"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's promise Free from Meatballs 16 oz pkg"

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

    def test_Natures_Promise_Take_and_Bake_Bread_or_Rolls(self):

        # Input and expected result.
        test_input_title = "Nature's Promise Take and Bake Bread or Rolls"
        test_input_description = "Selected Varieties, 1215 oz. pkg.,Found in Bakery"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's promise Take and Bake Bread or rolls 1215 oz pkg"

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

    def test_Natures_Promise_Free_From_Squeezable_Fruit(self):

        # Input and expected result.
        test_input_title = "Nature's Promise Free From Squeezable Fruit"
        test_input_description = "Selected Varieties, 3.2 oz. pkg., Found in theProduce Department"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's promise Free from squeezable Fruit 3.2 oz pkg"

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

    def test_Natures_Promise_Organic_Bananas(self):

        # Input and expected result.
        test_input_title = "Nature's Promise Organic Bananas"
        test_input_description = "Healthy and Delicious"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Nature's promise Organic Bananas"

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

    def test_Michigan_Honeycrisp_Apples(self):

        # Input and expected result.
        test_input_title = "Michigan Honeycrisp Apples"
        test_input_description = "First of the Season!or Organic Washington HoneycrispApples, $2.99 lb with Card"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Michigan Honeycrisp Apples Organic Washington Honeycrisp Apples"

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

    def test_Gemmy_Light_Show_Projectors(self):

        # Input and expected result.
        test_input_title = "Gemmy Light Show Projectors"
        test_input_description = "Select Styles & Varieties"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Gemmy Light Show projectors"

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

    def test_Ground_Chuck(self):

        # Input and expected result.
        test_input_title = "Ground Chuck"
        test_input_description = "Fresh, Sold in a 3 lb Package for $10.47"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Ground Chuck Fresh Sold in A 3 lb package"

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

    def test_CocaCola_Pepsi_or_Dr__Pepper_Products(self):

        # Input and expected result.
        test_input_title = "Coca-Cola, Pepsi or Dr. Pepper Products*"
        test_input_description = "24 pk./12 oz. cans.Select varieties. Plusdeposit where applicable.All items must be purchased in a single transaction. No cash back."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Coca-Cola Pepsi or Dr. Pepper products 24 pk/12 oz cans"

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

    def test_Doritos_9_259_75_oz__or_Lays_Potato_Chips_9_510_oz_(self):

        # Input and expected result.
        test_input_title = "Doritos 9.25-9.75 oz. or Lay's Potato Chips* 9.5-10 oz."
        test_input_description = "Select varieties.All items must be purchased in the single transaction. No cash back."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Doritos 9.25 oz or Lay's Potato Chips 9.5-10 oz"

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

    def test_Kraft_Chunk_Shredded_or_Natural_Slice_Cheese(self):

        # Input and expected result.
        test_input_title = "Kraft Chunk, Shredded or Natural Slice Cheese*"
        test_input_description = "6.67-8 oz.Excludes parmesan.All items must be purchased in the single transaction. No cash back."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Kraft Chunk Shredded or Natural Slice Cheese 6.67-8 oz Excludes Parmesan."

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

    def test_Apple_Cider_Gallon_or_6_Ct__Cake_Donuts_1824_oz_(self):

        # Input and expected result.
        test_input_title = "Apple Cider Gallon or 6 Ct. Cake Donuts 18-24 oz."
        test_input_description = "All varieties. Bakery Dept."
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Apple Cider gallon or 6 ct Cake Donuts 18-24 oz"

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

