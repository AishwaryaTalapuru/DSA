class Solution:
    def check_ascending_order(self, nums):
        for ind in range(1, len(nums)):
            if nums[ind-1] > nums[ind]:
                return False      
        return True
    def check_descending_order(self, nums):
        for ind in range(1, len(nums)):
            if nums[ind-1] < nums[ind]:
                return False      
        return True

    def check_sorted_array(self, nums):
        if len(nums) == 0:
            return True
        
        if self.check_ascending_order(nums) == True or self.check_descending_order(nums) == True:
            return True
        return False
sol = Solution()

#T.C = O(n)
#S.C = O(1) where n is the length of the array "nums"

sol = Solution()
inputs = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 5, 4]]
outputs = [True, True, False]
for ind in range(0, len(inputs)):
    actual = sol.check_sorted_array(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")