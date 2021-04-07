import pika


auth = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.102', '5672', '/', auth))
channel = connection.channel()
channel.queue_declare(queue="william")
channel.basic_publish(
    exchange="",
    routing_key="william",
    body="hello world"
)

print("send rabbit_mq ...")
connection.close()