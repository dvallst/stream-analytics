# Streaming Analytics

This project was developed as a master's thesis in BI & Big Data Analytics at the Universitat Oberta de Catalunya (UOC).
The topic of the thesis is Streaming Analytics, and this project implements a use case to monitor aircraft flights (events) through a data pipeline.
The pipeline acquires events from The Open Sky Network API, publishes them to a Kafka topic, consumes them from a Plotly dashboard, and finally stores them in a containerized PostgreSQL database.
