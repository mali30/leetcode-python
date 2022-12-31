"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

from collections import Counter
class Solution:
    def buildRansomeNote(self, ransomeNote, magazine):

        if ransomeNote is None or magazine is None:
            return False 
        
        ransomeNoteDict = Counter(ransomeNote)

        for char in magazine:
            if char in ransomeNoteDict:
                ransomeNoteDict[char] -= 1
                if ransomeNoteDict[char] == 0:
                    del ransomeNoteDict[char]
        
        return len(ransomeNoteDict) == 0

sol = Solution()
print(sol.buildRansomeNote("a", "b"))
print(sol.buildRansomeNote("aa", "ab"))
print(sol.buildRansomeNote("aa", "aab"))