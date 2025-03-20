create database if not exists db_clinica_medica
charset utf8mb4 collate utf8mb4_general_ci;

use db_clinica_medica;

create table if not exists tb_especialidade(
	id_especialidade int primary key auto_increment,
    descricao varchar(255) not null
) auto_increment=1;

create table if not exists tb_medico(
	id int primary key auto_increment,
    nome varchar(255) not null,
    id_especialidade_medico int not null,
    -- Criando a chave estrangeira para a tabela tb_especialidade
    constraint fk_tb_especialidade foreign key (id_especialidade_medico) references tb_especialidade(id_especialidade)
    
) auto_increment=1;

# DROP TABLE tb_medico;

create table if not exists tb_paciente(
	id int primary key auto_increment,
    nome varchar(255) not null
)auto_increment=1;

create table if not exists tb_consulta(
	id int primary key auto_increment,
    data_consulta date not null,
    id_medico int not null,
    id_paciente int not null,
    
    constraint fk_tb_medico foreign key (id_medico) references tb_medico(id),
    constraint fk_tb_paciente foreign key (id_paciente) references tb_paciente(id)
)auto_increment=1;

show tables;