# CLI command for local is: mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp9" --nsFrom="temp1.*" --nsTo="temp9.*" --nsInclude="*" --gzip --archive
import os

# for now we will not use as this is issue of running cli command using python , File upload in json format will be used
# os.system('mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp11" --nsFrom="temp1.*" --nsTo="temp11.*" --nsInclude="*" --gzip --archive')
import subprocess

# subprocess.run(
#     ['mongodump --uri="mongodb://localhost:27017/temp1" --gzip --archive | mongorestore --uri="mongodb://localhost:27017/temp11" --nsFrom="temp1.*" --nsTo="temp11.*" --nsInclude="*" --gzip --archive '])
# subprocess.run(
#     ['mongoimport E:/6th Sem/Project/final/NLP-based-data-integration/books.json -d bookdb -c books --drop'])
os.system('mongoimport "C:/Users/Harsheet/Downloads/Github repos/NLP-based-data-integration/dataset.json" -d temp -c temp2 --drop')
