#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from WebServices import *


#
# 
#
class TestWebServices(object):

    #
    # Create the Device Under Test (DUT).
    #
    def setup_method(self, method):
        # Maintain cookies for interactions with retailer's website(s).
        self.cookieSession = requests.Session()

    #
    # Perform any necessary clean-up.
    #
    def teardown_method(self, method):
        pass

    ##############
    # Test-Cases #
    ##############

    def test_url_check_status_google_status_200(self):

        # Input and expected results.
        url_input = 'http://www.google.com/'
        result_expected = True

        # Perform the test.
        dut_result = urlCheckStatus(self.cookieSession,
                                    url_input)

        # Verify the results.
        assert dut_result == result_expected
