


from alllists import alllist

print(alllist

#
create table Distant_HongLian_linux(
id int not null primary key auto_increment,
title text,
links text,
type varchar(20)
) engine=InnoDB  charset=utf8;

drop table Distant_HongLian_linux;
#
insert into Distant_HongLian_linux(title,links)
SELECT distinct title,links FROM YunWei_PL.HongLian_linux;