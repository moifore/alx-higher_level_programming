-- Creates the database hbtn_0d_usa and table cities in the hbtn_0d_usa database on MYSQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id)
	);
