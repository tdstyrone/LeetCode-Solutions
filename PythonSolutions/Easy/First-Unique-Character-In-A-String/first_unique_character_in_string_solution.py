class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = set(s)
        letter_array = []

        for char in letters:
            if s.count(char) == 1:
                letter_array.append(char)

        for character in s:
            if character in letter_array:
                return s.index(character)
        return -1