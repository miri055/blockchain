# Simple Blockchain Simulation

## Overview 💮

This project simulates a basic blockchain system in Python. It demonstrates core blockchain principles, including block structure, hash generation, and the chain validation process. The project helps to understand how blockchain technology works at a fundamental level, showcasing how blocks are linked together and how tampering with the data can be detected.

The project includes:
- A basic proof-of-work mechanism.
- A method to validate the integrity of the blockchain.
- Simulates the creation of blocks with transactions.
- Demonstrates how tampering with a block in the chain would invalidate the entire blockchain.

## Features

### Block Structure:
Each block contains:
- **Block index**: Position of the block in the chain.
- **Timestamp**: Time at which the block is created.
- **A list of transactions**: Transactions recorded in the block.
- **Previous block's hash**: Hash of the previous block, linking them together.
- **Current block's hash**: Hash of the current block, generated using SHA-256.

### Blockchain Class:
Manages the blockchain by:
- **Adding new blocks**: Adding new blocks with transactions.
- **Validating the chain's integrity**: Ensuring that all blocks are linked properly and haven’t been tampered with.

## How the Blockchain Works in This Project

### 1. **Genesis Block**
The first block in the blockchain is created without any predecessor. This is known as the *genesis block*.
### 2. **Adding Transactions**
Transactions are added to blocks. Each block can contain multiple transactions, which are stored as a list.
### 3. **Mining a Block**
After a set of transactions is added, a new block is mined. This involves calculating the block's hash using the previous block’s hash and the current block's data.
### 4. **Validation**
The chain's integrity is verified by checking:
- If the current block’s hash matches its data.
- If the previous block's hash is correctly linked to the current block.
### 5. **Tampering**
If the data in any block is modified (for example, changing a transaction), the block’s hash changes, and the blockchain becomes invalid. This shows how tampering with data is detectable in a blockchain system.
