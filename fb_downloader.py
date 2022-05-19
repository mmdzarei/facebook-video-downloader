#change line 39,44,100
#Add token to line 39 add trusted users to line 44, and add admin(bot owner's telegram user_id to line 100)


import wget
from lxml import html
import requests
import os
import telebot



import mechanize



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

#from webdriver_manager.chrome import ChromeDriverManager















####################'''
#bot
TOKEN='*************************************'
bot=telebot.TeleBot(TOKEN)


#add trusted users
users=['trusted_users1','trusted_users2','trusted_users3']
global link0
global hd_link

link0=''
hd_link=''
'''#### rooye add user kar shavad

users_text_file.writelines("%s" % i for i in users)
users_text_file.close()
users_text_file= open("users.txt","r+")
useuse=users_text_file.readlines()
print("useuse::\n",useuse)


def read_users():
	users=[]
	users_text_file= open("users.txt","r")
	for line in users_text_file:
		line.rstrip("\n\r")
		print(line)
		users.append(line)
	print(users)
	return(users)

users=read_users()

def write_users(new_user):
	users_text_file= open("users.txt","w")
'''

def dnld(link,name):
	print('\nDownloading Started\n')
	wget.download(link,name)
	print('\nDownloaded\n')


def get_fb_link(url0):
	url=url0.replace('https://www','https://m')
	page = requests.get(url0)
	tree = html.fromstring(page.content)
	##print("treeeeee\n\n\:\n",tree.xpath('//meta[10]'))
	link = tree.xpath('//meta[@property="og:video:secure_url"]//@content')[0]
	print('\n\n\n\n\nlink1:',link)



	return(link)


@ bot.message_handler(commands=['start','go'])
def start_hanlder(message):
	bot.send_message(message.chat.id,'Hello, Send me the facebook link, dude')

@ bot.message_handler(commands=['add_user'])
def add_user_hanlder(message):
	if(message.from_user.username=='ADMIN_USERNAME'):  
		txt="Hello, Admin. What's the user's username?"+"\n(Without "+"-@-"+")"
		msg=bot.send_message(message.chat.id,txt)
		bot.register_next_step_handler(msg,get_user)
	else:
	    bot.send_message(message.chat.id,"Only the admin can add users 😜")

'''
@ bot.message_handler
def hd_hanlder(message):
    if (message.text=="sd"):
        print("\n\n\n\n\nYYYYEEESSS")
    	#msg=bot.send_message(message.chat.id,"HD? or SD?")
        bot.register_next_step_handler(message,get_hd_link)
    	#print("HD link=\t",link0)
'''

def get_hd_link(message):
    try:
        if (message.text=="/sd"):
            chat_id=message.chat.id
            bot.send_message(message.chat.id,"Sending ...")
            link=get_fb_link(link0)
            #bot.send_message(message.chat.id,link)                  #direct link
            lnlnln = '[This is the SD link]'+"("+str(link)+")"
            bot.send_message(message.chat.id,lnlnln,parse_mode='MarkdownV2')
            bot.send_message(message.chat.id,'Downloading')
            video_name=str(chat_id)+'.mp4'
            dnld(link,video_name)
            bot.send_message(message.chat.id,'Downloaded')
            video = open(video_name, 'rb')
            bot.send_message(message.chat.id,'Uploading Video...')
            bot.send_video(chat_id, video)
            #file_id = 'AxxxxZZZzzz'
            #bot.send_video(chat_id, file_id)
            os.remove(video_name)                                #remove from server
        elif (message.text=="/hd"):
            chat_id=message.chat.id
            bot.send_message(message.chat.id,"Sending ...")
            '''
            page=requests.get(link0)
            tree=html.fromstring(page.content)
            #text = tree.xpath('//*[@id="facebook"]/body/script[10]/text()')
            text = tree.xpath('/html/body/script[86]/text()')
            s=text[0]
            #print("\n\n\n\nS\s:",s)

            start = 'hd_src:"'
            end = '",sd_src'
            hd_link=s[s.find(start)+len(start):s.rfind(end)]
            '''
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.get(link0)
            elem = browser.find_element_by_xpath('//*[@id="facebook"]/body/script[23]')
            elem_t=elem.get_attribute('innerHTML')
            resault = re.search('playable_url_quality_hd":"(.*?)",', elem_t)
            resault2=str(resault.group(1))
            resault2=resault2.replace("\\u0025","%")
            resault2=resault2.replace("\\","")
            print(resault2)
            browser.close()








            #bot.send_message(message.chat.id,resault2)       #HD link
            lnlnln = '[This is the HD link]'+"("+str(resault2)+")"
            bot.send_message(message.chat.id,lnlnln,parse_mode='MarkdownV2')
            #bot.send_message('@atron_fb_ch',resault2)       #Send to channel
            bot.send_message('@atron_fb_ch',lnlnln,parse_mode='MarkdownV2')
            #print("HD Link====",hd_link)
            #print("\n\n\n\n\n\n\n")
            video_name=str(chat_id)+'.mp4'

            ###########     Download and upload to telegram

            dnld(hd_link,video_name)
            video = open(video_name, 'rb')
            bot.send_video(chat_id, video)                 #upload video "file too big"
            os.remove(video_name)

            return
    except:
        print(bot.send_message(message.chat.id,'Not downloadable or something else went wrong'))

def get_user(message):
	text=message.text.lower()
	chat_id=message.chat.id
	users.append(text)
	print(users)
	bot.send_message(message.chat.id,"Apended!")
	return

@ bot.message_handler(content_types=['text'])
def text_handler(message):
	global link0
	global hd_link

	text=message.text.lower()
	link0=text
	chat_id=message.chat.id
	if (message.from_user.username in users):
		if ('facebook.com' in text):
			bot.send_message(message.chat.id,"/hd? or /sd?")
			bot.register_next_step_handler(message,get_hd_link)


		elif (text=='hello'):
			print("ID==\t",message.from_user.id)
			print("User_name==\t",message.from_user.username)
			bot.send_message(message.chat.id,'Hello, Just send me the link, man')
		else:
			bot.send_message(message.chat.id,'da fuq? Send me a facebook video URL')

	else:
		bot.send_message(message.chat.id,"You're not a friend, only my friends are allowed to use me!")


#bot.polling(none_stop=True)
'''
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://www.facebook.com/login.php'
browser.open(url)
browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
browser.form['email'] = '*********@*****.com'
browser.form['pass'] = '***********'
response = browser.submit()
print (response.read())
'''
bot.polling()
