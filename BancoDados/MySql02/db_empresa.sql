CREATE DATABASE if not exists db_empresa
charset utf8mb4 collate utf8mb4_croatian_ci;

USE db_empresa;

CREATE TABLE if not exists tb_funcionario(
	id int primary key auto_increment,
    nome varchar(100) not null,
    cargo varchar(50) not null,
    salario float(10.2) not null,
    data_admissao date not null
)auto_increment=1;

INSERT INTO tb_funcionario (nome, cargo, salario, data_admissao) VALUES ('Guilerme Frana', 'Gastro-testador', 1500.00, '2004-05-27');
INSERT INTO tb_funcionario (nome, cargo, salario, data_admissao) VALUES ('Yanzin Rei Dela', 'Analista de Esquemas de piramide', 10000.00, '2003-08-15');
INSERT INTO tb_funcionario (nome, cargo, salario, data_admissao) VALUES ('Carlao das Trevas', 'Programador Noturno', 500.00, '2008-03-05');
INSERT INTO tb_funcionario (nome, cargo, salario, data_admissao) VALUES ('Jorgeson', 'Gerente', 6000.00, '2009-06-28');
INSERT INTO tb_funcionario (nome, cargo, salario, data_admissao) VALUES ('Jorgeson', 'Gerente', 16000.00, '2009-06-28');

SELECT * FROM tb_funcionario;

-- delete from tb_funcionario where nome = 'Guilerme Frana';

SELECT * FROM tb_funcionario where cargo = 'Gerente';
SELECT * FROM tb_funcionario where salario > 5000;
SELECT * FROM tb_funcionario ORDER BY nome ASC;

-- UPDATE aluno SET curso = 'Ciência da Computação' WHERE nome = 'João';

UPDATE tb_funcionario SET salario = 2500 WHERE nome = 'Guilerme Frana';
DELETE FROM tb_funcionario WHERE id = 6;

ALTER TABLE tb_funcionario ADD departamento varchar(50) not null;

UPDATE tb_funcionario SET departamento = 'Gestao';

UPDATE tb_funcionario SET salario = LEAST(salario, 15000);

UPDATE tb_funcionario SET nome = 'Jerisvalderson' WHERE salario = 15000;

ALTER TABLE tb_funcionario DROP data_admissao;

TRUNCATE tb_funcionario; 

DROP TABLE tb_funcionario;

DROP DATABASE db_empresa;