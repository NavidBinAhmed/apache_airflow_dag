from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime, timedelta
import random

# tasks of workflow
def ingest_data():
    print("Ingesting raw data from source...")

def validate_data():
    print("Validating data quality and schema...")

def choose_path():
    # Simulation of condition-based branching
    return "transform_data" if random.choice([True, False]) else "skip_transform"

def transform_data():
    print("Transforming data...")

def skip_transform():
    print("Skipping transformation due to data condition.")

def load_to_warehouse():
    print("Loading data into warehouse...")

def notify_success():
    print("Pipeline completed successfully!")

def notify_failure(context):
    print(f"Pipeline failed: {context['task_instance_key_str']}")

default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(seconds=30),
    "on_failure_callback": notify_failure,
}

# airflow 3.0.0 changes 'schedule_interval' to 'schedule'

with DAG(
    dag_id="dag2",
    start_date=datetime(2025, 5, 1),
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    tags=["demo", "branching", "retries"]
) as dag:

    start = EmptyOperator(task_id="start")
    end = EmptyOperator(task_id="end")

    ingest = PythonOperator(task_id="ingest_data", python_callable=ingest_data)
    validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    branching = BranchPythonOperator(task_id="branch_decision", python_callable=choose_path)

    transform = PythonOperator(task_id="transform_data", python_callable=transform_data)
    skip = PythonOperator(task_id="skip_transform", python_callable=skip_transform)

    '''require DB access to implement this step, skipped for now'''
    load = PythonOperator(task_id="load_to_warehouse", python_callable=load_to_warehouse)
    notify = PythonOperator(task_id="notify_success", python_callable=notify_success)

    # dependencies
    start >> ingest >> validate >> branching
    branching >> transform >> load
    branching >> skip >> load
    load >> notify >> end
