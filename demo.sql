-- show all the databases
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



-- create a table countries
create table countries (c_id int primary key, country varchar(50), capital varchar(50));

-- insert some values
insert into countries values (1, "India", "New Delhi");
insert into countries values (2, "USA", "Washington DC");
insert into countries values (3, "Canada", "Ottawa");
insert into countries values (4, "Thailand", "Bangkok");
insert into countries values (5, "South Korea", "Seoul");

-- order by
select * from countries order by country; -- ascending order
select * from countries order by country desc; -- descending order

-- aggregate functions
select count(c_id) from countries;
select count(c_id) from countries where c_id > 3;
select sum(c_id) from countries;

-- like
select * from countries where country like '___';
select * from countries where country like '%a';
select * from countries where country like '_n%';