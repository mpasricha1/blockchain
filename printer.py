import stdiomask

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
		print('-------------------------')
		print('')
		print(': ')
		choice = input() 

		return choice

	def print_login_credentials_screen(self):
		credentials = {}
		print('-------------------------')
		print('Enter username: ')
		credentials['user_name'] = input()
		print('Enter password: ')
		credentials['password'] = stdiomask.getpass()

		return credentials
 
	def print_welcome_screen(self):
	 	print('-------------------------')
	 	print('Welcome to Somecoin name')
	 	print('------------------------')
	 	print('')
	 	print('What would you like to do?')
	 	print('')
	 	print('1. Add New User')
	 	print('2.')
	 	print('3.')

	 	choice = input('Please enter selection: ')
	 	return choice

	def print_new_user_screen(self):
		new_user = {}
		print('----------------------')
		print('Enter new users first name: ')
		new_user['first_name'] = input()
		print('Enter new users last name: ')
		new_user['last_name'] = input()
		print('Enter username: ')
		new_user['user_name'] = input()
		print('Enter password: ')
		new_user['password'] = stdiomask.getpass()

		return new_user