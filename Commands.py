CREATE TABLE Employee(
	emp_id varchar(3) NOT NULL,
	f_name varchar(20),
	l_name varchar(20),
	ssn char(9),
	dob date,
	addr varchar(35),
	PRIMARY KEY (emp_id));

CREATE TABLE Top(
	t_no INT NOT NULL,
	size INT,
	emp_id varchar(3),
	type varchar(10),
	PRIMARY KEY (t_no)
	FOREIGN KEY (emp_id) REFERENCES Employee);

CREATE TABLE Ticket(
	tkt_no INT NOT NULL,
	status varchar(15),
	day date,
	t_no INT,
	emp_id varchar(3),
	PRIMARY KEY(tkt_no),
	FOREIGN KEY (t_no) REFERENCES Top ON DELETE CASCADE
									  ON UPDATE CASCADE,
	FOREIGN KEY (emp_id) REFERENCES Employee ON DELETE CASCADE
											 ON UPDATE CASCADE);
CREATE TABLE Payment(
	p_no INT NOT NULL,
	tkt_no INT
	amount NUMERIC(5,2),
	type varchar(10),
	cc_no varchar(16),
	exp date,
	ccv char(3),
	PRIMARY KEY (p_no,tkt_no),
	FOREIGN KEY (tkt_no) REFERENCES Ticket
					on UPDATE CASCADE
					on DELETE CASCADE);

CREATE TABLE Dish(
	name varchar(30) NOT NULL,
	type varchar(15),
	price NUMERIC(5,2),
	cost NUMERIC(5,2),
	amount INT,
	PRIMARY KEY(name));


CREATE TABLE Sold(
	tkt_no INT,
	name varchar(30),
	PRIMARY KEY (tkt_no, name),
	FOREIGN KEY (tkt_no) REFERENCES Ticket ON DELETE CASCADE
									  ON UPDATE CASCADE,
	FOREIGN KEY (name) REFERENCES Dish ON DELETE CASCADE
											 ON UPDATE CASCADE);

CREATE TABLE Hours(
	emp_id varchar(3),
	c_in datetime,
	c_out datetime,
	PRIMARY KEY (emp_id, c_in),
	FOREIGN KEY (emp_id) REFERENCES Employee
						ON UPDATE CASCADE
						ON DELETE CASCADE);


CREATE TABLE Manager(
	emp_id varchar(3),
	mgr_id varchar(3) NOT NULL,
	type varchar(15),
	PRIMARY KEY (emp_id, mgr_id),
	FOREIGN KEY (emp_id) REFERENCES Employee
						on UPDATE CASCADE
						on DELETE CASCADE,
    CHECK (mgr_id LIKE 'M%'));

CREATE TABLE Server(
	emp_id varchar(3),
	serv_id varchar(3) NOT NULL,
	level varchar(15),
	PRIMARY KEY (emp_id, serv_id),
	FOREIGN KEY (emp_id) REFERENCES Employee
						on UPDATE CASCADE
						on DELETE CASCADE
    CHECK (serv_id LIKE 'S%'));

CREATE TABLE Cook(
	emp_id varchar(3),
	cook_id varchar(3) NOT NULL,
	type varchar(15),
	PRIMARY KEY (emp_id, cook_id),
	FOREIGN KEY (emp_id) REFERENCES Employee
						on UPDATE CASCADE
						on DELETE CASCADE
    CHECK (cook_id LIKE 'C%'));



CREATE TABLE Cashout(
	cash_id INT NOT NULL,
	serv_id varchar(3),
	tipout NUMERIC(2,3),
	sales NUMERIC(5,2),
	PRIMARY KEY (cash_id, serv_id),
	FOREIGN KEY (serv_id) REFERENCES Server
						on UPDATE CASCADE
						on DELETE CASCADE);

CREATE TABLE Supplier(
	supp_id varchar(3) NOT NULL,
	name varchar(15),
	addr varchar(35),
	phone char(10),
	PRIMARY KEY (supp_id));

CREATE TABLE Makes(
	name varchar(30),
	cook_id varchar(3),
	day datetime,
	status varchar(30),
	PRIMARY KEY(name,cook_id),
	FOREIGN KEY (name) REFERENCES Dish ON DELETE CASCADE
									  ON UPDATE CASCADE,
	FOREIGN KEY (cook_id) REFERENCES Cook ON DELETE CASCADE
											 ON UPDATE CASCADE);

CREATE TABLE Requisition(
	req_id int NOT NULL,
	supp_id varchar(3),
	mgr_id varchar(3),
	d_placed date,
	d_filled date,
	PRIMARY KEY(req_id,mgr_id),
	FOREIGN KEY (mgr_id) REFERENCES Manager ON DELETE CASCADE
									  ON UPDATE CASCADE,
	FOREIGN KEY (supp_id) REFERENCES Supplier ON DELETE CASCADE
											 ON UPDATE CASCADE);


CREATE TABLE Restock(
	req_id int,
	name varchar(30),
	amount int,
	PRIMARY KEY(req_id, name),
	FOREIGN KEY (req_id) REFERENCES Requisition ON DELETE CASCADE
									  ON UPDATE CASCADE,
	FOREIGN KEY (name) REFERENCES Dish ON DELETE CASCADE
											 ON UPDATE CASCADE);


INSERT INTO Dish
	VALUES('Tea','Drink',3.25,0.01,1000);

INSERT INTO Dish
	VALUES('Soda','Drink',3.25,0.01,1000);

INSERT INTO Dish
	VALUES('Water','Drink',0.00,0.00,1000);

INSERT INTO Employee
	VALUES('12A','John','Smith','222336666','11/12/1990','Clear Lake');

INSERT INTO Employee
	VALUES('23A','Daisy','Jones','111336666','1/22/1995','Webster');

INSERT INTO Top
	VALUES(2,4,'-999','Booth');

INSERT INTO Top
	VALUES(3,4,'-999','Booth');

INSERT INTO Top
	VALUES(4,4,'-999','Booth');

INSERT INTO Top
	VALUES(11,6,'-999','Table');

INSERT INTO Top
	VALUES(12,6,'-999','Table');

INSERT INTO Top
	VALUES(41,6,'-999','Table');

INSERT INTO Top
	VALUES(42,6,'-999','Table');

INSERT INTO Top
	VALUES(43,6,'-999','Table');

INSERT INTO Top
	VALUES(61,4,'-999','Booth');

INSERT INTO Top
	VALUES(62,4,'-999','Booth');

INSERT INTO Top
	VALUES(63,4,'-999','Booth');

INSERT INTO Top
	VALUES(51,4,'-999','Table');

INSERT INTO Top
	VALUES(52,4,'-999','Table');

INSERT INTO Top
	VALUES(53,4,'-999','Table');

INSERT INTO Top
	VALUES(21,2,'-999','Booth');

INSERT INTO Top
	VALUES(22,2,'-999','Booth');

INSERT INTO Top
	VALUES(23,2,'-999','Booth');

INSERT INTO Top
	VALUES(31,2,'-999','Booth');

INSERT INTO Top
	VALUES(32,2,'-999','Booth');

INSERT INTO Top
	VALUES(33,2,'-999','Booth');
