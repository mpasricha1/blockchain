import sqlalchemy
from sqlalchemy.sql import select, update, text, insert
import psycopg2
import configparser


config = configparser.ConfigParser()
config.read('./configs/db_config.ini')

class DBConnector:
	def __init__(self): 
		self.host = config['Database']['host']
		self.user = config['Database']['user']
		self.password = config['Database']['password']
		self.database = config['Database']['database']
		self.engine = self.connect()

	def connect(self):
		try:
			return sqlalchemy.create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.database}')
		except Exception as e: 
			print(e)

	def close(self):
		self.engine.dispose()	

	def reflect_table(self, table_name): 
		metadata = sqlalchemy.MetaData(bind=self.engine)

		return sqlalchemy.Table(table_name, metadata , autoload=True)

	def get_user(self, user_name):
		table = self.reflect_table('users')

		stmt = select([table]).where(table.c.username == user_name)

		with self.engine.connect() as conn: 
			result = conn.execute(stmt)
			conn.close() 

		return result.first()


	def insert_new_user(self, new_user, client):
		table = self.reflect_table('users')

		stmt = insert(table).values(firstname=new_user['first_name'], lastname=new_user['last_name'],
									username = new_user['user_name'], password = new_user['password'],
									clientpickle=client)

		with self.engine.connect() as conn:
			result = conn.execute(stmt)
			conn.close()
			
			new_id = result.inserted_primary_key[0]

		self.create_account(new_id)

	def create_account(self, id):
		table = self.reflect_table('account')

		stmt = insert(table).values(userid=id, balance=0)

		with self.engine.connect() as conn:
			result = conn.execute(stmt)
			conn.close()

	def get_balance(self, user_id):
		table = self.reflect_table('account')

		stmt = select([table.c.balance]).where(table.c.userid == user_id)

		with self.engine.connect() as conn:
			result = conn.execute(stmt)
			conn.close()

		return result.first()
