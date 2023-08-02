import pandas as pd
from pymongo import MongoClient
import json


def mongoimportcsv(csv_path, db_name, coll_name, db_url='localhost', db_port=27017):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(db_url, db_port)
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    # coll.remove_one()
    coll.insert_many(payload)
    return ("done")


# ans = mongoimportcsv(
#     'C:/Users/Harsheet/Downloads/NLP-based-data-integration/connectors/cities_final.csv', 'temp1', 'temp')
# print(ans)
