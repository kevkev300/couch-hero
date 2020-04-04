from pastor_voluenteer import *

phone_no = sys.argv[1]
zip_code = sys.argv[2]
pastor = sys.argv[3]

ADD_VOLUENTEER(phone_no, zip_code,"voluenteer_name",pastor)

print("Thank you for voluenteering. You will recieve an SMS when your help is needed")

