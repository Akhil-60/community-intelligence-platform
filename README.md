# Community Intelligence Platform

## 🚀 Live Demo

### AWS Production Deployment

🔗 https://communityintel.duckdns.org

### Streamlit Cloud Deployment

🔗 https://community-intelligence-platform-e4z3n2nugpclbakdsnjmbx.streamlit.app

### GitHub Repository

🔗 https://github.com/Akhil-60/community-intelligence-platform

---

# 📖 Overview

Community Intelligence Platform is a research analytics and network intelligence system designed to discover hidden collaboration patterns within scientific research communities.

The platform automatically collects research publications from the OpenAlex database, constructs author collaboration networks, detects research communities using graph-based algorithms, identifies influential researchers, and analyzes emerging research trends through interactive visualizations.

Traditional research databases provide publication records but often fail to reveal the underlying collaboration structure among researchers. This project addresses that challenge by transforming publication metadata into a collaboration network where researchers are represented as nodes and co-authorship relationships are represented as edges.

Using NetworkX and the Louvain Community Detection Algorithm, the system identifies groups of closely connected researchers, enabling the discovery of research communities, influential contributors, and domain-specific collaboration patterns.

The final output is presented through an interactive Streamlit dashboard that provides real-time insights into research communities, collaboration networks, researcher rankings, and topic distributions.

---

# 🎯 Problem Statement

Modern scientific research generates massive volumes of publications across multiple disciplines. While publication databases provide access to research papers, they do not easily reveal:

* Hidden collaboration communities
* Influential researchers within a field
* Community-level research interests
* Emerging research trends
* Structural relationships among researchers

Researchers, institutions, and policymakers require these insights to understand knowledge flow, identify experts, evaluate collaborations, and discover emerging areas of research.

This project addresses these challenges using graph analytics, network science, and community detection techniques.

---

# 🎯 Objectives

* Collect research publication data using OpenAlex API
* Construct researcher collaboration networks
* Detect hidden research communities
* Rank influential researchers
* Identify dominant research topics
* Visualize collaboration structures interactively
* Generate actionable research intelligence

---

# ✨ Key Features

## Research Paper Collection

* Fetches research publications using OpenAlex API
* Extracts author and publication information
* Stores structured research datasets

## Collaboration Network Construction

* Builds author collaboration networks
* Creates graph representations of research communities
* Maps researcher relationships

## Community Detection

* Uses Louvain Community Detection Algorithm
* Identifies hidden research communities
* Groups researchers with similar collaboration patterns

## Researcher Ranking

* Measures researcher influence using network connectivity
* Identifies top contributors within communities
* Ranks influential researchers automatically

## Topic Detection

* Extracts community research interests
* Identifies dominant research themes
* Discovers emerging research areas

## Interactive Dashboard

* Built using Streamlit
* Displays community statistics
* Shows researcher rankings
* Provides searchable research insights
* Interactive community visualization

---

# ⚙️ Methodology

### 1. Research Data Collection

The platform retrieves publication metadata from the OpenAlex API, including:

* Research papers
* Authors
* Affiliations
* Keywords
* Publication information

### 2. Collaboration Network Construction

A co-authorship graph is generated where:

* Nodes represent researchers
* Edges represent collaboration relationships

The resulting graph captures the structure of research collaborations.

### 3. Community Detection

The Louvain Community Detection Algorithm is applied to identify densely connected groups of researchers.

### 4. Researcher Ranking

Researchers are ranked based on network influence and connectivity, helping identify key contributors within each community.

### 5. Topic Detection

Community publications are analyzed to identify dominant research themes and emerging topics.

### 6. Interactive Visualization

Results are presented through a Streamlit dashboard for exploration and analysis.

---

# 🏗️ System Architecture

![System Architecture](assets/System%20framework.png)

## Workflow

```text
OpenAlex API
      ↓
Research Data Collection
      ↓
Author Collaboration Network
      ↓
Graph Construction (NetworkX)
      ↓
Community Detection (Louvain Algorithm)
      ↓
Researcher Ranking
      ↓
Topic Detection
      ↓
Interactive Dashboard (Streamlit)
```

---

# 🛠️ Technology Stack

## Backend

* Python

## Data Source

* OpenAlex API

## Graph Analytics

* NetworkX

## Community Detection

* Louvain Algorithm

## Data Processing

* Pandas
* JSON

## Visualization

* Streamlit
* PyVis

## Cloud & Deployment

* AWS EC2
* Nginx Reverse Proxy
* DuckDNS
* Let's Encrypt SSL
* Streamlit Community Cloud
* GitHub

---

# 📊 Project Statistics

Current Dataset:

* Research Papers: 50+
* Researchers: 98+
* Communities Detected: 22
* Collaboration Links: 206+

---

# 🌍 Real-World Applications

* Academic Research Analysis
* Research Community Discovery
* Collaboration Network Analysis
* Expert Identification
* Research Trend Detection
* Scientific Knowledge Mapping
* Institutional Research Assessment
* Research Intelligence Systems

---

# 🚀 Deployment

### AWS Production

https://communityintel.duckdns.org

### Streamlit Cloud

https://community-intelligence-platform-e4z3n2nugpclbakdsnjmbx.streamlit.app

### GitHub Repository

https://github.com/Akhil-60/community-intelligence-platform

---

# 💻 Local Installation

```bash
git clone https://github.com/Akhil-60/community-intelligence-platform.git

cd community-intelligence-platform

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

streamlit run community/dashboard.py
```

Local URL:

```text
http://localhost:8501
```

---

# 🔮 Future Enhancements

* Graph Neural Networks (GCN/GNN)
* Community Evolution Tracking
* Citation Network Analysis
* AI-Based Research Summarization
* Research Recommendation System
* Agentic AI Research Assistant
* Real-Time Research Monitoring
* Docker Containerization
* CI/CD Automation

---

# 👨‍💻 Author

**Akhil Kumar**

Integrated B.Tech + M.Tech (Artificial Intelligence & Robotics)

Gautam Buddha University, Greater Noida

---

# 📜 License

MIT License
