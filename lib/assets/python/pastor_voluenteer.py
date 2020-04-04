import sys
import mysql.connector
import random
from textmagic.rest import TextmagicRestClient

mydb = mysql.connector.connect(
    host="34.76.64.123",
    user="root",
    passwd="v^6R953p3zp#n1u",
    database="shopping_voluenteers"
)
mycursor = mydb.cursor()

# Textmagic
username = "christianhinge"
token = "XnyI8onJ31O6RQYujpXs9sHiZjcR80"

## ARGUMENTS: 1) Phone number 2) Zip code
def FIND_PASTOR(zip_code,name):

    sql = 'SELECT * FROM pastors WHERE name = %s AND zip = %s;'
    mycursor.execute(sql,(name,zip_code))
    pastor = mycursor.fetchall()
    
    return pastor[0]

def ADD_VOLUENTEER(phone_no, zip_code, name, pastor):

    pastor_obj = FIND_PASTOR(zip_code, pastor)
    pastor_id = pastor_obj[0]
    
    sql = "INSERT INTO voluenteers (name, phone_no, zip, pastor_id) VALUES (%s, %s, %s, %s)"
    val = (name, phone_no, zip_code, pastor_id)
    mycursor.execute(sql, val)
    mydb.commit()
    
def APPROVE_VOLUENTEER(voluenteer_id):
    
    sql = "UPDATE voluenteers SET approved = TRUE WHERE id = {};".format(voluenteer_id)
    mycursor.execute(sql);
    mydb.commit()



## ARGUMENTS: 1) Phone number 2) Zip code
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

def DO_DEED(voluenteer_id):
    
    sql = "UPDATE voluenteers SET deeds = deeds+1 WHERE id = {};".format(voluenteer_id)
    mycursor.execute(sql);
    mydb.commit()

def SEND_SMS_VOLUENTEER(phone_no_v,phone_no_r):

    message = "Hi! A citizen in your area needs help shopping. Please contact him/her via the following phone number: {}. Thank you for helping".format(phone_no_r)
    try:
        client = TextmagicRestClient(username, token)
        client.messages.create(phones=phone_no_v, text=message)
    except:
        print("Error")




