import os          
import sys 

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta

with DAG(
    dag_id=f"subdomain_finder_flow",
    start_date=datetime(2023,7,28),
    schedule=timedelta(minutes=10),
    catchup=False,
    tags= ["kafka", "spark", "mongoDB"],
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=3)
    }
) as dag:
    t0 = DummyOperator(
        task_id='start_pipeline',
    )
    
    t1 = BashOperator(
        task_id='kafka_producer',
        bash_command='/home/mehrdad/watchdog/airflow/dags/run_producer.sh ',
    )
    
    t0 >> t1