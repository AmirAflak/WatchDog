.PHONY: install run docker consumer airflow

install:
	@echo "Installing packages ..."
	@pip install -r requirements.txt

docker:
	@echo "Initializing docker-compose ..."
	@cd docker && docker-compose up -d --remove-orphans

consumer:
	@echo "Initializing spark streaming ..."
	@nohup python spark_consumer.py > /dev/null 2>&1 &

scheduler:
	@echo "Initializing airflow scheduler ..."
	@cd airflow && nohup airflow scheduler > /dev/null 2>&1 &

webserver:
	@echo "Initializing airflow webserver GUI ..."
	@cd airflow && nohup airflow webserver > /dev/null 2>&1 &

stop:
	@echo "Stopping docker-compose containers ..."
	cd docker && docker-compose down 





