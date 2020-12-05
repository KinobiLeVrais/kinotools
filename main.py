#!/usr/bin/python3

import os
from urllib import request,parse
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
  print(colored("     \/  \/  \___||_.__/ |_|  |_| \___/  \___/ |_|\_|", 'green'))



def main():
    clear()
    kinotools()
    n = input("[1] WebHook Discord \n[2] SOON... \n[3] SOON... \n\n[x] Quitter \n\nChoisis une fonction : \n\n")
    if n == "1":
        clear()
        webhook()
        discord1()

    if n == "x":
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

if __name__ == "__main__":
    main()
