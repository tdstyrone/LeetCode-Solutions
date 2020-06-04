class Solution:
    def reverseOnlyLetters(self, S: str) -> str:

        letter_arr = []
        new_string = ""
        index = 0

        for i in range(len(S)):
            if (ord(S[i]) >= 65 and ord(S[i]) <= 90) or (ord(S[i]) >= 97 and ord(S[i]) <= 122):
                letter_arr.append(S[i])

        j = -1
        for letter in S:
            if letter not in letter_arr:
                new_string += letter
            else:
                new_string += letter_arr[j]
                j -= 1
        return new_string