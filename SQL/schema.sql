create table users (
	id SERIAL Primary Key ,
	firstname VARCHAR(50), 
	lastname VARCHAR(50), 
	username VARCHAR(100), 
	password VARCHAR(20),
	privatekey VARCHAR(1024), 
	publickey VARCHAR(1024), 
	signer VARCHAR(1024), 
	identity VARCHAR(1024)
)
drop table users
select * from user

create table account(
	id SERIAL Primary Key,
	userid INT NOT NULL,
	accountnumber SERIAL NOT NULL, 
	balance INT, 
	CONSTRAINT fk_users FOREIGN KEY(user_id) REFERENCES users(id)
)
drop table account
select * from account
alter sequence public.account_accountnumber_seq RESTART WITH 10000000