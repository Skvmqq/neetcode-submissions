class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(numCourses)]
        path = [False] * numCourses
        visited = [False] * numCourses
        output = []

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        def dfs(i):

            if path[i]:
                return False

            if visited[i]:
                return True

            path[i] = True
            visited[i] = True

            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            output.append(i)
            path[i] = False

            return True

        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        return output[::-1]
            



         