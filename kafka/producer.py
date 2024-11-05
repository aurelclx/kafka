from kafka import KafkaProducer


kafka_producer = KafkaProducer(
  bootstrap_servers="localhost:9093"
)

for i in range(1, 30):
    kafka_producer.send(topic="test", key="key-message".encode("utf-8"), value=f"New message # {i}".encode("utf-8"))

kafka_producer.flush()
