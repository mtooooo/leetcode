# 两数之和

"""
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lens = len(nums)
        for i in range(lens):
            x = nums[i]
            for j in range(lens):
                if i < j:
                    y = nums[j]
                    z = x + y
                    if z == target:
                        return [i, j]


nums = [2, 7, 11, 15]
target = 9

a = Solution()
a.twoSum(nums=nums, target=target)
