import mysql.connector
import pymongo
import datetime


def migrate(host_mo, host_mysql, client_mo, db_mysql, user_mysql, pass_mysql):
    mgoclient = pymongo.MongoClient(host_mo)

    mgodb = mgoclient[client_mo]
    db = mysql.connector.connect(
        host=host_mysql,
        user=user_mysql,
        passwd=pass_mysql,
        database=db_mysql

    )

    mycursor = db.cursor()
    mycursor.execute("show tables")
    tables = mycursor.fetchall()

    for table in tables:
        print("Table:"+table[0])
        cursor = db.cursor(dictionary=True)
        sql = "select * from " + table[0]
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        mgocol = mgodb[table[0]]
        for row in result:
            #print("row data is:"+str(row))
            for key in row:
                if (isinstance(row[key], datetime.datetime) or isinstance(row[key], datetime.date)):
                    row[key] = row[key].strftime('%Y-%m-%d %H:%M:%S')
                # print(key)
            try:
                mgocol.insert_one(row)
            except:
                print("error insert")
    return ("done")
