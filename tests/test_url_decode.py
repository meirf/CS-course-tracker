#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from url_manipulation.url_decode import get_url_param_mappings


class TestUrlDecode(unittest.TestCase):

    def setUp(self):
        self.x = "GET /taken?content=hey!!&a=xyz HTTP/1.1 Accept: text/html,application/"
        self.y = "GET /taken?content=hey HTTP/1.1 Accept: text/html,application/"
        self.z = "GET /taken? HTTP/1.1 Accept: text/html,application/"

    def test_url_decode_2_params(self):
        """
        Check that input can be mapped to 2 element dict
        """
        self.assertEqual(get_url_param_mappings(self.x), {'content': 'hey!!', 'a': 'xyz'})

    def test_url_decode_1_params(self):
        """
        Check that input can be mapped to 1 element dict
        """
        self.assertEqual(get_url_param_mappings(self.y), {'content': 'hey'})

    def test_url_decode_0_params(self):
        """
        Check that input can be mapped to empty dict
        """
        self.assertEqual(get_url_param_mappings(self.z), {})