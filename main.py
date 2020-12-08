#!/usr/bin/python3
from hashlib import sha256 #line:3
import os #line:4
from urllib import request ,parse #line:5
import ipfinder #line:6
import requests ,re ,json #line:7
import urllib #line:8
import time #line:9
from termcolor import colored #line:10
def clear ():#line:12
    os .system ('cls'if os .name =='nt'else 'clear')#line:13
def kinotools ():#line:14
    print (" ")#line:15
    print (" ")#line:16
    print (colored ("                  _  __ _             _______             _      ",'green'))#line:17
    print (colored ("                 | |/ /(_)           |__   __|           | |     ",'green'))#line:18
    print (colored ("                 | ' /  _  _ __    ___  | |  ___    ___  | | ___ ",'green'))#line:19
    print (colored ("                 |  <  | || '_ \  / _ \ | | / _ \  / _ \ | |/ __|",'green'))#line:20
    print (colored ("                 | . \ | || | | || (_) || || (_) || (_) || |\__ \ ",'green'))#line:21
    print (colored ("                 |_|\_\|_||_| |_| \___/ |_| \___/  \___/ |_||___/",'green'))#line:22
    print (colored ("By Kinobi",'grey'))#line:23
    print (" ")#line:24
def webhook ():#line:25
  print (colored (" __          __    _      _    _                _    ",'green'))#line:26
  print (colored (" \ \        / /   | |    | |  | |              | |   ",'green'))#line:27
  print (colored ("  \ \  /\  / /___ | |__  | |__| |  ___    ___  | | __",'green'))#line:28
  print (colored ("   \ \/  \/ // _ \| '_ \ |  __  | / _ \  / _ \ | |/ /",'green'))#line:29
  print (colored ("    \  /\  /|  __/| |_) || |  | || (_) || (_) ||   < ",'green'))#line:30
  print (colored ("     \/  \/  \___||_.__/ |_|  |_| \___/  \___/ |_|\_\ ",'green'))#line:31
def iplocalisatorstyle ():#line:32
  print (colored ("  _____  _____    _                     _  _              _                     ",'green'))#line:33
  print (colored (" |_   _||  __ \  | |                   | |(_)            | |                    ",'green'))#line:34
  print (colored ("   | |  | |__) | | |  ___    ___  __ _ | | _  ___   __ _ | |_  ___  _   _  _ __ ",'green'))#line:35
  print (colored ("   | |  |  ___/  | | / _ \  / __|/ _` || || |/ __| / _` || __|/ _ \| | | || '__|",'green'))#line:36
  print (colored ("  _| |_ | |      | || (_) || (__| (_| || || |\__ \| (_| || |_|  __/| |_| || |   ",'green'))#line:37
  print (colored (" |_____||_|      |_| \___/  \___|\__,_||_||_||___/ \__,_| \__|\___| \__,_||_|   ",'green'))#line:38
  print ("\n\n")#line:39
def chiffrementstyle ():#line:40
  print (colored ("        _      _   __   __                                     _   ",'green'))#line:41
  print (colored ("       | |    (_) / _| / _|                                   | |  ",'green'))#line:42
  print (colored ("   ___ | |__   _ | |_ | |_  _ __  ___  _ __ ___    ___  _ __  | |_ ",'green'))#line:43
  print (colored ("  / __|| '_ \ | ||  _||  _|| '__|/ _ \| '_ ` _ \  / _ \| '_ \ | __|",'green'))#line:44
  print (colored (" | (__ | | | || || |  | |  | |  |  __/| | | | | ||  __/| | | || |_ ",'green'))#line:45
  print (colored ("  \___||_| |_||_||_|  |_|  |_|   \___||_| |_| |_| \___||_| |_| \__|",'green'))#line:46
  print (colored ("        _   ",'green'))#line:48
  print (colored ("       | |  ",'green'))#line:49
  print (colored ("   ___ | |_ ",'green'))#line:50
  print (colored ("  / _ \| __|",'green'))#line:51
  print (colored (" |  __/| |_ ",'green'))#line:52
  print (colored ("  \___| \__|",'green'))#line:53
  print (colored ("      _              _      _   __   __                                     _   ",'green'))#line:55
  print (colored ("     | |            | |    (_) / _| / _|                                   | |  ",'green'))#line:56
  print (colored ("   __| |  ___   ___ | |__   _ | |_ | |_  _ __  ___  _ __ ___    ___  _ __  | |_ ",'green'))#line:57
  print (colored ("  / _` | / _ \ / __|| '_ \ | ||  _||  _|| '__|/ _ \| '_ ` _ \  / _ \| '_ \ | __|",'green'))#line:58
  print (colored (" | (_| ||  __/| (__ | | | || || |  | |  | |  |  __/| | | | | ||  __/| | | || |_ ",'green'))#line:59
  print (colored ("  \__,_| \___| \___||_| |_||_||_|  |_|  |_|   \___||_| |_| |_| \___||_| |_| \__|",'green'))#line:60
  print (colored ("\nAvec XOR sous SHA256",'grey'))#line:62
