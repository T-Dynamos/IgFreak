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
	
def printBox(str,r):
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
	if a == "Y".lower:
		main()
	else:
		sys.exit(0)
def main():
	cls()
	print(logo)
	printBox("Choose above options",R)
	print(f"""
	{C}[{W}1{C}] {Y}Bruteforce
	{C}[{W}2{C}] {Y}Phishing
	{C}[{W}3{C}] {Y}Report\n
	{C}[{W}>{C}] {G}Update Tool
	{C}[{W}*{C}] {G}Donate
	{C}[{W}${C}] {G}Report Bugs
	""")
	option = ask(">>")
	print("")
	if  option == "1":
		username = ask("Enter username ")
		passlist = ask("Enter passlist location")
		print()
		os.system(f"python3 igfreak.py --bruteforce -u {username} -pl {passlist} ")
		res()
	else:
		error1("Wrong option")
		res()
	res()
main()