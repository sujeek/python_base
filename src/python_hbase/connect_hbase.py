# -*- encoding='utf-8' -*-S

from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
import happybase


# thrift默认端口是9090
def get_client():
    socket = TSocket.TSocket('localhost',9090)
    socket.setTimeout(5000)

    transport = TTransport.TBufferedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = Hbase.Client(protocol)
    socket.open()
    return client


def get_conn():
    conn = happybase.Connection("localhost", 9090)
    return conn

client = get_client()
conn = get_conn()

print client.getTableNames()
print conn.tables()