"""
test.testUtil

Testing module for experiment.util module
"""

import unittest
from experiment.util import compare_object_dict
from collections import namedtuple
from typing import Optional, List


class TestUtil(unittest.TestCase):
    def test_compare_object_dict(self):
        left = 1
        right = 1
        self.__test_compare(left, right, True)

        left = 2
        right = 1
        self.__test_compare(left, right, False)

    def __test_compare(
        self,
        left: object,
        right: object,
        expected: bool,
        override: Optional[List[str]] = None,
    ):
        self.assertEqual(compare_object_dict(left, right, override), expected)


if __name__ == "__main__":
    unittest.main()
