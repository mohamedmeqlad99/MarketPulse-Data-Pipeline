from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the Python function to be executed
def print_message():
    print("Data ingestion task is running!")

# Define the default arguments for the DAG
default_args = {
    'owner': 'meqlad',
    'retries': 1,
    'start_date': datetime(2023, 10, 11),
}

# Define the DAG
with DAG(
    dag_id='market_data_ingestion_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Run daily
    catchup=False,
) as dag:

    # Task 1: Print the current date using Bash
    print_date_task = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    # Task 2: Run the Python function to print a message
    python_task = PythonOperator(
        task_id='print_message',
        python_callable=print_message
    )

    # Set task dependencies
    print_date_task >> python_task
