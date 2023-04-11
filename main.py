import string
import random
import requests
from colorama import Fore, init
from os import system
from time import sleep

init()

usedNames = []
proxyList = []

validNames = [] # List for the valid usernames
invalidNames = [] # List for the invalid usernames

# Add the before generated usernames to the usedNames list
with open("valid.txt", "r") as f:
	for line in f:
		usedNames.append(line.strip())
		validNames.append(line.strip())

with open("invalid.txt", "r") as f:
	for line in f:
		usedNames.append(line.strip())
		invalidNames.append(line.strip())

# Add the proxies to the proxyList list
with open("proxies.txt", "r") as f:
	for line in f:
		proxyList.append(line.strip())

print("Loaded " + str(len(proxyList)) + " proxies\n" + Fore.GREEN +"Valid usernames: " + str(len(validNames)) + "\n" + Fore.RED + "Invalid usernames: " + str(len(invalidNames)))

length = int(input(Fore.RESET + "Enter the length of the usernames: "))
useProxies = input("Use proxies? (y/n): ")
if useProxies == "y":
	pass
else:
	proxyList = [""]
	print(Fore.YELLOW + "WARNING | Not using proxies is not recommended and unstable!")

authLink = "https://auth.roblox.com/v1/usernames/validate?birthday=2015-03-04T00:00:00.000Z&context=Signup&username="
checkedUsers = 0 # Value for the amount of usernames checked in a minute


def generate_username(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def check_username(username):
	global checkedUsers

	# Check if the username is already used
	if username in usedNames:
		return
	else:
		pass

	# Check if the username is valid
	if useProxies == "y": # If the user wants to use proxies
		try:
			currentProxy = random.choice(proxyList)
		except:
			print(Fore.RED + "ERROR | No proxies found in proxies.txt!")
			sleep(5)
			exit()
	else:
		currentProxy = ""
	
	try:
		if currentProxy == "": # If the currentProxy is empty, don't use proxies
			r = requests.get(authLink + username)
			data = r.json()
		else:
			r = requests.get(authLink + username, proxies={"https": currentProxy})
			data = r.json()
	except:
		print(Fore.RED + "ERROR | " + username + " | Reason: Invalid Proxy | Proxy: " + currentProxy)
		proxyList.remove(currentProxy)
		# Update the proxies.txt file
		with open("proxies.txt", "w") as f:
			for proxy in proxyList:
				f.write(proxy + "\n")
		return
	
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