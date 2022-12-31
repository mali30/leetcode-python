"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

class Solution:
    def isPanagram(self, word):

        if word is None:
            return False

        updated = [0] * 26
        for char in list(word):
            updated[ord(char) - ord('a')] = True 
        
        for boolean in updated:
            if not boolean:
                return False 
        
        return True


sol = Solution()
print(sol.isPanagram("thequickbrownfoxjumpsoverthelazydog"))
print(sol.isPanagram("leetcode"))
print(sol.isPanagram(None))
