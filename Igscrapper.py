import requests,os
import json as js
import urllib.request
username=input("Enter UserName Of the Target:  ")
loginkey=input("Enter Key Generated From Rapid Api: ")
	print('''
 __    _______      _______.  ______ .______          ___      .______   .______    _______ .______      
|  |  /  _____|    /       | /      ||   _  \        /   \     |   _  \  |   _  \  |   ____||   _  \     
|  | |  |  __     |   (----`|  ,----'|  |_)  |      /  ^  \    |  |_)  | |  |_)  | |  |__   |  |_)  |    
|  | |  | |_ |     \   \    |  |     |      /      /  /_\  \   |   ___/  |   ___/  |   __|  |      /     
|  | |  |__| | .----)   |   |  `----.|  |\  \----./  _____  \  |  |      |  |      |  |____ |  |\  \----.
|__|  \______| |_______/     \______|| _| `._____/__/     \__\ | _|      | _|      |_______|| _| `._____|''')
	print("Connecting to Server:")
	url = f"https://instagram188.p.rapidapi.com/userid/{username}"
	headers = {"X-RapidAPI-Key": f"{loginkey}","X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	if a['success']==True:
		print("Connection Successful")
		userid=a['data']
	else:
		print("Connection Failed")

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

# To see Contact details
# def Contact_details(userid):
# 	url = f"https://instagram188.p.rapidapi.com/usercontact/{userid}"
# 	response = requests.request("GET", url,headers=headers)
# 	res=response.json()
# 	print(res['data'])
# 	print("Country Code : >> ",res['data']['user']['public_phone_country_code'])
# 	print("Phone Number : >> ",res['data']['user']['public_phone_number'])
# 	print("zip Code : >> ",res['data']['user']['zip'])
# 	print("Latitude : >> ",res['data']['user']['latitude'])
# 	print("Longitude : >> ",res['data']['user']['longitude'])

print("Profile Picture {:>12}".format("p"))
print("Contact Info {:>15}".format("i"))
print("Quit {:>23}".format("q"))
# print("Contact Details {:>12}".format("c"))
loop=True
while loop :
	command=input("Enter Commands >> ")
	if command=="p":
		profile_picture(username)
	elif command=="i":
		Contact_info(userid)
	# elif command=="c":
	# 	Contact_details(userid)
	elif command=="q":
		loop=False
	else:
		print("Invalid Command")

