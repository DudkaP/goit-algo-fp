import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#0B1F3A"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def hex_gradient(i, n):
    start = (11, 31, 58)
    end = (190, 230, 255)
    t = i / max(1, n-1)
    r = int(start[0] + (end[0]-start[0]) * t)
    g = int(start[1] + (end[1]-start[1]) * t)
    b = int(start[2] + (end[2]-start[2]) * t)
    return f"#{r:02X}{g:02X}{b:02X}"

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_visual(root):
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    for i, node in enumerate(order):
        node.color = hex_gradient(i, len(order))
        draw_tree(root)

def bfs_visual(root):
    order = []
    q = deque([root])
    while q:
        node = q.popleft()
        order.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    for i, node in enumerate(order):
        node.color = hex_gradient(i, len(order))
        draw_tree(root)

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print("DFS visualization...")
    dfs_visual(root)

    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print("BFS visualization...")
    bfs_visual(root)
