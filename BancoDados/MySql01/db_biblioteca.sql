create database if not exists db_biblioteca
charset utf8mb4 collate utf8mb4_general_ci;

use db_biblioteca;

create table if not exists tb_autor(
	id int primary key auto_increment,
	nome varchar(35) not null
)auto_increment=1;

create table if not exists tb_livro(
	id int primary key auto_increment,
    titulo varchar(35) not null,
    ano_publicacao date not null,
    id_autor int not null,
    
    constraint fk_tb_autor foreign key (id_autor) references tb_autor(id)
)auto_increment=1;

create table if not exists tb_usuario(
	id int primary key auto_increment,
    nome varchar(35) not null,
    email varchar(35)
)auto_increment=1;

create table if not exists tb_emprestimo(
	id int primary key auto_increment,
    data_emprestimo date not null,
    data_devolucao date not null,
    id_livro int not null,
    id_usuario int not null,
    
    constraint fk_tb_livro foreign key (id_livro) references tb_livro(id),
	constraint fk_tb_usuario foreign key (id_usuario) references tb_usuario(id)
)auto_increment=1;

show tables;