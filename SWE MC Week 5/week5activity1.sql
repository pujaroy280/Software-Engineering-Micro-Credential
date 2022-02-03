CREATE TABLE students(
	id SERIAL,
	name VARCHAR(30),
	email VARCHAR(128) UNIQUE,
	PRIMARY KEY (id)
);

INSERT INTO students(id,name,email)
      VALUES
	  (2, 'Alice', 'alice@wonderland.com'),
	  (3, 'Clark Kent', 'clark@metropolis.com')
;

CREATE TABLE ACTORS(
	actor_id SERIAL,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	Gender CHAR(1),
	date_of_birth DATE,
	PRIMARY KEY(actor_id)
);

INSERT INTO actors(actor_id,first_name,last_name,gender,date_of_birth)
VALUES
(1,'Puja','Roy','F','2022-01-31'),
(2,'Vishnu','Priya','F','2022-05-28'),
(3,'Shiv','Parvati','M','2022-02-3');

CREATE TABLE directors(
	director_id SERIAL,
	first_name VARCHAR(30),
	last_name VARCHAR(30),
	date_of_birth DATE,
	nationality VARCHAR(20),
	PRIMARY KEY (director_id)
);

INSERT INTO directors(director_id,first_name,last_name,date_of_birth,nationality)
VALUES
(1,'Puja','Roy','2022-01-31','American Asian'),
(2,'Saraswati','Brahma','2022-05-03','Asian'),
(3,'Peter','Pan','2022-02-10','American');
