# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

def defangIPaddr(address:str) -> str:

    new_address = address.replace("." , "[.]")
    return new_address

print(defangIPaddr("1.1.1.1"))
