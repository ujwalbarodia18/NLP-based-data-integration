from nltk.stem.snowball import SnowballStemmer
import nltk
from difflib import SequenceMatcher
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


# access the database and collection
db = client["DataCheck"]
collection = db["connector"]

db2 = client["testsql"]
collection2 = db2["dataset"]

db3 = client["Datacheckmodel"]
collection3 = db3["datacheck"]


porter = nltk.PorterStemmer()
stemmer = SnowballStemmer("english")

print(stemmer.stem("phone_number"))
print(stemmer.stem("phone_no"))

print(porter.stem("phone_number"))
print(porter.stem("phone"))
similarity_ratio = SequenceMatcher(
    None, porter.stem("phone_number"), porter.stem("phone_no")).ratio()
print(similarity_ratio)
documents = collection.find()

lis1 = list(documents[0].keys())
lis1.pop(0)
print("Lis1:", lis1)


document2 = collection2.find()
lis2 = list(document2[0].keys())
# lis1.remove('_id')
lis2.pop(0)
print(lis2)


changedattributes = {}

for i in lis1:
    maxsim = 0
    for j in lis2:
        similarity_ratio = SequenceMatcher(
            None, porter.stem(i.lower()), porter.stem(j.lower())).ratio()
        if (similarity_ratio > 0.7 and similarity_ratio > maxsim):
            changedattributes[j] = i

attributes = {}
for i in lis1:
    if i not in attributes:
        attributes[i] = ""

for j in lis2:
    if j not in attributes:
        if j not in changedattributes:
            attributes[j] = ""

print(changedattributes)
print(attributes)

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
