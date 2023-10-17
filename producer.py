from kafka import KafkaProducer
import ssl

sasl_mechanism = 'PLAIN'
security_protocol = 'SASL_SSL'

# Create a new context using system defaults, disable all but TLS1.2
context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1

producer = KafkaProducer(bootstrap_servers='10.98.254.94:30010',
                         sasl_plain_username='user',
                         sasl_plain_password='TqQ9WIpiM7',
                         security_protocol=security_protocol,
                         ssl_context=context,
                         sasl_mechanism=sasl_mechanism,
                         api_version=(0, 10),
                         retries=5)

producer.send("test", "text")
#for _ in range(100):
#    producer.send('foobar', b'some_message_bytes')
