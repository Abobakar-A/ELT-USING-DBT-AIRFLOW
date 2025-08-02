from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dbt_project_run",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=["dbt"],
) as dag:
    # This task runs a dbt debug command to check the connection
    dbt_debug = BashOperator(
        task_id="dbt_debug",
        # The working directory is set to the dbt project path inside the container
        # Note: This path must match where your dbt project is mounted in the Docker container
        cwd="/opt/airflow/dbt",
        bash_command="dbt debug",
    )

    # This task runs a dbt run command to execute all models
    dbt_run = BashOperator(
        task_id="dbt_run",
        cwd="/opt/airflow/dbt",
        bash_command="dbt run",
    )

    # This task runs a dbt test command to test all models
    dbt_test = BashOperator(
        task_id="dbt_test",
        cwd="/opt/airflow/dbt",
        bash_command="dbt test",
    )

    # Define the task dependencies
    dbt_debug >> dbt_run >> dbt_test
