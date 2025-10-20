SELECT
    p.id_produto,
    p.nome_produto,
    -- Contagem total de pedidos
    COALESCE(COUNT(pe.id_pedido), 0) as total_pedidos,

    -- Valores totais movimentados, compra e venda (0 se não houver)
    COALESCE(SUM(pe.quantidade * p.preco), 0) as valor_total_movimentado,
    COALESCE(SUM(CASE WHEN pe.tipo = 'COMPRA' THEN pe.quantidade * p.preco ELSE 0 END), 0) as valor_total_comprado,
    COALESCE(SUM(CASE WHEN pe.tipo = 'VENDA' THEN pe.quantidade * p.preco ELSE 0 END), 0) as valor_total_vendido,


    -- Estoque atual para referência
    p.estoque_atual

FROM produtos p
LEFT JOIN pedidos pe ON p.id_produto = pe.id_produto
GROUP BY p.id_produto, p.nome_produto, p.estoque_atual
ORDER BY valor_total_movimentado DESC