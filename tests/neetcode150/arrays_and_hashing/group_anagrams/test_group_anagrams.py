from neetcode150.arrays_and_hashing.group_anagrams.group_anagrams import group_anagrams

def test_group_anagrams_good():
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = group_anagrams(strs)
    assert res == [["bat"],["nat","tan"],["ate","eat","tea"]]
    
def test_group_anagrams_empty():
    strs = [""]
    res = group_anagrams(strs)
    assert res == [[""]]
    
def test_group_anagrams_single_input():
    strs = ["a"]
    res = group_anagrams(strs)
    assert res == [["a"]]