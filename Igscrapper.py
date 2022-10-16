import requests,os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--user", required=True, help="Enter User to Scan")
args = vars(ap.parse_args())
os.system("clear")
if args['user']:
	username=args["user"]
	url = f"https://instagram188.p.rapidapi.com/userid/{username}"
	headers = {
	"X-RapidAPI-Key": "529183e6d5msh15e3e2c37b1dc5ep154286jsnaba59a2fe040",
	"X-RapidAPI-Host": "instagram188.p.rapidapi.com"}
	response = requests.request("GET", url,headers=headers)
	a=response.json()
	if a['success']==True:
		userid=a['data']
