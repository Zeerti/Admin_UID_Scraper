import subprocess
import win32com
import win32com.client

class EblvdHandler():

	# Open EBLVD
	# def open_eblvd(self):
		# eblvd_process = subprocess.Popen('"C:\\Program Files (x86)\\eblvd\\ebclient.exe"', shell=True)
		# 

	# def connect(self, client):

	def connect(self):
		shell = win32com.client.Dispatch('Eblvd.Application')
		shell.Run('C:\Program Files (x86)\eblvd\ebclient.exe')

		




#C:\Program Files (x86)\eblvd\ebclient.exe