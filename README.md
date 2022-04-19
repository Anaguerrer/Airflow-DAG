# Airflow-DAG
PRUEBA TÉCNICA Data Engineering - Telefónica - Ana Guerrero


NOTA: Se ha configurado la tarea para que no se pida ninguna autenticación al entrar.
NOTA: El DAG se ejecutará cada minuto porque así se ha programado (a no ser que se pause).
NOTA: Con Python 3.8 parece que hay problemas a la hora de instalar apache-airflow; recomiendo actualizar la versión a Python 3.10

Para ejecutar esta tarea serán necesarios los siguientes pasos:

1. Tener un entorno local de Python (creamos el entorno virtual: python3 -m venv env).

2. Activamos el entorno virtual con el comando: source env/bin/activate.

4. Declaramos la variable de entorno necesaria ejecutando el comando: export AIRFLOW_HOME=/Users/<nombre_usuario>/Desktop/airflow-prueba/airflow (con la ruta personalizada correspondiente). Este paso es necesario para que no nos pida la autenticación al entrar.

3. Instalamos Apache Airflow: 'pip install apache-airflow'. Una vez termine iniciamos la bbdd con el comando 'airflow db init'


5. Accedemos al fichero que acaba de generarse con el nombre "webserver_config.py" y añadimos lo siguiente:

* AUTH_ROLE_PUBLIC = 'Admin' (podemos descomentar el que ya viene)

5. Una vez esté todo instalado y configurado ejecutamos el comando 'airflow webserver' para desplegar la UI de Airflow y poder interactuar con la tarea creada.

6. En este punto ya podemos acceder a la interfaz en la ruta "localhost:8080", dónde veremos nuestro DAG y algunos ejemplos.

7. En otra terminal, repitiendo el paso 2 y exportando la variable de entorno (export AIRFLOW_HOME=/Users/<nombre_usuario>/Desktop/airflow-prueba/airflow); ejecutamos 'airflow scheduler' para poder ejecutar nuestra tarea.

8. Entramos en la interfaz, ejecutamos el DAG y podremos ver en los logs la siguiente frase actualizada:

                  'the value of bitcoin is currently: 41,612.7631 USD'
