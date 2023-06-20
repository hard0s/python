import sqlite3 as sl

con = sl.connect('test.db')

con.execute('create table cars(id_c int primary key not null autoincrement, model varchar(30) not null, price int not null)')

sq = 'insert into cars(id_c, model, price) values(?,?,?)'
data = [(1, 'bmw', 25000),
         (2, 'mercedec', 30000),
         (3, 'waga', 40000)]
con.executemany(sq, data)