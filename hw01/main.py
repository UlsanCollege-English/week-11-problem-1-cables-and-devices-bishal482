# def build_graph(edges, directed=False):
#     graph = {}

#     for u, v in edges:
#         # ensure nodes exist
#         if u not in graph:
#             graph[u] = []
#         if v not in graph:
#             graph[v] = []

#         # add edge u -> v
#         graph[u].append(v)

#         # if undirected, also add the reverse direction
#         if not directed:
#             graph[v].append(u)

#     return graph


# def degree_dict(graph):
#     d = {}
#     for node in graph:
#         d[node] = len(graph[node])
#     return d
