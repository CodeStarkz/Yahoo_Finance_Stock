from airflow.decorators import task, dag
from pendulum import datetime
from datetime import timedelta
from airflow.sensors.external_task import ExternalTaskSensor

from orchestration_plan1 import default_args
@dag(
    dag_id="transform_and_ingestion",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2026,1,1),
    catchup=False,
    is_paused_upon_creation=False
)
def transform_and_ingestion():

    wait_for_scraper_YFS = ExternalTaskSensor(
        task_id="wait_for_scraper_YFS",
        external_dag_id="dag_to_trigger_scrappers",
        external_task_id="trigger_scraper_YFS",
        mode="reschedule",
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
    wait_for_scraper_YFS >> transformation >> insertion_into_db

transform_and_ingestion()
