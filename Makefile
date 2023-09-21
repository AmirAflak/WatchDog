.PHONY: install run docker consumer airflow

install:
	pip install -r requirements.txt

docker:
	cd docker && docker-compose up -d --remove-orphans

consumer:
	nohup python spark_consumer.py > /dev/null 2>&1 &

scheduler:
	cd airflow && nohup airflow scheduler > /dev/null 2>&1 &

webserver:
	cd airflow && nohup airflow webserver > /dev/null 2>&1 &

stop:
	cd docker && docker-compose down 





