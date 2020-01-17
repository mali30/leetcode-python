# 217. Contains Duplicate
# Share
# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

def containsDuplicate(arr):
    head = 0
    tail = len(arr) - 1

    if arr is None:
        return 0

    while head < tail:
        if arr[head] == arr[tail]:
            return arr[head]
        elif arr[head] != arr[tail]:
            head += 1


print(containsDuplicate([5,4,3,2,1,1]))
# fails for this case
print(containsDuplicate([5,5,4,4,3,3,2]))
print(containsDuplicate([1,2,1]))
print(containsDuplicate([]))
# fails for this case
print(containsDuplicate([5,3,3,4]))




# Time Complexity - O(1) 
# Space Complexity - O(N) due to set creation
def containsDuplicate2(arr):
    my_set = set()
    for val in arr:
        if val in my_set:
            return True
        else:
            my_set.add(val)
    return False

print(containsDuplicate2([1,2,1,1]))
print(containsDuplicate2([1,1]))
print(containsDuplicate2([1,2]))
