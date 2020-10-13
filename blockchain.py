# -*- coding: utf-8 -*-
"""This is our Blockchain class which chains blocks via previous hashes."""

from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        """Initialise the blockchain with a unique block."""
        self.chain.append(Block([], "0"))

    def add_block(self, transactions):
        """Add new blocks to be added to the blockchain."""
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)
        self.chain.append(new_block)

        # Allows nodes to verify Proof-of-Work via proof_nonce.
        proof, proof_nonce = self.proof_of_work(new_block)
        return proof, proof_nonce, new_block

    def validate(self):
        """Check blockchain veracity."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.generate_hash():
                print("""The hash of block {i} does not equal its 
generated hash.""".replace("\n", "").format(i = i))
                return False
            if current_block.previous_hash != previous_block.generate_hash():
                print("""The hash of block {j} does not equal the previous 
hash value stored in block {i}."""
                      .replace("\n", "").format(j = i-1, i = i))
                return False
        print("This blockchain is valid.")
        return True

    def proof_of_work(self, block, difficulty = 2):
        """Implement Proof-of-Work prior to adding blocks.

        Arguments:
        block -- the block to be added to the blockchain
        difficulty -- higher difficulties need more computational work
        """
        proof = block.generate_hash()
        while proof[:difficulty] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
            proof_nonce = block.nonce
        block.nonce = 0
        return proof, proof_nonce
