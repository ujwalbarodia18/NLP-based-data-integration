import pymongo
import pandas as pd

# connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# access the database and collection
db = client["temp1"]
collection = db["harsh"]

db2 = client["temp4"]
collection2 = db2["accounts"]

db3 = client["finaltest"]
collection3 = db3["sampletest"]


# keys = collection.distinct('')
# print(keys)

# find all documents in the collection
documents = collection.find()
# iterate over the documents and print their content
# for document in documents:
#     print(document)

# print(documents[0])

lis1 = list(documents[0].keys())
print(lis1)

document2 = collection2.find()
lis2 = list(document2[0].keys())
print(lis2)

attributes = {}

NLPattributes = {
    "Name": ["name", "customer_name", "cust_name", "cname", "c_name", "customer_name", "firstname", "lastname", "middlename"],
    "Id": ["id", "roll_no", "roll", "user_id", "customer_id"]
}

HelpAttributes = {
    "firstname": ["firstname", "fname", "first_name"],
    "middlename": ["middlename", "mname", "middle_name"],
    "lastname": ["lastname", "lname", "last_name"],
}
Helpat = False
NLPkeys = list(NLPattributes.keys())
HelpKeys = list(HelpAttributes.keys())

flag = False

changedatttributes = {}
for i in lis1:
    flag = False
    for j in NLPkeys:
        if (i in NLPattributes[j]):
            flag = True
            if j not in attributes:
                attributes[j] = ""
                if i not in changedatttributes:
                    changedatttributes[i] = j
                break
            else:
                if i not in changedatttributes:
                    changedatttributes[i] = j
        if (flag == True):
            break
    if (flag == False):
        if (i not in attributes):
            attributes[i] = ""

changedatttributes2 = {}
for i in lis2:
    flag = False
    for j in NLPkeys:
        if (i in NLPattributes[j]):
            flag = True
            if j not in attributes:
                attributes[j] = ""
                if i not in changedatttributes2:
                    changedatttributes2[i] = j
                break
            else:
                if i not in changedatttributes2:
                    changedatttributes2[i] = j
        if (flag == True):
            break
    if (flag == False):
        if (i not in attributes):
            attributes[i] = ""

print(attributes)

for i in documents:
    for k in attributes:
        attributes[k] = ""
    templis = list(i.keys())
    for j in templis:
        if j in changedatttributes:
            attributes[changedatttributes[j]] = i[j]
        else:
            attributes[j] = i[j]
    helplis = []
    for m in changedatttributes:
        if changedatttributes[m] == "Name":
            helplis.append(m)
    print(helplis)
    # if ("firstname" in changedatttributes2):
    #     firstname = ""
    #     lastname = ""
    #     middlename = ""
    #     if ("firstname" in templis):
    #         firstname = i["firstname"]
    #     if ("lastname" in templis):
    #         lastname = i["lastname"]
    #     if ("middlename" in templis):
    #         middlename = i["middlename"]
    #     attributes['Name'] = firstname+" "+middlename+" "+lastname
    if (len(helplis) > 1):
        attributes['Name'] = ""
        order = ["", "", ""]
        for t in helplis:
            var = 0
            for k in HelpKeys:
                if t in HelpAttributes[k]:
                    order[var] = t
                var += 1

        attributes['Name'] = i[order[0]]+" "+i[order[1]]+" "+i[order[2]]
    attributes.pop("_id")
    print(attributes)
    collection3.insert_one(attributes)

for i in document2:
    for k in attributes:
        attributes[k] = ""
    templis = list(i.keys())
    for j in templis:
        if j in changedatttributes2:
            attributes[changedatttributes2[j]] = i[j]
        else:
            attributes[j] = i[j]
    helplis = []
    for m in changedatttributes2:
        if changedatttributes2[m] == "Name":
            helplis.append(m)
    print(helplis)
    # if ("firstname" in changedatttributes2):
    #     firstname = ""
    #     lastname = ""
    #     middlename = ""
    #     if ("firstname" in templis):
    #         firstname = i["firstname"]
    #     if ("lastname" in templis):
    #         lastname = i["lastname"]
    #     if ("middlename" in templis):
    #         middlename = i["middlename"]
    #     attributes['Name'] = firstname+" "+middlename+" "+lastname
    if (len(helplis) > 1):
        attributes['Name'] = ""
        order = ["", "", ""]
        for t in helplis:
            var = 0
            for k in HelpKeys:
                if t in HelpAttributes[k]:
                    order[var] = t
                var += 1

        attributes['Name'] = i[order[0]]+" "+i[order[1]]+" "+i[order[2]]
    attributes.pop("_id")
    print(attributes)
    collection3.insert_one(attributes)
