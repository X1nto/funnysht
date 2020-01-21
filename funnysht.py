#!/usr/bin/python3.6

import sys
import os
import time
from colorama import Fore

if len (sys.argv) != 1 :
   print("Usage:", str(sys.argv[0]))
   sys.exit (1)


print(f'{Fore.CYAN}Mini-Program by @X1nto{Fore.RESET}')

print('\nMAIN MENU\n')
while True:
    d1a = input ('1)Start \n2)Help \n3)About\n \n[1/2/3]?:')
    if d1a in ['1', '2', '3']:
       break

if d1a == "1":
    q = '\nQESTION:'

    print (q, '\nwhy are you gay?\n')
    while True:
       d1a = input ('A)Who says i\'m gay? \nB)I\'m not gay\n \n[A/B]?:')
       if d1a in ['A', 'B']:
          break

    if d1a == "A":
       print('\nYou are gay\n');
       d1a = input ('A)NO U \n[A]?:')
       if d1a == "A":
          print('ok :(\n')

    elif d1a == "B":
       print(q, '\nAre you Lesbian, Homosexual or transgenda?')
       while True:
           d1a = input ('\nA)Lesbian \nB)Homosexual \nC)Transgenda \nD)Wai are u asking sir?\n \n[A/B/C/D]? :')
           if d1a in ['A', 'B', 'C', 'D']:
              break

       if d1a == "A":
          print('Ya like girls?\n')
       elif d1a == "B":
           print('gtfo this app ffs\n')
       elif d1a == "C":
           print('ya like jazz?\n')
       elif d1a == "D":
           print('cuz why not lol\n')

    time.sleep(1.2)

    print('----------------')
    print('                ')
    print('wanna try again?')
    while True:
        d1a = input ('A)Yeah why not \nB)I don\'t play with gays\n \n[A/B]? :')
        if d1a in ['A', 'B']:
           break

    if d1a == "A":
       os.execl(sys.executable, sys.executable, *sys.argv)
    elif d1a == "B":
        print('u hurt meh')

if d1a == "2":
    print('There\'s only one thing you will need to play this game, it\'s called a keyboard. \nRemeber, type answers with capital letters only, or else it won\'t work!')
    while True:
        d1a = input ('return to main menu? \n[y/n]?:')
        if d1a in ['y', 'n']:
            break

    if d1a == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif d1a == 'n':
        print ('ok bye!')

elif d1a == "3":
    print(f'{Fore.CYAN}This app is made by Tornike Khintibidze \nCopyright @X1nto, all rights reserved XD{Fore.RESET}')
    while True:
        d1a = input ('\nreturn to main menu? \n[y/n]?:')
        if d1a in ['y', 'n']:
            break

    if d1a == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif d1a == 'n':
        print ('ok bye!')
