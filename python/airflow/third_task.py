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
    'hw_v-trebis_3',
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
    tags=['third_try'],
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

    def task_number_function(task_number):
        return f"task number is: {task_number}"


    # Генерируем таски в цикле - так тоже можно
    for i in range(20):
        # Каждый таск будет спать некое количество секунд
        t2 = PythonOperator(
            task_id='task_number' + str(i),  # в id можно делать все, что разрешают строки в python
            python_callable=task_number_function,
            # передаем в аргумент с названием random_base значение float(i) / 10
            op_kwargs={'task_number': i},
        )
        # настраиваем зависимости между задачами
        # run_this - это некий таск, объявленный ранее (в этом примере не объявлен)
    t2.doc_md = dedent(
        """\
    #### Task_2 Documentation
    Using Markdown for this task:
    `for i in range(20):` i **would** like to *present* our cycle
    So... our **simple** documentation is ready!
    """
    )
    t1 >> t2