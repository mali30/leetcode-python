def maximum69Number (self, num: int) -> int:
        str_list = list(str(num))
        for val in range(len(str_list)):
            if str_list[val] != "9":
                str_list[val] = "9"
                break
        
        print(str_list)
        return int(''.join(str_list))
                
      