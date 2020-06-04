class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string = s.split(" ")
        new_array = []

        for elem in split_string:
            if elem != "":
                new_array.append(elem)

        if len(new_array) == 0:
            return 0
        return len(new_array[-1])  