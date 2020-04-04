import sys
import mysql.connector

def ADD_VOLUENTEER(phone_no, zip_code):
    mydb = mysql.connector.connect(
        host="34.76.64.123",
        user="root",
        passwd="v^6R953p3zp#n1u",
        database="shopping_voluenteers"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO voluenteers (phone_no, zip) VALUES (%s, %s)"
    val = (phone_no, zip_code)
    mycursor.execute(sql, val)
    mydb.commit()

phone_no = sys.argv[1]
zip_code = sys.argv[2]

ADD_VOLUENTEER(phone_no, zip_code)
print("Thank you for voluenteering. You will recieve an SMS when your help is needed")

