from typing import List


class Solution:
    def shortest_word_distance(self, words: List[str], word1: str, word2: str) -> int:
        # initialize shortest dist, w1, w2
        # for i in indices of words
        #   if words[i] is one of the words and w1 is None, set w1 to i
        #   if w1 is not None and words[w1] == words[i], set w1 to i
        #   if w1 is not None and words[i] != words[w1] and words[i] is one of the words, set w1 to i and update shortest if shortest < i - w1
        #   

        shortest, w1, w2 = float('inf'), None, None
        for i, w in enumerate(words):
          if w == word1:
             w1 = i

          if w == word2:
            w2 = i
          
          if w1 is not None and w2 is not None and shortest > abs(w2 - w1):
            shortest = abs(w2 - w1)

        return shortest