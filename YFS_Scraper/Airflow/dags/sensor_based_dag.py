from airflow.decorators import task, dag
from pendulum import datetime
from datetime import timedelta
from airflow.sensors.external_task import ExternalTaskSensor

from YFS_Scraper.Airflow.dags.orchestration_plan1 import default_args

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}
@dag(
    dag_id="transform_and_ingestion",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2026,1,1),
    catchup=False,
    paused_upon_creation=True
)
def transform_and_ingestion():
    event_completeion=ExternalTaskSensor(
        task_id="trigger_scraper_YFS",
        timeout=600
    )

    @task.python(task_id="transformations")
    def transformation():
        pass

    @task.python(task_id="insertion_into_db")
    def insertion_into_db():
        pass

    # invoking task
    transformation=transformation()
    insertion_into_db=insertion_into_db()

    # setting order
    transformation >> insertion_into_db

transform_and_ingestion()

