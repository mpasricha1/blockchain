from transaction import Transaction
from client import Client
from db_connector import DBConnector
import pickle as cPickle
from user import User

db = DBConnector()


def display_transaction(transaction):
   #for transaction in transactions:
   dict = transaction.to_dict()
   print ("sender: " + dict['sender'])
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')

transactions = []

Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()



# t1.print_self()

print('Dinesh before db insert')
print('------------------------')
print(Dinesh._private_key)
print(Dinesh._public_key)
print(Dinesh._signer)
print(Dinesh.identity)
print('')
print('')

new_user = {
   'first_name': 'test', 
   'last_name': 'test', 
   'user_name': 'test', 
   'password': 'test'
}

client_pickle = cPickle.dumps(Dinesh)

db.insert_new_user(new_user, client_pickle)

Dinesh2 = db.get_user('test')
print(Dinesh)

Dinesh2 = cPickle.loads(Dinesh2[5])

user = db.get_user('markp')

client = cPickle.loads(user[5])

print('Dinesh after db insert')
print('------------------------')
print(Dinesh2._private_key)
print(Dinesh2._public_key)
print(Dinesh2._signer)
print(Dinesh2.identity)
print('')
print('')
print(Dinesh.identity)
print(Dinesh.identity)

print(Dinesh==Dinesh2)

t1 = Transaction(
   Dinesh,
   client.identity,
   15.0
)

t1.sign_transaction()

# user = db.get_user('markp')

# client = cPickle.loads(user[5])
# print(client._private_key)
# print(client._public_key)
# print(client._signer)
# print(client.identity)
# user = User(user,client)



# t1 = Transaction(
#    Dinesh,
#    client.identity,
#    15.0
# )

# t1.sign_transaction()