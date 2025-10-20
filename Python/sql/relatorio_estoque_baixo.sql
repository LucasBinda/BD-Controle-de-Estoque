SELECT
    id_produto,
    nome_produto,
    estoque_atual
FROM produtos
WHERE estoque_atual <= 30   -- valor ajustavel
ORDER BY estoque_atual ASC