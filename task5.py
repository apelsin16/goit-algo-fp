import uuid
import networkx as nx
import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited=None, highlight_color="#FF0000"):
    if visited is None:
        visited = []
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    labels = {}
    for node in tree.nodes(data=True):
        node_id = node[0]
        node_data = node[1]
        if node_id in visited:
            colors.append(highlight_color)
        else:
            colors.append(node_data['color'])
        labels[node_id] = node_data['label']
    
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def hex_color_gradient(start_color, end_color, steps):
    start_color = start_color.lstrip('#')
    end_color = end_color.lstrip('#')
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (0, 2, 4))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (0, 2, 4))
    gradient = []
    for step in range(steps):
        interp_rgb = (
            int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * step / (steps - 1)),
            int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * step / (steps - 1)),
            int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * step / (steps - 1))
        )
        gradient.append('#{:02x}{:02x}{:02x}'.format(*interp_rgb))
    return gradient

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def bfs(root):
    queue = [root]
    visited = []
    total_nodes = count_nodes(root)
    gradient = hex_color_gradient("#000080", "#00FFFF", total_nodes)
    while queue:
        node = queue.pop(0)
        if node:
            visited.append(node.id)
            draw_tree(root, visited, gradient[len(visited) - 1])
            queue.append(node.left)
            queue.append(node.right)
            time.sleep(1)

def dfs(root):
    stack = [root]
    visited = []
    total_nodes = count_nodes(root)
    gradient = hex_color_gradient("#000080", "#00FFFF", total_nodes)
    while stack:
        node = stack.pop()
        if node:
            visited.append(node.id)
            draw_tree(root, visited, gradient[len(visited) - 1])
            stack.append(node.right)
            stack.append(node.left)
            time.sleep(1)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева з обходом в ширину
print("Обхід в ширину (BFS):")
bfs(root)

# Відображення дерева з обходом в глибину
print("Обхід в глибину (DFS):")
dfs(root)
