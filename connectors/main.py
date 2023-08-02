import mysql_mongodb as connector

val = connector.migrate("mongodb://localhost:27017/",
                        "127.0.0.1", "temp4", "banking_db", "root", "",)
print("Successfully data migrated from mysqldb to mongodb:"+str(val))
