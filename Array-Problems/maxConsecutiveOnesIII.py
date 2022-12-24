class Solution:
    def longestOnes(self, nums, k):
        
        left = 0
        
        for right in range(len(nums)):
            curr_right = nums[right]
            if curr_right == 0:
                k -= 1
            
            if k < 0:
                curr_left = nums[left]
                if curr_left == 0:
                    k += 1
                left += 1
            
        return right - left + 1

ll = [1,1,1,0,0,0,1,1,1,1,0]
solution = Solution()
print(solution.longestOnes(ll, 2))