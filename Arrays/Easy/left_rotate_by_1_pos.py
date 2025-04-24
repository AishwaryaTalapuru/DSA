class Solution:
    def left_rotate_by_1_pos(self, nums):
        if len(nums) <=1 :
            return nums
        temp = nums[0]
        ind = 1
        while ind < len(nums):
            nums[ind-1] = nums[ind]
            ind+=1
        nums[-1] = temp
        return nums


#T.C = O(n)
#S.C = O(n), where n is the length of the list "nums"
sol = Solution()
inputs = [[4, 4, 2, 1], [], [4, 4, 2, 3,]]
outputs = [[4, 2, 1, 4], [], [4, 2, 3, 4]]
for ind in range(0, len(inputs)):
    actual = sol.left_rotate_by_1_pos(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")




