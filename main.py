import string
import random
import requests
from colorama import Fore, init
import threading

init()

length = int(input("Enter the length of the usernames: "))

authLink = "https://auth.roblox.com/v1/usernames/validate?birthday=2015-03-04T00:00:00.000Z&context=Signup&username="
usedNames = []

def generate_username(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_username(username):
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

loop()