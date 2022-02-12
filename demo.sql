-- show all databases
show databases;

-- create a database
create database user_demo;

-- use newly made database
use user_demo;

-- create a new table
create table students(roll_no int, name varchar(100), gender char(1));
create table students(roll_no int primary key, name varchar(100), gender char(1));

-- see structure of the table
desc students;

-- add some rows to the table
insert into students values (1, "Kriti", "F");

-- update existing row
update students set name="XYZ";
update students set name="ABC" where roll_no=1;
update students set name="Shivay" where roll_no=5 and gender='M';

-- delete a row
delete from students where roll_no=3;

-- adding a primary key
alter table students add primary key(roll_no);