NAME = "flaks-demo"
VERSION = "latest"
.PHONY: build build-version up down
build: build-version
build-version:
	docker build -t ${NAME}:${VERSION} .
up:
	docker-compose up -d
down:
	docker-compose down --volumes
log:
	docker logs 0f ${NAME}

exec:
	docker exec -it ${NAME} sh