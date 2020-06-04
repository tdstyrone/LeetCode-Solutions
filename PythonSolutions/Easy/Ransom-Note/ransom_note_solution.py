class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        chars = set(ransomNote)
        for letter in chars:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True