def main ():#line:64
    clear ()#line:65
    kinotools ()#line:66
    print ("[1] WebHook Discord \n[2] Localiser IP \n[3] Chiffrement/dechiffrement \n\n[x] Quitter \n\n")#line:67
    OOOO000OO0O000000 =input ("Choisis une fonction : \n\n")#line:68
    if OOOO000OO0O000000 =="1":#line:69
        clear ()#line:70
        webhook ()#line:71
        discord1 ()#line:72
    if OOOO000OO0O000000 =="2":#line:74
        clear ()#line:75
        iplocalisatorstyle ()#line:76
        iplocalisator ()#line:77
    if OOOO000OO0O000000 =="3":#line:79
        clear ()#line:80
        chiffrementstyle ()#line:81
        chiffrement ()#line:82
    if OOOO000OO0O000000 =="x":#line:84
      clear ()#line:85
      print ("\nA bientot !\n")#line:86
      exit #line:87
    else :#line:89
        main ()#line:90
"""FONCTION N°1"""#line:93
def discord1 ():#line:94
  O000OO0OOOO0OOO0O =0 #line:95
  O00OOO000OO0OOOOO =input ("\n\n	[1] Spammer Webhook\n	[2] Supprimer Webhook\n\n    [3] Retourner au menu\n\n")#line:96
  if O00OOO000OO0OOOOO =="1":#line:97
    OOOOOOO0O00OO00OO =input ("\nlien du webhook: \n\n")#line:98
    O0O000OO0OO0O0O0O =input ("\nNom du webhook (au choix): \n\n")#line:99
    OOOOO00O00O00O0OO =input ("\nMessage: \n\n")#line:100
    try :#line:101
      for OOOO0OOOO00000OOO in range (0 ,10000 ):#line:102
        O000OO0OOOO0OOO0O +=1 #line:103
        postrequest (OOOOOOO0O00OO00OO ,O0O000OO0OO0O0O0O ,OOOOO00O00O00O0OO )#line:104
        print (str (O000OO0OOOO0OOO0O )+" | requête envoyé au webhook !.")#line:105
        time .sleep (2 )#line:106
    except urllib .error .HTTPError :#line:107
      discord1 ()#line:108
  if O00OOO000OO0OOOOO =="2":#line:109
    OOOOOOO0O00OO00OO =input ("lien du webhook a supprimer : \n")#line:110
    deleterequest (OOOOOOO0O00OO00OO )#line:111
    print ("Webhook supprimé !")#line:112
    time .sleep (5 )#line:113
    clear ()#line:114
    discord1 ()#line:115
  if O00OOO000OO0OOOOO =="3":#line:116
      main ()#line:117
def postrequest (O00000O0O0O0O00OO ,O00O0O0OO0O0OO00O ,OOO000O00O0O0O0OO ):#line:119
	OO00O0000O00O0O00 =bytes ("{\"username\":\""+O00O0O0OO0O0OO00O +"\",\"avatar_url\":\"\",\"content\":\""+OOO000O00O0O0O0OO +"\"}","utf-8")#line:120
	OO0O0O0OO0OO000OO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}#line:121
	O00OOOOOOOOO0OOOO =request .Request (O00000O0O0O0O00OO ,data =OO00O0000O00O0O00 ,headers =OO0O0O0OO0OO000OO )#line:122
	request .urlopen (O00OOOOOOOOO0OOOO )#line:123
def deleterequest (OO0O0000O000000O0 ):#line:125
	O000O0OOOO00O0000 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}#line:126
	O00O0000000O0O00O =request .Request (OO0O0000O000000O0 ,headers =O000O0OOOO00O0000 ,method ="DELETE")#line:127
	request .urlopen (O00O0000000O0O00O )#line:128
