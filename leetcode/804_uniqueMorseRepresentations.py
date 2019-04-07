import ipdb


class Solution:
    def uniqueMorseRepresentations(self, words):
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        d1 = dict()
        s1 = set()
        for i in range(97, 123, 1):
            d1[chr(i)] = code[i - 97]
        for word in words:
            st = ''
            for w in list(word):
                st += d1[w]
            if st not in s1:
                s1.add(st)
        unique_num = len(s1)

        return unique_num


sov = Solution()
result = sov.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
assert result == 2
