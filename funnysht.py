#!/usr/bin/python3.6

import sys
import os
from colorama import Fore

if len (sys.argv) != 1 :
   print("Usage:", str(sys.argv[0]))
   sys.exit (1)


print(f'{Fore.CYAN}Mini-Program by @X1nto{Fore.RESET}')

print ('why are you gay?')
while True:
   d1a = input ('A)Who says i\'m gay? \nB)I\'m not gay \n[A/B]?:')
   if d1a in ['A', 'B']:
      break

if d1a == "A":
   print('You are gay');
   d1a = input ('A)NO U \n[A?]:')
   if d1a == "A":
      print('ok :(\n')

elif d1a == "B":
   print('Are you Lesbian, Homosexual or transgenda?')
   while True:
       d1a = input ('A)Lesbian \nB)Homosexual \nC)Transgenda \nD)Wai are u asking sir? \n[A/B/C/D]? :')
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

print('wanna try again?')
while True:
    d1a = input ('A)Yeah why not \nB)i don\'t play with gays \n[A/B]? :')
    if d1a in ['A', 'B']:
       break

if d1a == "A":
   os.execl(sys.executable, sys.executable, *sys.argv)
elif d1a == "B":
    print('u hurt meh\n')
