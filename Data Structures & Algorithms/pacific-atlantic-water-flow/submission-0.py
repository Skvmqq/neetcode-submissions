class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(i, j, visited):
            if (i, j) not in visited:
                visited.add((i, j))

            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for dr, dc in directions:

                nr = i + dr
                nc = j + dc

                if (
                    (0 <= nr < ROWS)
                    and (0 <= nc < COLS)
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[i][j]
                ):
                    dfs(nr, nc, visited)


        pac = set()
        atl = set()
        ROWS = len(heights)
        COLS = len(heights[0])

        #checking if from pacific we can atlantic
        for j in range(ROWS):
            dfs(j, 0, pac)

        for i in range(COLS):
            dfs(0, i, pac)

        print(pac)

        #checking if from atl we can reach pacific 

        for k in range(ROWS):
            dfs(k, COLS - 1, atl)

        for m in range(COLS):
            dfs(ROWS - 1, m, atl)

        return list((pac & atl))





        

        