import unittest
import group

class TestCases(unittest.TestCase):
    pass
    def test_groups_of_3_no1(self):
        result=group.groups_of_3([1,2,3,4,5,6,7,8,9])
        expected=[[1,2,3],[4,5,6],[7,8,9]]
        self.assertEqual(result,expected)
    def test_groups_of_3_no2(self):
        result=group.groups_of_3([1,2,3,4,5,6,7,8])
        expected=[[1,2,3],[4,5,6],[7,8]]
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()