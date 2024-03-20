import pika

connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='localhost')
                )

channel = connection.channel()

channel.queue_declare(queue='greetings')

msg = "Hello World!!!"

channel.basic_publish(
                        exchange='',
                        routing_key='greetings',
                        body=msg
                    )

print(f"[x] Sent \"{msg}\"")

connection.close()