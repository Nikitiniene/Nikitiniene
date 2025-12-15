USE Loja;

IF OBJECT_ID('Produtos', 'U') IS NOT NULL
    DROP TABLE Produtos;

CREATE TABLE Produtos (
	IDProduto INT PRIMARY KEY IDENTITY,
	Nome VARCHAR(100),
	Preço DECIMAL(10,2)
);

INSERT INTO Produtos (Nome, Preço)
VALUES
('Celular',2800.00),
('Mouse',50.00),
('Teclado',120.00),
('Monitor',800.00),
('Cabo USB',20.00),
('Relógio',150.00);

SELECT AVG(Preço) AS Preço_Medio
FROM Produtos;