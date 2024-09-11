from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def xcompull(ti):

    xcom_value = ti.xcom_pull(
        key='return_value',
        task_ids='xcom_push'
    )

    print(xcom_value)


with DAG(
    'hw_v-trebis_10',
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
    tags=['tenth_try'],
) as dag:

    def print_string():
        return "Airflow tracks everything"

    t1 = PythonOperator(
        task_id='xcom_push',
        python_callable=print_string,
    )
    t2 = PythonOperator(
        task_id='xcom_pull',
        python_callable=xcompull,
    )

    t1 >> t2