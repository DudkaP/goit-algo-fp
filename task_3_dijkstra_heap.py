import heapq
from typing import Dict, List, Tuple

Graph = Dict[str, List[Tuple[str, int]]]

def dijkstra(graph: Graph, start: str) -> Dict[str, float]:
    dist = {v: float("inf") for v in graph}
    dist[start] = 0.0

    pq = [(0.0, start)]
    visited = set()

    while pq:
        cur_dist, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            nd = cur_dist + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

if __name__ == "__main__":
    graph: Graph = {
        "A": [("B", 5), ("C", 1)],
        "B": [("A", 5), ("C", 2), ("D", 1)],
        "C": [("A", 1), ("B", 2), ("D", 4), ("E", 8)],
        "D": [("B", 1), ("C", 4), ("E", 3)],
        "E": [("C", 8), ("D", 3)]
    }
    print(dijkstra(graph, "A"))
