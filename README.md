# Streaming Analytics

This project was developed as a master's thesis in BI & Big Data Analytics at the [Universitat Oberta de Catalunya](https://www.uoc.edu) (UOC).
The topic of the thesis is Streaming Analytics, and this project implements a use case to monitor aircraft flights (events) 
through a stream data pipeline.

The pipeline is made up of the following parts:
- Acquisition of events from [The Open Sky Network](https://opensky-network.org) API.
- Messaging that publishes the events in a containerized Kafka topic.
- Storage of the events in a containerized PostgreSQL database.
- Ingestion that consumes the events from Kafka and processes them using Pandas.
- Near-real-time dashboard using Plotly Dash that shows the calculated metrics.

## Prerequisites

### Required software

The following software is required to run the pipeline locally:

- [Git](https://git-scm.com/download)
- [Python](https://www.python.org/downloads)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Clone repository

Once the required software is installed, follow the steps below to clone the repository:

1. Clone the Git repository:  
```
git clone https://github.com/dvallst/stream-analytics.git
```
2. From the root directory of the cloned repository, create a virtual environment.  
This step  may take a few seconds:  
```
conda env create -p venv -f bin/local/environment.yml
```
3. From the `conf` subdirectory, copy `env_template.cfg` to a new file named `.env`

## Run

Once the `.env` file is created and Docker Desktop is running, run the pipeline with the following steps:

1. From the `conf` subdirectory, run the Docker Compose to start Kafka & PostgreSQL:  
```
docker compose up
```
2. Open another terminal, activate the virtual environment with the command shown in the creation step (step 2).  
It should be something like:  
```
conda activate /Users/dvt/stream-analytics/venv
```
3. From the root directory of the cloned repository, run the following Python module:  
```
python -m src.messaging.producer
```
4. Open another terminal, activate the virtual environment (step 2) and from the root directory of the cloned repository, run the Python module:  
```
python -m src.main
```
5. Open a web browser and go to http://127.0.0.1:8050 to use the dashboard.

## Maintainer

* **David Valls Teixid??** - *Author/Maintainer* - [dvallst@uoc.edu](https://github.com/dvallst)
