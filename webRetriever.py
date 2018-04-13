import urllib2
import sys
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Back, Style
# Ditmir Hasani
# script for scraping information on a given url
print "############################### WEB RETRIEVER ###############################"
web_address = raw_input('Please enter a URL : ').strip()
website = str(web_address)
web_page_load = urllib2.urlopen('http://{}'.format(web_address))
soup = BeautifulSoup(web_page_load,'lxml')
print "-------------------------------------"

store_urls = []
def retrieve_info():
	user_choice = int(input("Please select from the following options :  \n [1] Retrieve links from page, \n [2] Raw Page \n"
		" [3] Raw Links \n [4] Return all visible 'p' tags \n [5] Retrieve all text within p tags  \n [9] Exit  \n >>> "))
	if user_choice == 1:
		# print "The following links were retrieved from {}".format(web_page_load)
		for links in soup.find_all("a"):
			href = links.get("href")
			# print href
			# print "{}".format(links.get("href"))
			store_urls.append(href)
		check_href_tags()
		check_http_tags()
		check_https_tags()
		# print links
	elif user_choice == 2:
			print "The Raw page looks like this :{}".format(soup)
	elif user_choice == 3:
		print "Retrieving raw link tags....."
		for rawlinks in soup.find_all("a"):
			print rawlinks
	elif user_choice == 4:
		print "Retrieving all p tags ....."
		for ptags in soup.find_all("p"):
			print ptagtext.get_text()
	elif user_choice == 5:
		for ptagtext in soup.find_all("p"):
			print ptagtext.get_text()
	elif user_choice == 9:
		print 'Goodbye !'
		sys.exit()
	elif user_choice != 1 or 2 or 3 or 4 or 5 or 9:
		retry = raw_input("You have not made a valid selection , would you like to rety ? Y/N : " )
		if retry == 'y' or 'Y':
			retrieve_info()
		else:
			print 'Goodbye!'

def check_href_tags():
	print (Fore.BLUE + "---------- Checking HREF tags ----------")
	for urls in store_urls:
		if urls.startswith( '/' ):
			check_url = "http://www.{}{}".format(website,urls)
			open_web = urllib2.urlopen(check_url)
			try : open_web
			except urllib2.HTTPError as notfound:
				print
			check_status = open_web.getcode()
			if check_status == 200:
				print (Fore.GREEN + "{} is GOOD !  STATUS:{}".format(check_url, check_status))
			elif check_status != 200:
				print (Fore.RED + "ALERT !!! {} is BAD !  " + Fore.RED +"STATUS:{}".format(check_url, check_status))
			elif check_status == 301:
				print ""

def check_http_tags():
	print "---------- Checking HTTP tags ----------"
	for urls in store_urls:
		if "http://" in urls:
			open_web = urllib2.urlopen(urls)
			# try: open_web
			# except urllib2.HTTPError as notfound:
			# 	print notfound
			# 	print (Fore.YELLOW + str(notfound) + "> {}".format(urls))
			check_status = open_web.getcode()
			if check_status == 200:
				print (Fore.GREEN + "{} is GOOD !  STATUS:{}".format(urls, check_status))
			elif check_status != 200:
				print (Fore.RED + "ALERT !!! {} is BAD !  STATUS:{}".format(urls, check_status))
				bad_urls.append(urls)

def check_https_tags():
	print "---------- Checking HTTPS tags ----------"
	for urls in store_urls:
		if "https://" in urls:
			open_web = urllib2.urlopen(urls)
			try : open_web
			except urllib2.HTTPError as notfound:
				print (Fore.YELLOW + str(notfound) + "> {}".format(urls))
			check_status = open_web.getcode()
			if check_status == 200:
				print (Fore.GREEN + "{} is GOOD !  STATUS:{}".format(urls, check_status))
			elif check_status != 200:
				print (Fore.RED + "ALERT !!! {} is BAD !  STATUS:{}".format(urls, check_status))
				bad_urls.append(urls)
retrieve_info()

print "------------------------<>---------------------------"
# bad_urls = []

		# print bad_urls

		# print(Fore.RED + 'some red text')

		
	# 	for fail in bad_urls:
	# 		print fail

	# # 	print 'links start with www >>> {}'.format(urls)
	# # elif 'https://' in urls:
	# # 	print "links with https:// >> {}".format(urls)

