# your code goes here!
class Anagram:
    def __init__(self,word ="listen"):
        self.word = word 

    @property
    def word(self):
        return self._word
    @word.setter
    def word (self, word):
        self._word = word



    def match(self, possible_anagrams):
        anagrams = []
        for possible_anagram in possible_anagrams:
            possible_anagram_lower = possible_anagram.lower()
            if len(self.word) != len(possible_anagram_lower):
                continue
            if sorted(self.word) == sorted(possible_anagram_lower):
                anagrams.append(possible_anagram)
        return anagrams
  