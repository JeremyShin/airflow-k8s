# simple_dag.py

from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='simple_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    task_2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
    )

    task_3 = BashOperator(
        task_id='print_message',
        bash_command='echo "에어플로우 튜토리얼"',
    )

    task_1 >> task_2 >> task_3
