import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO,        # 控制台打印的日志级别
                    filename='main.log',
                    filemode='w',              # 模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )

hander = logging.StreamHandler()
logger.addHandler(hander)