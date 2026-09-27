from airflow.decorators import dag, task
from cachetools import keys
from pendulum import datetime
from datetime import timedelta
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}
@dag(
    dag_id="dag_to_trigger_scrappers",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    is_paused_upon_creation=True
)

def dag_to_trigger_scrappers():

    @task.bash(task_id="pointing_to_scrappper_directory")
    def pointing_to_scrappper_directory(**kwargs):
        ti=kwargs["ti"]
        scrapper_fire_dirctory= "/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/YFS_Scraper"
        ti.xcom_push(keys="scrapper_fire_dirctory",value=scrapper_fire_dirctory)
        return f"cd {scrapper_fire_dirctory}"
    @task.bash(task_id="trigger_scraper_YFS")
    def trigger_scraper_YFS(**kwargs):
        import os
        ti=kwargs["ti"]
        scrapper_fire_path=ti.xcom_pull(keys="scrapper_fire_path",task_id="pointing_to_scrappper_directory")
        os.chdir(scrapper_fire_path)
        return "scrapy crawl YFS_spider"

    #initiating the tasks
    pointing_to_scrappper_directory=pointing_to_scrappper_directory()
    trigger_scraper_YFS=trigger_scraper_YFS()


    # Setting dependencies
    pointing_to_scrappper_directory >> trigger_scraper_YFS

dag_to_trigger_scrappers()

