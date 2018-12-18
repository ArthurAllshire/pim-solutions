import igraph
from assertpy import assert_that
from two_color import two_color

# functions to detect proper coloring taken from book code


def improperly_colored(G, e):
    return G.vs[e.source]['color'] == G.vs[e.target]['color']


def properly_colored(G):
    return 0 == sum(1 for e in G.es if improperly_colored(G, e))


def test_not_2colorable():
    G = igraph.Graph.Full(3)
    colorable, colored = two_color(G)
    assert_that(colorable).is_false()
    assert_that(colored).is_none()


def test_is_2colorable():
    G = igraph.Graph(n=6)
    shape = [(0, 1), (0, 5),
             (1, 2), (1, 4),
             (2, 3), (4, 5)]
    G.add_edges(shape)
    colorable, colored = two_color(G)
    assert_that(colorable).is_true()
    assert_that(properly_colored(colored)).is_true()
