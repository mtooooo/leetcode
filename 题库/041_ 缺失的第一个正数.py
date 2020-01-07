# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        index = 0
        while index < ls:
            if nums[index] <= 0 or nums[index] > ls or nums[nums[index] - 1] == nums[index]:
                index += 1
            else:
                pos = nums[index] - 1
                nums[index], nums[pos] = nums[pos], nums[index]
        res = 0
        while res < ls and nums[res] == res + 1:
            res += 1
        return res + 1
