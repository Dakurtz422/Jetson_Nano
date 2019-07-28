import subprocess
from time import sleep
import datetime

# Script for checking a temperature of Jetson Nano cores
# Set your values here
max_temp = 50
sleep_time = 30


def temp():
	process = subprocess.run('cat /sys/devices/virtual/thermal/thermal_zone*/temp', shell=True, capture_output=True)
	temp_out = list((process.stdout.decode()).split("\n"))
	# Delete last one (none) and -2 (always 100°C)
	del temp_out[-1]
	del temp_out[-2]
	#print(temp_out)

	for y, x in enumerate(temp_out):
		x = (x) / 1000
		time = datetime.datetime.now()
		time = time.strftime(" -> /%m/%d  %H:%M")
		print(x ,"°C" , time)
		if x > max_temp:
			# If HOT do something here (send mails, etc..)
			print(f"Processor {y} is HOT" )

while True:
	temp()
	sleep(sleep_time)
	print("")
