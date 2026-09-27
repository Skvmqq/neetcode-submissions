class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph =[[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = [False] * numCourses
        path =[False] *numCourses


        def dfs(n):
            if path[n]:
                return False 
            if visited[n]: 
                return True 
            
            path[n] = True 
            visited[n] = True 

            for neighbour in graph[n]:
                if not dfs(neighbour):
                    return False 
            
            path[n] = False 

            return True 

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return False


        return True



        