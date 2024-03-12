graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'e' : [],
    'f' : [],

}

def dfs(graph, source):
    visited = set()
    stack = [source]

    while (stack):
        curr_vertex = stack.pop()
        print(f"{curr_vertex}->")

        if curr_vertex not in visited:
            visited.add(curr_vertex)

            for neighbour in graph.get(curr_vertex, []):
                if neighbour not in visited:
                    stack.append(neighbour)


dfs(graph, 'a')


