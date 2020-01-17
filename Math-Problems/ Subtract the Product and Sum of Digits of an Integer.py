class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        add_me = 0
        int_list = [int(item) for item in str(n)]
        mul_me = 1
      
        for val in int_list:
            add_me += val
            mul_me *= val
       
        return mul_me - add_me