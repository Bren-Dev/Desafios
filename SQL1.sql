/*Rodei o programa no pgAdmin. No caso, lá eu tive que
colocar os comandos para criar as tabelas, logo, estou
disponibilizando todo o código para que funcionasse para mim
quando fui rodando os códigos pela primeira vez*/

CREATE TABLE categories (
  id numeric PRIMARY KEY,
  name varchar
);

CREATE TABLE products (
  id numeric PRIMARY KEY,
  name varchar(50),
  amount numeric,
  price numeric(7,2),
  id_categories numeric REFERENCES categories (id)
);

INSERT INTO categories (id, name)
VALUES 
  (1,	'wood'),
  (2,	'luxury'),
  (3,	'vintage'),
  (4,	'modern'),
  (5,	'super luxury'),
  (6,	'futurist'),
  (7,	'sports'),
  (8,	'office'),
  (9,	'home office'),
  (10,	'gamer');
  
INSERT INTO products (id, name, amount, price, id_categories)
VALUES 
  (1,	'Two-doors wardrobe', 100,	800,	1),
  (2,	'Dining table',	1000,	560,	3),
  (3,	'Towel holder',	10000,	25.50,	4),
  (4,	'Computer Desk',	350,	320.50,	2),
  (5,	'Chair',	3000,	210.64,	4),
  (6,	'Single bed',	750,	460,	1),
  (7,	'Laser Gun', 38, 9999, 6),
  (8,	'RGB Led Strip', 200, 99, 10),
  (9,	'Gamer Chair', 200, 149, 10),
  (10,	'Office Desk', 3999, 70, 8),
  (11,	'Cheese trap', 0, 2, 1),
  (12,	'Synthetic grass 1x1m', 100, 20, 7);

select ctg.name, sum(prd.amount)
from products prd
    join categories ctg on prd.id_categories = ctg.id
group by ctg.name;