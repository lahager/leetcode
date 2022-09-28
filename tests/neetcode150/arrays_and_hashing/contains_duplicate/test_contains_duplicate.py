from neetcode150.arrays_and_hashing.contains_duplicate.contains_duplicate import contains_duplicate

def test_contains_duplicate_single_element():
    nums = [1]
    res = contains_duplicate(nums)
    assert res == False
    
def test_contains_duplicate_true():
    nums = [2, 1, 2]
    res = contains_duplicate(nums)
    assert res == True
    
def test_contains_duplicate_false():
    nums = [3, 2, 1]
    res = contains_duplicate(nums)
    assert res == False