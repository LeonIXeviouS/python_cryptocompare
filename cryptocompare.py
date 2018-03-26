#!/usr/bin/env python3.5
#-*- codding: utf-8 -*-
#Jérémy ROBIN B2b
import cryptocompare

global found
found = False
listeCrypto = cryptocompare.get_coin_list(format=True)
def triCrypto(coinSelected):
 for coin in listeCrypto:
   if coinSelected == coin:
     prix = cryptocompare.get_price(coin)
     found = True
     print(">> Prix d'un "+coin+" "+str(prix[coin]['EUR'])+" EUR")
 if(found == False):
   print('Veuillez entré une crypto dans la liste')

def Liste(liste):
 count = 0
 for i in liste:
   print(i)
#Core

Liste(listeCrypto)

coinSelected = input('Entrez une cryto-monnaie pour plus de détail : ')

if found == False:
  triCrypto(coinSelected)

