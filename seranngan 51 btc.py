import hashlib
import time

# Block structure for Bitcoin
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Simplified Blockchain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1', proof=100)
    
    # Create a new block in the chain
    def create_block(self, proof, previous_hash=None):
        block = Block(
            index=len(self.chain) + 1,
            previous_hash=previous_hash or self.hash(self.chain[-1]),
            timestamp=time.time(),
            data=self.current_transactions,
            hash=self.hash_block(proof, previous_hash or self.hash(self.chain[-1])),
        )
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    # Add a transaction to the blockchain
    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({'sender': sender, 'recipient': recipient, 'amount': amount})
        return self.last_block.index + 1  # Fix here to access index via dot notation
    
    # Get the last block in the chain
    @property
    def last_block(self):
        return self.chain[-1]
    
    # Hashing function to create hash of block
    @staticmethod
    def hash_block(proof, previous_hash):
        return hashlib.sha256(f'{proof}{previous_hash}'.encode('utf-8')).hexdigest()

    # Mining process to generate new block
    def mine_block(self, proof):
        previous_hash = self.hash(self.chain[-1])
        return self.create_block(proof, previous_hash)
    
    # Proof-of-Work algorithm
    def proof_of_work(self, previous_hash):
        proof = 0
        while not self.valid_proof(proof, previous_hash):
            proof += 1
        return proof
    
    def valid_proof(self, proof, previous_hash):
        guess = f'{proof}{previous_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    @staticmethod
    def hash(block):
        block_string = f'{block.index}{block.previous_hash}{block.timestamp}{block.data}{block.hash}'.encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

# Simplified 51% Attack Simulation
class Blockchain51Attack:
    def __init__(self):
        self.blockchain = Blockchain()
        self.attack_chain = Blockchain()

    def add_fake_blocks(self):
        # Simulate attacker chain being longer (51% attack)
        for _ in range(5):  # Adding extra blocks to attacker's chain
            proof = self.blockchain.proof_of_work(self.blockchain.last_block.hash)
            self.attack_chain.mine_block(proof)

    def run_attack(self):
        # Attack the blockchain by creating a longer chain (51% attack)
        self.add_fake_blocks()
        print("Attack chain length:", len(self.attack_chain.chain))
        print("Blockchain length:", len(self.blockchain.chain))
        
        # Compare chains to simulate attack
        if len(self.attack_chain.chain) > len(self.blockchain.chain):
            print("51% Attack success: Attacker's chain is longer")
            # Replace the blockchain with the attacker’s chain
            self.blockchain = self.attack_chain
            print("Blockchain is now replaced with the attacker's chain.")

# Main simulation
if __name__ == "__main__":
    attacker = Blockchain51Attack()
    
    # Add some transactions
    attacker.blockchain.add_transaction("Alice", "Bob", 50)
    attacker.blockchain.add_transaction("Bob", "Charlie", 30)
    
    # Miner mines block on main chain
    proof = attacker.blockchain.proof_of_work(attacker.blockchain.last_block.hash)
    attacker.blockchain.mine_block(proof)
    
    # Now run the 51% attack
    attacker.run_attack()
    
    # Check final state of the blockchain
    print("\nFinal Blockchain Length:", len(attacker.blockchain.chain))
    print("Final Attack Chain Length:", len(attacker.attack_chain.chain))

# Hasil dari program ini menunjukkan simulasi serangan 51% pada blockchain, di mana penyerang 
# membuat rantai blok yang lebih panjang daripada blockchain utama. 
# Penyerang berhasil menambahkan 5 blok ke rantai mereka, menjadikannya lebih panjang dari blockchain utama 
# yang hanya memiliki 2 blok. Karena rantai penyerang lebih panjang, blockchain utama digantikan dengan rantai penyerang. 
# Ini menggambarkan bagaimana serangan 51% dapat menggantikan blockchain yang sah dengan rantai 
# yang lebih panjang, meskipun dalam kenyataannya, untuk melakukan ini di Bitcoin memerlukan kontrol lebih dari 50% 
# dari total hashrate jaringan.