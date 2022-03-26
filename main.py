from client import Client
from transaction import Transaction
from block import Block
from db_connector import DBConnector
from user import User
from printer import Printer
import hashlib
import pickle as cPickle

TPCoins = []
transactions = []
logged_in_users = []
last_transaction_index = 0
last_block_hash = ""
printer = Printer()
db = DBConnector()

def initiate_block(user):
	t0 = Transaction('Genesis', user.identity, 0)
	t0.print_self()
	block0 = Block()
	block0.previous_block_hash = None
	block0.nonce = None

	block0.verified_transactions.append(t0)
	digest = hash(block0)
	block0.last_block_hash = digest

	TPCoins.append(block0)

def create_transaction(sender, receiver, amount): 
	t = Transaction(sender, receiver.identity, amount)
	t.print_self()
	t.sign_transaction()
	transactions.append(t)

def dump_blockchain (blockchain):
		print ("Number of blocks in the chain: " + str(len (blockchain)))
		for x in range (len(TPCoins)):
			block_temp = TPCoins[x]
			print ("block # " + str(x))
			for transaction in block_temp.verified_transactions:
				printer.display_transaction (transaction)
				print ('--------------')
				print ('=====================================')

def sha256(message):
	return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=1):
	assert difficulty >= 1
	prefix = '1' * difficulty

	for i in range(1000):
		digest = sha256(str(hash(message)) + str(i))
		if digest.startswith(prefix):
			print ("after " + str(i) + " iterations found nonce: "+ digest)
			return digest

def add_block():
	global last_transaction_index
	global last_block_hash
	global TPCoins
	
	block = Block()
	for i in range(3):
	   temp_transaction = transactions[last_transaction_index]
	   # validate transaction
	   # if valid
	   block.verified_transactions.append (temp_transaction)
	   last_transaction_index += 1

	block.previous_block_hash = last_block_hash
	block.Nonce = mine (block, 2)
	digest = hash (block)
	TPCoins.append (block)
	last_block_hash = digest

def logged_in(user):
	do_more = True
	while do_more:
		choice = printer.print_welcome_screen()

		if choice == '1':
			balance = db.get_balance(user.user_id)
			choice = printer.print_balance(user, balance[0])

			if choice.lower() == 'y':
				deposit_funds(user)
		if choice == '2':
			trans = printer.print_new_transaction_screen()
			receiver = db.get_user(trans['user_name'])
			receiver_client = cPickle.loads(receiver[5])
			create_transaction(user.client, receiver_client, trans['amount'])

		if choice == '3':
			do_more = False
		
	print('Would you like to logout?')
	choice = input('Choice (y/n): ')

	if choice.lower() == 'y' or choice.lower() == 'yes':
		main()
	else: 
		logged_in(user)

def deposit_funds(user):
	bank_accounts = db.get_bank_accounts(user.user_id)

	if bank_accounts:
		deposit  = printer.print_deposit_input_screen(bank_accounts)
		printer.print_deposit_load_screen()
		db.deposit_from_bank(user.user_id, deposit)
		logged_in(user)
	else:
		choice = printer.print_no_bank_accounts()

		if choice.lower() == 'y':
			bank = printer.print_new_bank_screen()
			db.insert_new_bank(user.user_id, bank)

			deposit_funds(user)
		else:
			main()

def main():
	choice = printer.print_login_choice_screen()

	if choice == '1':
		credentials = printer.print_login_credentials_screen()
		user = db.get_user(credentials['user_name'])

		if user == None:
			printer.print_login_error()
			main()
		
		if credentials['password'] == user[4]:
			client = cPickle.loads(user[5])

			user = User(user,client)
			logged_in_users.append(user)
			logged_in(user)
		else:
			printer.print_login_error()
			main()
	elif choice == '2':
		new_user = printer.print_new_user_screen()
		client = Client()

		client_pickle = cPickle.dumps(client)

		db.insert_new_user(new_user, client_pickle)
		user = User(user,client)
		logged_in_users.append(user)
		logged_in(user)
	else:
		print('Goodbye.')
		exit()

if __name__ == "__main__":
	seed_client = Client()
	initiate_block(seed_client)
	main()



