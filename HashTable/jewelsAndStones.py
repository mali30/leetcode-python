class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        # j -> types of stones that are jewels
        # s -> stones you have
        
        
        jewels = 0
        for stones in S:
            if stones in J:
                jewels +=1
        
        return jewels
        
        