# valid_anagram.py
# https://leetcode.com/problems/valid-anagram/

# Given two strings `s` and `t`, return `true` *if `t` 
# is an anagram of `s`, and `false` otherwise*.

# An **Anagram** is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically using 
# all the original letters exactly once.

def valid_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    # First, we can check if the lengths of s and t are equal - if not, we can return false here.
    if len(s) != len(t):
        return False

    # Create a dictionary to hold the chars of s.
    chars = {}

    # For each character in s, check if that char exists as a key.
    for c in s:
        if c in chars:
            # If it does, add 1 to the value
            chars[c] += 1
        else:
            # If not, create the key with 1 as the value.
            chars[c] = 1

    # Now, we will loop through t.
    # For each character in t, get the value of that key (char).
    for c in t:
        # If the key does not exist, return false
        if c not in chars:
            return False
        
        # If the value is < 1, return false
        if chars[c] < 1:
            return False

        # Otherwise, subtract 1 from the value.
        chars[c] -= 1

    # Once we are done looping through t, go through the keys in the dictionary.
    # If any values are not = 0, return false
    for c in chars:
        if chars[c] != 0:
            return False

    # Otherwise, return true.
    return True
