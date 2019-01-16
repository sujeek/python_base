# -*- encoding=utf-8 -*-
from kafka import KafkaConsumer
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s.%(msecs)d %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S'
)

log = logging.getLogger('kafka demo')


if __name__ == '__main__':
    consumer = KafkaConsumer('world', group_id='consumer-20171017', bootstrap_servers=['localhost:9092'])
    for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
        log.info(recv)
