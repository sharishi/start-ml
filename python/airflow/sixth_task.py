"""
Test documentation
"""
from datetime import datetime, timedelta
from textwrap import dedent


from airflow import DAG

from airflow.operators.bash import BashOperator
"""Возьмите BashOperator из третьего задания (где создавали task через цикл)
 и подбросьте туда переменную окружения NUMBER, чье значение будет равно i из цикла.
  Распечатайте это значение в команде, указанной в операторе (для этого используйте bash_command="echo $NUMBER")."""
with DAG(
    'hw_v-trebis_6',
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
    tags=['sixth_try'],
) as dag:

    for i in range(10):

        t1 = BashOperator(
            task_id='echo'+str(i),
            bash_command="echo $NUMBER",
            dag=dag,
            env={"NUMBER": str(i)},
        )

    t1.doc_md = dedent(
        """
    #### Task_1 Documentation
    Using Markdown for this task:
    `for i in range(10):` i **would** like to *present* our cycle
    """
    )
