# README

To use this application, you will need to have Python3 installed on your local desktop.

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