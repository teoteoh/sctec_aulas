CREATE TABLE IF NOT EXISTS processed (
    id_venda VARCHAR(50) NOT NULL,
    filial VARCHAR(10) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,
    preco_unitario NUMERIC(10,2) CHECK (preco_unitario >= 0),
    quantidade INTEGER CHECK (quantidade > 0),
    imposto NUMERIC(10,2) CHECK (imposto >= 0),
    valor_total NUMERIC(12,2) CHECK (valor_total >= 0),
    data_venda DATE,
    hora_venda TIME,
    forma_pagamento VARCHAR(50) NOT NULL,
    custo_mercadoria NUMERIC(12,2) CHECK (custo_mercadoria >= 0),
    margem_percentual NUMERIC(10,2),
    receita_bruta NUMERIC(12,2) CHECK (receita_bruta >= 0),
    avaliacao NUMERIC(4,2) CHECK (avaliacao BETWEEN 0 AND 10),
    
    PRIMARY KEY (id_venda)
);