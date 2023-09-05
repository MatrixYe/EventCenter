.PHONY: database build start proto help

## 创建数据库
database:
	echo "启动Postgres数据库... ..."
	docker-compose up -d

## 编译
build:
	sh ./build.sh

start:
	sh ./start.sh
## 生成grpc go文件
proto:
	protoc --go_out=./ --go-grpc_out=./ ./core.proto
## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo ' make target'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
	helpMessage = match(lastLine, /^## (.*)/); \
	if (helpMessage) { \
	helpCommand = substr($$1, 0, index($$1, ":")-1); \
	helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
	printf " %-20s %s\n", helpCommand, helpMessage; \
	} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)