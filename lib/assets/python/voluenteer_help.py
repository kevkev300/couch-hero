from pastor_voluenteer import *


parameters = sys.argv[1]
parameters = parameters.split(" ~ ")

phone_no = parameters[0]
zip_code = parameters[1]
pastor = parameters[2]

ADD_VOLUENTEER(phone_no, zip_code,"voluenteer_name",pastor)

print("Thank you for voluenteering. You will recieve an SMS when your help is needed")

