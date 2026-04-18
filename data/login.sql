create database if not exists login;

use login;

create table user_login(
    id int(11) not null auto_increment primary key,
    username varchar(255) not null,
    password varchar(255) not null
);
insert into user_login(username,password) values('admin','admin');