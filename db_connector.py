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
			return sqlalchemy.create_engine(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.database}', echo=True)
		except Exception as e: 
			print(e)

	def close(self):
		self.engine.dispose()	

	def reflect_table(self, table_name): 
		metadata = sqlalchemy.MetaData(bind=self.engine)

		return sqlalchemy.Table(table_name, metadata , autoload=True)

	def select_table(self, table_name):
		table = self.reflect_table(table_name)
		conn = self.engine.connect()

		s = select([table])
		results = conn.execute(s)
		conn.close()

		return results.first()

	def insert_new_user(self, new_user):
		table = self.reflect_table('users')

		stmt = insert(table).values(firstname=new_user['first_name'], lastname=new_user['last_name'],
									username = new_user['user_name'], password = new_user['password'])

		with self.engine.connect() as conn:
			result = conn.execute(stmt)
			conn.close()
			print(result)
