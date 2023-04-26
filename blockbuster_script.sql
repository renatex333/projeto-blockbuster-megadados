DROP DATABASE IF EXISTS blockbuster;
CREATE DATABASE blockbuster;
USE blockbuster;

DROP TABLE IF EXISTS filmes;
    CREATE TABLE filmes(
        id_filme INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        categoria VARCHAR(80) NOT NULL,
        duracao SMALLINT NOT NULL,
        ano SMALLINT NOT NULL,
        PRIMARY KEY (id_filme)
    );
    
DROP TABLE IF EXISTS avaliacoes;
    CREATE TABLE avaliacoes(
        id_avaliacao INT NOT NULL AUTO_INCREMENT,
        id_filme INT NOT NULL,
        nota TINYINT NOT NULL,
        comentario VARCHAR(200),
        PRIMARY KEY (id_avaliacao),
        FOREIGN KEY (id_filme)
			REFERENCES filmes(id_filme)
    );