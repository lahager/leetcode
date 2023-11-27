class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here
    if len(s) < 2:
      return s
    str_list = list(s)
    vowels = "AEIOUaeiou"
    start = 0
    end = len(s) - 1

    while start < end:
      if str_list[start] not in vowels:
        start += 1
      if str_list[end] not in vowels:
        end -= 1
      if str_list[start] in vowels and str_list[end] in vowels:
        temp = str_list[start]
        str_list[start] = str_list[end]
        str_list[end] = temp
        start += 1
        end -= 1
      print('start=', start, " end=", end, "  s=", str_list)

    s = "".join(str_list)
    return s
