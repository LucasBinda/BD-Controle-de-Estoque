SELECT
	p.id_pedido,
    pr.nome_produto,
    p.quantidade,
    p.tipo,
    p.data,
    pr.preco,
    (p.quantidade * pr.preco) as valor_total
FROM pedidos p
JOIN produtos pr ON p.id_produto = pr.id_produto
ORDER BY p.quantidade