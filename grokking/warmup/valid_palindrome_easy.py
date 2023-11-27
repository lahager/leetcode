class Solution:
  def isPalindrome(self, s: str) -> bool:
    # convert string. lowercase, strip non alpha
    str_list = []
    for l in s:
      if l.isalnum():
        str_list.append(l.lower())
    print(str_list)
    
    start, end = 0, len(str_list) - 1

    while start < end:
      if str_list[start] != str_list[end]:
        return False
      start += 1
      end -= 1
    return True
