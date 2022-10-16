import requests,os
import argparse
import urllib.request
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="Enter User to Scan")
args = vars(ap.parse_args())
os.system("clear")
if args['user']:
	username=args["user"]
	print("Connectiong to Server:")
	url = f"https://instagram188.p.rapidapi.com/userid/{username}"
	headers = {
	"X-RapidAPI-Key": "529183e6d5msh15e3e2c37b1dc5ep154286jsnaba59a2fe040",
	"X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	if a['success']==True:
		print("Connection Successful")
		userid=a['data']
	else:
		print("Connection Failed")
print("Enter Commmands")
def profile_picture(username):
	url =f'https://instagram188.p.rapidapi.com/userphoto/{username}'
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	urllib.request.urlretrieve(a['data'],r'Output/profile_image.jpg')
	print("Image Saved in Output Folder")
