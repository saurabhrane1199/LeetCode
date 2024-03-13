graph = {
    'a' : ['b', 'c'],
    'b' : ['d'],
    'c' : ['e'],
    'e' : [],
    'f' : [],

}



def pathExists(graph, src, dst):
    if src == dst:
        return True
    
    for neigh in graph.get(src, []):
        if pathExists(graph, neigh, dst):
            return True

    return False


print(pathExists(graph, 'a', 'f'))