import stdiomask
from tqdm import tqdm
import time

class Printer:

	def display_transaction(self,transaction):
	   dict = transaction.to_dict()
	   print ("sender: " + dict['sender'])
	   print ('-----')
	   print ("recipient: " + dict['recipient'])
	   print ('-----')
	   print ("value: " + str(dict['value']))
	   print ('-----')
	   print ("time: " + str(dict['time']))
	   print ('-----')

	def print_login_choice_screen(self):
		print('-------------------------')
		print('1. Login')
		print('2. Create new account')
		print('3. Quit')
		print('-------------------------')
		print('')
		choice = input('Choice: ')

		return choice

	def print_login_credentials_screen(self):
		credentials = {}
		print('-------------------------')
		credentials['user_name'] = input('Enter username: ')
		credentials['password'] = stdiomask.getpass('Enter password: ')

		return credentials
 
	def print_welcome_screen(self):
	 	print('-------------------------')
	 	print('Welcome to Somecoin name')
	 	print('------------------------')
	 	print('')
	 	print('What would you like to do?')
	 	print('')
	 	print('1. View Balance')
	 	print('2.')
	 	print('3. Logout')

	 	choice = input('Please enter selection: ')
	 	return choice

	def print_new_user_screen(self):
		new_user = {}
		print('----------------------')
		new_user['first_name'] = input('Enter new users first name: ')
		new_user['last_name'] = input('Enter new users last name: ')
		new_user['user_name'] = input('Enter username: ')
		new_user['password'] = stdiomask.getpass('Enter password: ')

		return new_user

	def print_login_error(self):
		print('')
		print('')
		print('Username or password incorrect')
		print('')

	def print_progress_bar(self, sleep, message):
		for i in tqdm(range(100), desc=message):
			time.sleep(sleep)

	def print_blanks(self,num):
		for x in range(num): 
			print('')

	def print_balance(self, user, balance):
		self.print_progress_bar(0.01, 'Getting bank accounts..')
		self.print_blanks(10)

		print('--------------------------------------------')
		self.print_blanks(2)
		print(f'Hello {user.first_name} {user.last_name}')
		print(f'Your current cash balance is ${balance}')

		if balance == 0:
			print('')
			print('Please deposit some funds to make some transactions')

		choice = input('Would you like to deposit funds now? (y/n):')
		self.print_blanks(10)

		return choice

	def print_no_bank_accounts(self):
		print('You have not linked any bank accounts')
		
		choice = input('Would you like to link one now? (y/n): ')

		return choice

	def print_new_bank_screen(self): 
		new_bank = {}

		new_bank['bank_name'] = input('Enter bank name: ')
		new_bank['routing_number'] = input('Enter routing number: ')
		new_bank['account_number'] = input('Enter account number: ')

		self.print_progress_bar(0.01, 'Connecting to your bank...')
		self.print_progress_bar(0.01, 'Verifying account...')

		return new_bank

	def print_deposit_input_screen(self, bank_accounts):
		deposit = {}
		print('----------------------')
		print('Bank list')
		print('----------------------')
		print(bank_accounts[2])
		self.print_blanks(2)

		deposit['bank'] = input('Choose your bank account: ')
		deposit['amount'] = input('Enter Amount: $')

		return deposit

	def print_deposit_load_screen(self):
		self.print_progress_bar(0.01, 'Connecting to your bank...')
		self.print_progress_bar(0.01, 'Verifying transaction...')
		self.print_progress_bar(0.01, 'Transfering funds...')





	