import requests,os
import argparse
import json as js
import urllib.request
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="Enter User to Scan")
args = vars(ap.parse_args())
os.system("clear")
loginkey=input("Enter Key Generated From Rapid Api: ")
if args['user']:
	username=args["user"]
	print("Connectiong to Server:")
	url = f"https://instagram188.p.rapidapi.com/userid/{username}"
	headers = {"X-RapidAPI-Key": f"{loginkey}","X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	if a['success']==True:
		print("Connection Successful")
		userid=a['data']
	else:
		print("Connection Failed")
print(userid)
# To Download Profile picture
def profile_picture(username):
	url =f"https://instagram188.p.rapidapi.com/userphoto/{username}"
	response = requests.request("GET", url,headers=headers)
	res=response.json()
	urllib.request.urlretrieve(res['data'],r'Output/profile_image.jpg')
	print("Image Saved in Output Folder")

# To See Contact Info 
def Contact_info(userid):
	url = f"https://instagram188.p.rapidapi.com/usercontact/{userid}"
	response = requests.request("GET", url,headers=headers)
	res=response.json()
	sub=res['data']['user']
	while "biography_with_entities" in sub:
		sub.popitem()
	pretty = js.dumps(sub, indent=4)
	print(pretty)

print("Profile Picture {:>8}".format("p"))
print("Contact Info {:>8}".format("i"))
loop=True
while loop :
	command=input("Enter Commands >> ")
	if command=="p":
		profile_picture(username)
	elif command=="i":
		Contact_info(userid)
	elif command=="q":
		loop=False
	else:
		print("Invalid Command")

