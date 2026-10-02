-- filial com mais faturamento:

SELECT
    filial,
    SUM(valor_total) AS faturamento_total
FROM public.processed
GROUP BY filial
ORDER BY faturamento_total DESC
LIMIT 1;

-- filial com maior quantidade de vendas:

SELECT
    filial,
    COUNT(DISTINCT id_venda) AS quantidade_vendas
FROM public.processed
GROUP BY filial
ORDER BY quantidade_vendas DESC
LIMIT 1;

-- linha de produto com maior faturamento:
SELECT
    linha_produto,
    SUM(valor_total) AS faturamento_total
FROM public.processed
GROUP BY linha_produto
ORDER BY faturamento_total DESC
LIMIT 1;


-- linha de produto com melhor avaliação média:

SELECT
    linha_produto,
    ROUND(AVG(avaliacao)::numeric, 2) AS avaliacao_media
FROM public.processed
GROUP BY linha_produto
ORDER BY avaliacao_media DESC
LIMIT 1;

-- forma de pagamento mais utilizada:

SELECT
    forma_pagamento,
    COUNT(DISTINCT id_venda) AS quantidade_vendas
FROM public.processed
GROUP BY forma_pagamento
ORDER BY quantidade_vendas DESC
LIMIT 1;

-- valor médio das vendas:
SELECT
    ROUND(AVG(valor_total)::numeric, 2) AS valor_medio_venda
FROM public.processed;

-- maior venda registrada:

SELECT
    id_venda,
    filial,
    linha_produto,
    valor_total,
    data_venda
FROM public.processed
ORDER BY valor_total DESC
LIMIT 1;

-- dia da semana com maior média de vendas:

SELECT
    TO_CHAR(data_venda, 'FMDay') AS dia_semana,
    ROUND(AVG(valor_total)::numeric, 2) AS media_vendas
FROM public.processed
WHERE data_venda IS NOT NULL
GROUP BY EXTRACT(ISODOW FROM data_venda), TO_CHAR(data_venda, 'FMDay')
ORDER BY media_vendas DESC
LIMIT 1;

