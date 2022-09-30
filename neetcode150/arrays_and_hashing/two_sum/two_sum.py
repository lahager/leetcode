# two_sum.py
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

def two_sum(nums, target):

    # First, we should initialize an empty dictionary. The key will be the integer and the value will be the index of that integer.
    d = {}

    # If size of nums is 2, we can return [0,1]
    if len(nums) == 2:
        return [0,1]

    # Loop through nums (we need the index too).
    for i, num in enumerate(nums):
        # Check if target - current int is in the dictionary
        if (target - num) in d:
            # If it is, return the current index and the one stored in the dict entry.
            return [d.get(target - num), i]
        
        # Else, add this element with its index to the dictionary
        d[num] = i

    # We are guaranteed to have exactly one pair of indices to solve it, so we will return at some point in the array.