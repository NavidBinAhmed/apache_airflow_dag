from airflow import DAG

from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime

'''this DAG demonstrates the workflow on an ETL pipeline'''

def extract():
    pass

def transform():
    pass

def load():
    pass

with DAG("Dag1", start_date=datetime(2025,2,5), schedule="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3
