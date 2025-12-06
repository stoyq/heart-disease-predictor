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
##		-p linux-aarch64

.PHONY: env
env:
	conda env remove -n group25-env -y || true
#	conda-lock install -n group25-env conda-lock.yml
	conda env create --file environment.yml

.PHONY: analysis
analysis:
	# Step 1: Download the data

	python scripts/01_data_download.py \
		--dataset_url="https://archive.ics.uci.edu/static/public/45/heart+disease.zip" \
		--dataset_filename="processed.cleveland.data" \
		--download_dir="./data/raw" \
		--output_dir="./data/processed"

	# Step 2:

	# Step 3:
	python scripts/eda.py \
		--processed-training-data data/processed/cleveland_clean.csv \
		--plot-to ./eda/img/
	python scripts/eda_part2.py \
    	--processed-training-data data/processed/cleveland_clean.csv \
		--output-to ./eda/tables/

	# Step 4:


.PHONY: report
report:
	rm -rf doc/heart_disease_predictor_quarto_report_files
	rm -f doc/heart_disease_predictor_quarto_report.pdf
	rm -f doc/heart_disease_predictor_quarto_report.html
	quarto render doc/heart_disease_predictor_quarto_report.qmd --to pdf
	quarto render doc/heart_disease_predictor_quarto_report.qmd --to html


.PHONY: clean
clean:
	rm -rf doc/heart_disease_predictor_quarto_report_files
