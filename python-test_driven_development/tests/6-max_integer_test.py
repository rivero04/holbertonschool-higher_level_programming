#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function."""

    def test_max_integer(self):
        """Test normal scenarios for max_integer."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1.0, 1.5, 1.6, 3.7, 2.3]), 3.7)

    def test_max_integer_exceptions(self):
        """Test exceptions for max_integer."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])
        with self.assertRaises(TypeError):
            max_integer(None)
