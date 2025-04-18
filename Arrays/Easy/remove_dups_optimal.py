class Solution:
    def remove_duplicates(self, nums):
        #modifying the same array
        if len(nums)<=1:
            return nums
        low, high = 0, 0
        while high < len(nums):
            if nums[low] != nums[high]:
                low+=1
                nums[low] = nums[high]
            high+=1
        return nums[:low+1]

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