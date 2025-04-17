#Given an array check if it is sorted in ascending or descending order
class Solution:
    def check_ascending_order(self, nums):
        res = sorted(nums)
        if res==nums:
            return True
        return False
    def check_descending_order(self, nums):
        res = sorted(nums, reverse=True)
        if res==nums:
            return True
        return False

    def check_sorted_array(self, nums):
        if len(nums) == 0:
            return True
        
        if self.check_ascending_order(nums) == True or self.check_descending_order(nums) == True:
            return True
        return False
sol = Solution()

#T.C = O(nlogn)
#S.C = O(n) where n is the length of the array "nums"

sol = Solution()
inputs = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 5, 4]]
outputs = [True, True, False]
for ind in range(0, len(inputs)):
    actual = sol.check_sorted_array(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")