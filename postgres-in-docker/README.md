# build

```shell
docker build . -t my-first-postgres:0.0.1
```

# Run

```shell
docker run -d --name my-postgres \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v $(pwd)/data:/var/lib/postgresql/data/pgdata \
    -p 5432:5432 \
  my-first-postgres:0.0.1

```

If the mounting fails, do:
```text
You can configure shared paths from Docker -> Preferences... -> Resources -> File Sharing.
```