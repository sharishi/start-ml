"""
Test documentation
"""
from datetime import datetime, timedelta
from textwrap import dedent


from airflow import DAG

from airflow.operators.bash import BashOperator

with DAG(
    'hw_v-trebis_5',
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
    start_date=datetime(2023, 12, 31),
    catchup=False,
    tags=['fifth_try'],
) as dag:
    """Создайте новый DAG, состоящий из одного BashOperator.
     Этот оператор должен  использовать шаблонизированную команду следующего вида:
      "Для каждого i в диапазоне от 0 до 5 не включительно распечатать значение ts
       и затем распечатать значение run_id". Здесь ts и run_id - это шаблонные переменные
        (вспомните, как в лекции подставляли шаблонные переменные)."""

    templated_code = dedent(
        """
        {% for i in range(5) %}
        echo "{{ ts }}"
        {% endfor %}
        echo "{{ run_id }}"
        """)
    t1 = BashOperator(
        task_id='command',
        bash_command=templated_code)

    t1