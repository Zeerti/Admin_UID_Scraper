import argparse
from getpass import getpass

def get_login_info():
	parser1 = argparse.ArgumentParser(description="Username for eblvd")
	parser1.add_argument("username")
	args = parser1.parse_args()