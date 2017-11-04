#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest

# DUT: Device Under Test.
from DocumentServices import *



#
# 
#
class TestDocumentServices(object):

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
        dummy_input = "dummy"
        dummy_path_to_file = "/tmp/dummy"

        # Perform the test.
        dut_output = writeContentToFile(dummy_input,
                                        dummy_path_to_file)

        # Verify the results.
        assert 1 == 1
