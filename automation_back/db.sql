create database if not exists asb;

use asb;

drop table users;

create table users(
id int not null auto_increment,
user_name varchar(20),
last_name varchar(50),
birthday date, 
user_password varchar(250),
phone varchar(20),
email varchar(100), 
primary key(id)
)ENGINE = innodb;

create table user_code(
id_code int not null auto_increment,
user_code varchar(13),
id_user int,
primary key(id_code),
foreign key(id_user) references users(id)
)ENGINE = innodb;