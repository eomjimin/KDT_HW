from pymongo import MongoClient
import banacrawling

nameList, addList, iNameList = banacrawling.bana()

url = 'mongodb+srv://jimini0920:JW4qxzzylk41IZe1@cluster0.kngcohp.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(url)

database = client['banapresso']
collection = database['stores']

for i in range(len(nameList)):
    store_insert = {'store': nameList[i], 'address': addList[i], 'file': iNameList[i]}
    result = collection.insert_one(store_insert)