class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        successful_words = ""

        for word in words:
            for letter in word:
                if word.count(letter) > chars.count(letter):
                    break
            else:
                successful_words += word

        return len(successful_words)