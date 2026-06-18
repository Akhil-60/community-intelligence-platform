import pickle
import community as community_louvain

# Graph load karo
with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

# Communities detect karo
partition = community_louvain.best_partition(G)

communities = {}

# Community-wise members store karo
for node, community_id in partition.items():

    if community_id not in communities:
        communities[community_id] = []

    communities[community_id].append(node)

print("\n===== COMMUNITY REPORT =====\n")

# Har community analyze karo
for community_id, members in communities.items():

    print(f"\nCommunity ID: {community_id}")
    print(f"Total Members: {len(members)}")

    researcher_scores = []

    for researcher in members:

        score = G.degree(researcher)

        researcher_scores.append(
            (researcher, score)
        )

    researcher_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop Researchers:")

    for researcher, score in researcher_scores[:5]:

        print(
            f"{researcher} | Connections: {score}"
        )

    print("-" * 40)

    report = []

report.append("===== COMMUNITY REPORT =====\n")

for community_id, members in communities.items():

    report.append(f"\nCommunity ID: {community_id}")
    report.append(f"Total Members: {len(members)}")

    researcher_scores = []

    for researcher in members:
        score = G.degree(researcher)
        researcher_scores.append((researcher, score))

    researcher_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    report.append("\nTop Researchers:")

    for researcher, score in researcher_scores[:5]:
        report.append(
            f"{researcher} | Connections: {score}"
        )

    report.append("-" * 40)

with open(
    "data/community_report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("\n".join(report))

print("Community Report Saved")
