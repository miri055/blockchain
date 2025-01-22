from blockchain_module import Blockchain

blockchain = Blockchain(difficulty=4)

blockchain.add_transaction("Martin pays Leah 5 BTC")
blockchain.add_transaction("Leah pays Hannah 3 BTC")
blockchain.add_block()

blockchain.add_transaction("Justin pays Bryce 2 BTC")
blockchain.add_transaction("Bryce pays Jessica 1 BTC")
blockchain.add_block()

blockchain.add_transaction("Tyler pays Courtney 2 BTC")
blockchain.add_transaction("Courtney pays Zach 1 BTC")
blockchain.add_block()

print("Blockchain state:")
blockchain.print_chain()



if blockchain.is_chain_valid():
    print("Blockchain is valid.")
else:
    print("Blockchain has been tampered!")
