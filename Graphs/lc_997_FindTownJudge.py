# The idea here is to keep a score of in-degree and out-degree, the judge would have in-degree of (n-1) and outdegree of 0

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Trusted = [0] * (n+1)
        for (a, b) in trust:
            Trusted[a] -= 1
            Trusted[b] += 1
            
        for i in range(1, len(Trusted)):
            if Trusted[i] == n-1:
                return i
        return -1