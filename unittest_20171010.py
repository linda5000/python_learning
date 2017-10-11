import unittest
from test.math_c import Math
from parameterized import parameterized


class TestMath(unittest.TestCase):


    def setUp(self):
        pass
        # print("test start")

    @parameterized.expand([
        ("01",1,1,2),
        ("02",2,2,4),
        ("03",3,3,6),
    ] )

    def test_add(self,name,a,b,expected):
        try:
            self.assertEqual(Math().add(a,b),expected)
            print("测试用例：",name)
        except Exception as e:
            print(e)
        else:
            print("add test pass")


    def test_sub(self):
        try:
            t = Math()
            result = t.sub(15,6)
            self.assertEqual(result,9,"方法结果错误")
        except AssertionError as e:
            print(e)
        else:
            pass
            # print("sub test pass")

    def tearDown(self):
        pass
        # print("test end")


if __name__ == '__main__':
    unittest.main()