import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--key", required=True, help="key")
args = vars(ap.parse_args())
os.system("clear")
if args['key']:
	loginkey=args["key"]
