#Given an array, get the unique second greatest element in it. Return -1 if the element does not exist
#Edge Cases [4, 4, 2, 1], [4, 4], [4], []
class Solution:
    def get_second_greatest_elem(self, nums):
        #Getting the first greatest element first
        if len(nums) == 0:
            return -1
        first_greatest_elem = nums[0]
        for ind in range(1, len(nums)):
            first_greatest_elem = max(first_greatest_elem, nums[ind])
        #Getting the second greatest element WHICH IS NOT EQUAL TO THE FIRST GREATEST ELEMENT
        if len(nums) <= 1:
            return -1
        #Finding the potential element for the seocnd greatest element
        #OR SECOND LARGEST INITIALLY SHOULD NOT BE EQUAL TO FIRST LARGEST AND SHOULD NOT MATCH ANY ELEMENT IN THE ARRAY (-2e9)
        #Good time to ask the interviewer what is the range of values within the array
        second_greatest_elem = nums[0]
        start = 0
        while start < len(nums):
            second_greatest_elem = nums[start]
            if second_greatest_elem != first_greatest_elem:
                break
            start+=1
        if second_greatest_elem == first_greatest_elem:
            return -1
        for ind in range(start, len(nums)):
            if nums[ind] > second_greatest_elem and nums[ind] < first_greatest_elem:
                second_greatest_elem = nums[ind]
        return second_greatest_elem
#T.C = O(n)
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
        

