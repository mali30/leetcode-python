class Solution:
    def sumZero(self, n: int) -> List[int]:
        
            arr = [0] * n
            start , end = 0 , n - 1
            while start < end:
                arr[start], arr[end] = end , -end
                start,end = start+ 1 , end - 1
            return arr
    
    
  