from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, end in sorted(tickets):
            graph[start].append(end)

        result = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            result.append(a)
        
        dfs("JFK")

        return result[::-1]