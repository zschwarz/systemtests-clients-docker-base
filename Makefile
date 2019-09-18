DOCKER_ORG	?= quay.io/enmasse
TAG ?= latest


all: download_java_clients docker_build docker_tag docker_push

docker_build:
	if [ -f Dockerfile ]; then docker build --build-arg version=$(VERSION) -t systemtests-clients:$(TAG) . ; fi
	docker images | grep systemtests-clients

docker_push:
	docker push $(DOCKER_ORG)/systemtests-clients:$(TAG)

docker_tag:
	docker tag systemtests-clients:$(TAG) $(DOCKER_ORG)/systemtests-clients:$(TAG)

download_java_clients:
	./download_java_clients.sh

.PHONY: download_java_clients docker_build docker_tag docker_push