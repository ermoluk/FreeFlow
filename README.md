<h1>🌀 FreeFlow</h1>
<p><strong>Decentralized, Offline-Resilient Mesh Networking with Built-In Incentives</strong></p>

<hr>

<h2>🌍 Overview</h2>
<p>
  <strong>FreeFlow</strong> is a protocol and system for creating 
  <strong>resilient, anonymous, and censorship-resistant</strong> 
  communication networks using mobile and portable devices.<br>
  It operates <strong>without internet access</strong>, 
  <strong>without centralized servers</strong>, 
  and thrives even in environments with weak or no connectivity.
</p>
<p>
  At its core lies the economic layer 
  <strong>PoCCA (Proof-of-Contact Credit Architecture)</strong> — 
  a mechanism that rewards devices for participating in the network 
  by connecting, relaying, and storing data, 
  allowing FreeFlow to expand organically.
</p>

<hr>

<h2>🎯 Project Goals</h2>
<ul>
  <li>Enable <strong>device-to-device communication</strong> during internet shutdowns or censorship.</li>
  <li>Use <strong>Bluetooth</strong>, <strong>Wi-Fi Direct</strong>, and <strong>local radio protocols</strong> to build mesh clusters.</li>
  <li>Implement <strong>store-and-forward</strong> propagation for disconnected regions.</li>
  <li>Ensure <strong>privacy and anonymity</strong> through cryptographic identities and <strong>onion routing</strong>.</li>
  <li><strong>Reward participation</strong> using decentralized credits (not blockchain-dependent).</li>
</ul>

<hr>

<h2>🧩 Core Concepts</h2>

<h3>🔹 Mesh Clusters</h3>
<p>
  Local networks formed between nearby devices using short-range radio. 
  Devices exchange identity, presence, and routing hints.
</p>

<h3>🔹 Bridge Nodes</h3>
<p>
  Devices that link separate clusters — physically (couriers, drones) 
  or via long-range radio — enabling data transfer between isolated zones.
</p>

<h3>🔹 Partial Routing</h3>
<p>
  Nodes do not know the global topology. 
  Instead, they maintain a small list of known clusters 
  and use probabilistic or shortest-path routing based on available data.
</p>

<h3>🔹 Store-and-Forward</h3>
<p>
  If no route exists to the destination, data is <strong>encrypted and stored</strong> locally, 
  then forwarded once a valid path appears.
</p>

<hr>

<h2>💠 PoCCA — Proof-of-Contact Credit Architecture</h2>
<p>
  An incentive model that generates <strong>cryptographic proofs of network activity</strong> and rewards useful behavior.
</p>

<ul>
  <li><strong>Proof of Contact (PoC):</strong> Two devices connect and exchange signed contact logs for credit.</li>
  <li><strong>Proof of Relay (PoR):</strong> Relay nodes sign the packet path and earn credit.</li>
  <li><strong>Proof of Store (PoS):</strong> Nodes that store data offline and later deliver it also gain credit.</li>
</ul>

<p>
  Each node maintains a <strong>local ledger</strong> of its actions, 
  which synchronizes and verifies when connecting to a wider mesh.  
  Credits can be used for <strong>priority transmission</strong>, 
  <strong>service access</strong>, or <strong>peer exchange</strong>.
</p>

<hr>

<h3>📡 Addressing Format</h3>
<p><code>ClusterID:NodeID.SessionID</code></p>

<h4>Example:</h4>
<p><code>A3xh:g7h6.bbqh</code></p>

<p>
  <strong>ClusterID</strong> — short hash of the cluster’s public key.<br>
  <strong>NodeID</strong> — short hash of the node’s public key.<br>
  <strong>SessionID</strong> — one-time identifier for each session or packet.
</p>

<hr>

<h3>🔐 Security & Privacy</h3>
<ul>
  <li>All messages are signed using <code>Ed25519</code> keys.</li>
  <li>Onion routing hides the complete route and encrypts each hop.</li>
  <li>Session IDs prevent replay attacks and spoofing.</li>
  <li>Trust is built using <strong>locally signed logs</strong> and <strong>PoCCA</strong> proofs.</li>
</ul>

<hr>

<h3>📦 Packet Example</h3>
<pre><code>{
  "from": "A3xh:g7h6",
  "to": "Jk92:kf45",
  "session": "bbqh",
  "type": "onion",
  "payload": "encrypted_blob",
  "signature": "sig_by_private_key",
  "hops_left": 5
}
</code></pre>

<hr>

<h2>👥 Needed Roles</h2>
<ul>
  <li>Python developers</li>
  <li>Rust developers</li>
  <li>Kotlin / Android developers</li>
  <li>Swift / iOS developers</li>
  <li>Cryptography & Protocol Engineers</li>
  <li>Distributed Systems Researchers</li>
  <li>C / C++ developers (ESP32 & embedded runtime)</li>
</ul>

<hr>

<h2>🚀 Why FreeFlow Matters</h2>
<p>
  When the internet is <strong>blocked, shut down, or unavailable</strong>, 
  people still need to communicate.  
  FreeFlow allows individuals to stay connected, share information, and remain free.
</p>

<p><em>Communication must be decentralized, anonymous, and unstoppable.</em></p>

<p><strong>© 2025 – ermoluk</strong></p>
