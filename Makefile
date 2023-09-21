.PHONY: install run docker consumer airflow

install:
	pip install -r requirements.txt

run: 
	docker

docker:
	docker-compose up -d
	sleep 30 # add a sleep time of 30 seconds
	nohup python consumer.py > /dev/null 2>&1 &
	sleep 30 # add a sleep time of 30 seconds
	cd airflow && airflow webserver -D && airflow scheduler -D