import pika, sys, os


def recieve_msg_callback(ch, method, props, body):
    print(f"[CHANNEL] \"{ch}\" \n")
    print(f"[METHOD] Recieved \"{method}\" \n")
    print(f"[PROPERTIES] Recieved \"{props}\" \n")
    print(f"[x] Recieved \"{body}\" \n")

def main():
    connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost')
                    )

    channel = connection.channel()
    channel.queue_declare(queue='greetings')
    
    channel.basic_consume(
        queue='greetings',
        auto_ack=True,
        on_message_callback=recieve_msg_callback
    )
    print(f"[x] Waiting for msgs ... \n")

    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except:
            os._exit(0)