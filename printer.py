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

	def print_welcome_message(self):
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