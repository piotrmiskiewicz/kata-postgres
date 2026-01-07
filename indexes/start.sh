#!/usr/bin/env bash
docker pull postgres:18
docker run \
  --name pgdev \
  -e POSTGRES_PASSWORD=Str0ngP@ssword \
  --volume $(pwd):/local \
  -d -p 5432:5432 --volume $(pwd)/data:/var/lib/postgresql/data  postgres