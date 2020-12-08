#!/usr/bin/python3

import os
from urllib import request,parse
import ipfinder
import requests, re, json
import urllib
import time
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def kinotools():
    print(" ")
    print(" ")
    print(colored("                  _  __ _             _______             _      ", 'green'))
    print(colored("                 | |/ /(_)           |__   __|           | |     ", 'green'))
    print(colored("                 | ' /  _  _ __    ___  | |  ___    ___  | | ___ ", 'green'))
    print(colored("                 |  <  | || '_ \  / _ \ | | / _ \  / _ \ | |/ __|", 'green'))
    print(colored("                 | . \ | || | | || (_) || || (_) || (_) || |\__ \ ", 'green'))
    print(colored("                 |_|\_\|_||_| |_| \___/ |_| \___/  \___/ |_||___/", 'green'))
    print(colored("By Kinobi", 'grey'))
    print(" ")

def webhook():
  print(colored(" __          __    _      _    _                _    ", 'green'))
  print(colored(" \ \        / /   | |    | |  | |              | |   ", 'green'))
  print(colored("  \ \  /\  / /___ | |__  | |__| |  ___    ___  | | __", 'green'))
  print(colored("   \ \/  \/ // _ \| '_ \ |  __  | / _ \  / _ \ | |/ /", 'green'))
  print(colored("    \  /\  /|  __/| |_) || |  | || (_) || (_) ||   < ", 'green'))
  print(colored("     \/  \/  \___||_.__/ |_|  |_| \___/  \___/ |_|\_\ ", 'green'))

def iplocalisatorstyle():
  print(colored("  _____  _____    _                     _  _              _                     ", 'green'))
  print(colored(" |_   _||  __ \  | |                   | |(_)            | |                    ", 'green'))
  print(colored("   | |  | |__) | | |  ___    ___  __ _ | | _  ___   __ _ | |_  ___  _   _  _ __ ", 'green'))
  print(colored("   | |  |  ___/  | | / _ \  / __|/ _` || || |/ __| / _` || __|/ _ \| | | || '__|", 'green'))
  print(colored("  _| |_ | |      | || (_) || (__| (_| || || |\__ \| (_| || |_|  __/| |_| || |   ", 'green'))
  print(colored(" |_____||_|      |_| \___/  \___|\__,_||_||_||___/ \__,_| \__|\___| \__,_||_|   ", 'green'))
  print("\n\n")


def main():
    clear()
    kinotools()
    n = input("[1] WebHook Discord \n[2] Localiser IP \n[3] SOON... \n\n[x] Quitter \n\nChoisis une fonction : \n\n")
    if n == "1":
        clear()
        webhook()
        discord1()

    if n == "2":
        clear()
        iplocalisatorstyle()
        iplocalisator()

    if n == "x":
      clear()
      print("\nA bientot !\n")
      exit

    else:
        main()


"""FONCTION N°1"""
def discord1():
  numberofrequest = 0
  discordwebhook = input("\n\n	[1] Spammer Webhook\n	[2] Supprimer Webhook\n\n    [3] Retourner au menu\n\n")
  if discordwebhook == "1":
    webhook = input("\nlien du webhook: \n\n")
    username = input("\nNom du webhook (au choix): \n\n")
    subject = input("\nMessage: \n\n")
    try:
      for i in range(0,10000):
        numberofrequest+=1
        postrequest(webhook,username,subject)
        print(str(numberofrequest)+" | requête envoyé au webhook !.")
        time.sleep(2)
    except urllib.error.HTTPError:
      discord1()
  if discordwebhook == "2":
    webhook = input("lien du webhook a supprimer : \n")
    deleterequest(webhook)
    print("Webhook supprimé !")
    time.sleep(5)
    clear()
    discord1()
  if discordwebhook == "3":
      main()

def postrequest(url,user,msg):
	data = bytes("{\"username\":\""+user+"\",\"avatar_url\":\"\",\"content\":\""+msg+"\"}","utf-8")
	headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
	req = request.Request(url,data=data,headers=headers)
	request.urlopen(req)

def deleterequest(url):
	headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
	req = request.Request(url,headers=headers,method="DELETE")
	request.urlopen(req)
"""FONCTION N°1"""

"""FONCTION N°2"""
def iplocalisator():
  ip = input(" Adresse IP: ")
  print("\n Localisation en cours '%s'..." % (ip))

  url = "http://ip-api.com/json/"
  data = requests.get(url+ip).content.decode('utf-8')
  values = json.loads(data)

  status = values['status']

  if status != "success":
    print("\n Adresse IP invalide.")
    time.sleep(3)
    main()

  else:
    print("\n\n\n"+ip)
    print("├──Isp")
    print("│  └──"+values['isp'])
    print("├──Org")
    print("│  └──"+values['isp'])
    print("├──Pays")
    print("│  └──"+values['country'])
    print("├──Region")
    print("│  └──"+values['regionName'])
    print("├──Ville")
    print("│  └──"+values['city'])
    print("├──Code Postal")
    print("│  └──"+values['zip'])
    localisation = str(values['lat'])+', '+str(values['lon'])
    print("└──Localisation")
    print("   └──"+localisation)

    infos = ("Maps", "https://www.google.fr/maps?q="+localisation)


    table = SingleTable(TABLE_DATA, ip)
    print("\n"+table.table)
    time.sleep(3)
    e = input("\n Appuie sur entrer pour revenir au menu")
    if e == "":
      main()
    else:
      exit

"""FONCTION N°2"""




if __name__ == "__main__":
    main()
