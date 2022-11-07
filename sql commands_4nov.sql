show databases;
create database
use poornimadb;
show tables;
create table Student(sid int,fname varchar(20),address varchar(50));
select * from Student;
insert Student values(1,'Agon','UK');
insert Student values(3,'Muyiwa','UK');

insert Student values(22,'Bagga','UK');
-- create table rooms(id int auto_increment,street varchar(255),owner_id int not null, primary key(id),fori

select * from Student order by fname;

-- disable safe update
/* hello*/
set sql_safe_updates=0;
update Student set fname='muyiwa'
 where sid=1
-- delete a row 
delete from Student where sid=1oky

drop table student1

select * from student1

create table Student1(sid int primary key,fname varchar(20) not null,address varchar(50) unique,
gender enum ('Male','Female'));


create table Student1(sid int primary key,fname varchar(20) not null,address varchar(50) unique,
gender varchar(20),constraint gender check ('Male'or'Female'));

drop table student1
create table marks(sid int,course varchar(20),marks int,
         foreign key(sid) references Student1(sid))
         
         insert student1 values(1,'Agon','UK','Male')
         
         insert marks values(1,'Scala',89)
         insert marks values(1,'Python',94)
           insert marks values(2,'Python',94)
           
           alter table student add mobile int
            alter table student drop column mobile 
           
           select * from student1
           describe student
           
           desc student
           
           
           
            alter table student modify fname varchar(30)
            
            create table Student1(sid int primary key,fname varchar(20) not null,address varchar(50) unique,
gender varchar(20),constraint gender check ('Male'or'Female'));


show databases;
use classicmodels
show tables
select * from customers
select Customernumber,customername from customers where customernumber >200 and customernumber <210

select Customernumber,customername from customers where customernumber between 200 and 210

select Customernumber,customername from customers where customernumber in (110,201,216)

-- wild card characters: _ one charcter ,% multiple character

select Customernumber,customername,contactfirstname from customers where contactfirstname like 'C%'

select Customernumber,customername,contactfirstname from customers where contactfirstname like 'c_r%'

-- how many customers from 

select city,count(*) from customers where customernumber>200 
group by city

select city,count(*) from customers -- where customernumber>200 
group by city

select city,count(city) from customers where customernumber>200 
group by city having city in ('NYC','Frankfurt')


-- how many customers are from specific city
select city,count(city) as cc from customers 
where customernumber>200 
group by city -- having city in ('NYC','Frankfurt')
order by city   -- order by sorting

-- Predefined function

select upper(city) from customers 

select lower(city) from customers 

select trim(city) from customers -- remove spaces from start and end

select length(city) from customers 

-- date functions
select now()
select adddate('2022-11-04 16:59:16',INTERVAL 1 MONTH)

select adddate('2022-11-04 16:59:16',INTERVAL 1 HOUR)







           
           
           






