/* Vou colocar o código, considerando que todas as tabelas foram criadas
todos os dados foram inseridos, e etc. Resumindo, supondo que todo o código 
disponibilizado por vocês já foi rodado*/ 

select ctg.name, sum(op.units_sold)  from orders_products as op
inner join products prd on prd.id = op.product_id
inner join categories as ctg on ctg.id = prd.id_categories
group by ctg.name
order by sum(op.units_sold) desc
limit 4;