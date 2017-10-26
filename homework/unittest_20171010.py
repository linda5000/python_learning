import unittest
from test.math_c import Math
from parameterized import parameterized


class TestMath(unittest.TestCase):


    def setUp(self):
        pass
        # print("test start")

    @classmethod
    def setUpClass(cls):
        print('set up class ran')

    @parameterized.expand([
        ("01",1,1,2),
        ("02",2,2,4),
        ("03",3,3,6),
    ] )

    def test_add(self,name,a,b,expected):
        self.assertEqual(Math().add(a,b),expected)




    def test_sub(self):
        t = Math()
        result = t.sub(15,6)
        self.assertEqual(result,9,"方法结果错误")




    def tearDown(self):
        pass
        # print("test end")

    @classmethod
    def tearDownClass(cls):
        print('tear down class ran')


if __name__ == '__main__':
    unittest.main(verbosity=2)


