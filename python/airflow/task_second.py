"""
Test documentation
"""
from datetime import datetime, timedelta
from textwrap import dedent


from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
with DAG(
    'hw_v-trebis_1',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 12, 27),
    catchup=False,
    tags=['first_try'],
) as dag:

    t1 = BashOperator(
        task_id='print_interior',
        bash_command='pwd',
    )

    def print_context(ds):
        print(ds)

    t2 = PythonOperator(
        task_id='print_the_context',  # нужен task_id, как и всем операторам
        python_callable=print_context,  # свойственен только для PythonOperator - передаем саму функцию
    )


    t1 >> t2
