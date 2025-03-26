-- comentário

-- Criar um banco de dados

-- Linguagem SQL

-- DDL , DML, DQL

-- DDL (Data Definition Language)
-- CREATE , DROP , ALTER
-- criar o banco de dados
DROP DATABASE if exists salaoestilorei; -- ddl
CREATE DATABASE if not exists salaoestilorei; -- ddl
-- usar o banco de dados
USE salaoestilorei;
-- criar a tabela
CREATE TABLE cliente(
    id int primary key auto_increment,
    nome varchar(80) NOT NULL,
    telefone char(13),
    email varchar(80) UNIQUE NOT NULL,
    senha varchar(255) NOT NULL
);
describe cliente;
-- DML

-- DROP table cliente;

INSERT INTO cliente(nome, telefone, email, senha)values('Rodrigo', '61987789878', 'rodrigo@aluno.senai.br', '123'), -- DML
('Guilherme', '61912345678', 'guilermefrana@gmail.com', '369852'),
('Safaderson', '61952639874', 'safinho@gmail.com', '123456'),
('Joarisvaldo', '61925638569', 'jojofag@gmail.com', '748'),
('Gordelas', '61969699696', 'gordinReiDelas', '669'),
('Goldengo', '61910000001', 'goldelas.r.silva@aluno.senai.br', 'CL7MXS2A'),
('Merlinpeay', '61955226633', 'melimpei@gmail.com', '952');

-- DQL
SELECT * FROM cliente;

-- Exercício : 1 ponto
-- Inserir todos os alunos presentes
--  e não presentes na tabela cliente
ALTER TABLE cliente MODIFY senha VARCHAR(64) NOT NULL;

-- mostrar a estrutura da tabela
describe cliente;
-- Exercício
-- "Marvin agora é só você..."
-- Criar a tabela Funcionario
-- Criar o servico
-- criar a tabela funcionário
CREATE TABLE funcionario(
    id int primary key auto_increment,
    nome varchar(80) NOT NULL  
);

INSERT INTO funcionario(nome)VALUES('Rodelas'),
('Gayres'),
('Martilho'),
('Bernadin'),
('Merivaldo');

-- DROP TABLE servico;
CREATE TABLE servico(
    id int primary key auto_increment,
    nome varchar(80) NOT NULL,
    valor decimal(8,2)   
);
-- Mostrar dados do serviço
SELECT * FROM servico;

INSERT INTO servico(nome, valor)VALUES('corte de cabelo', 30),
('modulagem de motor', 250),
('', ),
('unha postiça', 500);

-- Criar a tabela de agendamento
CREATE TABLE agendamento(
   id int primary key auto_increment,
   data_agenda date NOT NULL,
   hora time NOT NULL,
   fk_cliente_id int NOT NULL,  -- campo do tipo inteiro
   fk_servico_id int NOT NULL,  -- campo do tipo inteiro
   fk_funcionario_id int NOT NULL -- campo do tipo inteiro
);

-- alterar a tabela agendamento = alter table
-- adicionamos constraint com o nome FK
ALTER TABLE agendamento ADD CONSTRAINT FK_agendamento_cli
      foreign key(fk_cliente_id)
      references cliente(id)
      ON DELETE CASCADE;
      
ALTER TABLE agendamento ADD CONSTRAINT FK_agendamento_fun
      foreign key(fk_funcionario_id)
      references funcionario(id)
      ON DELETE CASCADE;
      
ALTER TABLE agendamento ADD CONSTRAINT FK_agendamento_ser
      foreign key(
      fk_servico_id)
      references servico(id)
      ON DELETE CASCADE;

SELECT * FROM cliente;
SELECT * FROM funcionario;

SELECT email FROM cliente;
-- Selecionando através de uma comparação de string.
SELECT email FROM cliente WHERE email LIKE '%@aluno.senai.br';
SELECT nome, email FROM cliente WHERE email LIKE '%@aluno.senai.br';

SELECT COUNT(*) FROM cliente;