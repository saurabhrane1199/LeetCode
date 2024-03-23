import collections
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        mdist = lambda p1, p2 : abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                d = mdist(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))

        ctr, ans, visit, heap = 1, 0, [0]*n, c[0]
        visit[0]=1
        heapq.heapify(heap)

        while heap:
            d, j = heapq.heappop(heap)
            if not visit[j]:
                visit[j],ctr, ans = 1, ctr+1, ans+d
                for node in c[j]:
                    heapq.heappush(heap, node)
            if ctr>=n:
                break

        return ans
        