# Community Intelligence Platform

## Overview

Community Intelligence Platform is a research analytics and network intelligence system that automatically collects research publications, builds collaboration networks, detects research communities, identifies influential researchers, and analyzes research trends.

The platform uses graph theory, network science, and community detection algorithms to transform research publication data into actionable insights.

---

## Key Features

### Research Paper Collection

* Fetches research publications using OpenAlex API
* Extracts author and publication information
* Stores structured research datasets

### Collaboration Network Construction

* Builds author collaboration networks
* Creates graph representations of research communities
* Maps researcher relationships

### Community Detection

* Uses Louvain Community Detection Algorithm
* Identifies hidden research communities
* Groups researchers with similar collaboration patterns

### Researcher Ranking

* Measures researcher influence using network connectivity
* Identifies top contributors within communities
* Ranks influential researchers automatically

### Topic Detection

* Extracts community research interests
* Identifies dominant research themes
* Discovers emerging research areas

### Interactive Dashboard

* Built with Streamlit
* Displays community statistics
* Shows researcher rankings
* Provides searchable research insights

---

## System Architecture

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

---

## Technology Stack

### Backend

* Python

### Data Source

* OpenAlex API

### Graph Analytics

* NetworkX

### Community Detection

* Louvain Algorithm

### Visualization

* PyVis
* Streamlit

### Data Processing

* JSON
* Pandas

---

## Project Statistics

Current Dataset:

* Research Papers: 50
* Researchers: 98
* Communities Detected: 22
* Collaboration Links: 206

---

## Research Applications

* Academic Research Analysis
* Research Community Discovery
* Collaboration Network Analysis
* Expert Identification
* Trend Detection
* Scientific Knowledge Mapping

---

## Future Enhancements

* Graph Neural Networks (GNN)
* Community Evolution Tracking
* Citation Analysis
* Real-Time Research Monitoring
* AI-Based Topic Summarization
* AWS Cloud Deployment
* Docker Containerization

---

## Author

Akhil Kumar

Integrated B.Tech + M.Tech (Artificial Intelligence & Robotics)

Gautam Buddha University

---

## License

MIT License
