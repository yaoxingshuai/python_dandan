class Solution:
    def toLowerCase(self, str):
        """
        :type str:str
        :rtype:str
        """
        new_str = ''
        for s in str:
            new_str += s.lower()
        return new_str


sov = Solution()
result = sov.toLowerCase(['Abc'])
assert result == 'abc'
