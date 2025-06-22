<h1>FreeFlow</h1>
Decentralized, Offline-Resilient Mesh Networking with Built-In Incentives

<h3>Overview:</h3>

FreeFlow is a protocol and system for creating resilient, anonymous, and censorship-resistant communication networks using mobile and portable devices.
It works without internet access, without centralized servers, and thrives in environments with poor or no connectivity.

The system is powered by a unique economic layer called PoCCA – Proof-of-Contact Credit Architecture. This mechanism rewards devices for participating in the network by connecting, relaying, and storing data, enabling FreeFlow to expand naturally.

<h3>Project Goals:</h3>

Enable device-to-device communication during internet shutdowns or censorship
Create mesh networks from smartphones, wearables, and other devices using Bluetooth, Wi-Fi Direct, or local radio protocols
Allow data to propagate across disconnected areas via store-and-forward
Provide strong privacy using cryptographic identities and onion routing
Reward participation using decentralized credits

<h3>Core Concepts:</h3>

Mesh Clusters: Local networks formed between nearby devices using short-range radio. Devices share identity, presence, and routing hints.
Bridge Nodes: Devices that link separate clusters. These can be physical couriers or long-range transmitters that carry data between zones.
Partial Routing: Nodes do not know the global topology. Instead, they maintain a small list of known clusters and use probabilistic or shortest-path routing based on available info.

Store-and-Forward: If no route exists to a destination, data is securely stored and forwarded once the path becomes available.
PoCCA – Proof-of-Contact Credit Architecture: An incentive model that generates cryptographic proofs of activity, including contact, relay, and storage. These proofs form the basis for credit and reputation systems within the mesh.
Addressing:

Each node address follows the format:

<ClusterID>:<NodeID>.<SessionID>

<h2>Example:</h2>

A3xh:g7h6.bbqh

ClusterID is a short hash of the cluster’s public key
NodeID is a short hash of the node’s public key
SessionID is a one-time identifier for each contact or packet
Security and Privacy:

All messages are signed using Ed25519 keys
Onion routing hides the full route and encrypts each hop
Session IDs prevent replay attacks and spoofing
Trust is established using cryptographically signed local logs
PoCCA (Proof-of-Contact Credit Architecture):

FreeFlow uses PoCCA to reward nodes for useful behavior.

Proof of Contact (PoC): Two devices that connect exchange signed contact logs for credit
Proof of Relay (PoR): Each relay node signs the packet path and earns credit
Proof of Store (PoS): If a node stores a packet offline and later delivers it, it also earns credit
Local Ledger: All activity is logged locally. When the device connects to a wider mesh, these logs are synchronized and verified.
Credits: Rewards can be used for priority transmission, service access, or peer exchange. They are not dependent on any specific blockchain.
Packet Example:

{
"from": "A3xh:g7h6",
"to": "Jk92:kf45",
"session": "bbqh",
"type": "onion",
"payload": "encrypted_blob",
"signature": "sig_by_private_key",
"hops_left": 5
}

<h3>Project Status:</h3>

Protocol and architecture are complete
Addressing system implemented
Routing algorithms (Dijkstra and TTL-flooding) tested in simulation
Python simulator in development
Android relay app in early testing
PoCCA token accounting in design phase
Roadmap:

Build functional network simulation in Python
Implement onion-layered routing
Develop Android app with BLE-based peer exchange
Create modular identity and validation layer
Design decentralized credit management system
Publish developer documentation and whitepaper
Contributors Wanted:

We are looking for collaborators who believe in building open, censorship-resistant infrastructure.

<h3>Needed roles include:</h3>

Python developers
Rust developers
Kotlin / Android developers
Swift / iOS developers
Cryptography and protocol engineers
Distributed systems researchers
C and C++ developers (for embedded mesh runtime, ESP32, and low-level device control)
Why FreeFlow Matters:

When the internet is censored, shut down, or simply unavailable — people still need to communicate. FreeFlow gives individuals the ability to stay connected, share information, and remain free.

Communication must be decentralized, anonymous, and unstoppable.

2025 ermoluk


