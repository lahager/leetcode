class Solution:
  def shortestDistance(self, words, word1, word2):
    # TODO: Write your code here
    position1, position2 = -1, -1
    distance = len(words)
    for i, w in enumerate(words):
      if w == word1:
        position1 = i
      if w == word2:
        position2 = i
      if position1 > -1 and position2 > -1:
        if abs(position1 - position2) < distance:
          distance = abs(position1 - position2)
    return distance
