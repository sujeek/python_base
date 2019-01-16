from pymongo import MongoClient

if __name__ == '__main__':
    mongodb_addr = ["web1:3900", "web2:3900", "web3:3900"]
    client = MongoClient(mongodb_addr)
    db = "test"
    prod_cols = ["col1", "col2"]

    for col in prod_cols:
        preview_col = col + "_preview"
        count = client[db][col].count()
        for x in range(0, count):
            cursor = client[db][col].find().skip(x).limit(1)
            obj = cursor.next()
            client[db][preview_col].save(obj)
