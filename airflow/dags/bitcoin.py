from datetime import datetime
import json
from urllib import request
import requests
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_bitcoin_value():

  res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

  response_dict = json.loads(res.text)
  print('the value of bitcoin is currently:', response_dict['bpi']['USD']['rate'], 'USD')

dag = DAG('bitcoin_value', description='Bitcoin value DAG',

schedule_interval='* * * * *',

start_date=datetime(2017, 3, 20),

catchup=False,)

hello_operator = PythonOperator(task_id='bitcoin_value', python_callable=print_bitcoin_value, dag=dag)