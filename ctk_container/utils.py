from pymongo import MongoClient

mongo_client = MongoClient(
                        host="mongo",
                        port=int('27017'),
                        username='root',
                        password='example'
                    )
