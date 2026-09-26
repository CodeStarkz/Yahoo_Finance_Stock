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
        return "pwd"
    @task.bash(task_id="checkCWD")
    def check_cwd():
        return "pwd"
    @task.bash(task_id="change_direcotry_to_scrapeyard")
    def change_direcotry_to_scrapeyard():
        return "cd /Users/abhisheksingh/Desktop/Yahoo_Finance_Stock/YFS_Scraper/YFS_Scraper"
    @task.bash(task_id="trigger_fobes_scraper")
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

# calling dag XatAxbsxzk7GfMWR
ingestion_dag()


#
"""


# 1. Fully kill any active background services
pkill -9 -f airflow
rm -f ./airflow-*.pid

# 2. Force Airflow to use THIS local directory as its official home
export AIRFLOW_HOME=$(pwd)

# 3. Double-check that your config value is accurately caught by Airflow
# (This should return 'False'. If it says True, change it in your local airflow.cfg file)
airflow config get-value core load_examples

# 4. Safely delete the SQLite db files again to start fresh
rm -f ./airflow.db ./airflow.db-shm ./airflow.db-wal

# 5. Initialize the clean, example-free database mapped specifically to this folder
airflow db migrate

# 6. Re-inject your admin/admin login password locally
echo '{"admin": "admin"}' > ./simple_auth_manager_passwords.json.generated

# 7. Apply Mac thread patch and launch everything cleanly
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
airflow api-server --port 8085 -D
airflow scheduler -D
airflow triggerer -D
airflow dag-processor


"""