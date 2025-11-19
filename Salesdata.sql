SELECT * FROM productdata.salesdata;
alter table salesdata drop total;
alter table salesdata drop gst;
alter table salesdata drop final_price;
set sql_safe_updates=0;
alter table salesdata
add column total int not null after quantity;
update salesdata set total = (price * quantity);
alter table salesdata
add column discount int not null after total;
alter table salesdata
add column final_price int not null after discount;
update salesdata set discount = price * 20/100;
update salesdata set final_price = (total - discount);
select * from salesdata where productid = 201 or productid = 205;
select * from salesdata where productID = 203 or ProductID = 201;
select * from salesdata where ProductID = 208 or ProductID = 210;