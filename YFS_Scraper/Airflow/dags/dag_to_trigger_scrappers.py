"""from airflow.decorators import dag, task
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
    schedule="@daily",
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

"""
from datetime import timedelta
from airflow.decorators import dag, task
from pendulum import datetime

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

@dag(
    dag_id="dag_to_trigger_scrappers",
    default_args=default_args,
    schedule="@daily",
    start_date=datetime(2026, 1, 1), # Added required start_date
    catchup=False,
    is_paused_upon_creation=True
)
def dag_to_trigger_scrappers():
    """
    this pipeline is used to run the scrappers(by tis moment we have two scrapper,\
     with the help of this dag we will trigger both of them paralelly )

    :return:
    """

    # We define the directory as a standard Python variable or template
    SCRAPER_DIR = "/Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/YFS_Scraper"

    # Using standard bash syntax to chain the CD and the run command together
    @task.bash(task_id="trigger_scraper_YFS")
    def trigger_scraper_YFS():
        return f"cd {SCRAPER_DIR} && scrapy crawl YFS_spider"

    @task.bash(task_id="trigger_scraper_fobes")
    def trigger_scraper_fobes():
        return f"cd {SCRAPER_DIR} && scrapy crawl fobes"

    # Initiating the task
    trigger_scraper_YFS= trigger_scraper_YFS()
    trigger_scraper_fobes = trigger_scraper_fobes()

    # Dependencies
    [trigger_scraper_YFS,trigger_scraper_fobes]



dag_to_trigger_scrappers()
