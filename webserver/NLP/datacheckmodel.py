import pymongo
import pandas as pd
import spacy
# import spacy

nlp = spacy.load(
    'E:/en_core_web_md-3.0.0/en_core_web_md-3.0.0/en_core_web_md/en_core_web_md-3.0.0')


def preprocess_text(text):
    """Preprocess text by removing stop words, punctuation, and converting to lowercase."""
    doc = nlp(str(text).lower())
    tokens = [
        token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)


attr1 = preprocess_text("dog")
attr2 = preprocess_text("cat")
similarity_score = nlp(attr1).similarity(nlp(attr2))
print(similarity_score)
# connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")


# access the database and collection
db = client["datatype"]
collection = db["test1"]

db2 = client["datatype"]
collection2 = db2["test2"]

db3 = client["datatype"]
collection3 = db3["result"]


# keys = collection.distinct('')
# print(keys)

# find all documents in the collection
documents = collection.find()
# iterate over the documents and print their content
# for document in documents:
#     print(document)

# print(documents[0])

lis1 = list(documents[0].keys())
lis1.pop(0)
print("Lis1:", lis1)


document2 = collection2.find()
lis2 = list(document2[0].keys())
# lis1.remove('_id')
lis2.pop(0)
print(lis2)

changedattributes = {}
maxsim = 0

for i in lis1:
    maxsim = 0
    for j in lis2:
        if (nlp(preprocess_text(documents[0][i])).similarity(nlp(preprocess_text(document2[0][j]))) > 0.7 and nlp(preprocess_text(documents[0][i])).similarity(nlp(preprocess_text(document2[0][j]))) > maxsim):
            maxsim = nlp(preprocess_text(documents[0][i])).similarity(
                nlp(preprocess_text(document2[0][j])))
            # if j not in changedattributes:
            changedattributes[j] = i

attributes = {}
for i in lis1:
    attributes[i] = ""
for i in lis2:
    if i not in changedattributes:
        attributes[i] = ""

print(attributes)

print(changedattributes)
dict1 = {}
for i in documents:
    for j in attributes:
        attributes[j] = ""
    templis = list(i.keys())
    templis.pop(0)
    # print(templis)
    # templis.pop(0)
    for j in templis:
        attributes[j] = i[j]
    if ("_id" in attributes):
        del attributes['_id']
    collection3.insert_one(attributes)

for i in document2:
    for j in attributes:
        attributes[j] = ""
    templis = list(i.keys())
    # print("2", templis)
    templis.pop(0)
    for j in templis:
        if j in changedattributes:
            attributes[changedattributes[j]] = i[j]
        else:
            attributes[j] = i[j]
    if ("_id" in attributes):
        del attributes['_id']
    collection3.insert_one(attributes)

# print(attributes)

# changed={}
# for i in lis1:
#     for j in lis2:
#         if(i==j):
#             changed[j]=i
