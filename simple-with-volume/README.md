## Starting PostgreSQL

Starting PostgreSQL with a volume for data persistence in the ./data folder.

```bash
./start.sh
```

## Run psql

```bash
docker exec -it pgdev psql -U postgres
```

## Copy CSV file into the table.

```postgresql
COPY test1 FROM '/local/test1.csv' DELIMITER ',' CSV HEADER;
```