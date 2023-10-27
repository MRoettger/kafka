from kafka import KafkaProducer, KafkaAdminClient, KafkaConsumer
from kafka.errors import KafkaError


p = KafkaProducer(bootstrap_servers='127.0.0.1:57476', key_serializer=str.encode, value_serializer=str.encode)
# Asynchronous by default
future = p.send('bar', key='foo', value=b'bar')
metrics = p.metrics()
print(metrics)
# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    pass

# Successful result returns assigned partition and offset
print (record_metadata.topic)
print (record_metadata.partition)
print (record_metadata.offset)

# for _ in range(100):
#    producer.send('foobar', b'some_message_bytes')
