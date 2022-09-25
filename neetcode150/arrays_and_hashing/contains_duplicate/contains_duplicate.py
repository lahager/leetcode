# contains_duplicate.py
# https://leetcode.com/problems/contains-duplicate/

# Given an integer array `nums`, return `true` if any value appears 
# **at least twice** in the array, and return `false` if every element 
# is distinct.


def contains_duplicate(nums):
    
    # First, we should initialize an empty set to hold values.
    seen = set()

    # Then, we can loop through the array one element at a time and 
    # try to add it to the dictionary.
    for i in nums:

        # In that loop, check if the element exists in the dictionary - 
        # if it does, we can immediately return `true` because this is 
        # our first duplicate. We do not need to check the rest of the array.
        if i in seen:
            return True
    
        # If the element is not in the set, we need to add it.
        seen.add(i)

    # If we finish the loop, then we have never returned `true` and we 
    # can return `false` at that point, guaranteed there are no 
    # duplicate integers
    return False