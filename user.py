class User:
	def __init__(self,user, client):
		self.user_id = user[0]
		self.first_name = user[1]
		self.last_name = user[2]
		self.user_name = user[3]
		self.client = client 