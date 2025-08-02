from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="test_dag",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["test"],
) as dag:
    EmptyOperator(task_id="start")