from pymongo import MongoClient


class MongoDB_Clinet(object):

    def __init__(self, mongo_addr):
        self.client = MongoClient(mongo_addr)

    def init_db(self, db):
        return self.client[db]

    def init_col(self, db, col):
        return self.client[db][col]

    def save(self, db, col, data):
        self.client[db][col].save(data)
