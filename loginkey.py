import os
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--key", required=True, help="key")
args = vars(ap.parse_args())
os.system("clear")
if args['key']:
	loginkey=args["key"]
