create table person (
    id serial primary key,
    first_name varchar(50) not null,
    age int not null,
    zip char(6),
    city char(32),
    data_s json,
    data_b jsonb
);

make in