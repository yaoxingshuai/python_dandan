class Solution:
    def sortArrayByParity(self, A):
        """
        :type A:List[int]
        rtype:list[int]
        """
        l1 = [x for x in A if x % 2 == 0]
        l2 = [y for y in A if y % 2 == 1]

        return l1 + l2


sov = Solution()
result = sov.sortArrayByParity([3, 1, 2, 4])
assert result == [2, 4, 3, 1]
