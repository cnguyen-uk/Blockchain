# -*- coding: utf-8 -*-
"""
This is our Block class for transaction storage.

Note that although every block has a timestamp, a proper
implementation should have a timestamp which is static from when a
block is finally placed into the blockchain. In our implementation
this timestamp changes every time the code is run.

Our hashing function is SHA-256 as it is used in most cryptocurrencies.
Information about SHA-256 can be found here:
https://en.wikipedia.org/wiki/SHA-2
"""

from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Initial guess for future Proof-of-Work.
        self.hash = self.generate_hash()
    
    def __repr__(self):
            return ("Timestamp: " + str(self.timestamp) + "\n"
                    + "Transactions: " + str(self.transactions) + "\n"
                    + "Current hash: " + str(self.generate_hash()))

    def generate_hash(self):
        """Return a hash based on key block information."""
        block_contents = (str(self.timestamp) + str(self.transactions)
                          + str(self.previous_hash) + str(self.nonce))
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()
