
def majorityElement(arr):
    my_dic = {}
    for val in arr:
        if val in my_dic:
            my_dic[val] += 1
        else:
            my_dic[val] = 1
            # the my_dic.get will return a value for the specified key.
            # for our case, that would be key with the highest value(repeated elements)
    return max(my_dic, key=my_dic.get)

print(majorityElement([1,1,2,2,3,3,3,4]))