create database asb
default character set utf8
default collate utf8_general_ci;


create table usuarios(
id_user int not null auto_increment,
nick_name varchar(30),
nome varchar(30),
sobrenome varchar(30),
email varchar(50),
senha varchar(20),
data_de_criação_perfil date,
primary key (id_user)
)engine=innodb, default charset=utf8;