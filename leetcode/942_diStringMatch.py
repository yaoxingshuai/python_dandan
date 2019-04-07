class Solution:
    def diStringMatch(self, S):
        """
        :type S:str
        rtype:list[int]
        """
        l2 = []
        number_min = 0
        number_max = len(S)

        for c in S:
            if c == 'I':
                l2.append(number_min)
                number_min += 1
            else:
                l2.append(number_max)
                number_max -= 1
        l2.append(number_max)
        return l2


sov = Solution()
result = sov.diStringMatch('IDID')
print(result)
