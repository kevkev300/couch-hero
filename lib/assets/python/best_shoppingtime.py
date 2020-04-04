import sys
import time
from math import ceil

def main(argv):
	state = argv[0]

	offset = {"Pacific Time Zone": 7*60*60, "Mountain Time Zone": 6*60*60, "Central Time Zone": 5*60*60,"Eastern Time Zone": 4*60*60,"Alaska Time Zone": 8*60*60,"Aleutian Time Zone": 10*60*60}

	location = {

		"Alabama":			"Central Time Zone",
		"Alaska":			"Alaska Time Zone",
		"Arizona":			"Mountain Time Zone",
		"Arkansas":			"Central Time Zone",
		"California":		"Pacific Time Zone",
		"Colorado":			"Mountain Time Zone",
		"Connecticut":		"Eastern Time Zone",
		"Delaware":			"Eastern Time Zone",
		"Florida":			"Eastern Time Zone",
		"Georgia":			"Eastern Time Zone",
		"Hawaii":			"Aleutian Time Zone",
		"Idaho":			"Mountain Time Zone",
		"Illinois":			"Central Time Zone",
		"Indiana":			"Eastern Time Zone",
		"Iowa":				"Central Time Zone",
		"Kansas":			"Central Time Zone",
		"Kentucky":			"Eastern Time Zone",
		"Louisiana":		"Central Time Zone",
		"Maine":			"Eastern Time Zone",
		"Maryland":			"Eastern Time Zone",
		"Massachusetts":	"Eastern Time Zone",
		"Michigan":			"Eastern Time Zone",
		"Minnesota":		"Central Time Zone",
		"Mississippi":		"Central Time Zone",
		"Missouri":			"Central Time Zone",
		"Montana":			"Mountain Time Zone",
		"Nebraska":			"Central Time Zone",
		"Nevada":			"Pacific Time Zone",
		"New Hampshire":	"Eastern Time Zone",
		"New Jersey":		"Eastern Time Zone",
		"New Mexico":		"Mountain Time Zone",
		"New York":			"Eastern Time Zone",
		"North Carolina":	"Eastern Time Zone",
		"North Dakota":		"Central Time Zone",
		"Ohio":				"Eastern Time Zone",
		"Oklahoma":			"Central Time Zone",
		"Oregon":			"Pacific Time Zone",
		"Pennsylvania":		"Eastern Time Zone",
		"Rhode Island":		"Eastern Time Zone",
		"South Carolina":	"Eastern Time Zone",
		"South Dakota":		"Central Time Zone",
		"Tennessee":		"Eastern Time Zon",
		"Texas":			"Central Time Zone", 
		"Utah":				"Mountain Time Zone",
		"Vermont":			"Eastern Time Zone",
		"Virginia":			"Eastern Time Zone",
		"Washington":		"Pacific Time Zone",
		"West Virginia":	"Eastern Time Zone",
		"Wisconsin":		"Central Time Zone",
		"Wyoming":			"Mountain Time Zone"
	}

	

	try:
		loc = location[argv[1]]
		tz = offset[loc]
	except:
		tz = offset["Eastern Time Zone"]

	t = time.gmtime(time.time() - tz)
	cur_hour = t[3]
	cur_day = t[6]

	worst_time = (16, 18)

	if cur_day in {5,6}: 
		print("You should not shop in the weekend as the store are most busy there. If you have to go shop: ", end = '')

	if worst_time[0] <= cur_hour and cur_hour <= worst_time[1]:
		print("You should wait at least ", ciel(worst_time[1] - cur_hour) , " hours before shopping to minimize infection risk", sep = '')
	else:
		print("You should go now before it gets too busy")
	return

if __name__ == "__main__":
	main(sys.argv[1:])

