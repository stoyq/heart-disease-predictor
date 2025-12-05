.PHONY: up
up: ## stop and start docker-compose services
	# stop existing containers
	make stop
	# try to pull from Docker Hub; if that fails, build locally
	docker compose pull || docker build -t josedmyt/heart-disease-predictor:latest .
	# then start services
	docker compose up -d

.PHONY: stop
stop: ## stop docker-compose services
	docker compose stop


.PHONY: cl
cl: ## create conda lock for multiple platforms
	# the linux-aarch64 is used for ARM Macs using linux docker container
	conda-lock lock \
		--file environment.yml \
		-p linux-64 \
		-p osx-64 \
		-p osx-arm64 \
		-p win-64 \
		-p linux-aarch64

.PHONY: env
env:
	conda env remove -n group25-env -y || true
#	conda-lock install -n group25-env conda-lock.yml
	conda env create --file environment.yml
	
.PHONY: report
report:
	quarto render doc/heart_disease_predictor_quarto_report.qmd --to pdf
	quarto render doc/heart_disease_predictor_quarto_report.qmd --to html

.PHONY: clean
clean:
	rm -rf doc/heart_disease_predictor_quarto_report_files
	rm -f doc/heart_disease_predictor_quarto_report.pdf
	rm -f doc/heart_disease_predictor_quarto_report.html