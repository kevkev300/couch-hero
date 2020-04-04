import sys
import mysql.connector
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
    mycursor = mydb.cursor()
    
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
    sql = "SELECT * FROM voluenteers WHERE zip = {}".format(zip_code)
    mycursor.execute(sql)
    voluenteers = mycursor.fetchall()
    selected_ix = random.randrange(0,len(voluenteers))
    return voluenteers[selected_ix]

def SEND_SMS_VOLUENTEER(phone_no_v,phone_no_r):

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
#%%
phone_no = sys.argv[1]
zip_code = sys.argv[2]

ADD_VOLUENTEER(phone_no, zip_code)
print("Thank you for voluenteering. You will recieve an SMS when your help is needed")



