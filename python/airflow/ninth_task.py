from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def xcompush(ti):
    ti.xcom_push(
        key='sample_xcom_key',
        value='xcom test'
    )


def xcompull(ti):

    xcom_value = ti.xcom_pull(
        key='sample_xcom_key',
        task_ids='xcom__push'
    )

    print(xcom_value)


with DAG(
    'hw_v-trebis_9',
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
    tags=['ninth_try'],
) as dag:
    t1 = PythonOperator(
        task_id='xcom__push',
        python_callable=xcompush,
    )
    t2 = PythonOperator(
        task_id='xcom__pull',
        python_callable=xcompull,
    )

    t1 >> t2