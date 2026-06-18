import pickle
import community as community_louvain

with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

partition = community_louvain.best_partition(G)

communities = {}

for node, comm_id in partition.items():
    communities.setdefault(comm_id, []).append(node)

print("Total Communities:", len(communities))

for comm_id, members in communities.items():
    print(f"\nCommunity {comm_id}")
    print("Members:", len(members))
    print(members[:5])