import sys
import random
from textmagic.rest import TextmagicRestClient
import mysql.connector


## Google Cloud MySQL credentials
mydb = mysql.connector.connect(
    host="34.76.64.123",
    user="root",
    passwd="v^6R953p3zp#n1u",
    database="shopping_voluenteers"
)
mycursor = mydb.cursor()

# Textmagic SMS credentials
username = "christianhinge"
token = "XnyI8onJ31O6RQYujpXs9sHiZjcR80"

## Get pastor based on zip code and last name
def FIND_PASTOR(zip_code,name):

    sql = "SELECT * FROM pastors WHERE name LIKE '%{}' AND zip = {}".format(name,zip_code)
    print(sql)
    mycursor.execute(sql)
    pastor = mycursor.fetchall()
    
    return pastor[0]

## Add voluenteer to pastor district
def ADD_VOLUENTEER(phone_no, zip_code, name, pastor):

    pastor_obj = FIND_PASTOR(zip_code, pastor)
    pastor_id = pastor_obj[0]
    
    sql = "INSERT INTO voluenteers (name, phone_no, zip, pastor_id) VALUES (%s, %s, %s, %s)"
    val = (name, phone_no, zip_code, pastor_id)
    mycursor.execute(sql, val)
    mydb.commit()
   
## Approve voluenteer for helping others
def APPROVE_VOLUENTEER(voluenteer_id):
    
    sql = "UPDATE voluenteers SET approved = TRUE WHERE id = {};".format(voluenteer_id)
    mycursor.execute(sql);
    mydb.commit()



## Get one of the voluenteers from a district based on that districts pastor and zip
def GET_VOLUENTEER(zip_code,pastor):
    pastor_obj = FIND_PASTOR(zip_code, pastor)
    pastor_id = pastor_obj[0]
    
    sql = "SELECT * FROM voluenteers WHERE pastor_id = {} AND approved = TRUE".format(pastor_id)
    
    mycursor.execute(sql);
    voluenteers = mycursor.fetchall()
    
    min_deeds = None
    selected_voluenteer = None
    
    #Choose the voluenteer that has voluenteered the least
    for voluenteer in voluenteers:
        if min_deeds == None or voluenteer[5] < min_deeds:
            selected_voluenteer = voluenteer;
            min_deeds = voluenteer[5]
    
    DO_DEED(voluenteer[5])
    return selected_voluenteer

#Register that a voluenteer has done a deed
def DO_DEED(voluenteer_id):
    
    sql = "UPDATE voluenteers SET deeds = deeds+1 WHERE id = {};".format(voluenteer_id)
    mycursor.execute(sql);
    mydb.commit()

#Send SMS to voluenteer informing that a person needs help
def SEND_SMS_VOLUENTEER(phone_no_v,phone_no_r):

    message = "Hi! A citizen in your area needs help shopping. Please contact him/her via the following phone number: {}. Thank you for helping".format(phone_no_r)
    client = TextmagicRestClient(username, token)
    client.messages.create(phones=phone_no_v, text=message)




