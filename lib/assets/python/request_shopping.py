from textmagic.rest import TextmagicRestClient
import sys
import mysql.connector
import random

from pastor_voluenteer import *

phone_no_r = sys.argv[1]
zip_code_r = sys.argv[2]

voluenteer = GET_VOLUENTEER(zip_code_r)

phone_no_v = voluenteer[0]
zip_code_v = voluenteer[1]

SendText(phone_no_v,phone_no_r)
print("A person willing to help with shopping should contact soon using the following number: {}.".format(phone_no_v))