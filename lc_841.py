def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n

        q = [0]

        while q:
            curr  = q.pop()
            for i in rooms[curr]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True
            visited[curr] = True

        return all(visited)