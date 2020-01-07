#  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 给列表建立索引
        num_index = [(v, index) for index, v in enumerate(nums)]
        # 排序
        num_index.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            two_sum = num_index[i][0] + num_index[j][0]
            if two_sum == target:
                print(num_index[i][1], num_index[j][1])
                return i, j
            elif two_sum < target:
                # 如果两数字和小于所需值，增加数字
                i += 1
            else:
                j -= 1

if __name__ == '__main__':
    # begin
    s = Solution()
    s.twoSum([2, 7, 11, 15], 9)
