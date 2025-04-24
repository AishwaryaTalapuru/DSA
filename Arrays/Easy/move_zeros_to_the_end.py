class Solution:
    def move_zeros_to_the_end(self, nums):
        if len(nums) <=1 :
            return nums
        low, high = 0, 1
        while high < len(nums):
            if nums[low] == 0 and nums[high] == 0:
                high+=1
            elif nums[low] == 0 and nums[high] != 0:
                temp = nums[low]
                nums[low] = nums[high]
                nums[high] = temp
                low+=1
                high+=1
            elif nums[low] != 0  and nums[high] == 0:
                low+=1
                high+=1
            else:
                high+=1
                low+=1
        return nums

#T.C = O(n)
#S.C = O(n), where n is the length of the list "nums"
sol = Solution()
inputs = [[0, 0, 0], [], [5, 0, 0, 2, 4, 0], [1, 2, 0, 3]]
outputs = [[0, 0, 0], [], [5, 2, 4, 0, 0, 0], [1, 2, 3, 0]]
for ind in range(0, len(inputs)):
    actual = sol.move_zeros_to_the_end(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")




