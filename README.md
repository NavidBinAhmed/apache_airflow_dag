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

Overview of UI DAGs in my environment:

![image](https://github.com/user-attachments/assets/6aafeeb1-ba95-4513-a403-127ab724abe8)

.
.

## Implementation of DAG Workflows: Directed Acrylic Graph
1. DAG for my data pipeline ETL project - DONE

![image](https://github.com/user-attachments/assets/a8102972-f2d4-4ff2-bafa-5570aaaa7aee)


![image](https://github.com/user-attachments/assets/af1c3801-e3c6-4b87-9a24-0c42b12a7d0b)

yeaaaa....scheduled a run (today) for this simple ETL DAG and works as expected. (ongoing)

2. DAG for an ETL pipeline with feedback - DONE

   ![image](https://github.com/user-attachments/assets/9f70218f-7a99-4805-80ad-b0d348ccb5e2)

3. DAG for selecting the best ML algorithm based on accuracies

![image](https://github.com/user-attachments/assets/b2ba3558-8e67-4138-9b3c-bb3019400cc0)

Both supports scheduling, dependancies, execution and processes.

## Coding Algorithm
Step 1: Importing airflow, datetime
Step 2: Define DAG() method
Step 3: Importing PythonOperator and defining flows
Step 4: Sequence of workflow

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


Refs:
# apache airflow doc, [link](https://airflow.apache.org/docs/)
# Data With Mark, [YouTube](https://www.youtube.com/watch?v=IH1-0hwFZRQ)
# Airflow, [GitHub](https://github.com/apache/airflow)
