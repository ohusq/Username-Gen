import string
import random
import requests
from colorama import Fore, init
from os import system
from time import sleep

init()

usedNames = []

# Add the before generated usernames to the usedNames list
with open("valid.txt", "r") as f:
	for line in f:
		usedNames.append(line.strip())

with open("invalid.txt", "r") as f:
	for line in f:
		usedNames.append(line.strip())

length = int(input("Enter the length of the usernames: "))
authLink = "https://auth.roblox.com/v1/usernames/validate?birthday=2015-03-04T00:00:00.000Z&context=Signup&username="
checkedUsers = 0 # Value for the amount of usernames checked in a minute


def generate_username(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_username(username):
	global checkedUsers
	checkedUsers += 1
	# Check if the username is already used
	if username in usedNames:
		return
	else:
		usedNames.append(username)

	# Check if the username is valid
	r = requests.get(authLink + username)
	data = r.json()
	if data["code"] == 0:
		print(Fore.GREEN + "VALID | " + username)
		with open("valid.txt", "a") as f:
			f.write(username + "\n")
	else:
		print(Fore.RED + "INVALID | " + username + " | Reason:" + data["message"])
		with open("invalid.txt", "a") as f:
			f.write(username + "\n")

def loop():
	while True:
		check_username(generate_username(length))

def resetCPM():
	global checkedUsers
	system("title CPM: " + str(checkedUsers) + " | Checked Users: " + str(len(usedNames)))
	checkedUsers = 0
	sleep(60)
	resetCPM()

loop()
resetCPM()