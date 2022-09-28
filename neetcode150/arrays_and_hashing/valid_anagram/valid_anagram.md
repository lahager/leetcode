Given two strings `s` and `t`, return `true` *if `t` is an anagram of `s`, and `false` otherwise*.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Understand

This problem will take in two strings, and we must return `true` if the letters can be rearranged such that `s` = `t`. Otherwise, we will return `false`.

## Questions

Q: Can the strings be empty?<br>
A: No, both strings are guaranteed to have at least one character.

Q: The wording `typically using all original letters exactly once` is throwing me off. If a string is a subset of the other string, is that a valid anagram? For example, is `car` an anagram of `carr`?<br>
A: No. The two strings will be the same length and have the same character makeup.

Q: What kinds of characters can the string contain?<br>
A: Only lowercase letters.


## Examples

```
Input: s = 'anagram', t = 'nagaram'
Output: true
```

```
Input: s = 'car', t = 'rat'
Output: false
```

```
Input: s = 'car', t = 'carr'
Output: false
```

```
Input: s = 'a', t = 'a'
Output: true
```

# Match

Two options come to mind.

We could sort both strings and then check if they are equal. This would not require extra space. The best sorting algorithms have O(n log n) time complexity - would likely use the built in Python function to sort which also has this time complexity, called Timsort. Then, we would have to check the strings are equal.

The other option I am thinking of would be to use a dictionary, with the key being the lowercase letter, and the value being the count of that letter. To load the dictionary would be O(n) time complexity, with O(n) extra space. Initially, I was thinking we would load both strings into their own dictionary, but now I am thinking we could just do one, say `s`, and then loop through the characters and remove them from `t`, and if all checks out then we know they are anagrams.

# Plan

First, we can check if the lengths of s and t are equal - if not, we can return false here.

Create a dictionary to hold the chars of s.

If they are equal, loop through s.
For each character in s, check if that char exists as a key.

If it does, add 1 to the value

If not, create the key with 1 as the value.

Now, we will loop through t.
For each character in t, get the value of that key (char).

If the key does not exist, return false

If the value is < 1, return false

Otherwise, subtract 1 from the value.

Once we are done looping through t, go through the keys in the dictionary.
If any values are not = 0, return false

Otherwise, return true.

# Implement

See [valid_anagram.py](valid_anagram.py)

# Review

Test cases added to [test_valid_anagram.py](../../../tests/neetcode150/arrays_and_hashing/valid_anagram/test_valid_anagram.py)

1. When s = 'anagram', and t = 'nagaram', their length is equal. After creating the dict with s, we should have {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
Then t loops through, and nicely removes each number.
Each value in the dict will be 0, so we return true.

2. When s = 'car', t = 'rat, their length is equal. After creating the dict with s, we should have {'c': 1, 'a': 1, 'r': 1}.
Then we loop through t. r gets a value of 0, so does a. but t is not in the dictionary, so we return False.

# Evaluate

The dict is created, so we have space complexity of O(n). This could be reduced, but at the cost of time complexity.

To add the chars of s is O(s) time. To remove the chars of t is O(t) time. Finally we loop through the chars again. This results in O(3"n") time, or O(n).

## My Mistakes

1. Was accidentally checking if c was "in" s or t instead of chars. Found this quickly through testing.