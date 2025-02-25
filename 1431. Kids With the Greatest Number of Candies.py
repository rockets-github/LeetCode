class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [(candy + extraCandies) >= max(candies) for candy in candies]


# This is Simple Solution with numpy
# import numpy as np

# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         return np.array(candies) >= (max(candies) - extraCandies)
