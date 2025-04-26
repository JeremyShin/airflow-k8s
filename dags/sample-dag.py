from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

with DAG(
    dag_id='sample-dag',
    schedule_interval='@once',
    start_date=datetime(2025, 4, 26),
    catchup=False
) as dag:
    def sample():
        print('hello wolrd')

    sample_task = PythonOperator(
        task_id='sample',
        python_callable=sample
    )

    sample_task

