from itertools import zip_longest


#  This is OneLiner
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join([w1 + w2 for w1, w2 in zip_longest(word1, word2, fillvalue="")])


#  Basic Solution
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         result = ""

#         for w1, w2 in zip(word1, word2):
#             result += (w1+w2)


#         ml = len(result) // 2

#         if len(word1) > len(word2):
#             result += word1[ml:]

#         if len(word1) < len(word2):
#             result += word2[ml:]

#         return result
