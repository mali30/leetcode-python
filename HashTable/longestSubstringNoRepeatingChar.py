"""
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

from collections import defaultdict
class Solution:
    # not passing all solutions
    def lengthOfLongestSubstring(self, word):

        if word is None:
            return -1

        result = left = 0
        hashSet = set()

        # abcabcbb
        for right in range(len(word)):
            curr = word[right] # abc a

            if curr in hashSet:
                left += 1
            
            hashSet.add(curr)  # abc a

            result = max(result, right - left + 1) # 0 1 2 

        return result

    def longestSubtring(self, word):
        
        if word is None:
            return -1

        
        result = left = 0
        hashMap = defaultdict(int)

        for right in range(len(word)):
            curr = word[right]
            hashMap[curr] += 1
        
            while hashMap[curr] > 1:
                leftMost = word[left]
                hashMap[leftMost] -= 1
                if hashMap[leftMost] == 0:
                    del hashMap[leftMost]
                left += 1
            
            result = max(result, right - left + 1)
        
        return result

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))


print(sol.longestSubtring("abcabcbb"))
print(sol.longestSubtring("bbbbb"))
print(sol.longestSubtring("pwwkew"))

