## Steps of implementation - Running Airflow on Docker

1. write `dpcker-compose.yaml` file

2. create directories

   `mkdir ./dags ./plugins ./logs`

4. set env variables

   `echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env`

5. initialization airflow

   `docker-compose up airflow-init`

6. building

   `docker-compose up`

   or

   `docker-compose up --build`

7. list

   `docker ps`

9. run `localhost:8081` on browser with username and password `airflow`

Summary statistics of our Airflow environment (**Home**) : Overview of UI
   ![image](https://github.com/user-attachments/assets/6aafeeb1-ba95-4513-a403-127ab724abe8)

Overview of all **DAGs** in our Airflow environment including example DAGs:
   ![image](https://github.com/user-attachments/assets/154ac422-aed8-4235-957e-2b7ab86643d8)

Overview of **assets** with dependencies:
   ![image](https://github.com/user-attachments/assets/3c83f4fb-5953-4ef2-a40a-18695f09df99)

.
.

## Implementation of DAG Workflows: Directed Acrylic Graph
1. DAG for my data pipeline ETL project - DONE

How the graph view of our first DAG (dag1) looks like:
   ![image](https://github.com/user-attachments/assets/a8102972-f2d4-4ff2-bafa-5570aaaa7aee)

**Status** of grid on the workflow:
   ![image](https://github.com/user-attachments/assets/af1c3801-e3c6-4b87-9a24-0c42b12a7d0b)

yeaaaa....scheduled a run (today) for this simple ETL DAG and works as expected. (ongoing)

2. DAG for an ETL pipeline with feedback - DONE

**Graph** visualization of the DAG's dependencies and their current status for a specific run.
   ![image](https://github.com/user-attachments/assets/9f70218f-7a99-4805-80ad-b0d348ccb5e2)

**Grid** representation DAG that spans across schdeduled/ manual time:
   ![image](https://github.com/user-attachments/assets/1bc73708-ee8a-4004-964b-ddac9888c4bf)

3. DAG for selecting the best ML algorithm based on accuracies

   ![image](https://github.com/user-attachments/assets/b2ba3558-8e67-4138-9b3c-bb3019400cc0)

Both supports scheduling, dependancies, execution and processes.

.
.

## Coding Algorithm
Step 1: Importing airflow, datetime

Step 2: Define DAG() method

Step 3: Importing PythonOperator and defining flows

Step 4: Sequence of workflow

Final: Refresh Airflow dashbard and explore the developed DAG

.
.

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
