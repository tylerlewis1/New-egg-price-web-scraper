#imports
import requests
import time
import smtplib
from bs4 import BeautifulSoup
#vars
Last_price = 0
done = 0
gmail_password = ""
gmail_user = ""
sent_form = ""
to = ""
body = ""
Subject = ""
url = ""

#initilizes the program by getting all the needed data
def init():
  global Last_price
  global htmltext
  global html
  global Subject
  global url
  global dones
  print("Make sure that you have let less secure apps use your email turned on!")
  gmail_user = input("Type in you email adress: ")
  gmail_password = input("Type in your email password: ")
  sent_form = gmail_user
  to = gmail_user
  body = "If you are getting this something went wrong"
  Subject = "Price Change On Newegg Product"
  url = input("Type in your link (New Egg)")
  return

def Checkprice():
    global Last_price
    global htmltext
    global html
    global Subject
    global url
    global dones
    for html in html.find_all('li'):
        if (html.get('class') == ['price-current']):
            if(float(html.find_all('strong')[0].string + html.find_all('sup')[0].string) != Last_price):
                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login(gmail_user, gmail_password)
                    current_price = float(html.find_all('strong')[0].string + html.find_all('sup')[0].string)
                    print(current_price)
                    change = round((((current_price - Last_price) / ((current_price + Last_price) / 2)) * 100))
                    server.sendmail(
                        gmail_user, 
                        gmail_user, 
                        'Subject: {} \n\n The price has changed form {} to {} the items price has changed by {}%. URL: {}'.format(Subject, Last_price, current_price, change, url))
                    server.quit()
                    Last_price = float(html.find_all('strong')[0].string + html.find_all('sup')[0].string)                    
                except:
                    print("something happend")
                print("ran")
            break
    return       
      

init()
while True:
    htmltext = requests.get(url).text
    html = BeautifulSoup(htmltext, 'html.parser')
    Checkprice()
    time.sleep(60) 
