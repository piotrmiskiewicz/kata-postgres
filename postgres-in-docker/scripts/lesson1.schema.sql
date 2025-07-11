create table person (
    id serial primary key,
    first_name varchar(50) not null,
    age int not null
);

create index idx_person_first_name on person (first_name);
alter table person drop index if exists idx_person_first_name;

create index idx_person_age on person (age);

create index idx_person_age on person (age);

-- generate
DO $$
DECLARE
i INT := 0;
   age INT := 0;
   v_first_name varchar(50);
BEGIN
    WHILE i < 1000000 LOOP
        v_first_name := (array_sample(ARRAY['john','mark', 'robert', 'chris', 'ada', 'barbara'], 1))[1];
        age := floor(random() * 60) + 20;
        insert into person (first_name, age) VALUES (v_first_name, age);
        i := i + 1;
END LOOP;
END
$$;

\timing on