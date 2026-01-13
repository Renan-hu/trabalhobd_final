# trabalhobd_final

CODIGO DO MYSQL

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
 
Renan: Usei ia para concertar um problema de conexão entre o python e o mysql, pois o connector não estava funcionando. Assim, usei o pymysql para fazer essa conexão.
       Tambem usei para me dar uma luz de como fazer para cadastras o id do cliente e as demais informações na table telefones.
