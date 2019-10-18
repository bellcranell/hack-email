# Create python3 
# Author Mr Bell
# 
import urllib.request  as urllib2 
import re
import sys,os
import random

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'
 
def info():
	VERSION = B+'1.0'+E
	AUTHOR =  B+'Mr.Bell'+E
	print("""
		#################################
		#                               # 
		#          Version-> %s        #
		#                               #
		#          Author->  %s     # 
		#                               #
		#################################
		""" % (VERSION, AUTHOR))

def banner():
	text1 = B+"""
HACK EMAIL
AUTHOR : MR.BELL
TEAM   : THE NEXT LEVEL
  
	ran = random.randrange(1, 4)
	if ran == 1:
		print(text1)
	elif ran == 2:
		print(text2)
	elif ran == 3:
		print(text3)


		
def mail():
	os.system('clear')
	banner()
	print(H+'Brut mail account'+E)
	print(B+'Enter login:'+E)
	mail = input(W+'Hunner»Mail»Login»'+E)
	print(B+'Enter password list:'+E)
	password = input(W+'Hunner»Mail»Password»'+E)
	if password == '':
		print(F+'Password list: password/password_list.txt'+E)
		password = 'password/password_list.txt'
	os.system('python3 modules/mail.py '+mail+' '+password)

def Main_Menu():
	print(head)
	desc()
	print('\n')
	print(B+'''
	
  	 1) HACK EMAIL
  	
		v = input('Hunner-»')
	except:
		print(' Good by ')
		exit()
	
	if v == 'help':
		info()
	elif int(v) == 1:
		mail()
	
	else:
		print(F+'[!]'+' You entered an incorrect value '+E)
		exit()
heads()
Main_Menu()
