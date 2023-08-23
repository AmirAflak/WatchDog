from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta


# constants
MY_NAME = "MY_NAME"
MY_NUMBER = 19

def multiply_by_23(number):
    """Multiplies a number by 23 and prints the results to Airflow logs."""
    result = number * 23
    print(result)
    
    
with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2022,7,28),
    schedule=timedelta(minutes=30),
    catchup=False,
    tags= ["tutorial"],
    default_args={
        "owner": MY_NAME,
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    }
) as dag:
    
    t1 = BashOperator(
        task_id="say_my_name",
        bash_command=f"echo {MY_NAME}"
    )

    t2 = PythonOperator(
        task_id="multiply_my_number_by_23",
        python_callable=multiply_by_23,
        op_kwargs={"number": MY_NUMBER}
    )

    t1 >> t2
