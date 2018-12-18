import igraph
from igraph.drawing import plot
from color import planar_five_color

color_dict = {0: 'green', 1: 'blue', 2: 'red', 3: 'yellow', 4: 'pink'}

five_regular = igraph.Graph(n=12)
five_reg = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 5), (1, 6), (1, 7),
            (2, 3), (2, 7), (2, 8),
            (3, 4), (3, 8), (3, 9),
            (4, 5), (4, 9), (4, 10),
            (5, 6), (5, 10),
            (6, 7), (6, 10), (6, 11),
            (7, 8), (7, 11),
            (8, 9), (8, 11),
            (9, 10), (9, 11),
            (10, 11)]

five_regular.add_edges(five_reg)
graph_colored = planar_five_color(five_regular)
graph_colored.vs['color'] = [color_dict[color] for color in graph_colored.vs['color']]
layout = graph_colored.layout("kk")
plot(graph_colored, target='graph.png', layout=layout)
