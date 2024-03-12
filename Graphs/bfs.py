graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'e' : [],
    'f' : [],

}

def bfs(graph, source):
    visited = set()
    queue = [source]

    while (queue):
        curr_vertex = queue.pop(0)
        print(f"{curr_vertex}->")

        if curr_vertex not in visited:
            visited.add(curr_vertex)

            for neighbour in graph.get(curr_vertex, []):
                if neighbour not in visited:
                    queue.append(neighbour)


bfs(graph, 'a')


