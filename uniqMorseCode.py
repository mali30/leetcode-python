# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:


# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".
MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
ORD_VALUE = ord('a')

def uniqueMorseRep(words):
    unique_rep = set()
    for val in words:
        unique_rep.add(mapMorseToAlphabet(val))
    return len(unique_rep)
    

def mapMorseToAlphabet(words):
    result = ""
    for word in words:
        result += MORSE[ord(word) - ORD_VALUE]
    return result


print(uniqueMorseRep(['gin' , 'zen', 'gig', 'msg']))
print(uniqueMorseRep(['hello' , 'world', 'its', 'moe']))