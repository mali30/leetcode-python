"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

"""

class Solution:
    def runningSum(self, nums):
        if nums is None:
            return []

        updated = [0] * len(nums)
        counter = 0
        sumSoFar = 0

        for item in range(len(nums)):
            sumSoFar += nums[item] 
            updated[counter] = sumSoFar 
            counter += 1
        
        return updated


sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningSum([1,1,1,1]))