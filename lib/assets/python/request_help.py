from pastor_voluenteer import *
import sys

parameters = sys.argv[1]
parameters = parameters.split()

phone_no_r = parameters[0]
zip_code = parameters[1]
pastor = parameters[2]


print(phone_no_r)

voluenteer = GET_VOLUENTEER(zip_code,pastor)
phone_no_v = voluenteer[4]

SEND_SMS_VOLUENTEER(phone_no_v,phone_no_r)

print("A person willing to help with shopping should contact soon using the following number: {}.".format(phone_no_v))
