from textmagic.rest import TextmagicRestClient
import sys
import mysql.connector
import random

def GET_VOLUENTEER(zip_code):
    mydb = mysql.connector.connect(
    host="34.76.64.123",
    user="root",
    passwd="v^6R953p3zp#n1u",
    database="shopping_voluenteers"
    )

    mycursor = mydb.cursor()
    sql = "SELECT * FROM voluenteers WHERE zip = {}".format(zip_code)
    mycursor.execute(sql)
    voluenteers = mycursor.fetchall()
    selected_ix = random.randrange(0,len(voluenteers))
    return voluenteers[selected_ix]


def SendText(phone_no_v,phone_no_r):
    username = "christianhinge"
    token = "XnyI8onJ31O6RQYujpXs9sHiZjcR80"
    message = "Hi! A citizen in your area needs help shopping. Please contact him/her via the following phone number: {}. Thank you for helping".format(phone_no_r)
    try:
        client = TextmagicRestClient(username, token)
        client.messages.create(phones=phone_no_v, text=message)
    except:
        print("Error")


phone_no_r = sys.argv[1]
zip_code_r = sys.argv[2]

voluenteer = GET_VOLUENTEER(zip_code_r)

phone_no_v = voluenteer[0]
zip_code_v = voluenteer[1]

SendText(phone_no_v,phone_no_r)
print("A person willing to help with shopping should contact soon using the following number: {}.".format(phone_no_v))