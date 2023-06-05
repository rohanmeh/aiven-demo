import time
from kafka import KafkaProducer
import uuid
import random
import json

TOPIC_NAME = "data_topic"

PRODUCT_OPTIONS = [ {"product_name": 'thing1', "product_cost": 1},
                    {"product_name": 'thing2', "product_cost": 2}, 
                    {"product_name": 'thing3', "product_cost": 3}, 
                    {"product_name": 'thing4', "product_cost": 4}, 
                    {"product_name": 'thing5', "product_cost": 5}, ]

producer = KafkaProducer(
    bootstrap_servers=f"kafka-1a00c87e-aiven-poc.aivencloud.com:14731",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

for i in range(100):
    new_uuid = uuid.uuid4()
    print(new_uuid)
    transaction_id = uuid.uuid4()
    receipt = random.choice(PRODUCT_OPTIONS)
    transaction = {
        "transaction_id": str(transaction_id),
        "receipt": receipt,
        "customer_id": str(i)
    }
    print(transaction)
    producer.send(TOPIC_NAME, json.dumps(transaction).encode('utf-8'))
    print(f"Message sent: {transaction}")
    time.sleep(1)

producer.close()