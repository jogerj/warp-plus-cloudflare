import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import pathlib
windowTitle = "WARP-PLUS-CLOUDFLARE By ALIILAPRO (version 3.0.0)"
os.system('title ' + windowTitle if os.name == 'nt' else 'PS1="\[\e]0;' + windowTitle + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print('      _______ _      __________________       _______ _______ _______ _______\n'
'     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
'     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
'     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
'     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
'     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
'     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
'     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n')
print ("[+] ABOUT SCRIPT:")
print ("[-] With this script, you can getting unlimited GB on Warp+.")
print ("[-] Version: 3.0.0")
print ("--------")
print ("[+] THIS SCRIPT CODDED BY ALIILAPRO") 
print ("[-] SITE: aliilapro.github.io") 
print ("[-] TELEGRAM: aliilapro")
print ("--------")

def newID():
	trueInput = False
	while not trueInput:
		referrer  = input("[#] Enter the WARP+ ID:")
		userInput = input(f"[?] Your ID = ({referrer}) is it correct? (y/n):")
		if userInput == "y":
			saveid = input("[?] Do you want to save your ID? (y/n):")
			if saveid == "y":
			    with open("referrer.txt","w") as file:
				    file.write(referrer)
			    trueInput = True
			elif saveid == "n":
				return referrer
			else:
			    print(f"\"{saveid}\" is not a valid parameter.")
		elif userInput == "n":
			trueInput = False
		else:
			print(f"\"{userInput}\" is not a valid parameter.")			
	return referrer

def progressBar():
	completeSeq = False
	c = 0
	animation = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	p = 0
	s = animation[p % len(animation)]
	while not completeSeq:
		for i in range(10):
			c += 1
			sys.stdout.write(f"\r[+] Waiting response...  " + s + f" {c}%")
			sys.stdout.flush()
			time.sleep(0.06)
		p += 1
		s = animation[p % len(animation)]
		if c == 100:
			sys.stdout.write("\r[+] Request completed... [■■■■■■■■■■] 100%")
			completeSeq = True

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(11)
		body = {"key": "{}=".format(genString(42)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "zh-CN"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print("")
		print(error)	

if pathlib.Path("referrer.txt").exists():
	trueInput = False
	while not trueInput:
		userInput = input("[?] Do you want to use saved WARP+ ID? (y/n):")
		if userInput == "y":
			with open("referrer.txt","r") as file:
				referrer = file.read().strip()
			trueInput = True
		elif userInput == "n":
			referrer = newID()
			trueInput = True
		else:
			print(f"\"{userInput}\" is not a valid parameter.")
else:
	referrer = newID()

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
	print("")
	sys.stdout.write("\r[+] Sending request...   [□□□□□□□□□□] 0%")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print(f"\n[-] WORK ON ID: {referrer}")    
		print(f"[:)] {g} GB has been successfully added to your account.")
		print(f"[#] Total: {g} Good {b} Bad")
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] After {i} seconds, a new request will be sent.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[:(] Error when connecting to server.")
		print(f"[#] Total: {g} Good {b} Bad")
		for i in range(10,0,-1):
			sys.stdout.write(f"\r[*] Retrying in {i}s...")
			sys.stdout.flush()
			time.sleep(1)
