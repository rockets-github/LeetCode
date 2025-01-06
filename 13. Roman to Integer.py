class Solution:
    def romanToInt(self, s: str) -> int:
        Roman_index = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        before = 1001
        for i in list(s):
            now = Roman_index[i]
            if before < now:
                result += now - 2 * before
            else:
                result += now
            before = now
        return result
