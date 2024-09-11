from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator


def branch_operator():
    from airflow.models import Variable
    if Variable.get("is_startml"):
        return 'startml_desc'
    return 'not_startml_desc'


def print_true():
    print("StartML is a starter course for ambitious people")


def print_false():
    print("Not a startML course, sorry")


with DAG(
    'hw_v-trebis_13',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 12, 29),
    catchup=False,
    tags=['thirteenth_try'],
) as dag:

    t1 = DummyOperator(task_id='before')

    t2 = BranchPythonOperator(
        task_id='choose_best_model',
        python_callable=branch_operator
    )

    t3 = PythonOperator(
                task_id='startml_desc',
                python_callable=print_true,
        )

    t4 = PythonOperator(
            task_id='not_startml_desc',
            python_callable=print_false,
        )
    t5 = DummyOperator(task_id='after')


    t1 >> t2 >> [t3, t4] >> t5