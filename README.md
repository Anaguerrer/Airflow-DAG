# Airflow-DAG
PRUEBA TÉCNICA Data Engineering - Telefónica - Ana Guerrero


NOTE: The DAG will run every minute as scheduled (unless paused).
NOTE: With Python 3.8 there seem to be problems installing apache-airflow; I recommend updating the version to Python 3.10
NOTE: all the commands are for the MAC operating system, if you have any other look for the analogs in the relevant documentation.


To execute this task, the following steps will be necessary:

1. Have a local Python environment (we create the virtual environment: python3 -m venv env).

2. We activate the virtual environment with the command: source env/bin/activate.

3. We declare the necessary environment variable by running the command: export AIRFLOW_HOME=/Users/<user_name>/Desktop/Airflow-DAG/airflow (with the corresponding custom path). This step is really important.


4. To prevent examples from being loaded by default, we run the following command: export AIRFLOW__CORE__LOAD_EXAMPLES=false

5. We install Apache Airflow: 'pip install apache-airflow'. Once finished we start the bbdd with the command 'airflow db init'.


6. We access the file that has just been generated with the name "webserver_config.py" and add the following:

* AUTH_ROLE_PUBLIC = 'Admin'. This step is important so that we can enter without authentication. 

5. Once everything is installed and configured, we execute the 'airflow webserver' command to display the Airflow UI and be able to interact with the created task.

6. At this point we can already access the interface in the path "localhost:8080", where we will see our DAG (but we will not be able to execute it yet).

7. In another terminal, repeating step 2 and exporting the environment variable (export AIRFLOW_HOME=/Users/<user_name>/Desktop/Airflow-DAG/airflow); we run 'airflow scheduler' to be able to execute our task.

8. We enter the interface, execute the DAG and we can see the following updated phrase in the logs:

                  'the value of bitcoin is currently: 41,612.7631 USD'
