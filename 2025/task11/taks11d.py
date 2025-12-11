FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    G = nx.DiGraph()
    for node, children in graph.items():
        for child in children:
            G.add_edge(node, child)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(100, 80))

    highlight_nodes = ['svr', 'fft', 'dac', 'out']

    node_colors = ["orange" if node in highlight_nodes else "lightblue" for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors,
            arrowsize=10, font_size=8, font_weight="bold", edge_color="gray")


    plt.show()

from functools import lru_cache

global stop

def find_paths(graph, start, end):
    @lru_cache(maxsize=None)
    def dfs(node):
        if node in stop:
            return 0
        if node == end:
            return 1

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        return total

    return dfs(start)


def get_stops(graph, start, max_level):
    result = set()
    current_level = [start]

    for level in range(max_level):
        next_level = []
        for node in current_level:
            for neigh in graph.get(node, []):
                if neigh not in result and neigh != start:
                    result.add(neigh)
                    next_level.append(neigh)
        current_level = next_level

    return result



def main():
    lines = read_file()

    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        name, rest = line.split(":")
        name = name.strip()
        outs = rest.strip().split()
        graph[name] = outs

    # draw_graph(graph)

    results = []
    main_path = [("svr", "fft", ["dac", "out"]), ("fft", "dac", ["out"]), ("dac", "out", [])]
    
    for p1, p2, stop_a in main_path:
        stop_a.append(get_stops(graph, p2, 700))

    global stop

    total = 1

    for p1, p2, stop_a in main_path:
        print(f"for {p1} -> {p2}")
        stop = stop_a
        result = find_paths(graph, p1, p2)
        results.append(f"{p1} -> {p2}: {result}")
        total *= result

    for r in results:
        print(r)

    print(f"total: {total}")


if __name__ == '__main__':
    main()
