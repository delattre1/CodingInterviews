import unittest 
from solution import Solution

class TestSolution(unittest.TestCase):
    def test1(self):
        sol = Solution()
        nums = [1,2,3,4]
        target = 3
        self.assertListEqual(sol.twoSum(nums, target), [0,1])

    def test2(self):
        sol = Solution()
        nums = [3,2,4]
        target = 6
        self.assertListEqual(sol.twoSum(nums, target), [1,2])

    def test3(self):
        sol = Solution()
        nums = [-1,-2,-3,-4,-5]
        target = -8
        self.assertListEqual(sol.twoSum(nums, target), [2,4])
        
