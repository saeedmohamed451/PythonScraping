#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from WebParsers import *

# Beautiful Soup for processing.
from bs4 import BeautifulSoup


#
# Want to make sure can convert date formats to Australian format.
#
class TestWebParsers(object):

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

    def test_dummy(self):

        # Input and expected results.
        soup_input = BeautifulSoup("", "lxml")

        # Perform the test.
        dut_output = parseFlippSoupItemDescription(soup_input)

        # Verify the results.
        assert 1 == 1
