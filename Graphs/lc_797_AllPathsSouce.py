class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = {}

        for idx, _g in enumerate(graph):
            adjList[idx]=_g

        finalRes = []
        
        def search(currPath, currNode):
            if currNode==(len(graph)-1):
                finalRes.append(list(currPath))

            for v in adjList[currNode]:
                currPath.append(v)
                search(currPath, v)
                print(currPath)
                currPath.pop()
                    

        search([0],0)

        return finalRes

                    


        