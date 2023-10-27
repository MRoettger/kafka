from kafka import KafkaConsumer

consumer = KafkaConsumer('bar', bootstrap_servers='127.0.0.1:51513')
for msg in consumer:
     print (msg)