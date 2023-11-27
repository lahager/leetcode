class Solution:
  def checkIfPangram(self, sentence):
    # TODO: Write your code here
    s = set()
    for l in sentence:
      if l.isalpha():
        l = l.lower()
        s.add(l)

    if len(s) != 26:
      return False
    return True
