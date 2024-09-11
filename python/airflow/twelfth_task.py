from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def get_variable():
    from airflow.models import Variable
    is_prod = Variable.get("is_startml")
    print(is_prod)


with DAG(
    'hw_v-trebis_12',
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
    tags=['twelfth_try'],
) as dag:

        t1 = PythonOperator(
                task_id='print_var',
                python_callable=get_variable,
        )

