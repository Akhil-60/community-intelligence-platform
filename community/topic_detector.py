import json
import pickle
import community as community_louvain

with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

with open("data/papers.json", "r", encoding="utf-8") as f:
    papers = json.load(f)

partition = community_louvain.best_partition(G)

author_topics = {}

for paper in papers["results"]:

    title = paper.get("title", "")

    for auth in paper.get("authorships", []):

        author = auth.get("author", {})
        name = author.get("display_name")

        if name:

            if name not in author_topics:
                author_topics[name] = []

            author_topics[name].append(title)

community_titles = {}

for author, cid in partition.items():

    if cid not in community_titles:
        community_titles[cid] = []

    if author in author_topics:
        community_titles[cid].extend(author_topics[author])

print("\n===== COMMUNITY TOPICS =====\n")

for cid, titles in community_titles.items():

    titles = list(set(titles))

    print(f"\nCommunity {cid}")

    for title in titles[:5]:
        print("-", title)

    print("-" * 40)