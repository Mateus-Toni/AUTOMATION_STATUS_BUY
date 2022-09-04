create database if not exists asb;

use asb;


create table users(
id int not null auto_increment,
user_name varchar(20),
last_name varchar(50),
birthday date, 
user_password varchar(250),
phone varchar(20),
email varchar(100), 
cpf varchar(14),
primary key(id)
)ENGINE = innodb;

create table user_code(
id_code int not null auto_increment,
user_code varchar(13),
id_user int,
surname varchar(250),
status_code text,
type_mensage varchar(100),
timing_to_mensage float,
primary key(id_code),
foreign key(id_user) references users(id)
)ENGINE = innodb;

drop table two_auth;

create table two_auth(
id_user int,
jwt text,
timming datetime,
primary key(id_user)
)ENGINE = innodb;

create table user_code_two_auth(
id_user int,
user_code varchar(6),
timming_code datetime,
primary key(id_user)
)ENGINE = innodb;

create table revoked_jwt(
id_user int,
jti varchar(36),
revoked_at datetime,
primary key(id_user)
)ENGINE = innodb;
