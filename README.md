# Community Intelligence Platform

## 🚀 Live Demo

### AWS Production Deployment

🔗 https://communityintel.duckdns.org

### Streamlit Cloud Deployment

🔗 https://community-intelligence-platform.streamlit.app

### GitHub Repository

🔗 https://github.com/Akhil-60/community-intelligence-platform

---

# Overview

Community Intelligence Platform is an AI-powered research analytics and network intelligence system that automatically collects research publications, builds collaboration networks, detects research communities, identifies influential researchers, and analyzes research trends.

The platform combines graph theory, network science, community detection algorithms, and interactive visualization to transform research publication data into actionable insights.

---

# Key Features

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

---

# System Architecture

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

# Technology Stack

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

# Project Statistics

Current Dataset:

* Research Papers: 50+
* Researchers: 98+
* Communities Detected: 22
* Collaboration Links: 206+

---

# Research Applications

* Academic Research Analysis
* Research Community Discovery
* Collaboration Network Analysis
* Expert Identification
* Research Trend Detection
* Scientific Knowledge Mapping
* Research Intelligence Systems

---

# Local Installation

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

# Deployment Links

### AWS Production

https://communityintel.duckdns.org

### Streamlit Cloud

https://community-intelligence-platform.streamlit.app

### Local Development

http://localhost:8501

---

# Future Enhancements

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

# Author

**Akhil Kumar**

Integrated B.Tech + M.Tech (Artificial Intelligence & Robotics)

Gautam Buddha University, Greater Noida

---

# License

MIT License



