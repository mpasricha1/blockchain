create table users (
	id SERIAL Primary Key ,
	firstname VARCHAR(50), 
	lastname VARCHAR(50), 
	username VARCHAR(100), 
	password VARCHAR(20),
	clientpickle bytea
)
drop table users
select * from users

create table account(
	id SERIAL Primary Key,
	userid INT NOT NULL,
	accountnumber SERIAL NOT NULL, 
	balance INT
	
)
drop table account
select * from account
alter sequence public.account_accountnumber_seq RESTART WITH 10000000

ALTER TABLE account
ADD CONSTRAINT userid 
FOREIGN KEY (userid) REFERENCES users (id);

create table bank_accounts(
	id SERIAL Primary Key, 
	userid INT NOT NULL,
	bankname VARCHAR(50),
	routingnumber INT,
	accountnumber INT
)

ALTER TABLE bank_accounts
ADD CONSTRAINT userid 
FOREIGN KEY (userid) REFERENCES users (id);