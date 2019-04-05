class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        li = [d1[ss] for ss in s]
        int = 0
        le = range(len(li))
        for i in le:
            if i + 1 == len(li):
                int += li[i]
            elif max(li[i + 1:]) > li[i]:
                int -= li[i]
            else:
                int += li[i]
        return int


sov = Solution()

result = sov.romanToInt('I')
assert result == 1

result = sov.romanToInt('MCMXCIV')
assert result == 1994

result = sov.romanToInt('LVIII')
assert result == 58

result = sov.romanToInt('III')
assert result == 3

result = sov.romanToInt('IV')
assert result == 4

result = sov.romanToInt('IX')
assert result == 9
