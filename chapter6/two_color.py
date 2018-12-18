colors = list(range(2))


def two_color(G):
    graph = G.copy()
    for v in graph.vs:
        v['color'] = -1
    visited_edge_ids = set()
    splits = []
    last_color = colors[0]
    next_vertex = graph.vs[0]
    while not len(visited_edge_ids) == len(graph.es):

        neighbors = [graph.vs[i] for i in graph.neighbors(next_vertex)]
        (n_colored, n_uncolored) = split_by_predicate(neighbors,
                                                      lambda x: x['color'] in colors)
        if last_color is None:
            # we have had to ascend after reaching tree end, get last_color from a painted vertex
            last_color = n_colored[0]['color']

        visited_edge_ids |= set([graph.get_eid(next_vertex, n) for n in n_colored])

        color = int(not last_color)
        next_vertex['color'] = color
        next_equal = [next_vertex['color'] == v['color'] for v in neighbors]
        not_two_colorable = any(next_equal)
        if not_two_colorable:
            return False, None

        if len(n_uncolored) > 0:
            # traverse edges that have not been traversed and do not have a coloured
            # vertex across from them
            next_vertex = n_uncolored[0]
            last_color = color
            if len(n_uncolored) > 1:
                splits.append(n_uncolored[1:])
        else:
            # we have reached the end of this way of traversing
            # backtrack to the last split
            last_color = None
            next_vertex = splits[-1].pop(-1)
            if len(splits[-1]) == 0:
                splits.pop(-1)
    return True, graph


def split_by_predicate(iterable, predicate):
    groups = {True: [], False: []}
    for v in iterable:
        groups[predicate(v)].append(v)
    return (groups[True], groups[False])
