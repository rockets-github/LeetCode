class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, val in enumerate(nums):
            num = target - val
            if val in num_dict.keys():
                return [num_dict[val], idx]
            else:
                num_dict[num] = idx
        return []
