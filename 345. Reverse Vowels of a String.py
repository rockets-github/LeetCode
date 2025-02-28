class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowels_list = [c for c in s if c in vowels]
        return "".join([vowels_list.pop() if c in vowels else c for c in s])


# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = {'a', 'e', 'i','o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         str_list = list(s)
#         i = 0
#         j = len(s) - 1
#         while (i < j):
#             if str_list[i] in vowels:
#                 if str_list[j] in vowels:
#                     str_list[i] , str_list[j] = str_list[j] , str_list[i]
#                     i += 1
#                     j -= 1
#                 else:
#                     j -= 1
#             else:
#                 i += 1

#         return ''.join(str_list)
