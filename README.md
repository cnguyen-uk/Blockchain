# Blockchain
*A simple locally run blockchain.*

A [blockchain](https://en.wikipedia.org/wiki/Blockchain) is a distributed public ledger, that is, anyone can view the transaction details in a blockchain, and the transaction data is spread over many nodes (typically computers), which makes the data difficult to meaningfully attack.

Anyone can make their own blockchain, and hence their own [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency). It should be noted that blockchains can be used for purposes other than cryptocurrency, but this is by far the most popular usage.

Blockchains are the typical backdrop for cryptocurrency transactions since it solves multiple issues inherent in cryptocurrency implementation such as:

1. Legitimacy of transactions - what happens if someone attempts to alter previously made transactions?
2. Safety of owned currency - how can we ensure that only the rightful owner may spend their cryptocurrency stash?
3. Creation of currency out of thin air - how do users of a cryptocurrency know that someone isn't just creating cryptocurrency at will (and hence cause inflation)?

Problem 1 entails several other problems such as allowing users to [double spend](https://en.wikipedia.org/wiki/Double-spending) cryptocurrencies (imagine being able to spend the same £100 twice) and users making transactions for items or services, and then simply reversing the transaction to restore previously spent cryptocurrency to their wallets. In particular, the resolution of Problem 2 is powered not only by blockchain technology, but by heavy mathematics in the field of [elliptic curve cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography).

To briefly illustrate how the blockchain makes the alteration of previous transactions difficult, suppose transaction1, transaction2 and transaction3 are placed into block1 in the blockchain. Suppose also that transaction3, transaction4, and transaction5 are placed into block2 in the blockchain after block1. For this to happen block2 will contain information about the previous block, which we'll call the previous hash, thereby creating a chain with block1. If someone altered transaction2 in block1, then the previous hash would no longer match up, thereby causing the chain to be invalidated. We can check for invalidations like this and reject falsely proposed versions of the blockchain. Furthermore, we need hashing to be computationally difficult to prevent attackers from simply computing hashes and proposing legitimate versions of the blockchain as replacements (typically resolved using a system known as [Proof-of-Work](https://en.wikipedia.org/wiki/Proof_of_work)). This essentially makes the blockchain immutable.

This blockchain project is an extension of my master's dissertation on the mathematics of Bitcoin in 2018 at the University of Warwick, where I looked at cryptocurrency, blockchain, and the underlying mathematics behind cryptocurrency security - the [Elliptic Curve Digital Signature Algorithm (ECDSA)](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm). There is a wealth of information available online to be found on cryptocurrency and the different blockchains that they use, which I refrain from discussing in further detail here. Instead I will simply provide a link to my dissertation (publication pending) and summarise the overall aim of this project here:

1. Our blockchain's purpose is to store transactions, so we need a way to represent said transactions.
2. Transactions are stored in blocks in the blockchain, so we need a way to create blocks.
3. Blocks need to be chained together somehow using a previous hash, so we need to use a hashing function to hash key information in the previous block.
4. We need to initialise our blockchain using a genesis block.
5. We need to be able to implement blockchain immutability by checking that all chains are valid and by introducing Proof-of-Work (to add blocks securely).

It should be noted that this is a simple local blockchain and misses some of the features of a fully online decentralised blockchain such as allowing for other nodes in the network to check blockchain legitimacy and proofs from any Proof-of-Work computations.
