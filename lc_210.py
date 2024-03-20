class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        import collections
        
        visited = set()
        graph = collections.defaultdict(list)

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])

        output = []

        def dfs(source):
            if source in visited:
                return False
            
            if graph[source]==[]:
                if source not in output:
                    output.append(source)
                return True

            visited.add(source)
            for _e in graph[source]:
                if not dfs(_e):
                    return False

            visited.remove(source)
            output.append(source)
            graph[source] = []
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output


        