NAME = "flask-demo"
VERSION = "latest"
.PHONY: build build-version up down
build: build-version
build-version:
	docker build -t ${NAME}:${VERSION} .
up:
	docker-compose up -d
down:
	docker-compose down --volumes
logs:
	docker logs -f ${NAME}
exec:
	docker exec -it ${NAME} sh