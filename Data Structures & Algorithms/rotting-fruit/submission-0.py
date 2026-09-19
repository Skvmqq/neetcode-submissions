from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
for this question it is asking for us to track min number of minutes it will take to rotten all the fruits 

what i am thinking is: using a bfs and process 
:
we should store the rotten food in a queue 
if queue is empty 
return -1  becuase then its not possible 

once we have then we run the normal bfs and track level wise 
one thing i am unsure is how will it work in case we have wrotten fruits but it can't rotten all of them 
okay so if all of the neioghors are 0 then not possible 
[1,0,1]
[0,2,0]
[1,0,1]

so lets try to write the code

        '''

        row = len(grid)
        col = len(grid[0])
        queue = deque()
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))

        
        count =0
        while queue:
            rotten_this_minute = False

            for _ in range(len(queue)):
                r,c =queue.popleft()
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+ dc

                    if (0 <= nr < row and
                        0 <= nc < col and
                        grid[nr][nc] == 1):
                            grid[nr][nc] = 2 
                            queue.append((nr,nc))
                            rotten_this_minute = True
            if rotten_this_minute:
                count +=1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return count






                

