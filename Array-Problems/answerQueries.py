def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    print('prefix', prefix)
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    print('prefix arr', prefix)
    
    ans = []
    for x, y in queries:
        print('prefix y', prefix[y])
        print('prefix x', prefix[x])
        print('nums[x]', nums[x])
        curr = prefix[y] - prefix[x] + nums[x]
        print('curr', curr)
        ans.append(curr < limit)

    return ans

print(answer_queries([1,2,3,4,5], [[0,2], [2,4]], 10))