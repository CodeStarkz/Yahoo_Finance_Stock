from airflow.decorators import dag, task
from pendulum import datetime
from datetime import timedelta
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}
# dag_property
@dag(
    dag_id="ingestion_dag",
    schedule="@daily",
    catchup=False,
    default_args=default_args,
    is_paused_upon_creation=True
)
# dag_definition
def ingestion_dag():

    #task to check server_health
    @task.bash(task_id= "server_health")
    def server_health():
        return "htop"
    @task.bash(task_id="checkCWD")
    def check_cwd():
        return "pwd"
    @task.bash(task_id="change_direcotry_to_scrapeyard")
    def change_direcotry_to_scrapeyard():
        return "cd /Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/YFS_Scraper"
    @task.bask(task_id="trigger_fobes_scraper")
    def trigger_fobes_scraper():
        return "scrapy crawl fobes"
    @task.bash(task_id="trigger_YFS_scraper")
    def trigger_YFS_scraper():
        return 'scrapy crawl YFS_spider'

    # initializing task
    server_health=server_health()
    check_cwd=check_cwd()
    change_direcotry_to_scrapeyard= change_direcotry_to_scrapeyard()
    trigger_fobes_scraper=trigger_fobes_scraper()
    trigger_YFS_scraper=trigger_YFS_scraper()

    # sequencing them
    server_health >> check_cwd >>change_direcotry_to_scrapeyard >>[trigger_fobes_scraper,trigger_YFS_scraper]

# calling dag
ingestion_dag()