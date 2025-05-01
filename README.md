## Steps of implementation - Running Airflow on Docker

1. write `dpcker-compose.yaml` file

2. create directories
   `mkdir ./dags ./plugins ./logs`

3. set env variables
   `echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env`

4. initialization airflow
   `docker-compose up airflow-init`

5. building
   `docker-compose up`

   or

   `docker-compose up --build`

6. list
   `docker ps`

7. run `localhost:8081` on browser with username and password `airflow`


![image](https://github.com/user-attachments/assets/6aafeeb1-ba95-4513-a403-127ab724abe8)

.
.

## Implementation of DAGs
1. I am developing a DAG for my data pipeline ETL project - DONE

#### Workflows: Directed Acrylic Graph
![image](https://github.com/user-attachments/assets/a8102972-f2d4-4ff2-bafa-5570aaaa7aee)

#### Runs:
![image](https://github.com/user-attachments/assets/af1c3801-e3c6-4b87-9a24-0c42b12a7d0b)

yeaaaa....scheduled a run (today) for this simple ETL DAG and works as expected. (ongoing)


2. Another for an ML algorithm preferance project

Both supports scheduling, dependancies, execution and processes.


## How I resolved issues
1. 'Docker Compose' was not working
- Installed docker compose via Linux terminal, followed this [link](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)
alternatively, tried the same while Docker Desktop was running

2. Linux command 'echo' not working
- Opened wsl terminal and retried command

3. 'docker compose up' encountered error saying container is unhealthy
ERROR: for airflow-worker  Container "1de6c71a669e" is unhealthy.

- It finds what was going wrong.
0027d38ebbe1   apache/airflow:3.0.0     "/usr/bin/dumb-init …"   16 minutes ago   Created      airflow-docker-airflow-worker-1

- Rebuild after running
docker-compose down --volumes --remove-orphans

and changing the external:internal ports to 8081:8080

4. 'import error'
- created virtual env and executed conda installation
- apache airflow 3.0.0 has a change in import and worked on how the method was called: a bit changed
  `from airflow.providers.standard.operators.python import PythonOperator`
