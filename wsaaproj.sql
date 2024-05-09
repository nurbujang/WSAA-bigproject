CREATE DATABASE wsaaproj;
SHOW DATABASES;

use wsaaproj;
create table login (username varchar(250) NOT NULL, 
password varchar(250) NOT NULL, 
priviledge text);
insert INTO login (username, password, priviledge) values ("admin", "password", "admin");
select * from login;

create table airport (country varchar(250) NOT NULL, 
year (int), 
main varchar(250),
other varchar(250),
small varchar(250)


