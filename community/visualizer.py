import pickle
from pyvis.network import Network
import community as community_louvain

with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

partition = community_louvain.best_partition(G)

net = Network(
    height="750px",
    width="100%",
    bgcolor="#222222",
    font_color="white"
)

for node in G.nodes():
    net.add_node(
        node,
        label=node,
        group=partition[node]
    )

for edge in G.edges():
    net.add_edge(edge[0], edge[1])

net.save_graph("data/community_network.html")

print("Visualization Saved")