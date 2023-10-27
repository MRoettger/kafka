from kafka import KafkaAdminClient
import ssl
# Create a new context using system defaults, disable all but TLS1.2
context = ssl.create_default_context()
context.options &= ssl.OP_NO_TLSv1
context.options &= ssl.OP_NO_TLSv1_1

producer = KafkaAdminClient(bootstrap_servers='localhost:9092',
                            client_id='test',
                            sasl_plain_username='user',
                            sasl_plain_password='TqQ9WIpiM7',
                            security_protocol="PLAINTEXT",
                            ssl_context=context,
                            sasl_mechanism="SASL_PLAINTEXT")

topics = producer.list_topics()
print(topics)