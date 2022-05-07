# Streaming Analytics

This project was developed as a master's thesis in BI & Big Data Analytics at the [Universitat Oberta de Catalunya](https://www.uoc.edu) (UOC).
The topic of the thesis is Streaming Analytics, and this project implements a use case to monitor aircraft flights (events) 
through a data pipeline.
The pipeline acquires events from The Open Sky Network API, publishes them to a Kafka topic, consumes them from a Plotly 
dashboard, and finally stores them in a containerized PostgreSQL database.

The following software is required to run the pipeline locally:

- [Git](https://git-scm.com/download)
- [Python](https://www.python.org/downloads)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Kafka
- [Docker Desktop](https://www.docker.com/products/docker-desktop)

Once the required software is installed, follow the steps below to run the pipeline:

1. Clone the Git repository:  
`git clone https://github.com/dvallst/stream-analytics.git`
2. From the root directory of the cloned repository, create a virtual environment:  
`conda env create -p venv -f bin/local/environment.yml`
3. Activate the virtual environment with the command shown when executed the previous step:  
`conda activate /Users/dvt/stream-analytics/venv`
4. Run the following Python script:  
`python -m src.messaging.producer`
5. Open another terminal, activate the virtual environment (step 3) and run the following Python script:  
`python -m src.main`
