from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        sum = 0
        flag = 1

        for x in c.values():
            if x % 2 == 1 and flag == 1:
                sum += x
                flag = 0
            elif x % 2 == 1 and flag == 0:
                sum += x - 1
            else:
                sum += x
        return sum
