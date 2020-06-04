class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if (len(coordinates) == 2):
            return True
        elif len(coordinates) < 2:
            return False

        try:
            gradient_m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        except ZeroDivisionError:
            return False

        for i in range(2, len(coordinates) - 1):
            try:
                new_m = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            except ZeroDivisionError:
                return False

            if new_m != gradient_m:
                return False
        return True