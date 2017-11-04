#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from Catalog import *


#
# 
#
class TestWebParsers(object):

    #
    # Create the Device Under Test (DUT).
    #
    def setup_method(self, method):
        print "Entered setup"
        print method
        self.location = "location"
        self.webserver = "webserver"
        self.dut = Catalog(self.location, self.webserver)

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
        expected_valid_from = ""
        self.justin = "lisa"
        # Perform the test.
        

        # Verify the results.
        assert self.dut.mValidFrom == expected_valid_from
