.PHONY: up
up: ## stop and start docker-compose services
	# by default stop everything before re-creating
	make stop
	docker compose up -d

.PHONY: stop
stop: ## stop docker-compose services
	docker compose stop