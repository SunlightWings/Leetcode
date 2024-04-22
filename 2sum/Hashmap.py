class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # use hashmap to eliminate 2nd loop (for lookup)
        # find complement number, lookup in hashmap, if found return index, then update hashmap by inserting key:value to the dictionary.
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]        # number of list = nums[i]
            if complement in map:
                return [i, map[complement]]      # return value of complement, value = dictionary[key]
            map[nums[i]] = i                     # insert key value to dictionary, dictionary[key] = value

