from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Coumn(db.String(50))
	username = db.Column(db.String(64), unique=True)

	def __repr__(self):
		return '<user {}>'.format(self.name)

class Account(db.Model): 
	id = db.Column(db.Integer, primary_key=True)
	account_number = Column(db.Integer)
	balance = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


	def __repr__(self):
		return '<account {}>'.format(self.name)