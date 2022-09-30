from neetcode150.arrays_and_hashing.two_sum.two_sum import two_sum

def test_two_sum_length_of_four():
    nums = [2,7,11,15]
    target = 9
    res = two_sum(nums, target)
    assert res == [0,1]
    
def test_two_sum_length_of_three():
    nums = [3,2,4]
    target = 6
    res = two_sum(nums, target)
    assert res == [1,2]
    
def test_two_sum_length_of_two():
    nums = [3,3]
    target = 6
    res = two_sum(nums, target)
    assert res == [0,1]
        
def test_two_sum_negatives():
    nums = [-2,-5,-7]
    target = -12
    res = two_sum(nums, target)
    assert res == [1,2]
    
def test_two_sum_split():
    nums = [5,3,1]
    target = 6
    res = two_sum(nums, target)
    assert res == [0,2]