CREATE SCHEMA sistema_gerenciamento;

USE sistema_gerenciamento;

CREATE TABLE Cliente(CPF    CHAR(11)    PRIMARY KEY, Nome   VARCHAR(100) NOT NULL, Data_Nasc    DATE    NOT NULL, Gestante  BOOLEAN NOT NULL, Deficiente BOOLEAN NOT NULL);

CREATE TABLE Funcionario(CPF    CHAR(11)    PRIMARY KEY, Funcao VARCHAR(100) NOT NULL,   Nome    VARCHAR(100) NOT NULL);

CREATE TABLE Veiculo(Placa VARCHAR(8) PRIMARY KEY, Cor VARCHAR(30), Modelo  VARCHAR(100),   CPF_Cliente CHAR(11),   CPF_Funcionario CHAR(11), foreign key(CPF_Cliente) references Cliente(CPF), foreign key(CPF_Funcionario) references Funcionario(CPF));

CREATE TABLE Vaga(Bloco CHAR(1),    Numero  INT,    Estado  BOOLEAN NOT NULL, primary key(Bloco, Numero));

CREATE TABLE Alocacoes(Id_Alocacao  INT PRIMARY KEY AUTO_INCREMENT, Data_Entrada DATE    NOT NULL, Hora_Entrada  TIME    NOT NULL, Data_Saida    DATE,   Hora_Saida  TIME,   bloco_vaga  CHAR(1) NOT NULL, numero_vaga   INT NOT NULL, placa_veiculo VARCHAR(8) NOT NULL, foreign key(bloco_vaga, numero_vaga) references Vaga(Bloco, Numero), foreign key(placa_veiculo) references Veiculo(Placa));