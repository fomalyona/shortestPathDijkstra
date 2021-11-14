def dijkstra_my(graph, start_graph, end_graph):
    distances = {}
    # вершины
    tops = {}
    # список узлов
    nodes = graph.keys()
    # Метка самой вершины полагается равной 0, метки остальных вершин — бесконечности
    for node in graph:
        distances[node] = float('inf')
        tops[node] = None
    distances[start_graph] = 0
    vis = []

    # пока есть узлы без посещения
    while len(vis) < len(nodes):

        still_in = {node: distances[node] \
                    for node in [node for node in \
                                 nodes if node not in vis]}

        # ближайший к текущему узлу узел
        closest = min(still_in, key=distances.get)

        # добавляем в посещенные узлы
        vis.append(closest)

        for node in graph[closest]:
            # если есть более короткий путь
            if distances[node] > distances[closest] + \
                    graph[closest][node]:
                # обновляем
                distances[node] = distances[closest] + \
                                  graph[closest][node]

                tops[node] = closest
    # окончательный путь
    path = [end_graph]
    while start_graph not in path:
        path.append(tops[path[-1]])

    return path[::-1], distances[end_graph]


def findPath(start_find, N, graph):
    arr = []
    for node_ in graph:
        if node_ != start_find:
            visited = []
            length_path = 0
            path_tmp, cost_tmp = dijkstra_my(graph=graph, start_graph=start_find, end_graph=node_)
            for path in path_tmp:
                visited.append(path)
            length_path += cost_tmp
            vis = visited.copy()
            visited_ = visited.copy()
            rec_search(length_path, visited_, graph, N, vis, arr)
    return arr


def rec_search(length_path, visited_, graph, N_, vis, arr):
    if len(set(visited_)) != N_:
        for node in graph:
            if node not in visited_:
                path, cost = dijkstra_my(graph=graph, start_graph=visited_[-1], end_graph=node)
                for p in path:
                    visited_.append(p)
                length_path += cost
                rec_search(length_path, visited_, graph, N_, vis, arr)
                for k in range(len(path)):
                    del visited_[-1]
                length_path -= cost
    else:
        path, cost = dijkstra_my(graph=graph, start_graph=visited_[-1], end_graph='1')
        print("final_path")
        print(visited_)
        length_path += cost
        arr.append(length_path)
        length_path -= cost



def read_graph(N):
    dict_graph = {}
    for i in range(0, N):
        dict_str = {}
        graph_str = list([int(i) for i in input().split()])
        for j in range(0, len(graph_str)):
            if graph_str[j] != 0:
                dict_str[str(j + 1)] = graph_str[j]
        dict_graph[str(i + 1)] = dict_str
    return dict_graph

if __name__ == '__main__':
    M = int(input())
    # M = 5
    # graph_test = {
    #     '1': {'2': 2, '3': 2},
    #     '2': {'1': 2, '3': 2, '4': 2},
    #     '3': {'1': 2, '2': 2, '5': 2},
    #     '4': {'2': 2, '5': 2},
    #     '5': {'3': 2, '4': 2}
    # }
    graph_test = read_graph(M)
    end = str(M)
    start = '1'
    cost_final = findPath(start, M, graph_test)
    # print(cost_final)
    print(min(cost_final))