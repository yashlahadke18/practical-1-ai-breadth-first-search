import streamlit as st
from collections import deque

# Title
st.title("Breadth First Search (BFS) Visualization")

# Graph definition
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e', 'f'],
    'd': [],
    'e': [],
    'f': ['g', 'h'],
    'g': [],
    'h': ['i'],
    'i': []
}

# BFS Function
def bfs(start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            traversal.append(node)
            visited.add(node)
            queue.extend(graph[node])

    return traversal

# Dropdown to select start node
start_node = st.selectbox("Select Starting Node:", list(graph.keys()))

# Run BFS on button click
if st.button("Run BFS"):
    result = bfs(start_node)
    st.success("BFS Traversal:")
    st.write(" ➝ ".join(result))
