from confluent_kafka import Producer
from datetime import datetime


def main():
    current_time = datetime.now().isoformat()

    producer = Producer({
        'bootstrap.servers': 'localhost:9092'
    })

    producer.produce('test-topic', f'Hello, {current_time}'.encode('utf-8'))
    producer.flush()

if __name__ == '__main__':
    main()
    print('Complete.')
