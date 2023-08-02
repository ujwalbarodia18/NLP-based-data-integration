import pymongo
import pandas as pd
from difflib import SequenceMatcher
# import spacy

# nlp = spacy.load(
# 'E:/en_core_web_md-3.0.0/en_core_web_md-3.0.0/en_core_web_md/en_core_web_md-3.0.0')

# similarity_score = nlp(preprocessed_attr1).similarity(nlp(preprocessed_attr2))
# similarity_ratio = SequenceMatcher(None, word1, word2).ratio()
# connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# access the database and collection


def nlp():
    db = client["temp"]
    collection = db["dataset"]

    db2 = client["temp"]
    collection2 = db2["temp2"]

    db3 = client["temp"]
    collection3 = db3["result_ftest"]

    # keys = collection.distinct('')
    # print(keys)

    # find all documents in the collection
    documents = collection.find()
    # iterate over the documents and print their content
    # for document in documents:
    #     print(document)

    # print(documents[0])

    lis1 = list(documents[0].keys())
    print("Current list of attr:", lis1)

    document2 = collection2.find()
    lis2 = list(document2[0].keys())
    print("Current list of attr:", lis2)

    attributes = {}

    NLPattributes = {
        "Name": ["name", "customer_name", "cust_name", "cname", "c_name", "customer_name", "firstname", "lastname", "middlename"],
        "Id": ["id", "ID", "roll_no", "roll", "user_id", "customer_id"],
        "Phone": ["phone_number", "phone_no", "mobile_number", "mobile", "p_no", "phone"]
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
    maxsim = -1
    maxattri = ""
    for i in lis1:
        # if i == "Phone_no":
        #     print(i)
        maxsim = 0
        flag = False
        flag2 = False
        for j in NLPkeys:
            # if i == "Phone_no":
            #     print(j)
            for k in NLPattributes[j]:
                similarity_ratio = SequenceMatcher(None, i, k).ratio()
                # if i == "Phone_no":
                #     print(similarity_ratio)
                if (similarity_ratio == 1):
                    maxattri = j
                    maxsim = 1
                    flag = True
                    break
                if (similarity_ratio > 0.8 and similarity_ratio > maxsim and not flag):
                    maxsim = similarity_ratio
                    maxattri = j
                    flag = True

            if (maxsim == 1 and flag == True):
                flag2 = True
                if maxattri not in attributes:
                    attributes[maxattri] = ""
                    if i not in changedatttributes:
                        changedatttributes[i] = maxattri
                    break
                else:
                    if i not in changedatttributes:
                        changedatttributes[i] = maxattri
                        break
                flag2 = True
            if (flag == True and flag2 == True):
                break
            if (flag == True and maxsim != 1):
                if maxattri not in attributes:
                    attributes[maxattri] = ""
                    if i not in changedatttributes:
                        changedatttributes[i] = maxattri
                    break
                else:
                    if i not in changedatttributes:
                        changedatttributes[i] = maxattri
                        break
        if (flag == False):
            if (i not in attributes):
                attributes[i] = ""

    changedatttributes2 = {}
    for i in lis2:
        maxsim = 0
        flag = False
        flag2 = False
        for j in NLPkeys:
            for k in NLPattributes[j]:
                similarity_ratio = SequenceMatcher(None, i, k).ratio()
                if (similarity_ratio == 1):
                    maxattri = j
                    maxsim = 1
                    flag = True
                    break
                if (similarity_ratio > 0.8 and similarity_ratio > maxsim):
                    maxsim = similarity_ratio
                    maxattri = j
                    flag = True

            if (maxsim == 1 and flag == True):
                if maxattri not in attributes:
                    attributes[maxattri] = ""
                    if i not in changedatttributes2:
                        changedatttributes2[i] = maxattri
                    break
                else:
                    if i not in changedatttributes2:
                        changedatttributes2[i] = maxattri
                        break
                flag2 = True
            if (flag == True and flag2 == True):
                break
            if (flag == True):
                if maxattri not in attributes:
                    attributes[maxattri] = ""
                    if i not in changedatttributes2:
                        changedatttributes2[i] = maxattri
                    break
                else:
                    if i not in changedatttributes2:
                        changedatttributes2[i] = maxattri
                        break
        if (flag == False):
            if (i not in attributes):
                attributes[i] = ""

    print("Now new attributes of db will be:", attributes)
    print("Changed attr of db1:", changedatttributes)
    print("Changed attr of db2:", changedatttributes2)

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
        # print(helplis)
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
        # print(attributes)
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
        # print(helplis)
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
        # print(attributes)
        collection3.insert_one(attributes)
    return ("done")
