#!/usr/bin/python3
import json
# import pymysql   # python3 默认携带
import mysql.connector  # pip install mysql-connector-python  （mysql 官方）
from mysql.connector import errorcode

dbConfig = {
    "user": "root",
    "password": "denglt",
    "host": "desktop-denglt.mshome.net",
    "database": "med2",
    "raise_on_warnings": True,
    "use_pure": False
}

try:
    cnx = mysql.connector.connect(**dbConfig)
    # cnx.autocommit(False)
    cursor = cnx.cursor()

    cursor.execute("delete from user")
    print(cursor)

    cursor.execute("insert user (name) values('denglt')")
    rowid = cursor.lastrowid  # 自增长id
    print(rowid)

    sql = """
          select doc_id, result, diagnosis_json from  olt_prescription_ol
           where doc_id is not null and (result is not null or diagnosis_json is not null)
           limit 10
          """
    cursor.execute(sql)
    print(cursor)
    rows = cursor.fetchmany(10)  # fetchall fetchmany   fetchone
    print(len(rows))
    for row in rows:
        print(row)
    rows = cursor.fetchmany(10)
    print(len(rows))
    cnx.commit()
    cursor.close()
    cnx.close()
except mysql.connector.Error as err:
    print("发生错误：")
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    print(err)
    print(type(err))
except Exception as err:
    print(type(err))
    print(err)

else:
    cnx.close()
