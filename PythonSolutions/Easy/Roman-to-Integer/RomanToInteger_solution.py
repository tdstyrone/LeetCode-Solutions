class Solution:
    def romanToInt(self, s: str) -> int:
        sym_to_val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = sym_to_val[(s[0])]
        for i in range(1, len(s)):
            if (sym_to_val[(s[i - 1])] >= sym_to_val[(s[i])]):
                total += sym_to_val[(s[i])]
            else:
                total = total - (2 * sym_to_val[(s[i - 1])]) + sym_to_val[(s[i])]
        return total