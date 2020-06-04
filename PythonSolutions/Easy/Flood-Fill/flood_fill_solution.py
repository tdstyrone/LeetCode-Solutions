class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        num_rows = len(image)
        num_cols = len(image[0])

        color_location = image[sr][sc]
        if color_location == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color_location:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < num_rows:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < num_cols:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image