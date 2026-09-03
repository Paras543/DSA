class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            graph[b].append(a)
        
        visited = [False] * numCourses
        path_visited = [False] * numCourses
        stack = []

        def dfs(node):
            visited[node] = True
            path_visited[node] = True

            for nei in graph[node]:
                if path_visited[nei]:
                    return True
                if not visited[nei]:
                    if dfs(nei):
                        return True

            path_visited[node] = False
            stack.append(node)
            return False

        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        stack.reverse()
        return stack


            


        