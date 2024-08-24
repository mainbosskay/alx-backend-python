#!/usr/bin/env python3
"""Module for testing function in utils file"""
import unittest
from unittest.mock import patch, Mock
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Unittest for function access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """Testing for function access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        """Tests for access_nested_map exception raising"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unittest for function get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Testing for get_json function output"""
        mockAttrbs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**mockAttrbs)) as getMock:
            self.assertEqual(get_json(test_url), test_payload)
            getMock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unittest for function memoize"""
    def test_memoize(self) -> None:
        """Testing for memoize function output"""
        class TestClass:
            """Unittest for function memoize decorator"""
            def a_method(self):
                """Method that returns fixed value"""
                return 42

            @memoize
            def a_property(self):
                """Method to call a_method for memoize decorator"""
                return self.a_method()
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as mockMethod:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mockMethod.assert_called_once()
