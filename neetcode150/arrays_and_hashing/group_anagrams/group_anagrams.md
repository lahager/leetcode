Given an array of strings `strs`, group *the anagrams* together. You can return the answer in any order.

An *Anagram* is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Understand

This problem is asking us to look at an array of words (strings) and if they have the same composition or makeup of letters, they need to be put in the same array.

## Questions

Q: Can the array consist of anything but letters?<br>
A: Only lowercase letters.

Q: What is the range of lengths for each word in the array?<br>
A: It can be inclusive, between 0 and 100 characters long.

Q: What is the range of lengths for the array itself?<br>
A: Between 1 and $10^{4}$

## Examples

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
```

```
Input: strs = [""]
Output: [[""]]
```

```
Input: strs = ["a"]
Output: [["a"]]
```

# Match

We are given an array and need to return an array of arrays; in python, this would respectively be a List and List of Lists.

The input array is not sorted and sorting it doesn't really benefit us.

Each character is assigned a numeric value, I had a thought to utilize it to get the total numeric value of the word, but there are multiple ways you can come to the same sum, so this won't work.

However, if the input were sorted alphabetically, then words would appear identical to each other if they have the same makeup.

Let's say the number of items in the `strs` array is `n`, and the length of each word in the array is `m`. Sorting a word is O(m log m), and we will need to do this for each word (n times).

We should store each word in a HashMap (Dict), with the key being that word in alphabetical rearranged order, and adding each word into the value that is a List.

# Plan

First, we should initialize an empty Dict to hold the values.

Then, we can loop through the `strs` array, and in each iteration, alphabetize it and add it to the dict. If that key is not found, we will add it with a new list with the word. And if the key is found, we will append to the value (list).

The return value for our function will be the dict we initialize.

# Implement

See [group_anagrams.py](group_anagrams.py)

# Review

Test cases added to [test_group_anagrams.py](../../../tests/neetcode150/arrays_and_hashing/group_anagrams/test_group_anagrams.py)

# Evaluate

We have to sort each word alphabetically - this is O(m log m) time complexity.

We have to iterate over each word in the array - this is O(n) time complexity. We can't do better than this as we have to evaluate each word at least once.

So the total time complexity m \* n log n

We are also using O(n) space with the hashmap, and new list of return values.

## My Mistakes

1. The sorted() function returns a list of individual letters, so I had to join it back together.

2. Initially I just returned the dictionary, but instead I needed to strip the values out of it.

3. I could have just returned groups.values()

4. This was not the optimal solution - instead you can use a tuple with count of each letter as the key for time complexity O(m \* n)