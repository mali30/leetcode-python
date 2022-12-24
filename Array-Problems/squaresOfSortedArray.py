"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


"""

class Solution:
    def sortedSquares(self, nums):
        
        if nums is None:
            return []

        
        updated = [0] * len(nums)

        start = 0
        end = len(nums) - 1
        counter = len(nums) - 1

        """
        Input: nums = [-7,-3,2,3,11]
        Output: [4,9,9,49,121]
        start = 49
        end = 122

        [0,0,9,49,122]
        """
        print('start', nums[start] * nums[start])
        print('end', end)
        while start <= end:
            if (abs(nums[start]) > abs(nums[end])):
                result = nums[start] * nums[start]
                start += 1
            else:
                result = nums[end] * nums[end]
                end -= 1

            updated[counter] = result
            counter -= 1
        
        return updated


sol = Solution()

print(sol.sortedSquares([-7,-3,2,3,11]))