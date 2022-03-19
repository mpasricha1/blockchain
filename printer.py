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
	 	print('3. Quit')

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