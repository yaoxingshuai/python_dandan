class Solution:
    def sortedSquares(self, A):
        """
        :type A:List[int])
        rtype:int
        """

        return sorted(x * x for x in A)


sov = Solution()
result = sov.sortedSquares([-4, -1, 0, 3, 10])
print('result={}'.format(result))
assert result == [0, 1, 9, 16, 100]

sov = Solution()
result = sov.sortedSquares([-7, -3, 2, 3, 11])
print('result={}'.format(result))
assert result == [4, 9, 9, 49, 121]

sov = Solution()
result = sov.sortedSquares([-2, 0])
print('result={}'.format(result))
assert result == [0, 4]
