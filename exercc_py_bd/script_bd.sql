CREATE DATABASE algoritmos;
USE algoritmos;

CREATE TABLE disciplina(
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT
    ,nome VARCHAR(50) NOT NULL
    ,ch INT
    ,professor VARCHAR(50)
    ,chr INT
);

SELECT * FROM disciplina;