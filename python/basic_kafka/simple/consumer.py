from confluent_kafka import Consumer


def main():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'HuMan',
        'default.topic.config': {
            'auto.offset.reset': 'earliest'
        }
    })

    consumer.subscribe(['test-topic'])
    message = consumer.poll(1.0)

    print(f"Message {message.value()}")

if __name__ == '__main__':
    main()
