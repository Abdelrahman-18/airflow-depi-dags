from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import random


def print_welcome():
    print("Welcome Abdelrahman")  

def generate_random():
    number = random.randint(1, 100)
    with open("/tmp/random.txt", "w") as f:
        f.write(str(number))
    print(f"Generated random number: {number}")



with DAG(
    dag_id="Airflow_depi",
    start_date=datetime(2025, 10, 1),
    schedule_interval=timedelta(minutes=1),
    catchup=False,

) as dag:

    
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    task2 = PythonOperator(
        task_id='welcome_message',
        python_callable=print_welcome
    )

    
    task3 = PythonOperator(
        task_id='generate_random',
        python_callable=generate_random
    )

    
    task1 >> task2 >> task3
