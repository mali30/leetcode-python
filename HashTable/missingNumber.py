"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.

"""

# O(N^2) time
class Solution:
    def missingNumber(self, nums):

        if nums is None:
            return -1
        
        numsSize = len(nums)
        missingNumber = None

        for num in range(numsSize + 1):
            if num not in nums:
                missingNumber = num
        
        return missingNumber if missingNumber != None else -1

    #O(N) time O(N) space for set
    def missingNumberImproved(self, nums):

        if nums is None:
            return -1
        
        mySet = set(nums)
        numsSize = len(nums)

        # O(nlogn) time for sorting
        nums.sort()

        for idx, element in enumerate(nums):
            # since now sorted the index and element will be equal to each other
            # the missing number will not match its index so we return the index
            if element != idx:
                return idx
        

        # if we get here then the missing number would be the size of the list
        return numsSize





sol = Solution()
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([0,1]))
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
