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
class TestFlippForVpnTitles(object):

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

    def test_Lysol_Disinfecting_Spray(self):

        # Input and expected result.
        test_input_title = "Lysol Disinfecting Spray"
        test_input_description = "Lysol Disinfecting Spray kills 99.9% of bacteria and viruses (†)"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Lysol Disinfecting Spray"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Mucinex_SE_Extended_Release_BiLayer_Tablets_28ct__40_ct(self):

        # Input and expected result.
        test_input_title = "Mucinex SE Extended Release Bi-Layer Tablets 28ct - 40 ct"
        test_input_description = "12 Hours of congestion relief with just one tablet"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Mucinex Se Extended Release Bi-Layer Tablets 28Ct - 40 ct"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Select_Airborne_Effervescent_Tablets(self):

        # Input and expected result.
        test_input_title = "Select Airborne Effervescent Tablets"
        test_input_description = "A specially crafted blend of Vitamin C + 9 Vitamins, Mineral & Herbs"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Airborne Effervescent Tablets"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_50x60_Photo_Blankets(self):

        # Input and expected result.
        test_input_title = "50x60 Photo Blankets"
        test_input_description = "Promo Code: PBLANKET50Expiration Date: September 23, 2017"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "50X60 Photo Blankets"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Photo_Cards_min__40(self):

        # Input and expected result.
        test_input_title = "Photo Cards (min. 40)"
        test_input_description = "Promo Code: PCARD40Expiration Date: September 23, 2017"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Photo Cards"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Photo_Books(self):

        # Input and expected result.
        test_input_title = "Photo Books"
        test_input_description = "Promo Code: PBOOK50Expiration Date: September 23, 2017"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Photo Books"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_4x6_Prints_min__75(self):

        # Input and expected result.
        test_input_title = "4x6 Prints (min. 75)"
        test_input_description = "Promo Code: PRINT75Expiration Date: September 23, 2017"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "4X6 prints"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_Passport_Prints(self):

        # Input and expected result.
        test_input_title = "Passport Prints"
        test_input_description = "Print In-Store Coupon and Save $2"
        test_input_price = "9.99"
        test_expected_price_cleansed = float(9.99)
        test_expected_multibuy = ""
        test_expected_promotion_type = PRICE_REDUCTION
        test_expected_title_cleansed = "Passport prints"

        # Perform the test
        self.dut.mTitle = test_input_title
        self.dut.mDescription = test_input_description
        self.dut.mPrice = test_input_price
        # Perform the cleanse.
        self.dut.cleanse()
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_1_99_excludes_Fiber_One_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "1.99 (excludes Fiber One)."
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

    def test_2_44__plus_deposit_where_required_by_law_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "2.44 ⟡ plus deposit where required by law."
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
        # Verify the result.
        assert self.dut.mTitleCleansed == test_expected_title_cleansed
        assert self.dut.mPriceCleansed == test_expected_price_cleansed
        assert self.dut.mMultibuy == test_expected_multibuy
        assert self.dut.mPromotionType == test_expected_promotion_type

    def test_0_88_Plus_deposit_where_requires_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "0.88 ⟡Plus deposit where requires."
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

    def test_27_99_PLUS_1_00_manufacturers_coupon_in_most_Sunday_newspapers_Coupons_from_Sunday_newspaper_must_be_presented_at_time_of_purchase_(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = "27.99 PLUS $1.00 manufacturer's coupon in most Sunday newspapers** **Coupons from Sunday newspaper must be presented at time of purchase."
        test_expected_price_cleansed = float(27.99)
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

    def test__Manufacturers_coupon_in_most_Sunday_newspapers(self):

        # Input and expected result.
        test_input_title = "test title"
        test_input_description = "test description"
        test_input_price = " Manufacturers coupon in most Sunday newspapers"
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

