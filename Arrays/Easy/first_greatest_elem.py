#Given an array, return the first greatest element in it
class Solution:
    def first_greatest_elem(self, nums):
        if len(nums) == 0:
            return -1
        first_max = nums[0]
        for ind in range(1, len(nums)):
            first_max = max(first_max, nums[ind])
        return first_max
#T.C = O(n)
#S.C = O(1) where n is the length of the array "nums"

sol = Solution()
inputs = [[1, 7, 8, 900, 200], [200], []]
outputs = [900, 200, -1]
for ind in range(0, len(inputs)):
    actual = sol.first_greatest_elem(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")