#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from DocumentParsers import *



#
# 
#
class TestDocumentParsers(object):

    #
    # Create the Device Under Test (DUT).
    #
    def setup_method(self, method):
        pass

    #
    # Perform any necessary clean-up.
    #
    def teardown_method(self, method):
        pass

    ##############
    # Test-Cases #
    ##############

    def test_remove_comma(self):

        # Input and expected results.
        string_input = "this is a test string, with a comma."
        string_expected = "this is a test string with a comma."

        # Perform the test.
        dut_result = cleanStringForCsv(string_input)

        # Verify the results.
        assert dut_result == string_expected
