class Block:
	def __init__(self): 
		self.verified_transactions = []
		self.previous_block_hash = ''
		self.nonce = ''

	last_block_hash = ""