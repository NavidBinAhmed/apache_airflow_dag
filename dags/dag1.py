from airflow import DAG

from airflow.providers.standard.operators.python import PythonOperator

from datetime import datetime

'''this DAG demonstrates the workflow on an ETL pipeline'''

# tasks
def extract():
    pass

def transform():
    pass

def load():
    pass

# schedule
'''The airflow UI will show the name as it is defined here: 'dag1' '''
with DAG("dag1", start_date=datetime(2025,2,5), schedule="@daily", catchup=False) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

# dependencies and sequence of workflow
    t1 >> t2 >> t3
