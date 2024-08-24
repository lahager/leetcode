# group_anagrams.py
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

def group_anagrams(strs):
    #First, we should initialize an empty Dict to hold the values.
    groups = {}

    #Then, we can loop through the `strs` array, and in each iteration, alphabetize it and add it to the dict. 
    #If that key is not found, we will add it with a new list with the word. And if the key is found, we will append to the value (list).
    for s in strs:
        alpha = ''.join(sorted(s))
        
        if groups.get(alpha):
            groups.get(alpha).append(s)
        else:
            groups[alpha] = [s]

    # build a new list of only the value lists
    ret = []
    for k,v in groups.items():
        ret.append(v)
    return ret