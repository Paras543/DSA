from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):

        adj = defaultdict(list)

        # Make every character a node
        for word in words:
            for ch in word:
                adj[ch] = []

        # Build graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Invalid case
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        visiting = set()
        visited = set()
        result = []

        def dfs(ch):

            if ch in visiting:
                return False

            if ch in visited:
                return True

            visiting.add(ch)

            for nei in adj[ch]:
                if not dfs(nei):
                    return False

            visiting.remove(ch)
            visited.add(ch)
            result.append(ch)

            return True

        for ch in adj:
            if not dfs(ch):
                return ""

        return "".join(result[::-1])