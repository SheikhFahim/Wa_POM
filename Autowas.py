from selenium import webdriver
import sys,time
import xlrd                                                               #Importing necessary libraries for the code to work
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from page_object.login import Login
from page_object.message import Send
from page_object.logout import Logout

class Automation():
    s = Service("C:\\Users\\sheik\\Desktop\\Assignment 1 office\\chromedriver_win32\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    message='Hello there!'

    path='C:\\Users\\sheik\\Desktop\\Assignment 1 office\\number.xlsx'          #Importing the number from the excel sheet
    ex=xlrd.open_workbook(path)
    ed=ex.sheet_by_index(0)
    p=(int(ed.cell_value(0,0)))
    p=str(p)
    number='0'+p
    d="Delivered"

    def Send_Text(n,message):      #Created a method for the whole process for sending message so it can be used in future to send more than one contact
        s = Service("C:\\Users\\sheik\\Desktop\\Assignment 1 office\\chromedriver_win32\\chromedriver.exe")
        chrome = webdriver.Chrome(service=s)
        chrome.get('https://web.whatsapp.com/')  # Going toh the whatsapp web server
        time.sleep(35)
        Login.page_search(chrome,n)              #Logging in and searching the number
        Send.send_message(chrome,message)        #Sending the message
        try:
            i,q= Send.check_status(chrome)       #checking the status
            Send.excel(i,q)
        except NoSuchElementException as ve:
            Send.excel('Sent','Not seen')
        Logout.logout(chrome)                    #Logout process
    try:
        Send_Text(number,message)
    except NoSuchElementException as se:
        print('Oops!!time elaspsed try again by re-runnning the code') #If the user forgets to login the exception is handeled here.
        sys.exit()