# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = []
        b = []
        next_01 = l1.next
        next_02 = l2.get('next')
        while next_01 != None:
            a.append(l1.get('val'))
            l1 = l1.get('next')
        while next_02 != None:
            b.append(l2.get('val'))
            l2 = l2.get('next')
        print(a,b)
        a = int(''.join(str(l1[::-1])[1:-1].split(', ')))
        b = int(''.join(str(l2[::-1])[1:-1].split(', ')))

        c = str(a + b)[::-1]
        d = []
        for i in range(len(c)):
            d.append(int(c[i]))
        print(d)
        return d


if __name__ == '__main__':
    # begin
    s = Solution()
    l1 = {'val': 2, next: {'val': 4, next: {'val': 3, next: None}}}
    l2 = {'val': 5, next: {'val': 6, next: {'val': 4, next: None}}}
    s.addTwoNumbers(l1, l2)

# A = '4321'
# a = [4, 3, 2, 1]
# b = int(''.join(str(a[::-1])[1:-1].split(', ')))
