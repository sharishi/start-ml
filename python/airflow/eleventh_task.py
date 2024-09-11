from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from airflow.providers.postgres.hooks.postgres import PostgresHook

def get_user():
    postgres = PostgresHook(postgres_conn_id="startml_feed")
    with postgres.get_conn() as conn:
        with conn.cursor() as cursor:
            """найти пользователя, который поставил больше всего лайков"""
            cursor.execute(
                """
            SELECT user_id, COUNT(action) as count
            FROM feed_action
            WHERE action = 'like'
            GROUP BY user_id
            ORDER BY count desc
            LIMIT 1
            """
            )
            results = cursor.fetchone()
            return results



with DAG(
    'hw_v-trebis_11',
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
    tags=['eleven_try'],
) as dag:

        t1 = PythonOperator(
                task_id='user_return',
                python_callable=get_user,
        )

