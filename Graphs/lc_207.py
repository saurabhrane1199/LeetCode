import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = collections.defaultdict(list)

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        def dfs(source):
            if source in visited:
                return False
            if graph[source] == []:
                return True
            visited.add(source)
            for _e in graph[source]:
                if not dfs(_e):
                    return False
            visited.remove(source)
            graph[source] = []
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True


        