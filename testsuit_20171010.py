import unittest
from unittest_20171010 import TestMath

suite = unittest.TestSuite()
test = TestMath("test_add")

suite.addTest(test)

# suite.addTest(TestMath("test_sub"))

runner = unittest.TextTestRunner()

runner.run(suite)