-- codigo que foi usado para criar o DB e as tables no mySQL


create database gestao_clientes;
use gestao_clientes;

create table clientes(
	id int primary key auto_increment,
    nome varchar(200) not null,
    idade int(3),
    cpf varchar(11) unique not null,
	email varchar(100) unique,
    endereco varchar(100),
    localidade varchar(100),
    data_nascimento date,
    status_ boolean
);

create table telefones(
	id int primary key auto_increment,
    id_clientes int not null,
    numero varchar(20),
    tipo varchar(100),
    
    foreign key (id_clientes) references clientes(id)
);
 
