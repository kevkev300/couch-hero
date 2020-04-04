from urllib import parse, request
from datetime import date
import json
import sys

def convertCountryCode(country):
  if country == "United States":
    return "US"
  else:
    return country


def appendInt(num):
    if num > 9:
        secondToLastDigit = str(num)[-2]
        if secondToLastDigit == '1':
            return 'th'
    lastDigit = num % 10
    if (lastDigit == 1):
        return 'st'
    elif (lastDigit == 2):
        return 'nd'
    elif (lastDigit == 3):
        return 'rd'
    else:
        return 'th'


country = "United States"
if len(sys.argv) > 1:
  country = sys.argv[1]
countryCode = convertCountryCode(country)
url = "https://api.covid19api.com/total/country/" + countryCode + "/status/confirmed"


data = request.urlopen(url).read()
data = json.loads(data)
data = data[-1]
currDate = data['Date']
currDate = date.fromisoformat(currDate[:10])
cases = data['Cases']
currDate = '{0:%d}{1} of {0:%B} {0:%Y}'.format(currDate, appendInt(currDate.day))
message = "On the " + currDate + ", the total number of confirmed cases of COVID-19 in " + country + " was " + str(cases) + "."
print(message)


