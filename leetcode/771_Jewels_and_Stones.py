class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        i = 0
        for stone in S:
            for jewel in J:
                if jewel == stone:
                    i += 1
                    break
        return i


if __name__ == '__main__':
    s1 = Solution().numJewelsInStones('aA', 'aAAbbbb')
    s2 = Solution().numJewelsInStones(J="z", S="ZZ")

    print('s1={}, s2={}'.format(s1, s2))
    assert s1 == 3 and s2 == 0
