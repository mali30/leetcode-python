"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

 

Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.
 

Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 1000
"""

class Solution:
    def largestUniqueNumber(self, nums):
        
        mySet = set()
        maxSoFar = float('-inf')
        secondMax = 0
        
#         [5,7,3,9,4,9,8,3,1]
# secondMax: -inf 5 7 7
# maxSoFar: 5 7 9 7(second 9) 8
# set: 5  7 3 9 4 8
        for item in nums:
            if item > maxSoFar: 
                secondItem = maxSoFar  # -inf
                maxSoFar = item        # 11
            if item in mySet and maxSoFar == item:
                maxSoFar = secondItem # 
            mySet.add(item)  # 11 10
        
        return -1 if maxSoFar == float('-inf') else maxSoFar



    def largestUniqueNumber2(self, nums):
        hashMap = {}
        maxSoFar = 0
        
        for item in nums:
            if item not in hashMap:
                hashMap[item] = 0
            hashMap[item] += 1
        
        for key, value in hashMap.items():
            if value == 1:
                maxSoFar = max(maxSoFar, key)
        
        return maxSoFar if maxSoFar != 0 else -1
                

sol = Solution()
# print(sol.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
# print(sol.largestUniqueNumber([9,9,8,8]))
# print(sol.largestUniqueNumber([11, 10, 11]))

print(sol.largestUniqueNumber2([5,7,3,9,4,9,8,3,1]))