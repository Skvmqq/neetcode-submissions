class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # the condition for cycle ?
        # if we visit a visited node and its parent is not that node then its a cycle?
        graph = [[] for _ in range(numCourses)]

        # prerequisite -> course
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visited = [False] * numCourses
        path = [False] * numCourses

        def dfs(course):

            # We reached a course already in the current path
            if path[course]:
                return False

            # Already completely explored
            if visited[course]:
                return True

            visited[course] = True
            path[course] = True

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Leave the current DFS path
            path[course] = False

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

        