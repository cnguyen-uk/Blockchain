# -*- coding: utf-8 -*-
"""
This file demonstrates some of the capabilities of our blockchain
implementation.  In particular, we show how to:
- Add blocks to the blockchain;
- Print block information;
- Print Proof-of-Work information to validate for yourself; and
- Validate blockchain veracity in the case of an attack.
"""

from blockchain import Blockchain

# This function returns transaction data in a dictionary format.
def transaction(amount, sender, receiver):
    return {"amount": amount, "sender": sender, "receiver": receiver}

# Setting up some example transactions.
transaction1 = transaction("30", "Alice", "Bob")
transaction2 = transaction("200", "Bob", "Alice")
transaction3 = transaction("300", "Alice", "Charlie")
transaction4 = transaction("350", "David", "Erin")
transaction5 = transaction("100", "Vanna", "Pat")
transaction6 = transaction("600", "Olivia", "Bob")
transaction7 = transaction("400", "Erin", "Pat")

# The mempool consists of all transactions awaiting confirmation.
mempool = [transaction1, transaction2, transaction3, transaction4,
           transaction5, transaction6, transaction7]

# Blocks have a limited amount of space and so miners can only work on
# a limited number of them at a time.  This can cause heavy delays
# during times of peak popularity such as in 2018 with Bitcoin.
block_transactions1 = mempool[:3]
block_transactions2 = mempool[3:5]
block_transactions3 = mempool[5:7]

# We now initialise our blockchain.
blockchain = Blockchain()

# To add transactions into a block, we simply use the add_block()
# method.  We never need to create a block from scratch.
#
# We also have the option of printing the add_block() information which
# is particularly useful if we want to check the Proof-of-Work and the
# successful nonce used to generate the Proof-of-Work.
blockchain.add_block(block_transactions1)
print(blockchain.add_block(block_transactions2))
blockchain.add_block(block_transactions3)

# We can print the timestamp, transactions and hash of the entire chain
# or just a particular block in the chain (if it exists).
print(blockchain.chain)
print(blockchain.chain[2])

# A small test case to demonstrate what happens if an attacker attempts
# to change a previous transaction.  In this case, we try to remove the
# existence of transaction3.
blockchain.validate()
blockchain.chain[1].transactions = [transaction1, transaction2]
blockchain.validate()
