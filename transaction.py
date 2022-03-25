import datetime
import collections
import binascii 
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

class Transaction:
	def __init__(self, sender, recipient, value): 
		self.sender = sender
		self.recipient = recipient
		self.value = value 
		self.time = datetime.datetime.now()

	def print_self(self):
		print(self.sender)
		print(self.recipient)
		print(self.value)

	def to_dict(self): 
		if self.sender == 'Genesis':
			identity = 'Genesis'
		else: 
			identity = self.sender.identity

		return collections.OrderedDict({
			'sender': identity, 
			'recipient': self.recipient,
			'value': self.value, 
			'time': self.time})

	def sign_transaction(self): 
		private_key = self.sender._private_key
		signer = PKCS1_v1_5.new(private_key)
		h = SHA.new(str(self.to_dict()).encode('utf8'))

		return binascii.hexlify(signer.sign(h)).decode('ascii')


		

