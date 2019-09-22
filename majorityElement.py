
def majorityElement(arr):
    my_dic = {}
    for val in arr:
        if val in my_dic:
            my_dic[val] += 1
        else:
            my_dic[val] = 1
    return max(my_dic, key=my_dic.get)

print(majorityElement([1,1,2,2,3,3,3,4]))