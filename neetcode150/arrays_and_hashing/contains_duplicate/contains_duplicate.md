Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

# Understand

This problem is asking us to look at an array and, if there is an integer that shows up more than once, we will return `true`, indiciating that yes, this array does contain duplicates.

If the array has only unique integers, we will return `false`. 

## Questions

Q: Can the array be empty?<br>
A: No, the array is guaranteed to have at least one element.

Q: What is the range of nums in the array (can they be negative)?<br>
A: Values are whole numbers between $-10^{9}$ and $10^{9}$.

Q: Is the array sorted?<br>
A: No guarantees that this is a sorted array.

## Examples

```
Input: nums = [1]
Output: false
```

```
Input: nums = [2, 1, 2]
Output: true
```

```
Input: nums = [3, 2, 1]
Output: false
```

# Match

In python, an array is usually a List so we can assume this is the data structure we are given.

It's key that the input is not sorted, so a sort or leveraging that is probably not the most efficient.

We can use a HashMap (Python - dict) for O(1) insert and O(1) lookup - but it will require O(n) storage space for the efficiency.

# Plan

First, we should initialize an empty set to hold values.

Then, we can loop through the array one element at a time and try to add it to the set.

In that loop, check if the element exists in the set - if it does, we can immediately return `true` because this is our first duplicate. We do not need to check the rest of the array.

If the element is not in the set, we need to add it.

If we finish the loop, then we have never returned `true` and we can return `false` at that point, guaranteed there are no duplicate integers.

# Implement

See [contains_duplicate.py](contains_duplicate.py)

# Review

Test cases added to [test_contains_duplicate.py](../../../tests/neetcode150/arrays_and_hashing/contains_duplicate/test_contains_duplicate.py)

1. When nums = [1], we will create the set. We will iterate through the loop once. 1 will not be in seen, so we will add it. Then, drop out of the loop and return False. Expected result.

2. When nums = [2, 1, 2], we will create the set. We will iterate through the loop 3 times. First, 2 will get added to the set. Then, 1 will get added to the set. Then, 2 will be in seen, so we will return True. Expected result.

3. When nums = [3, 2, 1], we will create the set. We will iterate through the loop 3 times. First, 3 will get added to the set, because 3 is not in seen. Then, 2 will get added to the set, because 2 is not in seen. Then, 1 will get added to the set, because 1 is not in seen. We will drop out of the loop. False is returned. Expected result.

# Evaluate

The set is created, so we have additional storage with a space complexity of O(n).

The set, though, has O(1) insert and O(1) lookup. We run through the loop (when we insert, and lookup) n times. So the algorithm time complexity is O(n)

## My Mistakes

1. Assumed I would need a HashMap (dict) instead of a HashSet (set). When I was implementing, I realized there was no point in the dictionary. I was not using the key. Just checking if something had been seen, so the set was a better play.

2. In my plan, I forgot about the step to add the integer to the set if it was not seen - a big miss, resulting in failed test cases.
