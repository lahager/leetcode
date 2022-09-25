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


