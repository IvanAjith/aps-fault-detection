import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.

client = pymongo.MongoClient("mongodb://localhost:27017")

#DataBase and Collection name
database = 'APS'
collection = 'sensor'
path = '/config/workspace/aps_failure_training_set1.csv'

if __name__ == '__main__':
    df = pd.read_csv(path)
    print(f'Rows and Columns, {df.shape}')

    #Inserting the csv file into mongo db after converting to json
    df.reset_index(drop = True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    client[database][collection].insert_many(json_record)
    print('Insertion done')