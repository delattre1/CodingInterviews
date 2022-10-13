class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #print(f'\n----\nNums: {nums}, desired:{target}')
        # Iterate over array to set the first number

        compDic = {} # complement

        for i in range(len(nums)):
            n = nums[i]
            comp = target - n

            if n in compDic:
                return [compDic[n], i]
            else:
                compDic[comp] = i
