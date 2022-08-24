def solution(entrances, exits, path):
    paths = find_all_paths(entrances, exits, path)
    bunnies = 0
    for path in paths:
        bunnies += path[1]
    return bunnies

def find_all_paths( us, ds,path):
    result = []
    for u in us:
        for d in ds:
            while True:
                found_path,max_weight = find_path( u, d,path)
                if found_path is None:
                    break
                result.append((found_path,max_weight))
                for i in range(len(found_path)-1):
                    # update the weight of the path
                    path[found_path[i]][found_path[i+1]] -= max_weight
    return result

def find_path( u, d,path):
    visited = [False for _ in range(len(path[0]))]
    found_path = []
    max_weight = 2000000 #largest possible weight
    while u != d:
        visited[u] = True
        for i in range(len(path[u])):
            if (not visited[i] and path[u][i] > 0):
                found_path.append(u)
                #calculate the max weight along the path
                max_weight = min(max_weight, path[u][i])
                u = i
                break
            # backward if no path found
            if i == len(path[u])-1:
                if len(found_path) != 0:
                    u = found_path.pop()
                else:
                    return None,None
    found_path.append(d)
    return found_path,max_weight
        