"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
class Solution:
    def reverseString(self, word) -> None:
        print('here')
        """
        Do not return anything, modify s in-place instead.
        """

        if word is None:
            return None
        
        start = 0
        end = len(word) - 1
    
        while start < end:
            self.helper(start, end, word)
            start += 1
            end -= 1

        return word

    def helper(self, start, end, word):
        temp = word[start]
        word[start] = word[end]
        word[end] = temp

sol = Solution()
word = ['m', 'o', 'h', 'a', 'm', 'e', 'd']
print(sol.reverseString(word))

