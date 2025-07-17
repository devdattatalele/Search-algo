import time
from collections import deque

class Graph:
    def __init__(self, data):
        self.graph = data
    def get_nodes(self):
        return list(self.graph.keys())
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    def bfs(self, start_node, target_node):
        start_time = time.perf_counter()
        if start_node not in self.graph or target_node not in self.graph:
            end_time = time.perf_counter()
            return [], 0, end_time - start_time
        queue = deque([(start_node, [start_node])])
        visited = set()
        nodes_visited_count = 0
        while queue:
            current_node, path = queue.popleft()
            if current_node in visited:
                continue
            visited.add(current_node)
            nodes_visited_count += 1
            if current_node == target_node:
                end_time = time.perf_counter()
                return path, nodes_visited_count, end_time - start_time
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        end_time = time.perf_counter()
        return [], nodes_visited_count, end_time - start_time
    def dfs(self, start_node, target_node):
        start_time = time.perf_counter()
        if start_node not in self.graph or target_node not in self.graph:
            end_time = time.perf_counter()
            return [], 0, end_time - start_time
        stack = [(start_node, [start_node])]
        visited = set()
        nodes_visited_count = 0
        while stack:
            current_node, path = stack.pop()
            if current_node in visited:
                continue
            visited.add(current_node)
            nodes_visited_count += 1
            if current_node == target_node:
                end_time = time.perf_counter()
                return path, nodes_visited_count, end_time - start_time
            neighbors = self.get_neighbors(current_node)
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        end_time = time.perf_counter()
        return [], nodes_visited_count, end_time - start_time 