import pickle

with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

researchers = []

for node in G.nodes():
    researchers.append((node, G.degree(node)))

researchers.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\n===== TOP 20 RESEARCHERS =====\n")

for rank, (name, score) in enumerate(researchers[:20], start=1):
    print(f"{rank}. {name} | Connections: {score}")

print("\nMost Influential Researcher:")
print(researchers[0][0])
print("Connections:", researchers[0][1])