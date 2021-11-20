class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        highestLevel = 1
        result = 0
        for ch in s[::-1]:
            level = mapping[ch]
            if level >= highestLevel:
                result += level
                highestLevel = level
            else:
                result -= level
        return result


# class Solution:

#     SYMBOL_VALUES = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000,
#     }

#     def romanToInt(self, s: str) -> int:
#         ans = 0
#         n = len(s)
#         for i, ch in enumerate(s):
#             value = Solution.SYMBOL_VALUES[ch]
#             if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
#                 ans -= value
#             else:
#                 ans += value
#         return ans