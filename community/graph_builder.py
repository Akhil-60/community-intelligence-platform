import json
import networkx as nx

with open("data/papers.json", "r", encoding="utf-8") as f:
    data = json.load(f)

G = nx.Graph()

papers = data.get("results", [])

for paper in papers:

    authors = []

    for auth in paper.get("authorships", []):
        author = auth.get("author", {})
        name = author.get("display_name")

        if name:
            authors.append(name)

    for i in range(len(authors)):
        for j in range(i + 1, len(authors)):
            G.add_edge(authors[i], authors[j])

print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

import pickle

with open("data/research_graph.pkl", "wb") as f:
    pickle.dump(G, f)

print("Graph Saved Successfully")
