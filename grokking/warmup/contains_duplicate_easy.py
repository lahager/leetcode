class Solution:
    def containsDuplicate(self, nums):
      # TODO: Write your code here
      unique = set()
      for n in nums:
        if n in unique:
          return True
        else:
          unique.add(n)
      return False