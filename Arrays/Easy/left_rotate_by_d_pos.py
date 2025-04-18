class Solution:
    def left_rotate_by_d_pos(self, nums, d):
        if len(nums) == 0:
            return nums
        if d >= len(nums):
            d = d%len(nums)
        temp = []
        for ind in range(0, d):
            temp.append(nums[ind])
        start = 0
        for ind in range(d, len(nums)):
            nums[start] = nums[ind]
            start+=1
        curr = 0
        while start < len(nums) and curr < len(temp):
            nums[start] = temp[curr]
            curr+=1
            start+=1
        return nums
#T.C = O(n)
#S.C = O(n), where n is the length of the list "nums"
sol = Solution()
inputs = [[[4, 4, 2, 1], 2], [[], 3], [[4, 4, 2, 1,], 6]]
outputs = [[2, 1, 4, 4], [], [2, 1, 4, 4]]
for ind in range(0, len(inputs)):
    actual = sol.left_rotate_by_d_pos(inputs[ind][0], inputs[ind][1])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")




