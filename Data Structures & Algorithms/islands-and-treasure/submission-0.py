from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        queue =deque()

        directions =[ 
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==0:
                    queue.append((i,j))

        dist = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                
                for dr, dc in directions:
                    new_row = r+dr
                    new_col = c+dc

                    if (0<=new_row<len(grid)
                        and (0<=new_col<len(grid[0]))
                        
                        and grid[new_row][new_col] == 2147483647
                    ): 
                        grid[new_row][new_col] = dist
                        queue.append((new_row,new_col))
            dist +=1


# so if its -1 then we don't do anyhting 
# if its 0 then 
                      



