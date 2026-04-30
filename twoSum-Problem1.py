class Solution(object):
    def twoSum(self, nums, target):
        """
        :type target: int
        :type need: int
        :type nums: List[int]
        :type seen: dict[int:int]
        :rtype: List[int]
        :rtype: List[int]
        :rtype: dict[int:int]
        """
        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i
