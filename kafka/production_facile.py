from kafka import KafkaProducer


def encode_str(string):
    return(string.encode("utf-8"))


kafka_producer = KafkaProducer(
  bootstrap_servers="localhost:9093",
  client_id="production_facile",
  value_serializer=encode_str
)

for i in range(1, 6):
    kafka_producer.send(topic="test2", value=f"Pas besoin d'encodage # {i}")

kafka_producer.flush()
