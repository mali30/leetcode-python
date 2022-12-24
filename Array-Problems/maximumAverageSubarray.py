"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    def findMaxAverage(self, nums, k):

        result = total = 0

        # get the sum of elements from 0 to k
        # shortcut is to use sum() function also
        for element in range(0, k):
            result += nums[element]
        total = result # this line is important
        
        # now loop from k to the end of the array

        for element in range(k, len(nums)):
            # we can calculate result 
            result += nums[element] - nums[element - k]
            total = max(total, result)
        
        return total / k


sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4))
print(sol.findMaxAverage([5], 1))
