# AIoT-Greenhouse-Health-Assessment
This repository contains the source code and proof-of-concept (PoC) implementation described in the book chapter: "AI-based Health Assessment of Greenhouse Crops: A Case Study for Sustainable Agriculture".

he project presents an AIoT-enabled framework designed for precision agriculture, specifically targeting greenhouse tomato crops. It leverages the Stack4Things (S4T) platform to orchestrate an Edge-Cloud continuum, combining physiological sensing, Deep Learning (LSTM & CNN), and automated visual inspection.

## Context

In the context of Smart Cities and sustainable environments, this solution aims to:
- Monitor plant health in real-time using physiological data (transpiration, canopy temperature).
- Detect growth anomalies using Long Short-Term Memory (LSTM) networks.
- Trigger event-driven visual inspections for disease classification using Convolutional Neural Networks (CNN).
- Optimize resource usage (water, phytosanitary treatments) through early stress detection.

## Repository Structure

The codebase simulates the interaction between the sensing layer (Edge) and the decision-making modules (Cloud/Gateway), as detailed in the "Algorithmic Framework and Implementation" section of the chapter.

-  sensing_client.py`: Simulates the IoT "Lightning-rod" plugin. It generates synthetic physiological and environmental data (simulating Plantarray sensors) and transmits telemetry to the processing node.
- `processing_node.py`: A Flask-based server acting as the orchestrator. It ingests telemetry, runs anomaly detection logic (threshold-based/proxy for LSTM), and triggers alerts to the administration dashboard.

## Getting Started

### Prerequisites
* Python 3.8+
* `flask`
* `requests`
* `scikit-learn` (for model integration)
* `tensorflow` / `keras` (if running the DL models)

