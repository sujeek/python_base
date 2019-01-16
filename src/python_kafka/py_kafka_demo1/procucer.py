
from kafka import KafkaProducer
import time
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s.%(msecs)d %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

log = logging.getLogger('kafka demo')


def list_file():
    while True:
        log.info("===>>>running")
        time.sleep(2)
        producer.send('world',key=b'foo', value=b'bar')
        producer.flush()


if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    list_file()
    producer.close()