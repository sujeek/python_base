import logging

logger = logging.getLogger(__name__)


def get_hbase_row(hbase_client, table_name, row):
    result = None
    try:
        result = hbase_client.getRow(table_name, row)
    except:
        logger.error("table is not exists!")
    return result