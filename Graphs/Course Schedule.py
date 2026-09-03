class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [False] * numCourses
        path_visited = [False] * numCourses
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)


        def dfs(node):
            visited[node] = True
            path_visited[node] = True

            for neighbour in graph[node]:
                if path_visited[neighbour]:
                    return True
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
            path_visited[node] = False
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True
            
