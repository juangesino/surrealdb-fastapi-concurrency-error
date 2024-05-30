# SurrealDB FastAPI Concurrency Error

The purpose of this repo is to showcase how to reproduce an error that arises when concurrent requests hit a FastAPI endpoint that interacts with a SurrealDB instance.

This is the exception raised:

```
RuntimeError: cannot call recv while another coroutine is already waiting for the next message
```

To reproduce this error, you can follow these steps:

1. Clone this repository
1. Build and start the docker services: `make build`
1. Run the sequential test (this should not fail): `make sequential`
1. Run the concurrent test (this will fail): `make concurrent`

Not only will the server throw the exception mentioned before, it will not recover. The server hangs and needs to be restarted.

Here are the commands in case you don't have [GNU Make](https://www.gnu.org/software/make/) installed:

1. Clone this repository
1. Build and start the docker services: `docker-compose -f docker-compose.yml up --build --force-recreate`
1. Run the sequential test (this should not fail): `docker exec -it surreal-demo-server-1 python demo_sequential.py`
1. Run the concurrent test (this will fail): `docker exec -it surreal-demo-server-1 python demo_concurrent.py`
