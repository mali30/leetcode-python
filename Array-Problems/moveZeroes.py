# Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Time is O(N) - Not passing all cases. Needs fixing
def moveZeroes(arr):
    val = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[val],arr[i] = arr[i],arr[val]
            i+=1
    return arr

# Time is O(n^2) because of del in python
def moveZeroes2(arr):
    start = 0
    end = len(arr)

    while start < end:
        if arr[start] == 0:
            del arr[start]
            arr.append(0)
            end-=1
        else:
            start +=1
    return arr

print(moveZeroes([0,0,1,2,3]))
print(moveZeroes2([0,1,2,0,4,5]))