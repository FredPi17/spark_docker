# airflowRedditPysparkDag.py
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import os

'''
input arguments for downloading S3 data
and Spark jobs
REMARK:
Replace `srcDir` and `redditFile` as the full paths containing your PySpark scripts
and location of the Reddit file will be stored respectively
'''

srcDir = os.getcwd() + '/src/'
sparkSubmit = '/usr/local/spark/bin/spark-submit'

## Define the DAG object
default_args = {
    'owner': 'FRED',
    'depends_on_past': False,
    'start_date': datetime(2016, 10, 15),
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}
dag = DAG('countingWords', default_args=default_args, schedule_interval=timedelta(1))

'''
Defining three tasks: one task to download S3 data
and two Spark jobs that depend on the data to be
successfully downloaded
task to download data
'''
downloadData= BashOperator(
    task_id='counting-words',
    bash_command=sparkSubmit + ' test.py',
    dag=dag)
"""
#task to compute number of unique authors
numUniqueAuthors = BashOperator(
    task_id='unique-authors',
    bash_command=sparkSubmit + ' ' + srcDir + 'pyspark/numUniqueAuthors.py ' ,
    dag=dag)
#Specify that this task depends on the downloadData task
numUniqueAuthors.set_upstream(downloadData)
"""
#task to compute average upvotes
averageUpvotes = BashOperator(
    task_id='average-upvotes',
    bash_command=sparkSubmit + ' ' + srcDir + 'pyspark/averageUpvote.py ' + redditFile,
    dag=dag)
averageUpvotes.set_upstream(downloadData)