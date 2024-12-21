# UGM Semester Study Archive: Ethereum Blockchain

This repository is a comprehensive archive of my academic journey at Universitas Gadjah Mada (UGM), showcasing coursework, projects, and practical experiments with Ethereum blockchain technologies.

## 🌟 Features
- **Blockchain Essentials:** Learn how to set up and operate a private Ethereum blockchain with Geth.  
- **Code Examples:** Python and JavaScript scripts for blockchain interactions, from account creation to smart contract deployment.  
- **Practical Notes:** Insights into configuring private blockchains, managing transactions, and working with Solidity smart contracts.  
- **Integration with IoT:** Explore the connection between IoT devices and Ethereum smart contracts.  

---

## 📝 Contents

### 1. **Ethereum Basics**
   - Account creation and management.
   - Configuring `genesis.json` for private blockchain networks.
   - Mining and interacting with accounts via Geth.

### 2. **Script and Automation**
   - Automating Ethereum operations with Python and JavaScript.
   - Sample scripts for Ether transfers:
     - `transfer.js` (JavaScript)
     - `transfer.py` (Python)
   - Deployment scripts for Solidity contracts:
     - `deploy.py`, `store.py`, and `retrieve.py`.

### 3. **IoT Integration**
   - Integrating IoT devices with Ethereum smart contracts.
   - Examples using Solidity and Python APIs.

### 4. **Setup Notes**
   - Running a local blockchain node.
   - Securing Ethereum accounts and keystore files.
   - Working with RLP transactions and custom genesis files.

---

## 📚 Learning Goals
- Understand the foundations of blockchain and Ethereum technology.
- Create, manage, and interact with Ethereum accounts.
- Deploy and interact with smart contracts on a private blockchain.
- Integrate IoT systems with Ethereum-based solutions.

---

## 💡 Highlights from Notes
- **Private Blockchain Setup:**
  ```bash
  mkdir blockchain
  cd blockchain
  mkdir data
  geth --datadir data account new
  ```
- **Ether Transfer Script Example:**
  ```javascript
  var senderAddress = "0xb5d83AC8B1d4829FF68844DA34Fe9E7778a6D06B";
  var receiverAddress = "0x572fdAD8DB65b28500987c194e9A5f49655Fd431";

  var tx = {
      from: senderAddress,
      to: receiverAddress,
      value: web3.toWei(0.01711, "ether"),
      gas: 21000,
      gasPrice: web3.toWei('20', 'gwei')
  };
  eth.sendTransaction(tx);
  ```
- **Python Implementation for Transactions:** Simplified blockchain interaction using Web3.py.

---

## 🚀 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/UGM-Semester-Study-Archive.git
   ```
2. Follow the instructions in the `notes/` directory to replicate setups and experiments.
3. Use the scripts in the `scripts/` folder to interact with your private blockchain.

---

## 📂 File Structure
```plaintext
blockchain/
│
├── data/                     # Ethereum private blockchain data
│   ├── geth/                 # Geth client files
│   └── keystore/             # Securely stored Ethereum account keys
│
├── data1/                    # Additional experimental data
├── data2/                    # Alternative data configurations
│
├── deploy.py                 # Script for deploying smart contracts
├── genesis.json              # Genesis configuration for blockchain
├── retrieve.py               # Script for retrieving data from contracts
├── store.py                  # Script for storing data into contracts
├── transfer.js               # Ether transfer in JavaScript
├── transfer.py               # Ether transfer in Python
└── transfer2.py              # Alternative Python script for Ether transfer
```
