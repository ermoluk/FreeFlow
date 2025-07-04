# FreeFlow Simulation

FreeFlow is a decentralized, offline-resilient mesh networking protocol designed for environments with poor or no internet connectivity. This repository contains a simulation of FreeFlow’s core architecture, demonstrating clustering, Bridge Nodes, Proof-of-Contact (PoC) token accumulation, and resilience to node and cluster failures.

# Overview

This simulation validates the following key components of FreeFlow:
	•	Dynamic clustering: nodes form local clusters based on proximity and connectivity.
	•	Bridge Nodes: special nodes that connect separate clusters for global synchronization.
	•	Proof-of-Contact (PoC): nodes earn credits for relaying, storing, and forwarding data.
	•	Failure simulation: random node and cluster failures to test resilience.
	•	Network metrics: tracks average latency, percentage of offline nodes, and PoC efficiency.

# How to Run
	1.	Clone the repository:
git clone https://github.com/<your-username>/FreeFlow.git && cd FreeFlow
	2.	Install dependencies:
pip install -r requirements.txt
	3.	Run the simulation:
python3 simulations/test_simulation.py
	4.	View logs:
Simulation logs are saved in log.txt.

# Simulation Report

# Goals
	•	Model FreeFlow’s clustering and Bridge Node architecture.
	•	Test PoC credit system under dynamic network conditions.
	•	Analyze resilience under node and cluster failures.

# Configuration
	•	Nodes: 100
	•	Area Size: 200x200 units
	•	Connection Radius: 30 units
	•	Transaction Probability: 10%
	•	Packet Loss Probability: 10%
	•	Failure Simulation:
	•	Random Bridge Node failures every 50 frames
	•	Random cluster failures every 100 frames

# Metrics

Average Latency ~21 ms

% Offline Nodes ~55%

PoC Efficiency ~6.3 credits/node

Successful Transactions ~82%


# Features
	•	Real-time visualization with dynamic clustering
	•	Packet loss and degraded links simulation
	•	Journal synchronization across clusters
	•	Logs of all events: transactions, failures, and cluster changes
	•	Mini-map view of global mesh state


# Example Log Output

=== FreeFlow Simulation Detailed Log ===

CLUSTER FAILURE: Cluster 69 failed
TX: ff://1/4/fcbf → ff://1/24/40b4
TX: ff://1/9/22f9 → ff://1/32/46cc
TX: ff://1/29/f0b6 → ff://1/74/fdac
TX: ff://1/54/0659 → ff://1/49/13d3
TX: ff://1/56/ddf9 → ff://1/99/adff
TX: ff://1/67/f8ca → ff://1/8/b5fa
CLUSTER FAILURE: Cluster 1 failed
BRIDGE FAILURE: Node 97 failed

# License
This project is licensed under the MIT License.

# Learn More
	•	FreeFlow Whitepaper: https://github.com/ermoluk/FreeFlow/wiki
	•	Project website: https://freeflw.net/