#Given two sorted arrays, find the union of the two arrays
class Solution:
    def find_union(self, nums1, nums2):
        ptr1, ptr2 = 0, 0
        stack = [-2e9]
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] <= nums2[ptr2]:
                if nums1[ptr1] != stack[-1]:
                    stack.append(nums1[ptr1])
                ptr1+=1
            else:
                if nums2[ptr2] != stack[-1]:
                    stack.append(nums2[ptr2])
                ptr2+=1
        while ptr1 < len(nums1):
            if nums1[ptr1] != stack[-1]:
                stack.append(nums1[ptr1])
            ptr1+=1
        while ptr2 < len(nums2):
            if nums2[ptr2] != stack[-1]:
                stack.append(nums2[ptr2])
            ptr2+=1
        return stack[1:]



#T.C = O(n)
#S.C = O(n), where n is the length of the list "nums"
sol = Solution()
inputs = [[[], []], [[], [1, 2, 2, 3, 3, 4]], [[1, 1, 2, 2, 3], [2, 2, 4, 4, 5]]]
outputs = [[], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
for ind in range(0, len(inputs)):
    actual = sol.find_union(inputs[ind][0], inputs[ind][1])
    if actual == outputs[ind]:
        print(f"Test Case {ind+1} Passed ")
    else:
        print(f"Test Case {ind+1} Failed ")