class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)

        state = [0]*n
        def dfs(node):
            if state[node]== 1:
                return False
            if state[node]== 2:
                return True
            state[node] = 1
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node] = 2
            return True


        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans



### Revise the logic of the code 