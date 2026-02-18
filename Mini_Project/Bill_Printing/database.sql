create database if not exists billingdb;
use billingdb;

create table customer (
    customer_id int primary key auto_increment,
    name varchar(100) not null,
    mobile varchar(15) not null
);

create table product_details (
    product_id int primary key auto_increment,
    product_name varchar(100) not null,
    price decimal(10,2) not null
);

create table order_details (
    order_id int primary key auto_increment,
    customer_id int,
    product_id int,
    quantity int not null,
    foreign key(customer_id) references customer(customer_id),
    foreign key(product_id) references product_details(product_id)
);

create table transaction_details (
    transaction_id int primary key auto_increment,
    order_id int,
    total_amount decimal(10,2) not null,
    transaction_date datetime not null,
    foreign key(order_id) references order_details(order_id)
);

insert into customer (name, mobile) values 
('ram', '9876543210'),
('shyam', '9876543211');

insert into product_details (product_name, price) values 
('idli', 60.00),
('dosa', 80.00),
('vada', 40.00);

select 'database created + sample data added!' as status;
