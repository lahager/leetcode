Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

# Understand

This problem is asking us to return indices of 2 numbers whose value adds up to the target.

## Questions

Q: What is the minimum length of nums?<br>
A: The array has at least two elements.

Q: What is the range of nums in the array (can they be negative)?<br>
A: Values are whole numbers between $-10^{9}$ and $10^{9}$.

Q: Is the array sorted?<br>
A: No guarantees that this is a sorted array.

**We were told exactly one pair of answers would fulfill the target so no need to ask this**

## Examples

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1] ((nums[0] = 7) + (nums[1] = 2) = 9)
```

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

```
Input: nums = [-2,-5,-7], target = -12
Output: [1,2]
```

# Match

It's important that this array is not sorted - otherwise we would have other options.

The brute force method would be a nested for loop, for each element, adding it to each subsequent element until we find the ones that add to target. This is an O(n^2) algorithm.

We can use a dictionary, and for each element we see, add a key being the integer at that element and the value being the index. Then before we add each element, we can check if its complement (target - this integer) is in the dictionary - then we would have both indexes we can immediately return. We need at most one pass through the array - so O(n) time, with additional storage in the dictionary.

# Plan

First, we should initialize an empty dictionary. The key will be the integer and the value will be the index of that integer.

If size of nums is 2, we can return [0,1]

Loop through nums (we need the index too).
Check if target - current int is in the dictionary
If it is, return the current index and the one stored in the dict entry.

Else, add this element with its index to the dictionary

We are guaranteed to have exactly one pair of indices to solve it, so we will return at some point in the array.

# Implement

See [two_sum.py](two_sum.py)

# Review

Test cases added to [test_two_sum.py](../../../tests/neetcode150/arrays_and_hashing/test_sum/test_two_sum.py)

1. When nums = [2,7,11,15], target = 9, we initialize the empty dict. The length is not 2. We start looping through. The first check is if 9 - 2 = 7 if in dict - nope. So we add the first pair d = {2 : 0}. Now num = 7. We check is 9 - 7 = 2 in dict? Yep. So we get the value in the dict = 0. And the current index 1. And return them as a list [0,1]

2. When nums = [5,3,1], target = 6, initialize the empty dict and length is not 2 so keep going. Start the loop. First check is if 6 - 5 = 1 in dict? Nope. dict = {5: 0}. Is 6 - 3 in dict? Nope. dict = {5: 0, 3: 1}. Is 6 - 1 = 5 in dict? Yep. So we return the list with the value in the array 0, and current index 2 [0, 2]

# Evaluate

The time complexity is O(n), which is the best we can do given the array is unsorted and the worst case is we look at each element once. This comes at the cost of space complexity, because we created a dictionary, holding up to n elements (O(n))

We could have sorted the dictionary first O(n log n) and then we could use two pointers to go through the array up to log n times. This would have been a greater time complexity but O(1) space complexity.

We certainly did better than the brute force solution of O(n^2), with an inner loop checking all possibilities.

## My Mistakes

:)
