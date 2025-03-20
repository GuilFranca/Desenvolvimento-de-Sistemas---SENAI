create database if not exists db_vendas_online
charset utf8mb4 collate utf8mb4_croatian_ci;

use db_vendas_online;

-- drop database db_vendas_online;

create table if not exists tb_produto(
	id int primary key auto_increment,
    nome varchar(35) not null,
    preco float not null
)auto_increment=1;

create table if not exists tb_cliente(
	id int primary key auto_increment,
    nome varchar(35),
    email varchar(35)
)auto_increment=1;

create table if not exists tb_pedido(
	id int primary key auto_increment,
    data_pedido date not null,
    id_cliente int not null,
    
    constraint fk_tb_cliente foreign key (id_cliente) references tb_cliente(id)
)auto_increment=1;

create table if not exists tb_pedido_produto(
	id_pedido int not null,
    id_produto int not null,
    
    constraint fk_tb_pedido foreign key (id_pedido) references tb_pedido(id),
    constraint fk_tb_produto foreign key (id_produto) references tb_produto(id)
);

drop table tb_cliente;