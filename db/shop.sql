.mode table
create table goods (good_id integer primary key, name text, category text, provider integer, quanity integer, price_USD integer);
create table buys (id integer primary key, name_surname text, goods_ids integer, quanity integer,price_for_one integer, sumed_price integer, discount_amount integer, final_price integer);
create table providers (provider_id integer, provider_name text primary key, goods_ids integer, good_type text);
create table special_buyers (id integer primary key, name_surname text, discount_amount integer);
create table category (id integer primary key, good_category text);
create table orders_contain(order_id integer primary key, goods_ids id, goods_names text, quanities text, goods_prices integer);
insert into goods (good_id, name, category, provider, quanity, price_USD) values (1, 'Fender Telecaster', 'Electro Guitar', 1, 10, 2500);
insert into buys (id, name_surname, goods_ids, quanity, price_for_one, sumed_price, discount_amount, final_price) values (1, 'Федор Сумкин', 1, 2, 2500,5000 , 25, 3750);
insert into providers (provider_id,provider_name, goods_ids, good_type) values (1,'Fender USA', 1, 'Electro Guitar');
insert into category (id, good_category) values (1,'Electro_guitar');
insert into orders_contain (order_id, goods_ids, goods_names, quanities, goods_prices) values (1, 1,'Fender Telecaster', 2, 2500);
select * from category;
select * from goods;
select * from buys;
select * from providers;
select * from orders_contain