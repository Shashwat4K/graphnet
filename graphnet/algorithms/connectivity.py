import math

def get_bridge_edges(graph):
    """
    Detect all the bridge edges in the graph

    Parameters
    ----------
    graph: Graph
        graph instance to where the the nodes are.
    
    returns
    -------
    bridges: List[Tuple[Node]]
        A list of tuples. 
        Each tuple contains source and destination node of a bridge edge.
    """
    dfs_counter = 0
    dfs_ord = {node: math.inf for node in graph}
    low_link = {node: math.inf for node in graph}
    visited_vertices = {node: False for node in graph}
    parent_vertex = {node: -1 for node in graph}
    bridges = []
    for node in graph:
        if visited_vertices[node] == False:
            bridge_util(node, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, graph, bridges)
    return bridges

def bridge_util(u, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, graph, bridges):
    visited_vertices[u] = True
    dfs_ord[u] = dfs_counter
    low_link[u] = dfs_counter
    dfs_counter += 1
    for v in u.adjacent_nodes:
        if visited_vertices[v] == False:
            parent_vertex[v] = u
            bridge_util(v, visited_vertices, parent_vertex, low_link, dfs_ord, dfs_counter, graph, bridges)
            low_link[u] = min(low_link[u], low_link[v])
            if low_link[v] > dfs_ord[u]:
                bridges.append((u, v) if u.value < v.value else (v, u))
        elif v != parent_vertex[u]:
            low_link[u] = min(low_link[u], dfs_ord[v])
