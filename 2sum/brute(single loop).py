class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in nums) and (i != nums.index(complement)) :
                return [i, nums.index(complement)]
