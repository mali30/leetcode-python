
# LeetCode Remove Vowels from a String
# Time Complexity: O(N) 
# Space Complexity: O(N)
def removeVowels(my_string):
    if my_string is None or my_string is "":
        return "I am empty"
    my_vowels = ["a","e","i","o","u"]
    iter = list(my_string)
    new_string = ""
    for val in iter:
        if val in my_vowels:
            new_string = iter.remove(val)
            return new_string
    return iter

print(removeVowels("aeiou"))
print(removeVowels("bcdfghjk"))
print(removeVowels(""))
