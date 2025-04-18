class Solution:
    def remove_duplicates(self, nums):
        #using a new array (stack)
        if len(nums) <= 1:
            return nums
        stack = [nums[0]]
        for ind in range(1, len(nums)):
            if nums[ind] != stack[-1]:
                stack.append(nums[ind])
        return stack
#T.C = O(n)
#S.C = O(n), where n is the length of the list "nums"
sol = Solution()
inputs = [[1, 2, 2, 3, 3, 3], [], [4], [1, 2, 3], [7, 7, 7, 6], [-1, -2, -3, -4]]
outputs = [[1, 2, 3], [], [4], [1, 2, 3], [7, 6], [-1, -2, -3, -4]]
for ind in range(0, len(inputs)):
    actual = sol.remove_duplicates(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")