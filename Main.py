from selenium import webdriver
from time import sleep
import os
from bs4 import BeautifulSoup
import requests

def banner():
	print("""
		 ____            _           _     
		|  _ \ _ __ ___ (_) ___  ___| |_ _ 
		| |_) | '__/ _ \| |/ _ \/ __| __(_)
		|  __/| | | (_) | |  __/ (__| |_ _ 
		|_|   |_|  \___// |\___|\___|\__(_)
		              |__/
		    _         _        ____             _   
		   / \  _   _| |_ ___ |  _ \ ___  _   _| |_ 
		  / _ \| | | | __/ _ \| |_) / _ \| | | | __|
		 / ___ \ |_| | || (_) |  _ < (_) | |_| | |_ 
		/_/   \_\__,_|\__\___/|_| \_\___/ \__,_|\__|

                                                """)


def menu():
	print("""

		1)	Open A Port
		2)	Delete A Open Port
		3)	Quit

					""")

def AddService():
	name = input("What's The Name of The Service? -> ")
	port = input("What's The Port? -> ")
	last3ip = input("Input The Last 3 Digits of the local IP. -> ")
	#print('yey')
	print("Are You Sure?")
	try:
		user_input = input("User Input: ->  ").lower()
	except ValueError as err:
		print("Invalid Input")
		print(err)
	if user_input.startswith('y'):

		driver = webdriver.Chrome(executable_path=r'chromedriver')
		driver.implicitly_wait(30)
		driver.get("http://admin:password@www.routerlogin.net/FW_forward_service.htm")
		aproachf1 = driver.find_element_by_name('portname')
		aproachf1.send_keys(name)
		aproachf2 = driver.find_element_by_name('ex_port_range')
		aproachf2.send_keys(port)
		aproachf3 = driver.find_element_by_name('server_ip4')
		aproachf3.send_keys(last3ip)
		aproachf4 = driver.find_element_by_name('Apply')
		aproachf4.click()
		driver.quit()
		print("Success!")
	#end

def DeleteService():
	print("Are You Sure?")
	try:
		user_input = input("User Input: ->  ").lower()
	except ValueError as err:
		print("Invalid Input")
		print(err)
	if user_input.startswith('y'):

		#page = requests.get("http://admin:lolbit121@www.routerlogin.net/FW_forward.htm")
		#soup = BeautifulSoup(page.content, 'html.parser')
		#service_table = soup.find(id='main')
		#items = service_table.find_all(class_= 'tables')
		#print(items[0].find(class_ = 'ttext').get_text())


		driver = webdriver.Chrome(executable_path=r'/home/kitcoy/Documents/chromedriver')
		driver.implicitly_wait(30)
		driver.get("http://admin:lolbit121@www.routerlogin.net/FW_forward.htm")
		quitdel = input("Press Q when done.  -> ")
		if quitdel == 'q':
			os._exit(0)
		elif quitdel == 'Q':
			os._exit(0)
		else:
			print("did you type that right? Exting anyway...")
			sleep(2)
			os._exit(0)



def Main():
	os.system('clear||cls')
	banner()
	menu()
	try:
		user_input = int(input("User Input: ->  "))
	except ValueError as err:
		print("Invalid Input")
		print(err)
	if user_input == 1:
		AddService()
	elif user_input == 2:
		DeleteService()
	elif user_input == 3:
		os._exit(0)
	else:
		print("how did you get to this line?")
Main()
