import array

# First try solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        something = []
        for i, item in enumerate(nums):
            x = target - item
            nums[i] == item
            if x in nums:
                j = nums.index(x)
                if i != j:
                    something.append(i)
                    something.append(j)
                    break
        return something

        