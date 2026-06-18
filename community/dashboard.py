import streamlit as st
import json
import pickle
import community as community_louvain

st.set_page_config(
    page_title="Community Intelligence Platform",
    layout="wide"
)

st.title("🚀 Community Intelligence Platform")

# Papers
with open("data/papers.json", "r", encoding="utf-8") as f:
    papers = json.load(f)

# Graph
with open("data/research_graph.pkl", "rb") as f:
    G = pickle.load(f)

partition = community_louvain.best_partition(G)

total_papers = len(papers["results"])
total_authors = G.number_of_nodes()
total_communities = len(set(partition.values()))

col1, col2, col3 = st.columns(3)

col1.metric("📄 Papers", total_papers)
col2.metric("👨‍🔬 Authors", total_authors)
col3.metric("🌐 Communities", total_communities)

st.divider()

researchers = []

for node in G.nodes():
    researchers.append(
        (node, G.degree(node))
    )

researchers.sort(
    key=lambda x: x[1],
    reverse=True
)

st.subheader("🏆 Top Researchers")

for name, score in researchers[:10]:
    st.write(f"{name} — Connections: {score}")
    st.divider()

st.subheader("🔍 Search Researcher")

search_name = st.text_input(
    "Enter Researcher Name"
)

if search_name:

    found = False

    for node in G.nodes():

        if search_name.lower() in node.lower():

            st.success(f"Researcher: {node}")

            st.write(
                f"Connections: {G.degree(node)}"
            )

            st.write(
                f"Community: {partition[node]}"
            )

            found = True

    if not found:

        st.error(
            "Researcher not found"
        )
        st.divider()

st.subheader("📚 Community Topics")

topics = {
    20: "Deep Learning Community Detection",
    5: "Overlapping Community Detection",
    9: "Social Media Community Detection",
    6: "Louvain Community Detection",
    11: "Directed Network Community Detection"
}

for cid, topic in topics.items():
    st.write(f"Community {cid}: {topic}")
    st.divider()

st.subheader("🌐 Interactive Research Network")

with open(
    "data/community_network.html",
    "r",
    encoding="utf-8"
) as f:

    html_content = f.read()

st.components.v1.html(
    html_content,
    height=700,
    scrolling=True
)