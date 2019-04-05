import ipdb


class Solution:
    def isPalindrome(self, x: int):
        y = list(str(x))
        z = list(reversed(y))
        if y == z:
            return True
        else:
            return False


sov = Solution()
flag = sov.isPalindrome(121)
assert flag is True

flag = sov.isPalindrome(111)
assert flag is True

flag = sov.isPalindrome(0)
assert flag is True

flag = sov.isPalindrome(-123)
assert flag is False

flag = sov.isPalindrome(-111)
assert flag is False
