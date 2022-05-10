# Streaming Analytics

This project was developed as a master's thesis in BI & Big Data Analytics at the [Universitat Oberta de Catalunya](https://www.uoc.edu) (UOC).
The topic of the thesis is Streaming Analytics, and this project implements a use case to monitor aircraft flights (events) 
through a data pipeline.
The pipeline acquires events from The Open Sky Network API, publishes them to a Kafka topic, consumes them from a Plotly 
dashboard, and finally stores them in a containerized PostgreSQL database.

## Prerequisites

The following software is required to run the pipeline locally:

- [Git](https://git-scm.com/download)
- [Python](https://www.python.org/downloads)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Apache Kafka.  
Recommended guide for macOS: [Apache Kafka Installation on Mac using Homebrew](https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

Once the required software is installed, follow the steps below to start Kafka (macOS command examples):

1. Start the Zookeeper server.  
`zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties`
2. Start the Kafka server:  
`kafka-server-start /opt/homebrew/etc/kafka/server.properties`

Once Kafka is up and running, follow the steps below to clone the repository:

1. Clone the Git repository:  
`git clone https://github.com/dvallst/stream-analytics.git`
2. From the root directory of the cloned repository, create a virtual environment:  
`conda env create -p venv -f bin/local/environment.yml`

## Run

Once the virtual environment is created, run the pipeline with the following steps:

1. From the `conf/database` subdirectory, run the PostgreSQL container:  
`docker compose -f docker-compose-postgres.yml up`
2. Activate the virtual environment with the command shown in the creation step.  
It should be something like:  
`conda activate /Users/dvt/stream-analytics/venv`
3. Run the following Python script:  
`python -m src.messaging.producer`
4Open another terminal, activate the virtual environment (step 2) and run the Python script:
`python -m src.main`
4. Open a web browser and go to http://127.0.0.1:8050