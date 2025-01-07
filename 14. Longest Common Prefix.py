class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre_str = strs[0]
        for i in strs:
            pre_str = pre_str[: min(len(i), len(pre_str))]
            for j in range(min(len(i), len(pre_str))):
                if i[j] != pre_str[j]:
                    pre_str = pre_str[:j]
                    break
        return pre_str
