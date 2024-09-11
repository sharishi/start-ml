"""
Test documentation
"""
from datetime import datetime, timedelta
from textwrap import dedent


from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
"""Создайте новый DAG и объявите в нем 30 задач. Первые 10 задач сделайте типа BashOperator
 и выполните в них произвольную команду, так или иначе использующую переменную цикла
  (например, можете указать f"echo {i}")."""
with DAG(
    'hw_v-trebis_7',
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
    tags=['seventh_try'],
) as dag:

    for i in range(10):

        t1 = BashOperator(
            task_id='echo'+str(i),
            bash_command=f"echo {i}",
        )

    t1.doc_md = dedent(
        """\
    #### Task_1 Documentation
    Using Markdown for this task:
    `for i in range(10):` i **would** like to *present* our cycle
    """
    )

    def print_arguments(ts, run_id, **kwargs):
        print(ts)
        print(run_id)


    for i in range(20):

        t2 = PythonOperator(
            task_id='task_number' + str(i),
            python_callable=print_arguments,
            op_kwargs={'task_number': i},
        )

    t2.doc_md = dedent(
        """\
    #### Task_2 Documentation
    Using Markdown for this task:
    `for i in range(20):` i **would** like to *present* our cycle
    So... our **simple** documentation is ready!
    """
    )
    t1 >> t2