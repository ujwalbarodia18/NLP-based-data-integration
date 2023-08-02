from thefuzz import fuzz
from thefuzz import process
# https://towardsdatascience.com/natural-language-processing-for-fuzzy-string-matching-with-python-6632b7824c49

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


# access the database and collection
def nlp():
    db = client["temp"]
    collection = db["dataset"]

    db2 = client["temp"]
    collection2 = db2["temp2"]

    db3 = client["temp"]
    collection3 = db3["result_leven"]

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
            similarity_ratio = fuzz.partial_ratio(i.lower(), j.lower())
            if (similarity_ratio > 80 and similarity_ratio > maxsim):
                changedattributes[j] = i

    attributes = {}
    for i in lis1:
        if i not in attributes:
            attributes[i] = ""

    for j in lis2:
        if j not in attributes:
            if j not in changedattributes:
                attributes[j] = ""

    print("Changed Attributes: ", changedattributes)
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

    a = fuzz.partial_ratio('phone_number', 'phone_no')
    print(a)
    return ("done")
