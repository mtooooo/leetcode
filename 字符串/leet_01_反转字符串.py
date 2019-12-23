class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lens = len(s)
        if lens == 0 or lens == 1:
            return s
        elif lens == 2:
            s[0], s[1] = s[1], s[0]
            print(s)
            return s
        if lens % 2 == 0:
            for i in range(lens // 2):
                s[i], s[lens - i - 1] = s[lens - i - 1], s[i]
            print(s)
            return s
        if lens % 2 == 1:
            for i in range((lens - 1) // 2):
                s[i], s[lens - i - 1] = s[lens - i - 1], s[i]
            print(s)
            return s


# a = ["h", "e", "l", "l", "o"]
a = ["a", "."]
b = Solution()
b.reverseString(a)
