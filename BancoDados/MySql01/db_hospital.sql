create database if not exists db_hospital;

use db_hospital;

create table if not exists tb_especialidade(
	id int primary key auto_increment,
    descricao varchar(255) not null
)auto_increment=1;

show tables;
select * from tb_especialidade;

create table if not exists tb_medico(
	id int primary key auto_increment,
    nome varchar(255) not null,
    id_especialidade int not null,
    
constraint fk_tb_especialidade foreign key (id_especialidade) references tb_especialidade(id)
)auto_increment=1;
