#Given an array, get the unique second greatest element in it. Return -1 if the element does not exist
#Edge Cases [4, 4, 2, 1], [4, 4], [4], []
class Solution:
    def get_second_greatest_elem(self, nums):
        if len(nums) <=1:
            return -1
        #get first element
        nums_sorted = sorted(nums, reverse=True)
        first_greatest_elem = nums_sorted[0]
        second_greatest_elem = nums_sorted[1]
        start = 1
        while start < len(nums_sorted):
            if first_greatest_elem != nums_sorted[start]:
                second_greatest_elem = nums_sorted[start]
                break
            start+=1
        if first_greatest_elem != second_greatest_elem:
            return second_greatest_elem
        else:
            return -1
        

#T.C = O(nlogn)
#S.C = O(1), where n is the length of the list "nums"
sol = Solution()
inputs = [[4, 4, 2, 1], [4, 4], [4], [], [7, 7, 7, 6], [-1, -2, -3, -4]]
outputs = [2, -1, -1, -1, 6, -2]
for ind in range(0, len(inputs)):
    actual = sol.get_second_greatest_elem(inputs[ind])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")
        

