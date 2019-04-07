class Solution:
    def repeatedNTimes(self, A):
        """
        :type A:List[int]
        rtype:int
        """
        l1 = set()
        str = ''
        for i in A:
            if i in l1:
                str = i
            else:
                l1.add(i)
        return str


sov = Solution()
result = sov.repeatedNTimes([1, 2, 3, 3])
assert result == 3
