build:
	docker-compose -f docker-compose.yml up --build --force-recreate

start:
	docker-compose -f docker-compose.yml up

sequential:
	docker exec -it surreal-demo-server-1 python demo_sequential.py

concurrent:
	docker exec -it surreal-demo-server-1 python demo_concurrent.py