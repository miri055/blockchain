import hashlib
import time
import json

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):

        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self, difficulty=3):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):

        genesis_block = Block(0, ["Genesis Block"], "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):

        self.pending_transactions.append(transaction)

    def add_block(self):
        if not self.pending_transactions:
            print("No transactions to add.")
            return

        last_block = self.chain[-1]
        new_block = Block(len(self.chain), self.pending_transactions, last_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = [] 

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                print(f"Block {i} has been tampered!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Chain linkage broken at block {i}!")
                return False

        return True

    def tamper_block(self, block_index, new_transactions):

        if 0 < block_index < len(self.chain):
            self.chain[block_index].transactions = new_transactions
            self.chain[block_index].hash = self.chain[block_index].compute_hash()
        else:
            print("Invalid block index!")

    def print_chain(self):

        for block in self.chain:
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print("-" * 75)
