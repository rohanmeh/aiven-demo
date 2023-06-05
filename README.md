# Aiven Order Processing App

This is a sample application for processing orders using Aiven for Apache Kafka and Flink.

![Aiven POC](./Aiven%20POC.png)

### Prerequisites

To use this application, you will need to have Python3 installed on your local desktop. You will also need to set up Aiven for Apache Kafka and Flink on console.aiven.io. You'll be granted security keys for the ca.pem, service.cert, and service.key files after you set up Kafka within the Aiven console.

### Running the application

1. For creating sample orders to be sent to Aiven for Apache Kafka, run order_producer.py.
```console
python order_producer.py
```
2. For processing the filtered orders after they've been pushed into the appropriate topics by Aiven for Apache Flink, run thing1_order_consumer.py and thing2_5_order_consumer.py. You can open a new terminal for each of these scripts to receive the orders in parallel.
```console
python thing1_order_consumer.py
```
```console
python thing2_5_order_consumer.py
```