import pika

auth = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.102', '5672', '/', auth))
channel = connection.channel()
channel.queue_declare(queue="william")

def callback(ch, method, properties, body):
    print("Received: {}".format(body))

channel.basic_consume(
    on_message_callback=callback,
    queue="william",
    auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()