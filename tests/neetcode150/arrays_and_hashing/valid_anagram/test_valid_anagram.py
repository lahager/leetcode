from neetcode150.arrays_and_hashing.valid_anagram.valid_anagram import valid_anagram

def test_valid_anagram_good():
    s = 'anagram'
    t = 'nagaram'
    res = valid_anagram(s, t)
    assert res == True
    
def test_valid_anagram_bad():
    s = 'car'
    t = 'rat'
    res = valid_anagram(s, t)
    assert res == False
    
def test_valid_anagram_bad_subset():
    s = 'car'
    t = 'carr'
    res = valid_anagram(s, t)
    assert res == False

def test_valid_anagram_good_single_char():
    s = 'a'
    t = 'a'
    res = valid_anagram(s, t)
    assert res == True