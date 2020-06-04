class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        return "".join([char * freq for char, freq in Counter(s).most_common()])