"""FONCTION N°1"""#line:129
"""FONCTION N°2"""#line:131
def iplocalisator ():#line:132
  O0OO000OO00O0OO00 =input (" Adresse IP: ")#line:133
  print ("\n Localisation en cours '%s'..."%(O0OO000OO00O0OO00 ))#line:134
  OO0OOO00000OO0OOO ="http://ip-api.com/json/"#line:136
  OOOOOO00O000O0O0O =requests .get (OO0OOO00000OO0OOO +O0OO000OO00O0OO00 ).content .decode ('utf-8')#line:137
  O0O00OO0O000OO0OO =json .loads (OOOOOO00O000O0O0O )#line:138
  O0OOO0OO0O0O0O0OO =O0O00OO0O000OO0OO ['status']#line:140
  if O0OOO0OO0O0O0O0OO !="success":#line:142
    print ("\n Adresse IP invalide.")#line:143
    time .sleep (3 )#line:144
    main ()#line:145
  else :#line:147
    print ("\n\n\n"+O0OO000OO00O0OO00 )#line:148
    print ("├──Isp")#line:149
    print ("│  └──"+O0O00OO0O000OO0OO ['isp'])#line:150
    print ("├──Org")#line:151
    print ("│  └──"+O0O00OO0O000OO0OO ['isp'])#line:152
    print ("├──Pays")#line:153
    print ("│  └──"+O0O00OO0O000OO0OO ['country'])#line:154
    print ("├──Region")#line:155
    print ("│  └──"+O0O00OO0O000OO0OO ['regionName'])#line:156
    print ("├──Ville")#line:157
    print ("│  └──"+O0O00OO0O000OO0OO ['city'])#line:158
    print ("├──Code Postal")#line:159
    print ("│  └──"+O0O00OO0O000OO0OO ['zip'])#line:160
    O000OOO00OO00O0OO =str (O0O00OO0O000OO0OO ['lat'])+', '+str (O0O00OO0O000OO0OO ['lon'])#line:161
    print ("└──Localisation")#line:162
    print ("   └──"+O000OOO00OO00O0OO )#line:163
    time .sleep (3 )#line:165
    O00O0OOO0O0OOO0OO =input ("\n Appuie sur entrer pour revenir au menu")#line:166
    if O00O0OOO0O0OOO0OO =="":#line:167
      main ()#line:168
    else :#line:169
      exit #line:170
"""FONCTION N°2"""#line:171
"""FONCTION N°3"""#line:173
def chiffrement ():#line:174
  print ("")#line:175
  print ("")#line:176
  OO0O00OOO000000O0 =input ("\nentrez le nom du fichiez a chiffrer/déchiffrer : \n\n")#line:177
  OO0000O0OO000O000 =input ("\nentrez le nom du fichier de sortie : \n\n")#line:178
  OOO00000OO0O0OOO0 =input ("\nentrez la clé : \n\n")#line:179
  OOO0OOOOO0O000O00 =sha256 (OOO00000OO0O0OOO0 .encode ('utf-8')).digest ()#line:180
  with open (OO0O00OOO000000O0 ,'rb')as OO0O0OOOOOO0000OO :#line:181
    with open (OO0000O0OO000O000 ,'wb')as OO000OOO0O00O0OO0 :#line:182
  	  OO0O00000OOO0OOO0 =0 #line:183
  	  while OO0O0OOOOOO0000OO .peek ():#line:184
  	    OOOO000OO000OO000 =ord (OO0O0OOOOOO0000OO .read (1 ))#line:185
  	    OOO0O0OOO0OO0000O =OO0O00000OOO0OOO0 %len (OOO0OOOOO0O000O00 )#line:186
  	    OO00O00OOO000O0O0 =bytes ([OOOO000OO000OO000 ^OOO0OOOOO0O000O00 [OOO0O0OOO0OO0000O ]])#line:187
  	    OO000OOO0O00O0OO0 .write (OO00O00OOO000O0O0 )#line:188
  	    OO0O00000OOO0OOO0 =OO0O00000OOO0OOO0 +1 #line:189
  print (colored ("fichier chiffré/dechiffré avec succes !","green"))#line:190
  time .sleep (3 )#line:191
  clear ()#line:192
  main ()#line:193
"""FONCTION N°3"""#line:194
if __name__ =="__main__":#line:196
    main ()
