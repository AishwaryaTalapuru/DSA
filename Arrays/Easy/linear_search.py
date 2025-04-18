#Given an array, find the smallest index where the target element appears
class Solution:
    def linear_search(self, nums, target):
        if len(nums) == 0:
            return -1
        for ind in range(0, len(nums)):
            if nums[ind] == target:
                return ind
        return -1
#T.C = O(n)
#S.C = O(1), where n is the length of the list "nums"
sol = Solution()
inputs = [[[4, 4, 2, 1], 4], [[4, 4], 3], [[4], 4], [[], 0], [[7, 7, 7, 6], 7], [[-1, -2, -3, -4], -2]]
outputs = [0, -1, 0, -1, 0, 1]
for ind in range(0, len(inputs)):
    actual = sol.linear_search(inputs[ind][0], inputs[ind][1])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")
        

